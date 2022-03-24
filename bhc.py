from setuptools import setup, Extension

setup(
    name='bhash',
    version='1.0',
    ext_modules=[
        Extension('bhash', ['bhash.c'])
    ]
)