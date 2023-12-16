import os

import pytest

from crypto.encrypter import Encrypter


@pytest.fixture
def encrypter():
    yield Encrypter(key_file_path='test.key')


def test_generate_key(encrypter):
    assert len(encrypter.encryption_key) > 35


def test_encrypt_file(encrypter):
    assert encrypter.encrypt_file('target/moby.txt') > 0


def test_decrypt_file(encrypter):
    assert encrypter.decrypt_file('target/moby.txt') > 0


def test_bulk_encrypt_decrypt(encrypter):
    directory_list = os.listdir('target')
    assert len(directory_list) > 0
    assert (sum([encrypter.encrypt_file(f'target/{file_name}') for file_name in directory_list]) >
            sum([encrypter.decrypt_file(f'target/{file_name}') for file_name in directory_list]))
