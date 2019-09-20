# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:20:27 2019

@author: damara064128
"""

import pandas as pd
import sys
import os
import json

os.chdir('models')
dir = os.getcwd()
sys.path.insert(0, dir)

##from apriori import Apriori
##from collaborative import Collaborative
##from content import ContentBased
#from hybrid import Hybrid
##from abtest import ABTesting


os.chdir('../dataset')
dir = os.getcwd()
sys.path.insert(0, dir)

df_apriori = pd.read_csv('apriori_dataset.csv',sep=';')
with open('collaborative_dataset.json', 'r') as f:
    df_collab = json.load(f)
df_content = pd.read_csv('content_dataset.csv')
df_hybrid = pd.read_csv('hybrid_dataset.csv',sep=';')

print('Association rule with apriori: ')
apr = Apriori(support=0.1,  confidence=0.1)
apr.main(df_apriori)
apr.result()

print('Collaborative Filtering: ')
collab = Collaborative(df_collab)
recommendation, score = collab.user_recommendations('ANI')
print('user recommendation for ANI with score: ', score)
print('user correlation score between ANI and Dpv: ', collab.person_correlation('ANI', 'Dpv'))
print('users who have similarities with ANI in genre film: ', collab.most_similar_users('ANI',1))

print('Recommendation with content based: ')
content = ContentBased(df_content)
print(content.predict('Avenger'))

print('Recommendation for ANI with hybrid algorithm:')
hybrid = Hybrid(film=df_hybrid, dataset=df_collab)
print(hybrid.predict())