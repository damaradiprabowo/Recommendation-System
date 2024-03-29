# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:20:27 2019

@author: damara064128
"""

from math import sqrt
import json
 
class Collaborative(object):

    def __init__(self, dataset):
        self.dataset = dict()
        print(len(dataset))
        for idx in dataset:
            self.dataset[idx] = dict()
            for movie in (dataset[idx]):
                if dataset[idx][movie] != 0:
                    self.dataset[idx][movie] = dataset[idx][movie]


    def similarity_score(self, person1, person2):

        # this Returns the ration euclidean distancen score of person 1 and 2

        # To get both rated items by person 1 and 2
        both_viewed = {}

        for item in dataset[person1]:
            if item in dataset[person2]:
                both_viewed[item] = 1
            
            # The Conditions to check if they both have common rating items
            if len(both_viewed) == 0:
                return 0

            # Finding Euclidean distance
            sum_of_eclidean_distance = []

            for item in dataset[person1]:
                if item in dataset[person2]:
                    sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item], 2))
            sum_of_eclidean_distance = sum(sum_of_eclidean_distance)
            
            return 1/(1+sqrt(sum_of_eclidean_distance))

    def person_correlation(self, person1, person2):

       # To get both rated items
        both_rated = {}
        for item in self.dataset[person1]:
            if item in self.dataset[person2]:
                both_rated[item] = 1

        number_of_ratings = len(both_rated)

        # Checking for ratings in common
        if number_of_ratings == 0:
            return 0

        # Add up all the preferences of each user
        person1_preferences_sum = sum([self.dataset[person1][item] for item in both_rated])
        person2_preferences_sum = sum([self.dataset[person2][item] for item in both_rated])

        # Sum up the squares of preferences of each user
        person1_square_preferences_sum = sum([pow(self.dataset[person1][item],2) for item in both_rated])
        person2_square_preferences_sum = sum([pow(self.dataset[person2][item],2) for item in both_rated])

        # Sum up the product value of both preferences for each item
        product_sum_of_both_users = sum([self.dataset[person1][item] * self.dataset[person2][item] for item in both_rated])

        # Calculate the pearson score
        numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
        denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))

        if denominator_value == 0:
            return 0
        else:
            r = numerator_value / denominator_value
            return r

    def most_similar_users(self, person, number_of_users=24):

        # returns the number_of_users (similar persons) for a given specific person
        scores = [(self.person_correlation(person, other_person), other_person) for other_person in self.dataset if other_person != person]

        # Sort the similar persons so the highest scores person will appear at the first
        scores.sort()
        scores.reverse()
        return scores[0:number_of_users]
            
    def user_recommendations(self, person):
        # Gets recommendations for a person by using a weighted average of every other user's rankings
        totals = {}
        simSums = {}
        #rankings_list =[]
        for other in self.dataset:
            # don't compare me to myself
            if other == person:
                continue
            sim = self.person_correlation(person, other)
            #print ">>>>>>>",sim

            # ignore scores of zero or lower
            if sim <=0: 
                continue
            for item in self.dataset[other]:

                # only score movies i haven't seen yet
                if item not in self.dataset[person] or self.dataset[person][item] == 0:

                # Similrity * score
                    totals.setdefault(item,0)
                    totals[item] += self.dataset[other][item]* sim
                    # sum of similarities
                    simSums.setdefault(item,0)
                    simSums[item]+= sim

            # Create the normalized list

        rankings = [(total/simSums[item],item) for item,total in totals.items()]
        rankings.sort()
        rankings.reverse()
        # returns the recommended items
        recommendataions_list = [recommend_item for score,recommend_item in rankings]
        
        return recommendataions_list, rankings
            
    def main():
        #optParser = OptionParser()

        #optParser.add_option('-n', '--nama', dest='nama',
         #   help='Nama pelanggan',
          #  type='string',
           # default=None)

        #(options, args) = optParser.parse_args()
        #nama = options.nama
        recommendation = self.user_recommendations('Damar Teman Firli')
        #print('Recommendation for jul: ',recommendation)
        return recommendation
        #print('Person correlation: ',person_correlation('jul','Hania'))
        #print('Similarity score: ',similarity_score('jul','Hania'))
        #print('most similar person to jul: ',most_similar_users('jul',24))

