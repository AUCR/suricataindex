"""The suricataindex python package."""
# coding=utf-8
import os
from setuptools import setup, find_packages
from suricataindex import __version__

setup(
    name="suricataindex",
    version=__version__,
    packages=find_packages(exclude=['docs', 'tests', 'tools', 'utils']),
    url="https://github.com/aucr/suricataindex/",
    license='Apache 2.0',
    author="Wyatt Roersma",
    author_email="wyatt@aucr.io",
    description="This is the Python library to index suricata alert json data into elasticsearch.",
    include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache 2.0',
                 'Programming Language :: Python :: 3.8'],
    package_data={
        'suricataindex': ['*.txt']
    },
    scripts=['suricataindex/sur_cli.py'],
    )
