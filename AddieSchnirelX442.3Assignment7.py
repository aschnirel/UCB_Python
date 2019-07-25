# Questiom 1
# Suppose you want to determine whether an arbitrary text string can be converted to a number.
# Write a function that uses a try/except clause to solve this problem. Can you think of another way to solve this problem?

text1="dfg986df896gp96"
text2="4957304975"
text3="grg5t.54ts"
text4="970745.345345"

def text2num(text):
    try:
        num=float(text)
    except ValueError:
        num=0
        print("There was an error: this string cannot be converted to a number.")

    return num

print(text2num(text1))
print(text2num(text2))
print(text2num(text3))
print(text2num(text4))

#another way to solve this problem:

def text2num2(text):
    countdigits=0
    digitlist=["0","1","2","3","4","5","6","7","8","9","."]
    for digit in text:
        if digit in digitlist:
            countdigits=countdigits+1
    if countdigits==len(text):
        num=float(text)
    else:
        print("Error: this string is not a number.")
        num=0
    return num

print(text2num2(text1))
print(text2num2(text2))
print(text2num2(text3))
print(text2num2(text4))

#Questiom 2
# The input function will read a single line of text from the terminal.
# If you wanted to read several lines of text, you could embed this function inside a while loop
# and terminate the loop when the user of the program presses the interrupt key (Ctrl-C under UNIX, Linux and Windows.)
# Write such a program, and note its behavior when it receives the interrupt signal.
# Use a try/except clause to make the program behave more gracefully.


def input_lines():
    while True:
        try:
            lineoftext = input("Enter some text: ")
            print(lineoftext)

        except KeyboardInterrupt:
            print("Control-C resulted in quitting the function")

print(input_lines())