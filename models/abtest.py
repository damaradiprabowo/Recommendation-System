# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:00:47 2019

@author: damara064128
"""

import statsmodels.api as sm

class ABTesting():

    def __init__(self, p_value):
        self.p_value = p_value

    def fit(self, df):
        # calculate click page from old and new page, also calculate the number of old and new page
        self.click_old = (df.query('landing_page=="old_page"')['action']=='click').sum()
        self.click_new = (df.query('landing_page=="new_page"')['action']=='click').sum()
        self.page_old = (df['landing_page']=='old_page').sum()
        self.page_new=(df['landing_page']=='new_page').sum()

    def predict(self):
        # calculate z_score and p_value
        z_score, p_value = sm.stats.proportions_ztest([self.click_new, self.click_old], [self.page_new, self.page_old], alternative='smaller')
        print('The p-value is', p_value)
        if p_value > self.p_value:
            print('P-value is higher than ',self.p_value,', so the H0 is not rejected')
        else:
            print('P-value is lower than ',self.p_value,', so the H0 is rejected')