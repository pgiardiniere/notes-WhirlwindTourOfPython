# Strings and Regex in Python

x = 'string'
y = "string"
x == y          # returns True (!)

multiLineStr = """\
first
second
third\
"""
print(multiLineStr)

#########################
### Formatting Strings
#########################
# Adjust case with      upper(), lower(), capitalize(), title(), swapcase()
fox = "tHe qUICk bROWn fOx."

fox.upper()
fox.lower()
fox.title()           # Capitalize each  word's first letters
fox.capitalize()      # Capitalize first word's first letter
fox.swapcase()

# Removing spaces with  strip(), lstrip(), rstrip()
line = '        content         '
print ( line.strip(), '\n' )      # remove whitespace from both ends

line.rstrip()               # remove whitespace trailing right
line.lstrip()               # remove whitespace trailing left

num = "000034"
num.strip('0')              # remove character '0' from string

# Adding space with     center(), ljust(), rjust()
line = "content"
line.center(30)

line.ljust(30)
line.rjust(30)

'435'.rjust(10, '0')    # both pad with 0s
'435'.zfill(10)


#########################
### Finding and Replacing substrings
#########################
# find() & rfind() ,  index() / rindex() , replace()
line = "the quick brown fox jumped over a lazy dog"
line.find('fox')        # if not found, returns -1          
line.index('fox')       # if not found, returns ValueError

# rfind() / rindex() are identical, but search for first occurrence from str END
line.rfind('fox')

line.startswith('fox')      # False
line.endswith('dog')        # True

# replace() works exactly like you'd expect
print ( line.replace('brown', 'red') )
print ( line.replace('o', '--'), '\n')
# ... but regex's are generally the more flexible approach

#########################
### Splitting and Partitioning strings
#########################
# partition() returns tuple :  (substr pre-split, split point, substr post-split)
# partitions on First Instance of pattern only.
print ( line.partition('fox') ) # & rpartition() begins search at str END

# split() returns list : 
# splits string on ALL instances of pattern, ONLY returning substrings w/o split points
print ( line.split() )      # default: split on whitespace

# splitline() -- for obvious reasons is similar
multi = """this is
a string
of 3 lines"""
m = multi.splitlines()
print(m)

# UNDO a split :: use join(), returns str built from split-value and iterable
print( ' '.join(['1', '2', '3']) )  # undo split()
print( "\n".join(m) )               # undo splitlines()

#########################
### Format Strings
#########################
# can use curly braces as escape strings
pi = 3.14159
str(pi)         # '3.14159'
"the value of pi is " + str(pi)     # acceptable
"the value of pi is {}".format(pi)  # format string mode

# format strings with args, insert from list
"""First sub: {0}. Last sub: {1}""".format('poopy', 'butthole')

# format strings with args, named list items
s = """First sub: {first}. Last sub: {last}""".format(first="poop", last="butt")
print(s)

"pi = {0:3f}".format(pi)    # pi as a string to 3 digits of precision


#########################
### Regular Expressions
#########################
# first, we compile a regular expression. Then, we use it to split a string.
import re
regex = re.compile(r'\s+')
regex.split(line)

for s in ["     ", "abc  ", "  abc"]:
    if regex.match(s):
        print(repr(s), "matches")
    else:
        print(repr(s), "no match")

# now, we compare regex.search() to str.index()/str.find()
print ( line.index('fox') )

regex = re.compile('fox')
match = regex.search(line)
print ( match.start() )

# now, we compare regex.sub() to str.replace()
print ( line.replace('fox', 'bear') )

print ( regex.sub('BEAR', line) )


# Why bother? Regex's are more powerful than their simpler counterparts.
# parsing (basic) email addresses
text = "To email guido, try guido@python.org or the older adress guido@google.com"
email = re.compile(r'\w+@\w+\.[a-z]{3}')
email.findall(text)

print (email.findall(text))

# alternatively, hide addresses
email.sub('--@--.--', text)

print ( email.sub('--@--.--', text) )

#########################
### RegEx Syntax (basics)
#########################
# simple strings are matched directly
regex = re.compile('ion')
regex.findall('Great Expectations')

# characters with special meanings:
# . ^ $ + ? { } [ ] \ | ( )
# To match any of those characters directly, escape by using a backslash
regex = re.compile(r'\$')
regex.findall("the cost is $20")

# r prefix in r'\$' indicates "Raw String"
# in standard python, backslash indicates special characters (e.g. \n newline) 
# but in raw strings, those substitutions are not made.
print( 'a\tb\tc')
print(r'a\tb\tc')

# with raw strings, now special characters can match character groups
# e.g. "\w" is a special marking matching any alphanumeric chars, "\s" == whitespace, etc.
regex = re.compile(r'\w\s\w')   # regex matches any two alphanum. chars with whitespace between them
regex.findall('the fox is 9999')

# ------------ table: ------------------------------
# char  description         char  description
# \d    Match any digit     \D    Match any !(digit)
# \s    Match any whitesp   \S    Match any !(whitesp)
# \w    Match any alphanum  \W    Match any !(alphanum)
# --------------------------------------------------

#########################
### Square brackets ++
#########################
# Square Brackets match custom character groups
regex = re.compile(r'[aeiou]')
regex.split('consequential')

# Dashes within square brackets specify a range
regex = re.compile('[A-Z][0-9]') # _capitalLetter_ _digit_
regex.findall('1043879, G2, H6')

# Wildcards match repeated characters
regex = re.compile(r'\w{3}')
regex.findall('The quick brown fox')  # the, qui, bro, fox

regex = re.compile(r'\w+')  # + == "1 or more"
regex.findall('The quick brown fox')

# ------------ table: ------------------------------
# char  description       
#  ?    Match zero or  one repetitions (preceding)
#  *    Match zero or more repetitions (preceding)
#  +    Match  one or more repetitions (preceding)
# {n}   Match n            repetitions (preceding)
# {m,n} Match between m and n repetitons (preceding)
# --------------------------------------------------

# Now can make a more sophisticated email matcher !
email2 = re.compile(r'[\w.]+@\w+\.[a-z]{3}')
email2.findall('barack.obama@whitehouse.gov')   # can handle multiple periods


### Parentheses indicate Groups to extract
# Often, want to extract components instead of full match. Use parens!
text = "To email Guido, try guido@python.org or the older address guido@google.com."
email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
email3.findall(text)        # gets only the alphanum chars, not the . and @

# We can name extracted parts using "(?P<name>)", which does so in Dictionaries
email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')
match = email4.match('guido@python.org')
match.groupdict()