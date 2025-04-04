
#Q1.print frequency of each words 

input_str = "Hello world and Hello Earth" 
word_dict={}
for word in input_str.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(f"Frequency of each word : \n {word_dict}")


#Q2.Operations on Dictionaries

D1={'ok':1,'nok':2}
D2={'ok':2,'new':3}

#1.union of keys, #value does not matter

D_UNION={}

for key,value in D1.items():
    D_UNION[key] = value
    
for key,value in D2.items():
    if key not in D_UNION:
        D_UNION[key] = value
        
print(f"Union of Keys D_Union : {D_UNION}")

#2.intersection of keys, #value does not matter

D_INTERSECTION={}

for key,value in D1.items():
    if key in D2:
        D_INTERSECTION[key] = value
        
print(f"Intersection of Keys D_Intersection : {D_INTERSECTION}")

#3.D1-D2

D1_sub={}

for key,value in D1.items():
    if key not in D2:
        D1_sub[key] = value
        
print(f"Subtraction of D1-D2 : {D1_sub}")

#4.values are added for same keys

D_Merge={}

for key,value in D1.items():
    D_Merge[key]=value
    
for key,value in D2.items():
    if key in D_Merge:
        D_Merge[key] += value
    else:
        D_Merge[key] = value
        
print(f"Merge of given dictionaries D_Merge : {D_Merge}")

 







        

    