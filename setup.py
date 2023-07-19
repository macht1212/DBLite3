from setuptools import setup
from LiteDB import __version__, __author__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="LiteDB",
    version=__version__,
    author=__author__,
    author_email="nasimov.alexander@gmail.com",
    description="NoSQL database",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/macht1212/LiteDB/",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: MIT",
    ],
)