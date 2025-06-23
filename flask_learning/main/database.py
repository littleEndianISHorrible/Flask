#the taskmannager must track what tasks i have done and give quizetime hence add stuff
#assign tasks
#save tasks

#schedual things
import numpy as np
import pandas as pd
def adduser():
    return 0
def schedule():
    return 0
class autotasks:
    timestart=0
    timeend=0
    date=0
    name=0
    complete=False
    description = "defult task"
    def __init__(self, atimestart, atimeend, adate, aname, acomplete, adescription):
        timestart = atimestart
        timeend = atimeend
        date = adate
        name = aname
        complete = acomplete
        description = adescription
    def appendtodataframe(self, filename):
        df = pd.dataframe()
