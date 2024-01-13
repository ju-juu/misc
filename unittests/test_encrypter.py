import os

import pytest

from crypto.encrypter import Encrypter

DIRECTORY = '../target'
TEST_FILE_NAME = 'moby.txt'


@pytest.fixture
def encrypter():
    yield Encrypter(key_file_path='test.key')


def test_generate_key(encrypter):
    assert len(encrypter.encryption_key) > 35


def test_encrypt_file(encrypter):
    assert encrypter.encrypt_file(f'{DIRECTORY}/{TEST_FILE_NAME}') > 0


def test_decrypt_file(encrypter):
    assert encrypter.decrypt_file(f'{DIRECTORY}/{TEST_FILE_NAME}') > 0


def test_encrypt_decrypt_files(encrypter):
    files_to_process = encrypter.traverse_directory_iteratively(DIRECTORY)
    assert len(files_to_process) > 0

    total_encrypted = 0
    total_decrypted = 0
    for file_name in files_to_process:
        file_path = os.path.join(DIRECTORY, file_name)

        if os.path.isfile(file_path):
            total_encrypted += encrypter.encrypt_file(file_name)
            total_decrypted += encrypter.decrypt_file(file_name)

    assert total_encrypted > 0 and total_decrypted > 0
