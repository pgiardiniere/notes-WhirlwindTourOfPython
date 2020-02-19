### Attribution of code:
### A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.
# All comments my own


##################################################
############ Strings: ############################
# single quotes and double quotes are functionally equivalent
# multi-line strings declared with triple-quote - i.e.
multiline = """
one
two
three
"""

### Some basic String Methods:
s = "stRiNG"

### methods for Case stuff
s.upper()
s.lower()
s.title()
s.capitalize()
s.swapcase()

### methods for add/removal of spaces(or arbitrary characters)
s.strip()
s.rstrip()
s.lstrip()
# note: def. arg = ' ', so this behaves similar to rstrip/lstrip - only removes from outside edges
s.strip('0f')

# strip() inverse would be center(), ljust(), rjust()
s.center(30)
s.ljust(30)
s.rjust(30)
# optionally, can specify character to fill instead of whitespace
s.center(30, '-')
# zero-filling, a common use
s.rjust(30, '0')
# b/c zero-filling is so common, there is a standalone method  
s.zfill(6)
# note that zfill behavior is slightly different, arg specifies TOTAL digits, not total indent. e.g.:
s = '453'
s.zfill(6)

#########################
### Finding and replacing substrings
line = 'the quick brown fox jumped over a lazy dog'

# find/index behave identically when it matches the string
line.find('fox')
line.index('fox')

# find/index behave differently when it does NOT match the string
line.find('dsf')
# print(line.index('dsf')) # index('dsf') throws 'ValueError: substring not found' where find('dsf') returns -1

# rfind/rindex search beginning at the end of string. Returns absolute index position, not relative to end.
line.rfind('a')
line.rindex('a')
line.find('a')
line.index('a')

# these do exactly what you would think - returns bool
line.startswith('fox')
line.endswith('dog')

# instead of just finding, replace() will insert a new substring
# note: you can get more precise/flexibility with regexs
line.replace('brown', 'red')

#########################
### Format strings
pi = 3.14159
str(pi), type(str(pi))
pi, type(pi)

# for more complicated formats, you may be tempted to do the following:
"The value of pi is " + str(pi)

# the more flexible way is to use Format Strings
# they are strs with special markers (curly braces) into which string-formatted values are insterted
"The value of pi is {}".format(pi)

# you can include more information on 'what' apppears in the curly braces. nums refer to index of arg to ins
"""First letter: {0}. Last letter: {1}.""".format('A', 'Z')

# for numeric inputs, you can include format codes. e.g. to round & return your float pi to 3 dec places...
"pi = {0:.3f}".format(pi)

#########################
### Regular Expressions
### regex / re

### additional resources:
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html
# http://shop.oreilly.com/product/9780596528126.do 

# duplicating str.split() functionality with regex.split() method
import re
regex = re.compile(r'\s')
regex.split(line)

for s in ["     ", "abc  ", "  abc"]:
    if regex.match(s):
        repr(s), "matches"
    else:
        repr(s), "does not match"


# working with var line to compare str methods and regex methods. re-assign regex to fox
regex = re.compile('fox')
match = regex.search(line)

# regex.search is similar to str.index() ** str.find()
line.index('fox')
match.start()

# regex.sub() is similar to str.replace()
line.replace('fox', 'bear')
regex.sub('bear', line)

### demonstration of regex's comparitive flexibility over str methods
email = re.compile(r'\w+@\w+\.[a-z]{3}')
text = "To email Guido, try guido@python.org or the older address guido@google.com."
print(email.findall(text))
print(email.sub('--@--.--', text))

### basics of regex syntax
# exact string matches for simple strings
regex = re.compile('ion')
print(regex.findall('Greate Expectations'))

# all re special characters: . ^ $ * + ? { } [ ] \ | ( )
# match a special character by escaping with a backslash
regex = re.compile(r'\$')
print(regex.findall("the cost is $20"))

# the r prefix we have been using indicates a Raw String
# see the difference in output below to denote it's use. 
# It specifies to stop use of Python-denoted string special chars. Comes into play when backslashing
print('a\tb\tc')
print(r'a\tb\tc')

# escaping with backslash also turns normal chars into special chars
regex = re.compile(r'\w\s\w')
print(regex.findall('the fox is 9 years old'))
# \d \s \w (and their inverse, capitalized counterparts, \D \S \W) for digits, spaces, alphanumeric words + '_'
# complete list at https://docs.python.org/3/library/re.html#re-syntax 
# also see personal notes, 'Regular Expressions.txt' in your technical txt folder

# Square brackets for character groups (in a single index/position)
regex = re.compile('[aeiou]')
print(regex.split('consequential'))

# dash specifies a range w/in brackets
regex = re.compile('[A-Z][0-9]')
print(regex.findall('1043879, G2, H6'))

# wildcards to match repeated characters
regex = re.compile(r'\w{3}')
print(regex.findall('The quick brown fox'))

# + operator to return 1 or more (arbitrarily high) occurrences of preceding character (or character group)
regex = re.compile(r'\w+')
print(regex.findall("The quick brown fox"))

# revisiting the initial email example
email  = re.compile(r'\w+@\w\.[a-z]{3}')
email2 = re.compile(r'[\w.]+@\w+\.[a-z]{3}')
print(email2.findall('barack.obama@whitehouse.gov'))
# this works b/c we added brackets and '.', i.e. :: \w+ > [\w.]+ :: [\w.]+ matches any word OR '.' 1 or more times

# parens indicate groups for extraction, so we avoid pulling '@' and '.'
email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text = 'To email Guido, try guido@python.org or the older address guido@google.com.'
print(email3.findall(text))

# can name extracted components, so instead of export as ...tuple? we get export as dict
email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')
match = email4.match('guido@python.org')
print(match.groupdict())
