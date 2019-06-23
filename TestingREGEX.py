import re

text_to_search='''abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com
www.help.edu
https://github.com
youtube.com
https://www.sfsu.edu
toronto.ca


321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T'''


pattern1=re.compile(r'ab')
matches1=pattern1.finditer(text_to_search)

for match in matches1:
    print(match)

pattern2=re.compile(r'\d')
matches2=pattern2.finditer(text_to_search)

for match in matches2:
    print(match)

pattern3=re.compile(r'\s')
matches3=pattern3.finditer(text_to_search)

for match in matches3:
    print(match)

#matching ones that have a word boundary
pattern4=re.compile(r'\bHa')
matches4=pattern4.finditer(text_to_search)

for match in matches4:
    print(match)

with open('data.txt','r') as f:
    contents=f.read()
#matching phone numbers
pattern5=re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches5=pattern5.finditer(contents)

for match in matches5:
    print(match)

#matching names
pattern6=re.compile(r'M(r|rs|s)\.?\s[A-Z]\w*')
matches6=pattern6.finditer(text_to_search)

for match in matches6:
    print(match)


#matching emails
pattern7=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.(com|edu|gov|net)')
matches7=pattern7.finditer(contents)

for match in matches7:
    print(match)

#matching emails
pattern8=re.compile(r'(https?://)?(www\.)?(\w+)(\.[a-z]+)')
matches8=pattern8.finditer(text_to_search)

for match in matches8:
    print(match)