#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
from langdetect import detect

MUSIC_DIR = 'C:\\Python_Env\\SERIOUS_SHIT\\SCHOOL\\MUSIC'

os.chdir(MUSIC_DIR)

def get_lang(text):
    """
    get language from string input.
    """
    try:
        return detect(text)
    except:
        return None

_ = pd.read_csv('C:\\Python_Env\\SERIOUS_SHIT\\SCHOOL\\MUSIC\\lyrics.csv')

def file_clean(_):
    """import godamn file"""
    _['LANG'] = _['lyrics'].apply(lambda lyrics: get_lang(lyrics))
    _ = _.drop('index', axis=1)
    _ = _.drop(_[(_.LANG != 'en')].index)
    _ = _.drop(_[(_.genre == 'Not Available')|(_.genre == 'Other')|(_.genre == 'Electronic')].index)
    _ = _.drop(_[(_.lyrics == 'INSTRUMENTAL')|(_.lyrics == '[INSTRUMENTAL]')\
            |(_.lyrics == '(INSTRUMENTAL)')|(_.lyrics == 'INSTRU')].index)
    _ = _.groupby('genre', group_keys=False).apply(lambda x: x.sample(1000))
    _.reset_index(drop=True, inplace=True)
    return _

TRAINING_SET = file_clean(_)

TRAINING_SET.dropna().to_excel(MUSIC_DIR+'\\'+'TRAIN_SET.xlsx', index=False)
