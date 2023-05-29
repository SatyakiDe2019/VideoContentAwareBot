################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 28-May-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal OpenAI-based video content    ####
#### enable bot.                            ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'MODEL_PATH': Curr_Path + sep + 'model' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'MODEL_DIR': 'model',
        'APP_DESC_1': 'LangChain Demo!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'Output.csv',
        'MODEL_NAME': 'gpt-3.5-turbo',
        'OPEN_AI_KEY': "sk-kfrjfijdrkidjkfjd9474nbfjfkfjfhfhf84i84hnfhjdbv6Bgvv",
        'YOUTUBE_KEY': "AIjfjfUYGe64hHJ-LOFO5u-mkso9pPOJGFU",
        'TITLE': "LangChain Demo!",
        'TEMP_VAL': 0.2,
        'PATH' : Curr_Path,
        'MAX_CNT' : 5,
        'OUT_DIR': 'data'
    }
