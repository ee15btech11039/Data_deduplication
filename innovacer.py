import numpy as np
import pandas as pd
import string
import math
from sklearn.cluster import KMeans
from collections import OrderedDict
print "Reading data ..."
data=pd.read_csv('data.csv') ##change with path of the input csv file if required



radix=128
def hash_func(data):
    data=[i.lower() for i in list(str(data))]
    total=0
    for i in range(len(data)):
            total=total+(((radix**i)*ord(data[i]))%731)
    return total
hashed_data=[]

for index,row in data.iterrows():
    mat=[]
    mat.append(hash_func(row['ln']))
    mat.append(hash_func(row['dob']))
    mat.append(hash_func(row['gn']))
    mat.append(hash_func(row['fn']))
    hashed_data.append(mat)

hashed_data=np.asarray(hashed_data)
##dividing the data into clusters
kmeans = KMeans(n_clusters=10, random_state=0).fit(hashed_data)  ##10 cluster centres considered
#print kmeans.labels_
genuine=[]
drop_index=[]
def compare(data,labels):
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            clusters=[]
            if(labels[i]==labels[j]):
                if(data.loc[i,'dob']==data.loc[j,'dob'] and data.loc[i,'gn']==data.loc[i,'gn']):
                    if(data.loc[i,'ln']==data.loc[j,'ln']):
                        ##some error in first name
                        ##we will allow threshhold
                        check1=data.loc[i,'fn']
                        check2=data.loc[j,'fn']
                        count = sum(1 for a, b in zip(check1, check2) if a != b)
                        if(count<=math.ceil(float(0.2*max(len(check1),len(check2))))):
                            drop_index.append(j)
                            for k in range(j+1,len(data)):
                                #check1=data.loc[i,'fn']
                                check2=data.loc[k,'fn']
                                count = sum(1 for a, b in zip(check1, check2) if a != b)
                                if(data.loc[i,'ln']==data.loc[k,'ln'] and count<=math.ceil(float(0.2*max(len(check1),len(check2))))):
                                    drop_index.append(k)
                    elif(data.loc[i,'fn']==data.loc[j,'fn']):
                        ##otherwise
                        check1=data.loc[i,'ln']
                        check2=data.loc[j,'ln']
                        count = sum(1 for a, b in zip(check1, check2) if a != b)
                        if(count<=math.ceil(float(0.2*max(len(check1),len(check2))))):
                            drop_index.append(j)
                            for k in range(j+1,len(data)):
                                #check1=data.loc[i,'fn']
                                check2=data.loc[k,'ln']
                                count = sum(1 for a, b in zip(check1, check2) if a != b)
                                if(data.loc[i,'fn']==data.loc[k,'fn'] and count<=math.ceil(float(0.2*max(len(check1),len(check2))))):
                                    drop_index.append(k)
                    else:
                        genuine.append(i)
                else:
                    genuine.append(i)  ##base case

compare(data,kmeans.labels_)
k=list(set(drop_index))
data.drop(data.index[k],inplace=True)
print "Deduplicated Data"
print data
data.to_csv('out.csv')   ##storing the dedupliated data in out.csv file
