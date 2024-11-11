from abc import ABC,abstractmethod

class father(ABC):
    @abstractmethod
    def talking(self):#declaration
        pass #no definition

    @abstractmethod
    def chatting(self):#declaration
        pass #no definition

class mother(father):
     def talking(self):#declaration
        print('hello')

     def chatting(self):#declaration
        print('hello world')

class child(father):
     def talking(self):#declaration
        print("Iam studying")

     def chatting(self):#declaration
        print('Iam chatting')

# father = father()
mother =mother()
child = child()

# father.talking()
mother.talking()
child.talking()
child.chatting()