import os.path
import requests
from os_path_scripts import PROJECT_ROOT_PATH


def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь

    tmp = os.path.join(PROJECT_ROOT_PATH, 'tmp')
    if not os.path.exists(tmp):
        os.mkdir(tmp)

    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    saved_file = os.path.join(tmp, 'saved_file.png')

    r = requests.get(url)
    with open(saved_file, 'wb') as file:  # w - write, wb - write bytes
        file.write(r.content)

    size = os.path.getsize(saved_file)

    assert size == 30803
