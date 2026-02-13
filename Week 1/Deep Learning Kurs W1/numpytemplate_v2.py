import numpy as np

#define a random generator with a seed here using numpy, using the newer convention for numpy https://numpy.org/doc/stable/reference/random/generator.html
rng = None


##################################################
# part 1 the easy stuff, indexing, searching
##################################################

a = np.arange(36).reshape((6, 6))

def index1(mat):
    #Return row indexed with 5 (and columns 0,1)
    return None

#res = index1(a)
#print(res)

def index2(mat):
    #Return column indexed with 2 (and rows 0,1)
    return None    

#res = index2(a)
#print(res)

def index3(mat):
    #Return the columns indexed with 1 and with 3 (and rows 0,1)
    return None    

#res = index3(a)
#print(res)

def index4(mat):
    #Return the rows indexed with 0 to 2 (and columns 0,1). It should be 3 rows here
    return None    

#res = index4(a)
#print(res)

def index5(mat):
    # return the last row using a negative index (and columns 0,1)
    return None

#res = index5(a)
#print(res)

def index6(mat): 
    # return the third last row using a negative index (and columns 0,1)
    return None

#res = index6(a)
#print(res)

def index7(mat):
    # return the the last two rows using a negative start index (and columns 0,1)
    return None

#res = index7(a)
#print(res)

def index8(mat):
    # return the the last three columns using a negative start index (and rows 0,1)
    return None

#res = index8(a)
#print(res)

def index9(mat):
    # return the columns indexed with 3,4 using a negative start index and a negative stop index (and rows 0,1)
    return None

#res = index9(a)
#print(res)

def index10(mat):
    # return the columns indexed with 0,1,2 using a negative start index and a negative stop index (and rows 0,1)
    return None

#res = index10(a)
#print(res)
    
def index11(mat):
    # return every 2nd column, starting at index 0  (and rows 0,1)
    return None    

#res = index11(a)
#print(res)

def index12(mat):
    # return every 3rd column, starting at index 1 (and rows 0,1)
    return None  

#res = index12(a)
#print(res)

def index13(mat):
    # return every 2nd column, starting at the last index, in reversed order  (and rows 0,1)
    return None   

#res = index13(a)
#print(res)

def index14(mat):
    # return every 2nd column, starting at the second last index, in reversed order (and rows 0,1) 
    return None   
 
#res = index14(a)
#print(res) 
    
b= np.arange(0,22)
def index15(mat):
    # return every 3rd element, between index 3 and 12 (12 not included)
    return None 

#res = index15(a)
#print(res)
      
a = rng.integers(low=2,high=15,size=(5,5))
def indexr1(mat):
    #Return a matrix which is true where mat-values are higher than 5  (and false otherwise) 
    return None    

#res = indexr1(a)
#print(res)

def indexr2(mat):
    #Return the indices of the matrix where mat-values are higher than 5   
    return None  

#res = indexr2(a)
#print(res)

def indexr3(mat):
    #Return the values where mat-values are higher than 5 
    #will the result be a matrix?  
    return None 

#res = indexr3(a)
#print(res)

def indexr4(mat):
    #Return the values where mat-values are higher than 5 and lower than 10
    #will the result be a matrix?  
    return None 

#res = indexr4(a)
#print(res)

##################################################
# part 2 the easy stuff,  element-wise operations
##################################################

a = np.arange(9).reshape((3, 3))+1

def op1(mat):
    # return the sum over all elements    
    return None    

#res = op1(a)
#print(res)

a = np.arange(36).reshape((3, 3, 4))      
def op2(mat):
    # return the sum over the axis #1 , indexing starts at 0
    return None    

#res = op2(a)
#print(res)
     
a = np.arange(9).reshape((3, 3))
def op3(mat):
    # return a scaled version so that it sums up to 1  
    return None    

#res = op3(a)
#print(res)

def op4(mat):
    # square each entry element wise  
    return None    

#res = op4(a)
#print(res)    

a = np.arange(6).reshape((3, 2))
b = np.arange(6).reshape((3, 2)) -5  
def op5(mat1,mat2):
    # multiply both element-wise
    return None    

#res = op5(a,b)
#print(res)

##################################################
# part 5 the intermediate stuff, inner products and the like
##################################################    

a = np.arange(6).reshape((3, 2))
b = np.arange(3) -5 

def op6(mat1,v):
    # compute the inner product between v and each vector in mat1 which is defined by fixing index in axis #1 and cycling through elements in axis #0
    return None   

#res = op6(a,b)
#print(res)

a = np.arange(12).reshape((4, 3))
b = np.arange(3) -5 

def op7(mat1,v):
    # compute the inner product between v and each vector in mat1 which is defined by fixing index in axis #0 and cycling through elements in axis #1
    return None   

#res = op7(a,b)
#print(res)        
  
a = np.arange(6).reshape((3, 2))
b = np.arange(3) -5
def op8(mat1,v):
    # matrix multiply v from the left to mat1
    # answer: is this equal to op6 or op7 ?
    return None 

#res = op8(a,b)
#print(res)

a = np.arange(72).reshape((4, 3,3,2))
b = np.arange(3) -5 

def op9(mat1,v):
    # compute the inner product between v and each vector in mat1 which is defined by fixing index in axis #0 and #1 and #3 and cycling through elements in axis #2
    return None   
        
#res = op9(a,b)
#print(res)  
     
