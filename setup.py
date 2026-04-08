#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hashcheck",
    version="1.0.0",
    author="Viktor Tsedrik",
    author_email="viktor_freelance@proton.me",
    description="Утилита для проверки хэш-сумм файлов с поддержкой множества алгоритмов",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/purposefulman/hashcheck",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "hashcheck=hashcheck.main:main",
        ],
    },
)