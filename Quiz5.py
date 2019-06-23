#Question1
# Write a regular expression that will match strings that are either all lower case or all upper case.
#Assume that the string is a single word that is at least two letters long and consists only of letters.
#For example, it will match AM, PM, am or parrot but NOT match Am, aM, Pm or Parrot.\


listofstrings=["AM", "PM", "am", "parrot", "Am", "aM", "Pm", "PArrot"]


import re

def stringcase(list):
    newstrings=[]
    for string in list:
        newstring=re.findall(r'\b([A-Z][A-Z]+|[a-z][a-z]+)\b',string)
        if len(newstring)>0:
            newstrings.append(newstring)
    return newstrings


test1=stringcase(listofstrings)

print("\nQuestion 1")
print("The correctly formatted strings are:")
print(test1)


#Question 2
# Write a substitution command that will change names like file1, file2, etc. to file01, file02, etc.
#but will not add a zero to names like file10 or file20.

filenames = ["file1", "file2", "file3", "file01", "file02", "file10", "file20", "file30", "file", "file00"]

def fileNMeditor(list):
    newfileNMs=[]
    fileNMformat=re.compile(r"file(\d)\Z|file\Z")
    for string in list:
        newstring=fileNMformat.sub(r"file0\1", string)
        newfileNMs.append(newstring)
    return newfileNMs

print("\nQuestion 2")
print("The modified list of file names is:")
print(fileNMeditor(filenames))


#Question 3
#Many news and mail readers automatically highlight URLs that appear in text,
# for example http://yahoo.com or www.msnbc.com.
#Construct a regular expression that will extract the names of URLs embedded in a string.

textstring = "Many news and mail readers automatically highlight URLs that appear in text, for example http://yahoo.comd or www.msnbc.com."

URLS=re.findall(r"(https?://)?(www\.)?(\w+)(\.[a-z]+)", textstring)

print("\nQuestion 3")
print("The list of URLS is:")
for url in URLS:
    url2=''
    for part in url:
        url2=url2+part
    print(url2)



#Question 4
#Write a function that takes times of the form 03:12:19 (in other words, three hours,
#twelve minutes, and nineteen seconds) and converts them to the corresponding number of seconds


def time2sec(string):
    hhmmss=re.split(":", string)
    seconds=(int(hhmmss[0]) * 60 * 60) + (int(hhmmss[1]) * 60) + int(hhmmss[2])
    return seconds

time1="08:21:31"
time2="08:21:30"
time3="00:01:00"


test1=time2sec(time1)
test2=time2sec(time2)
test3=time2sec(time3)

print("\nHere are some example conversations:")
print(time1, "converts to",test1, "seconds")
print(time2, "converts to",test2, "seconds")
print(time3, "converts to",test3, "seconds")