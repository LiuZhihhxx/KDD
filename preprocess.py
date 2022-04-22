import pandas as pd
import numpy as np
from sklearn import preprocessing
import os
import sys
"""
134turbs*184days*24h*6 = 3550464 samples
26496samples for each turb

Caveats:
    1.Zero values: if 𝑃𝑎𝑡𝑣 < 0, then 𝑃𝑎𝑡𝑣 = 0.
    2.Missing values: 𝑝𝑡0+𝑗 is a missing value, set |𝑝𝑡0+𝑗 − 𝑝ˆ𝑡0+𝑗 | = 0
    3.Unknown values: metrics treated as missing values
        (1)𝑃𝑎𝑡𝑣 ≤ 0 && 𝑊𝑠𝑝𝑑 > 2.5
        (2)𝑃𝑟𝑎𝑏1 > 89◦ || 𝑃𝑟𝑎𝑏2 > 89◦ || 𝑃𝑟𝑎𝑏3 > 89◦
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
# 查看每个turb的missing data数量
def get_missing(self):
    for i in range(1,135):
        n = self.loc[(self['Patv'].isnull()) & (self['TurbID']==i)].shape[0]
        print('Turb', i, ':', n)
get_missing(full_data)
