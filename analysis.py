#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import genfromtxt
import numpy as np
import csv
import collections
def _loadcvsForFeautreAnalysis(fileName="Members.csv"):
    """
    return dict for basic feature analysis
    """
    f=open(fileName)
    data=f.read()
    f.close()
    items=data.split("\r\n")
    result={}
    indexCount={}
    for i, val in enumerate(items):
        fields=val.split(",")        
        if i==0:
            for j,f in enumerate(fields):
                indexCount[j]=f
                result[f]=[]            
        else:
            for j,f in enumerate(fields):                
                result[indexCount[j]].append(f)
    return result

def _getCategoricalfeatures(DataList,DictEnable=True):
    """
    http://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features
    """
    s=set(DataList)
    l=list(s)
    l.sort()
    if DictEnable:
        d=dict(enumerate(l))
        res = dict((v,k) for k,v in d.iteritems())
        return res
    else:
        return l


    
def convertField(x,mappingList):
    return mappingList.index(x)
    

def loadcsv(fileName="Members.csv"):    
    #persontype = np.dtype({'names':['MemberID','AgeAtFirstClaim','Sex'],'formats':['i','S10', 'S1']})
    #persontype = np.dtype({'names':['MemberID','AgeAtFirstClaim','Sex'],'formats':['i','i', 'i']})
    #persontype = [('MemberID','i'),('AgeAtFirstClaim','i'),('Sex','i')]
    #dtype=[('myint','i8'),('myfloat','f8'),('mystring','S5')]
    #my_data = genfromtxt(fileName, delimiter=',',dtype= persontype,skiprows=1)
    #d=_loadcvsForFeautreAnalysis(fileName)
    #ageList=_getCategoricalfeatures(d['AgeAtFirstClaim'],False)
    #sexList=_getCategoricalfeatures(d['Sex'],False)    
    #ageConv = lambda x: ageList.index(x)
    #sexConv = lambda x: sexList.index(x)
    #np.loadtxt(fileName, delimiter=',')
    #result = genfromtxt(fileName, delimiter=',',skiprows=1,converters = {1:ageConv,2:sexConv},dtype= persontype)
    #reader=csv.reader(open(fileName,"rb"),delimiter=',')
    #result=np.loadtxt(fileName, delimiter=',',skiprows=1,converters = {1:ageConv,2:sexConv},dtype= persontype)
    #result=np.loadtxt(fileName, delimiter=',',dtype= None)
    result=np.genfromtxt(fileName, delimiter=',',dtype= None)
    #x=list(reader)
    #result=np.array(x[1:])
    
    #print ageList
    #print sexList
    
    #for i in range(result.shape[0]):
    #    result[i][1]=ageList[result[i][1]]
    #    result[i][2]=sexList[result[i][2]]
    
    return result

def temp():
    """
    charList
    Out[52]: {'0': 0, '1-2': 1, '3-4': 2, '5+': 3}

    """
    daylist={'': 0,
    '1 day': 1,
    '2 days': 2,
    '3 days': 3,
    '4 days': 4,
    '5 days': 5,
    '6 days': 6,
    '1- 2 weeks': 10,
    '2- 4 weeks': 20,
    '4- 8 weeks': 42,
    '26+ weeks': 105
    }





def _countFreq(items):
    """
    print(counter)
    # Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
    print(counter.values())
    # [4, 4, 2, 1, 2]
    print(counter.keys())
    # [1, 2, 3, 4, 5]
    print(counter.most_common(3))
    # [(1, 4), (2, 4), (3, 2)]
    """
    counter=collections.Counter(items)
    return counter
    



