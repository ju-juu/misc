from cx_Freeze import setup, Executable

executables = [Executable('launch.py')]

options = {
    'build_exe': {
        'includes': [],
    }
}

setup(
    name='EncrypterApp',
    version='1.0',
    description='Will recursively encrypt and then decrypt files in a directory.',
    executables=executables,
    options=options
)
