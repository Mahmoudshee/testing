# class overloading():
#     def add(self, a,b,c):
#         return a+b+c
        
    
#     def add(self, a,b):
        
#         return a + b 
    
# obj = overloading()
# print(obj.add(2))


# class overloading():
#     def add(self, a=None,b=None,c=None):
#         if a is not None and b is not None and c is not None:
#             return a + b + c 
#         elif a is not None and b is not None:
#             return a + b  
#         elif a is not None :
#             return a
#         else:
#             return 0 
# obj = overloading()
# print(obj.add(2,3,4))



# class overloading():
#     def add(self,*argv):
#         return sum(argv)
      
# obj = overloading()
# print(obj.add(2,3,4,8,9,10))





class overloading():
    
    def kenty(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None :
            return a + b 
        if a is not None :
            return a 
        else:
            return 0


# obj = overloading()
# print(obj.kenty(2,3,4))

class overloading():
    def kenty(self,* argv):
        return sum(argv)

obj= overloading()
print(obj.kenty(2,3,4,5,6,7,8,9))

