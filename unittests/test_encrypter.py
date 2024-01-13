import os

import pytest

from crypto.encrypter import Encrypter

directory = 'target'


@pytest.fixture
def encrypter():
    yield Encrypter(key_file_path='test.key')


def test_generate_key(encrypter):
    assert len(encrypter.encryption_key) > 35


def test_encrypt_file(encrypter):
    assert encrypter.encrypt_file(f'{directory}/moby.txt') > 0


def test_decrypt_file(encrypter):
    assert encrypter.decrypt_file(f'{directory}/moby.txt') >0


def test_bulk_encrypt_decrypt(encrypter):
    """ encrypts all files in a target directory and checks the output length then subsequently decrypts the files
     checking the output length and ensuring the post decryption value is less than the encrypted value. """
    directory_list = os.listdir('target')
    assert len(directory_list) > 0
    assert (
            sum([encrypter.encrypt_file(f'{directory}/{file_name}') for file_name in directory_list]) >
            sum([encrypter.decrypt_file(f'{directory}/{file_name}') for file_name in directory_list])
    )
