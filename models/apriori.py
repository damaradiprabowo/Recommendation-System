# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:21:08 2019

@author: damara064128
"""

from apyori import apriori

class Apriori(): 
    
    #Constructor to initialize the instance members of the class
    def __init__ (self,  support=0.05,  confidence=0.05, lift=1, length=1): 
        self.min_support = support 
        self.min_confidence = confidence
        self.min_lift = lift
        self.min_length = length
    
    #Function to find the association rules with apriori
    def main(self, data): 
        rows_count = data.shape[0]
        columns_count = data.shape[1]

        records = []
        for i in range(rows_count):
            records.append([str(data.values[i,j]) for j in range(columns_count)])

        self.association_rules = apriori(records, min_support=self.min_support, min_confidence=self.min_confidence, min_lift=self.min_lift, min_length=self.min_length)
        self.association_results = list(self.association_rules)
    
    #Function to show the result
    def result(self):
        for item in self.association_results:
            pair = item[0] 
            items1 = [x for x in pair]

            if len(items1) == 2:
                print("Rule: " + items1[0] + " -> " + items1[1])
            elif len(items1) == 3:
                print("Rule: " + items1[0] + " -> " + items1[1] + " -> " + items1[2])

            print("Support: " + str(item[1]))
            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")