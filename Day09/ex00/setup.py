from setuptools import setup, Extension

setup(
    name="calculator",
    version="1.0",
    description="This is a calculator module",
    author="Kcrius",
    author_email="rustik031rus@mail.ru",
    ext_modules=[
        Extension('calculator', sources=["calculator.c"])
    ])
