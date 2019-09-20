# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:20:27 2019

@author: damara064128
"""

import pandas as pd
import sys
import os

os.chdir('models')
dir = os.getcwd()
sys.path.insert(0, dir)

from apriori import Apriori
from collaborative import Collaborative
from content import ContentBased
from hybrid import Hybrid
from abtest import ABTesting

#change dir to main folder for geting a dataset in Dataset directory
os.chdir('../dataset')#change dir to Dataset folder for geting a dataset in that directory
dir = os.getcwd()
sys.path.insert(0, dir)

df_apriori = pd.read_csv('apriori_dataset.csv')


print('+ Association with apriori: ')
apr = Apriori('Watch')
apr.main(df_apriori)
apr.result()

##Content based
#print('+ Recommendation by content based Avenger: ')
#content = ContentBased(df_content)
#print(content.predict('Avenger'))
#
#print('=====================================')
##Collaborative
#print('+ Collaborative Filtering: ')
#julcollab = JulCollaborative(dataset)
#recommendation, score = julcollab.user_recommendations('Dpv')
#print('user recommendation for Dpv with score: ', score)
#print('user correlation score between Dpv and Star: ', julcollab.person_correlation('Dpv', 'Star'))
#print('users who have similarities with Dpv in genre film: ', julcollab.most_similar_users('Dpv',2))
#
#print('=====================================')
##Hybrid
#print('+ Recommendation user jul with hybrid algorithm (minimumscore = 0.1):')
#julhybrid = JulHybrid(film=df_hybrid2, dataset=dataset)
#print(julhybrid.predict())