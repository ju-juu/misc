import os

from crypto.encrypter import Encrypter


def encrypt_decrypt_files(directory):
    encrypter = Encrypter(key_file_path='test.key')
    files_to_process = encrypter.traverse_directory_iteratively('target')
    assert len(files_to_process) > 0
    total_encrypted = 0
    total_decrypted = 0
    for file_name in files_to_process:
        file_path = os.path.join(directory, file_name)

        if os.path.isfile(file_path):
            total_encrypted += encrypter.encrypt_file(file_name)
            total_decrypted += encrypter.decrypt_file(file_name)

    assert total_encrypted > 0 and total_decrypted > 0
    print(f'Total encrypted characters: {total_encrypted}')
    print(f'Total decrypted characters: {total_decrypted}')


if __name__ == '__main__':
    encrypt_decrypt_files(os.getcwd())
