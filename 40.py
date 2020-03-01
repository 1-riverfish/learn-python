#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'file io'

__author__ = 'Ncplain(North China Plain)'

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r', errors='ignore') as f:
    s = f.read()
    print(s)
