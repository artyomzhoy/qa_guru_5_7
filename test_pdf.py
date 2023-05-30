import os

from pypdf import PdfReader

from os_path_scripts import PROJECT_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf():
    pdf_path = os.path.join(PROJECT_ROOT_PATH, 'resources', 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    assert number_of_pages == 412
    assert 'pytest Documentation' in text
