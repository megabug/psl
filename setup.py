#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from setuptools import setup

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except:
    description = codecs.open('README.md', encoding='utf-8').read()

setup(name="publicsuffixlist",
      version="0.5.0",
      packages=["publicsuffixlist"],
      package_data={
          "publicsuffixlist": [
              "public_suffix_list.dat",
              "test_psl.txt",
          ]},
      author="ko-zu",
      author_email="causeless@gmail.com",
      description="publicsuffixlist implement",
      long_description=description,
      url="https://github.com/ko-zu/psl",
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
          "Topic :: Internet :: Name Service (DNS)",
          "Topic :: Text Processing :: Filters",
          "Operating System :: OS Independent",

        ],
      )
