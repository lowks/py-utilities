#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
import hashlib
import os


def concat(filenames, outfile_path):
    """
    Concatenates filename contents to outfile_path
    """
    with open(outfile_path, 'w') as f:
        for line in fileinput.input(filenames):
            f.write(line)


def file_ext(file_path):
    """
    Returns the file extension at file_path

    >>> file_ext('/foo/bar/what/temp.txt')
    '.txt'

    >>> file_ext('/foo/bar/what/temp.jpg')
    '.jpg'

    >>> file_ext('/foo/bar/what/temp.tar.gz')
    '.gz'

    >>> file_ext('/foo/bar/what/temp')
    ''

    >>> file_ext('')
    ''

    """
    return os.path.splitext(file_path)[-1]


def file_hexdigest(file_path, algo='md5'):
    """
    Returns the hexdigest hash of file_path using algo
    """
    hash = getattr(hashlib, algo)()

    with open(file_path, 'rb') as f:
        hash.update(f.read())
    return hash.hexdigest()


# vim: filetype=python