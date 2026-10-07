"""Packaging (skeleton, deps only)."""

from setuptools import find_packages, setup  # type: ignore  # pylint: disable=import-error

setup(
    name="my-voice",
    version="0.1.0",
    packages=find_packages(include=["src", "src.*"]),
    python_requires="==3.14.8",
    install_requires=[
        "torch==2.14.1",
        "torchaudio==2.11.0",
        "f5-tts==1.1.22",
        "omnivoice==0.2.1",
        "pyyaml==6.0.3",
    ],
    extras_require={
        "dev": ["pytest==9.1.1", "pylint==4.1.2"],
    },
)
