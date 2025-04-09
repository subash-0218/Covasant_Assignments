# Question-5 :

# from pkg.poly import Poly 
# a = Poly(1,2,3)  #an, ...., a0 
# b = Poly(1,0,1,1,2,3)
# c = a+b 
# print(c) #Poly ( 1,0,1, 2,4,6)

class Poly:
    
    def __init__(self,*nums):
        self.nums = list(nums)
        
    def __add__(self,other):
        
        max_len = max(len(self.nums),len(other.nums))
        
        out_put = [0]*max_len
        
        for i in range(-1,-max_len-1,-1):
            
            if i >= -len(self.nums):
                val_1 = self.nums[i]
            else :
                val_1 = 0
            if i >= -len(other.nums) : 
                val_2 = other.nums[i]
            else :
                val_2 = 0
            
            out_put[i] += val_1 + val_2
            
        return Poly(*out_put)
        
    def __str__(self):
        return f"Poly{tuple(self.nums)}"
        

if __name__ == "__main__":        
    a = Poly(1,2,3)
    b = Poly(1,0,1,1,2,3)
    c = a + b              #a.__add__(b)
    print(c)              #c.__str__()
