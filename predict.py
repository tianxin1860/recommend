#!/usr/bin/env python
# coding=utf-8

#author:tianxin

#_DEBUG = True
_DEBUG = False

import csv
from collections import defaultdict
import gl
import numpy as np
import scipy as sp
import scipy.sparse.linalg 

#import numpy as np


class Behavior(object):
    look = 0
    collect = 0
    add = 0
    buy = 0


UserDict = {}
ItemDict = {}
UserItem = defaultdict(Behavior)
UserItemFinal = {}


def BuildDict():
    with open('tianchi_mobile_recommend_train_user.csv','rb') as train_file:
    #with open('user.csv','rb') as train_file:
        reader = csv.reader(train_file)
        for list in reader:
            #list = line.split(',')
            UserID = list[0]
            ItemID = list[1]
            type = list[2]
            UserPos = list[3]
            ItemCate = list[4]
            time = list[5]
            UserDict[UserID] = (UserPos)
            ItemDict[ItemID] = (ItemCate)

            key = (UserID, ItemID)
            if type == '1':
                UserItem[key].look += 1
            elif type == '2':
                UserItem[key].collect += 1
            elif type == '3':
                UserItem[key].add += 1
            elif type == '4':
                UserItem[key].buy += 1
    for key in UserItem.keys():
        UserItemFinal[key] = (UserItem[key].look, UserItem[key].collect, UserItem[key].add, UserItem[key].buy)



def SaveUserPos(): 
    userfile = file('user_pos.csv', 'wb')
    writer = csv.writer(userfile)
    userdata = UserDict.items()
    writer.writerows(userdata)
    userfile.close()

def SaveItemCate():    
    itemfile = file('item_cate.csv', 'wb')
    writer = csv.writer(itemfile)
    itemdata = ItemDict.items()
    writer.writerows(itemdata)
    itemfile.close()

def SaveUserItem():    
    useritem = file('user_item.csv', 'wb')
    writer = csv.writer(useritem)
    itemdata = UserItem.items()
    writer.writerows(itemdata)
    useritem.close()

def SaveMatrix():    
    rating = file('matrix.csv', 'wb')
    writer = csv.writer(rating)
    itemdata = UserItem.items()
    writer.writerows(itemdata)
    useritem.close()

def SaveInfo():    
    SaveUserItem()
    

def ComputeRating(row, column):
    user = gl.UserList[row]
    item = gl.ItemList[column]
    key = (user, item)
    if key in UserItemFinal:
        if UserItemFinal[key][3] >= 1:
            return 5
        elif UserItemFinal[key][2] >= 1:
            return 4
        elif UserItemFinal[key][1] >= 1:
            return 3
        elif UserItemFinal[key][0] >= 2:
            return 2
        elif UserItemFinal[key][0] == 1:
            return 1
        else:
            return 0
    else:
        return 0


def StandardSort():
    gl.UserList = UserDict.keys()
    gl.ItemList = ItemDict.keys()
    if _DEBUG == True:
        print "User number:%d" %len(gl.UserList)
        print "Item number:%d" %len(gl.ItemList)
    gl.UserList.sort()
    gl.ItemList.sort()


def BuildMatrix():
    rows = len(UserDict)
    cols = len(ItemDict)
    if _DEBUG == True:
        print "rows:%d" %rows
        print "cols:%d" %cols
    matrix = [[0 for col in range(cols)] for row in range(rows)] 
    for i in range(rows):
        for j in range(cols):
            rating = ComputeRating(i, j)
            matrix[i][j] = rating
            print matrix[i][j],
        print "\n"


def ReadMatrix():
    '''read data to return matrix'''
    matrix = []    
    with open('matrix.txt','r') as InputFile:
            line = InputFile.readline()
            #i = 0
            #while i < 20:
            while line:
                line = line.strip().split(' ')
                row = map(int, line)
                matrix.append(row)
                line = InputFile.readline()
                #i += 1
            return matrix

def SVD(X):            
        #U, S, V = np.linalg.svd(X, full_matrices=False)
        U, S, V = scipy.sparse.linalg.svds(X, k=10)
        Ufile = open('u.txt','w')
        Sfile = open('s.txt','w')
        Vfile = open('v.txt','w')
        for i in range(U.shape[0]):
                Ufile.write(str(U[i]))
                Ufile.write('\n')
        for i in range(V.shape[0]):
                Vfile.write(str(V[i]))
                Vfile.write('\n')
        Sfile.write(str(S))
        #Sfile.write('\n')        


def ComputeSimi():
        data = ReadMatrix()
        matrix = np.array(data)
        print matrix.shape

#BuildDict()
#StandardSort()
#BuildMatrix()
#ComputeSimi()        
data = ReadMatrix()
matrix = np.array(data, dtype=float)
#print matrix
SVD(matrix)
