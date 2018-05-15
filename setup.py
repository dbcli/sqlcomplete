import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("sqlcomplete/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

description = "SQL Completion Engine"

install_requirements = ["sqlparse >=0.2.2,<0.3.0"]


setup(
    name="sqlcomplete",
    author="DBCLI Core team",
    author_email="pgcli-dev@googlegroups.com",
    version=version,
    license="BSD",
    url="https://www.dbcli.com",
    packages=find_packages(),
    package_data={"sqlcomplete": ["literals/sqlliterals.json"]},
    description=description,
    long_description=open("README.md").read(),
    install_requires=install_requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: SQL",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
