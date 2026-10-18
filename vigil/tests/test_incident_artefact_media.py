"""Approved offline Incident media acceptance contract; no network fixtures."""
import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'artefact_validator', Path(__file__).resolve().parents[1] / 'scripts/validate-vigil-records.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

SHA = 'a' * 40


def artefact(extension='png', mime='image/png', kind='source-screenshot'):
    filename = f'VIGIL/VIGIL-INC-000043.{extension}'
    return {
        'artefact_type': kind, 'media_type': mime,
        'permalink': f'https://github.com/CAM-Initiative/Registry/blob/{SHA}/{filename}',
        'render_url': f'https://raw.githubusercontent.com/CAM-Initiative/Registry/{SHA}/{filename}',
        'alt_text': 'Archived Gemini dialogue showing the homework prompt and hostile response.',
    }


class IncidentArtefactMediaTests(unittest.TestCase):
    def errors(self, record):
        errors = []
        v.validate_incident_artefacts(Path('VIGIL-INC-000043.json'), record, errors)
        return errors

    def check(self, item):
        return self.errors({'incident_artefacts': [item]})

    def test_optional_artefacts_and_source_documents_remain_valid(self):
        self.assertEqual(self.errors({}), [])
        self.assertEqual(self.errors({'incident_artefacts': []}), [])
        self.assertEqual(self.errors({'source_records': [{'source_url': 'https://example.org/report.md'}]}), [])

    def test_supported_image_extensions_and_mime_parameters(self):
        for ext in ['png', 'jpg', 'jpeg', 'gif', 'webp', 'avif', 'svg', 'PNG']:
            with self.subTest(ext=ext):
                self.assertEqual(self.check(artefact(ext, 'IMAGE/PNG; charset=utf-8')), [])

    def test_supported_video_extensions_without_image_alt(self):
        for ext in ['mp4', 'webm', 'ogg', 'ogv', 'm4v', 'mov']:
            with self.subTest(ext=ext):
                item = artefact(ext, 'video/mp4', 'other')
                item.pop('alt_text')
                self.assertEqual(self.check(item), [])

    def test_pdf_is_valid_as_document_but_not_screenshot(self):
        self.assertEqual(self.check(artefact('pdf', 'application/pdf', 'document')), [])
        errors = self.check(artefact('pdf', 'application/pdf'))
        self.assertTrue(any('.artefact_type' in e for e in errors))
        self.assertTrue(self.check(artefact('mp4', 'video/mp4')))

    def test_historical_markdown_pattern_and_spoofed_mime_are_blocked(self):
        for ext, mime in [('md', 'text/markdown'), ('md', 'image/png'),
                          ('json', 'image/png'), ('html', 'image/png'), ('txt', 'image/png')]:
            with self.subTest(ext=ext, mime=mime):
                self.assertTrue(any('.render_url/media_type' in e for e in self.check(artefact(ext, mime, 'document'))))

    def test_missing_or_incompatible_mime_is_blocked(self):
        for ext, mime in [('png', ''), ('png', None), ('png', 'text/markdown'),
                          ('png', 'video/mp4'), ('mp4', 'image/png'),
                          ('pdf', 'image/png'), ('png', 'image/')]:
            with self.subTest(ext=ext, mime=mime):
                self.assertTrue(self.check(artefact(ext, mime, 'other')))

    def test_images_require_nonempty_alt_text(self):
        for value in [None, '', '  ', 42]:
            with self.subTest(alt=value):
                item = artefact(kind='source-image')
                item['alt_text'] = value
                self.assertTrue(any('.alt_text' in e for e in self.check(item)))

    def test_moving_branch_and_short_shas_are_blocked_in_both_urls(self):
        for key in ['permalink', 'render_url']:
            for ref in ['main', 'preview/vigil-incident-ingestion', 'abcdef1']:
                with self.subTest(key=key, ref=ref):
                    item = artefact()
                    item[key] = item[key].replace(SHA, ref)
                    self.assertTrue(any(f'.{key} must be an immutable' in e for e in self.check(item)))

    def test_pinned_urls_must_match_commit_and_file(self):
        for replacement in [('a' * 40, 'b' * 40), ('000043.png', '000043-02.png')]:
            with self.subTest(replacement=replacement):
                item = artefact()
                item['render_url'] = item['render_url'].replace(*replacement)
                self.assertTrue(any('same Registry commit and file' in e for e in self.check(item)))

    def test_external_or_non_http_media_url_is_not_a_registry_reference(self):
        for url in ['https://example.org/source.png', 'file:///tmp/source.png',
                    'data:image/png;base64,abcd', 'https://[broken/source.png']:
            with self.subTest(url=url):
                item = artefact()
                item['render_url'] = url
                self.assertTrue(self.check(item))

    def test_malformed_entries_report_index_without_mutating_record(self):
        for value in [None, {}, 'text', [None], ['text']]:
            with self.subTest(value=value):
                record = {'incident_artefacts': value}
                before = copy.deepcopy(record)
                errors = self.errors(record)
                self.assertTrue(errors)
                self.assertEqual(record, before)
                self.assertTrue(all('VIGIL-INC-000043.json: incident_artefacts' in e for e in errors))

    def test_full_canonical_validator_blocks_invalid_media(self):
        errors, _ = v.validate_record(Path('fixture.json'), {
            'record_type': 'incident', 'incident_artefacts': [artefact('md', 'image/png')]})
        self.assertTrue(any('incident_artefacts[0].render_url/media_type' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
