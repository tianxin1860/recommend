#!/usr/bin/env python
# coding=utf-8



import csv

def read_user_item():
    user_item = {}
    '''read user_item.csv to ensure a user have never bought a item'''
    with open('user_item.csv','rb') as train_file:
        reader = csv.reader(train_file)
        for line in reader:
                user, item =  line[0].strip("()").split(',')
                user_id =  user.strip("'") 
                item_id =  item.strip(" '")
                value =  line[1].strip("()").split(',')
                key = (user_id, item_id)
                user_item[key] = value
            
    return user_item


