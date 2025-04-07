#Flattens the list

input_list = [1,2,3, [1,2,3,[3,4],2]]

def flatten_list(lst):
    
    output_list = []
    
    for element in lst:
        if isinstance(element,list):
            output_list.extend(flatten_list(element))
        else:
            output_list.append(element)
            
    return output_list
 
print(f"Flatten list for {input_list} : {flatten_list(input_list)}") 


#Converting Nested list of tuples in Nested list of lists

input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

def nested_lists(lst):
    
    if isinstance(lst,list):
        
        return [nested_lists(ele) for ele in lst]
        
    elif isinstance(lst,str):
        
        return [int(num) for num in lst.strip("()").split(",")]
        
    else:
        return lst
    

print(f"The Nested list of lists for given input is : {nested_lists(input)}")



        



        


    
