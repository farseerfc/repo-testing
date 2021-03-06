#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'


def pre_build():
    pypi_pre_build(
        depends=['python', 'python-terminaltables', 'python-tabulate'],
        license='BSD')


def post_build():
    pypi_post_build()


if __name__ == '__main__':
    single_main()
