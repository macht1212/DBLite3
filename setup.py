from setuptools import setup, find_packages
from NoSQLite3 import __version__, __author__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="NoSQLite3",
    version=__version__,
    author=__author__,
    author_email='nasimov.alexander@gmail.com',
    description="NoSQL database",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/macht1212/LiteDB/",
    download_url="https://github.com/macht1212/LiteDB/archive/{}.tar.gz".format(__version__),
    packages=['NoSQLite3'],
    package_data={'NoSQLite3': ['__init__.py']},
    keywords=['database', 'nosql', 'litedb'],
    license="MIT license",
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ]
)
