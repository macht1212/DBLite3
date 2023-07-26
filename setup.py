from setuptools import setup
from DBLite3 import __version__, __author__, __email__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="DBLite3",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="NoSQL database",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/macht1212/LiteDB/",
    download_url="https://github.com/macht1212/LiteDB/archive/{}.tar.gz".format(__version__),
    packages=['DBLite3'],
    package_data={'DBLite3': ['__init__.py']},
    keywords=['database', 'nosql', 'litedb', 'json'],
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
