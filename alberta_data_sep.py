# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:26:24 2022

@author: kmahadevan
"""

import pandas as pd
import numpy as np

df = pd.read_csv ("Aquanty_daily_data_2010_+.csv")
df2 = pd.DataFrame()
df1 = pd.DataFrame(df.STATION.unique())

for i in range (0, len(df1)):
    
    df2 = df[df.STATION == df1[0][i]]
    df2.to_csv(df1[0][i]+".csv")
    
    
    
    
    
   












