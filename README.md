# Data_deduplication
Removing redundant data from a data set using k means clustering

Algorithm :
1.Conversion:
  Converting input data to a uniform format,text data is converted to lowercases 
  and ASCII value of each character is used to allot values to a string.Formulae used :
  radix=128
  value=sum((radix^position)*ASCII val)modulo m)
  where m=731 (a large prime number can be taken)
  and position is counted from left to right
  for Ex in Ayush position of h is 0 and A is 4.
  
2.Feature Vector 
  For each columns in a particular row string to value conversion is done using the above
  methord.set of values of the columns of a particular row is used as feature vector.
  
3.Clustering 
  Clustering the feature vectors into n number of clusters.So as to reduce the time operation of 
  duplication finding as we will only compare the data which are in the same cluster group
  for duplication.
  Here n is taken as 10.
  If n is decreased accuracy will increase but costing extra computation time as here more comparision
  operatioin will be required.
  
4.Decision
  Here 'dob' and 'g' are considered as strict fields. i.e if there is any difference in any of these 
  two fields between data of two persons,then they are considered as different person.
  (Note : As it is highly unlikely for a person to type in an incorrect dob or g we have given these fields
  very strong weightage in classification then other fields)
  
  In case 'dob' and 'g' fields are similar
  we take into consideration other two fields 
  Case 1: if both fields are differnt both person are considered different
  Otherwise :
  If no. of character difference is less than a certain threshold then they are considered as same person
  i.e(Data duplication)
  (threshhold=ceil(0.2*max(length(data1,data2)) if number of character differneces between data1 and data 2
  is less than this threshhold then these data are considered to be of same person.
  
  
5.Removing the duplicated data and saving the output deduplicated data in a csv file.
