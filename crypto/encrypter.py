import os.path

from cryptography.fernet import Fernet


class Encrypter:

    def __init__(self, key_file_path):
        self.key_file_path = key_file_path
        self.encryption_key = self._set_key()
        self.crypto = Fernet(self.encryption_key)

    def _set_key(self):
        return self._get_existing_key() if self._get_existing_key() else self._generate_key()

    def _get_existing_key(self) -> bytes:
        if os.path.exists(self.key_file_path):
            return self._read_file(self.key_file_path)

    def _generate_key(self) -> bytes:
        key = Fernet.generate_key()
        if self._write_file(self.key_file_path, key):
            return key

    def encrypt_file(self, file_path: str) -> int:
        file_data = self._read_file(file_path)
        encrypted_data = self.crypto.encrypt(file_data)
        return self._write_file(file_path, encrypted_data)

    def decrypt_file(self, file_path: str) -> int:
        encrypted_data = self._read_file(file_path)
        decrypted_data = self.crypto.decrypt(encrypted_data)
        return self._write_file(file_path, decrypted_data)

    @staticmethod
    def _read_file(file_path: str):
        with open(file_path, 'rb') as file:
            return file.read()

    @staticmethod
    def _write_file(file_path: str, data: any):
        with open(file_path, 'wb') as file:
            return file.write(data)
