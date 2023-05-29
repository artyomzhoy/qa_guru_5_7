import os
import time

from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from os_path.os_path_scripts import PROJECT_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_file_with_browser():
    tmp = os.path.join(PROJECT_ROOT_PATH, '..', 'tmp')
    if not os.path.exists(tmp):
        os.mkdir(tmp)

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp,
        "download.prompt_for_download": False,
    }

    options.add_argument("--headless=old")
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open('https://github.com/pytest-dev/pytest')
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(10)

    download_file = os.path.join(tmp, 'pytest-main.zip')
    assert os.path.exists(download_file)

