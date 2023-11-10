#!/usr/bin/env python3

import os
from shutil import make_archive


os.makedirs('./output/', exist_ok=True)

make_archive(
    base_name='./output/botanico.tdesktop-theme',
    format='zip',
    root_dir='./src/'
)

os.rename(
    './output/botanico.tdesktop-theme.zip',
    './output/botanico.tdesktop-theme'
)
