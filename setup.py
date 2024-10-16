# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from distutils.util import convert_path


_package_name = "my_template"

_namespace_dict = {}
_version_path = convert_path(f"{_package_name}/__version__.py")
with open(_version_path) as _version_file:
    exec(_version_file.read(), _namespace_dict)
_package_version = _namespace_dict["__version__"]

setup(
    name=_package_name,
    packages=find_packages(),
    version=f"{_package_version}",
    license="MIT",
    description=f"'{_package_name}' is a template for python package.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Asadbek Kiyomov",
    author_email="asadbey0331@gmail.com",
    url="https://github.com/akiyomov/module.python-template",
    download_url=f"https://github.com/akiyomov/module.python-template/archive/v{_package_version}.tar.gz",
    keywords=[
        _package_name,
        "template",
        "python",
        "package",
        "module",
    ],
    python_requires=">=3.7",
    install_requires=[
        # "pydantic[email]>=2.1.1,<3.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
