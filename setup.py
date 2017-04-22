from setuptools import setup

setup(
    name='pdf-processor',
    version='0.1',
    py_modules=['idk'],
    install_requires=[
        'Click',
        'PyPDF2',
    ],
    entry_points='''
        [console_scripts]
        pdfsort=pdfsort:cli
    ''',
)
