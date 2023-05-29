#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 27-May-2023                     ####
#### Modified On 28-May-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### clsVideoContentScrapper class to extract    ####
#### the transcript from the YouTube videos.     ####
####                                             ####
#####################################################

import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime
import textwrap

import clsVideoContentScrapper as cvsc

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Get your global values        ####
######################################
debug_ind = 'Y'

# Initiating Logging Instances
clog = cl.clsL()

data_path = cf.conf['DATA_PATH']
data_file_name = cf.conf['FILE_NAME']

cVCScrapper = cvsc.clsVideoContentScrapper()

######################################
####         Global Flag      ########
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        #query = "What are they saying about Microsoft?"
        print('Please share your topic!')
        inputTopic = input('User: ')
        print('Please ask your questions?')
        inputQry = input('User: ')
        print()

        retList = cVCScrapper.extractContentInText(inputTopic, inputQry)
        cnt = 0

        for discussedTopic in retList:
            finText = str(cnt + 1) + ') ' + discussedTopic
            print()
            print(textwrap.fill(finText, width=150))

            cnt += 1

        r1 = len(retList)

        if r1 > 0:
            print()
            print('Successfully Scrapped!')
        else:
            print()
            print('Failed to Scrappe!')

        print('*'*120)
        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
