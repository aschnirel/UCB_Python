#Question 1
#  Write a simple Rectangle class. It should do the following:

##Accepts length and width as parameters when creating a new instance
##Has a perimeter method that returns the perimeter of the rectangle
##Has an area method that returns the area of the rectangle
##Don't worry about coordinates or negative values, etc.

###Python provides several modules to allow you to easily extend some of the basic objects in the language.
###Among these modules are UserDict, UserList, and UserString.
###(Refer to the chart in Topic 10.3 to see what the methods you need to override look like.
###Also, since UserDict and UserList are part of the collection module, you can import them using from
###collections import UserDict and from collections import UserList.)

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
        self.area=self.width*self.length
        self.perimeter=2*self.length+2*self.width
    def __str__(self):
        return "Length: %d\nWidth: %d\nArea: %d \nPerimeter: %d\n" % (self.length, self.width, self.area, self.perimeter)


print(Rectangle(2,5))
print(Rectangle(10,500))

#Question 2
# Using the UserList module, create a class called Ulist, and override the __add__, append, and extend methods
# so that duplicate values will not be added to the list by any of these operations.

from collections import UserList

#inherit Userlist class into Ulist
class Ulist(UserList):
    def __init__(self, ulist=[]):
        super().__init__(ulist)

    def __add__(self, item):
        newitemlist = []
        for i in item:
            if i in self.data:
                print(i, 'in list already, not added')
            else:
                newitemlist.append(i)
                print(i, " is something new, so it is added")
        return super().__add__(newitemlist)


    def extend(self, item):
        newitemlist = []
        for i in item:
            if i in self.data:
                print(i, 'in list already, not added')
            else:
               newitemlist.append(i)
               print(i, " is something new, so it is added")
        return super().extend(newitemlist)


    def append(self, item):
        newitemlist = []
        for i in item:
            if i in self.data:
                print(i, 'in list already, not added')
            else:
               newitemlist.append(i)
               print(i, " is something new, so it is added")
        return super().append(newitemlist)


    def __str__(self):
        return '%s' % self.data


#Test add

print("\nThe start list is:")
startlist=Ulist([1,2,3])
print(startlist)

print("\nthe first test is;")
newlist1=startlist.__add__([2,5])
print(newlist1)

print("\nthe second test is;")
newlist2=newlist1.__add__([3,6])
print(newlist2)


#Test append

print("\nThe start list for append is:")
startlistap=Ulist([1,2,3])
print(startlist)

print("\nthe first append test is;")
newlistap1=startlist.append([2,5])
print(newlist1)

print("\nthe second append test is;")
newlistap2=newlist1.append([3,6])
print(newlist2)


#Test extend

print("\nThe start list for extend is:")
startlistap=Ulist([1,2,3])
print(startlist)

print("\nthe first extend test is;")
newlistap1=startlist.extend([2,5])
print(newlist1)

print("\nthe second extend test is;")
newlistap2=newlist1.extend([3,6])
print(newlist2)
