import pandas as pd
import numpy as np
from sklearn import preprocessing
import os
import sys
"""
134turbs*184days*24h*6 = 3550464 samples
26496samples for each turb

Caveats:
    1.Zero values: if πππ‘π£ < 0, then πππ‘π£ = 0.
    2.Missing values: ππ‘0+π is a missing value, set |ππ‘0+π β πΛπ‘0+π | = 0
    3.Unknown values: metrics treated as missing values
        (1)πππ‘π£ β€ 0 && ππ ππ > 2.5
        (2)ππππ1 > 89β¦ || ππππ2 > 89β¦ || ππππ3 > 89β¦
"""

sys.argv[0]

original_data = pd.read_csv('sdwpf134_initial_kddcup.csv')
df = original_data.copy()
def value_correction(self):
    self.loc[self['Patv'] < 0, 'Patv'] = 0 # zero values
    self.loc[(self['Pab1'] > 89) | (self['Pab2'] > 89) | (self['Pab3'] > 89),'Patv'] = 0 #unknown values(1)
    self.loc[(self['Patv']<=0) & (self['Wspd']>2.5),'Patc'] = 'ukn'

value_correction(df)   

full_data = pd.read_csv('sdwpf_baidukddcup2022_full_original.CSV')
# ζ₯ηζ―δΈͺturbηmissing dataζ°ι
def get_missing(self):
    for i in range(1,135):
        n = self.loc[(self['Patv'].isnull()) & (self['TurbID']==i)].shape[0]
        print('Turb', i, ':', n)
get_missing(full_data)
