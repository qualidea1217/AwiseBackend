#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:28:33 2022

@author: chrisfeng
"""

import pandas as pd
import numpy as np
import sqlite3

dbFile = "/Users/chrisfeng/Desktop/AwiseBackend/db.sqlite3"
con = sqlite3.connect(dbFile)


user_data = ["user_id", "getup_time", "bed_time", "social", "academic",
             "bring_people", "animal", "instrument", "cleaning",
             "cook", "share", "smoke", "alcohol", "getup_time_w", "bed_time_w", 
             "social_w", "academic_w",
                    "bring_people_w", "animal_w", "instrument_w",
                    "cleaning_w", "cook_w", "share_w", "smoke_w",
                    "alcohol_w"]

df = pd.DataFrame(np.random.randint(1,10,size=(500, 25)), columns= user_data)

df['user_id'] = df.index


df.to_sql('surve_survey', con, if_exists='replace', index = False)


con.close()

