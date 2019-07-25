#Remember, the Final Project is due in Module 10. Choose one of the following options:

# Part 1
# A file with a name like picture.jpg is said to have an extension of "jpg";
# i.e. the extension of a file is the part of the file after the final period in its name.
# Write a program that takes as an argument the name of a directory (folder) and then finds the extension of each file.
# Then, for each extension found, it prints the number of files with that extension and the minimum, average,
# and maximum size for files with that extension in the selected directory.

import os
from statistics import mean

directory = input("What is your directory name?")

for root, dirs, files in os.walk(directory):
    filesizes=[]
    for file in files:
        print(os.path.join(root, file))
        if file.endswith(".jpg"):
            size=os.path.getsize(os.path.join(root,file))
            print(size)
            filesizes.append(size)
        elif file.endswith(".JPG"):
            size=os.path.getsize(os.path.join(root,file))
            print(size)
            filesizes.append(size)

maxfile=max(filesizes)
minfile=min(filesizes)
meansize=round(mean(filesizes),2)
print(filesizes)
print("The mean is", meansize)
print("The max is", maxfile)
print("The min is", minfile)


# Part 2
# Write a text analyzer. It should be in a form of a function that takes a file name as an argument.
# It should read and analyze a text file and then print:
#- the top 5 most frequently used words in the file
#- the number of times the top 5 words are used
#- should be sorted by most frequently used count
#- the longest word in the document
#- the average size of each word

def TextAnalyzer(filename):
    #open file, read and split lines, strip newl lines
    #generate list of all words, including duplicages
    with open(filename, 'r') as f:
        words = []
        for line in f:
            linewords= line.split(" ")
            for word in linewords:
                words.append(word.strip())
    print("\n\nThe file is:", filename)

    #build lies of unique words
    uniquewords=[]
    for word in words:
        if word in uniquewords:
            pass
        else:
            uniquewords.append(word)

    #count repeats of words in countlist
    #create list with named lengthwords
    countlist=[]
    lengthwords=[]
    for word in uniquewords:
        # check the length of each word
        lengthwords.append(len(word))
        count=0
        for i in words:
            if i==word:
                count+=1
        countlist.append(count)



    #find the words with the max length
    longestwordlength = max(lengthwords)
    iter=0
    maxwords=[]
    for lw in lengthwords:
        if lw==longestwordlength:
            maxwords.append(uniquewords[iter])
        iter+=1
    #create dictionary of words:count
    worddict = dict(zip(uniquewords,countlist))


    # - the top 5 most frequently used words in the file
    topwords=sorted(worddict, key=worddict.get, reverse=True)[:5]
    print("\nThe top most frequent words are:")

    # - the number of times the top 5 words are used
    for word in topwords:
        wordcount=worddict.get(word)
        print(word, " is seen ", wordcount, " times")

    # - should be sorted by most frequently used count
    sortedwords=sorted(worddict, key=worddict.get, reverse=True)
    print("The sorted words are:",sortedwords)

    # - the longest word in the document
    print("The longest words are:", maxwords)

    # - the average size of each word
    averagewordlength = round(mean(lengthwords),2)
    print("the average length word is:", averagewordlength)
    return worddict

test1=TextAnalyzer('textwords.txt')
print(test1)



