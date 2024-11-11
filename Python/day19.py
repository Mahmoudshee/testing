# overriding is a way of letting method of a subclass overide the method of a  super class

class father():
    def talking(self):
        print('Iam good in .......')

class child(father):
    def talking(self):
        print('Iam good in italian')
    # pass


obj = child()
obj.talking()

obj1= father()
obj1.talking()