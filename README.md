# Encrypter

This service takes a file and encrypts it. The module currently supports Fernet which is
a common symmetric encryption algorithm using Cipher Block Chaining (CBC) with a 128-bit key.

The module is intended to be extended to support multiple encryption modules.

I have included unit tests that can be run against some mock data in unitests/target folder.

```python
pytest -rP unittests/test_encrypter.py
```
