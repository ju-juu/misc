# Encrypt/Decrypt

This service takes a file and encrypts it. The module currently supports Fernet which is
a common symmetric encryption algorithm using Cipher Block Chaining (CBC) with a 128-bit key.

The module is intended to be extended to support multiple encryption modules.

I have included unit tests that can be run against some mock data in `target` folder.

Notably if you encrypt your files, and lose your encryption key, you're not going to have a great day.

Additionally, if you encrypt your files multiple times, you will need to decrypt them multiple times. 

### Running Unit Tests

Install Requirements:
```python
pip install -r requirements.txt
```
Run Tests: 
```python
pytest -rP unittests/test_encrypter.py
```


### Building the service to run as an executable

Using the cx_Freeze module we can build a binary for portability. The binary created is compiled using the 
systems OS that it was created on, so if you compile it in a WSL environment it will be executable in a similar
environment, likewise for Windows.

Create the executable:
```python
python setup.py build
```

Run the executable: 
```python
./build/exe.linux-x86_64-3.11/launch
```
