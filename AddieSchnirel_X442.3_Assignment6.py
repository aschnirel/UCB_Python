print("Part 1")
# 1
# Write a function that accepts the name of a file and returns a tuple containing the number of lines, words,
# and characters that are in the file. (Hint: Use the split function of the string module to help you count the words in the file.)

def filefeat(filename):
    '''This function accepts the name of a file and returns a tuple containing the number of lines, words,
# and characters that are in the file.'''
    file=open(filename, 'r')
    countlines = 0
    numwords=0
    numchar=0
    for line in file:
        countlines = countlines + 1
        stripline=line.strip()
        numchar=numchar+len(stripline)
        wordlist=stripline.split(sep=" ")
        numwords=numwords+len(wordlist)
    file.close()
    return countlines, numwords, numchar

test1=filefeat("test1.txt")

print(test1)

print("\n")
print("Part 2")


#2
# Write a function that accepts an arbitrary number of lists and returns a single list with exactly one occurrence of
# each element that appears in any of the input lists.

# First, I will borrow the merge function from the course notes 6.1
def merge(list1, list2):
    '''merge(list1,list2) returns a list consisting of
the original list1 along with any elements of list2
that were not already in list 1'''
    newlist = list1[:]
    for i in list2:
        if i not in newlist:
            newlist.append(i)

    return newlist

def listmerge(*lists):
    '''This function accepts an arbitrary number of lists and returns a single list with exactly one occurrence of
# each element that appears in any of the input lists.'''
    if len(lists) == 0:
        print("no go")
        return list()
    else:
        totallist=[]
        count=0
        for list in lists:
            totallist=merge(totallist, list)
            count=count+1
        #totallist.sort()
        print(totallist)

    return totallist

list1=[1,2,"three", 4.0, "cinco", 6, 7, 2**3]
list2=[-1,2,3,4,5, 6.0, "seven"]
list3=[9, -8, "siete", "seis", 5, 4, 3, 2]

test1_listmerge=listmerge(list1, list2, list3)

print("\n")
print("Part 3")

#3
# Use the map function to add a constant to each element of a list. Perform the same operation using a list comprehension.
#For example, the list (1, 20, 300, 400) and constant 8, will result in: 9, 28, 308, 408

def addc(numlist, constant):
    print("The original list is:", numlist)
    constantlist=len(numlist)*[constant]
    newlist = list(map(lambda x, y: x+y, numlist, constantlist))
    print("The new list is:", newlist)
    return newlist


list1=[34,2012,31,10]

maptest1=addc(list1,10)

print("\n")
print("Part 4")

#4
# Write a function that will take a variable number of lists. Each list can contain any number of words.
#This function should return a dictionary where the words are the keys and the values are the total count
# of each word in all of the lists
#For example, if we are given the following lists:

wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]

#the function should output the following dictionary (The order of the words is not important):
{'float': 1, 'int': 2, 'quadruple': 1, 'home run': 1, 'triple': 1, 'double': 3}

#Note, you may have to create an empty dictionary first (for example: dict = {}).

def list2dict(*lists):
    dict = {}
    for list in lists:
        for item in list:
            if item in dict.keys():
                dict[item]=dict[item]+1
            else:
                dict.update({item: 1})
    return dict

test4_1=list2dict(wl1,wl2,wl3)

print(test4_1)

test4_2=list2dict(wl1,wl3)

print(test4_2)

# (Optional)
# Write a function that combines several dictionaries by creating a new dictionary with all the keys of the original ones.
# If a key appears in more than one input dictionary, the value corresponding to that key in the new dictionary should be a
# list containing all the values encountered in the input dictionaries that correspond to that key.


def dicts2dict(*dicts):
    masterdict={}
    for dict in dicts:
        for key, value in dict:
            if key in masterdict:
                masterdict.update(key=[]