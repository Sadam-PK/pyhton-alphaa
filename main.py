# casting int - strings

my_number = 123

print(my_number)

x = int("123")

print(type(x))

print(x)

# can't convert alphabets to integers but, numbers in string can be converted like above

print(x)

# you can't do (x[1] = 222) because this to integer, int is single value not array

# String concatenation

string_one = 'Sharfo is a'

string_two = 'good guy.'

string_three = string_one + string_two

print(string_three)

# to upper

str = 'this is a string'

str.upper()

# to lower

str = 'THIS IS A STRING'

str.lower()

# see more string options

dir(str)

# run and test different string functions

help(str.capitalize)

help(str.casefold)

help(str.center)

help(str.count)

help(str.encode)

help(str.endswith)

help(str.expandtabs)

help(str.find)

help(str.format)

help(str.format_map)

help(str.index)

help(str.isalpha)

help(str.isascii)

help(str.isdecimal)

help(str.isdigit)

help(str.isidentifier)

help(str.islower)

help(str.isnumeric)

help(str.isprintable)

help(str.isspace)

help(str.istitle)

help(str.isupper)

help(str.join)

help(str.ljust)

help(str.lower)

help(str.lstrip)

help(str.maketrans)

help(str.partition)

help(str.removeprefix)

help(str.removesuffix)

help(str.replace)

help(str.rfind)

help(str.rindex)

help(str.rjust)

help(str.rpartition)

help(str.rsplit)

help(str.rstrip)

help(str.split)

help(str.splitlines)

help(str.startswith)

help(str.strip)

help(str.swapcase)

help(str.title)

help(str.translate)

help(str.upper)

help(str.zfill)

# string slicing - elemination of string letters

my_string = "My country is Pakistan"

print(my_string[0:6])  # eleminates all apart from first 6 letters of string including whitespaces

# reverse slicing - eleminate last part

print(my_string[0:-3])

# just first letter of string - particular index

print(my_string[0])

print(my_string[4])

# String formatting - substitution

var = 'python'
my_string = 'I like %s' % var

print(my_string)

print(f'I like {var}')

sumNum = "%i + %i = %i " % (1, 2, 3)

print(sumNum)

# float and its range

floatNum = '%f' % (1.23456)

print(floatNum)

floatNum = '%.2f' % (1.2345678)  # float upto 2 after decimal - add dot

print(floatNum)

# CAT in dictionary

print("%(lang)s is fun!" % {"lang": "Python"})

print("%(x)i + %(y)i + %(z)i" % {"x": 1, "y": 2, "z": 3})

# another formating

print("Python is a simple as {0} {1} {2}".format("a", "b", "c"))

xy = {"x": 1, "y": 10, }

print("Graph is a point where x = {x}, and y = {y}".format(**xy))


############# List  #################

fruits = ['apples', 'bananas', 'mangoes']

print(fruits)

############ in python list can save different types of data ##################

fruits = ['apples', 10, 20, 'mangoes']

print(fruits)

########## Merging lists ################

listOne = []

listTwo = [1,2,3]

listOne.extend(listTwo)

print(listOne)

############## another method of merge ##################

listA = [1,2,3]

listB = []

listC = listA + listB

print(listC)

############### sorting #####################

unSorted = [21,5,3,6,22,88,99,55]

unSorted.sort()

print(unSorted)

############## none list ####################

aList = [2,1,4,3,6,7,99,21]

sortA = aList.sort()

print(sortA) ######shows you will sort first and then assign it otherwise it won't be assigned at the same time

############ slicing a list ##################

print(aList[0:3])

print(aList)

############## List is mutable ##################

aList += [100]

print(aList)

########### Reverse slice ############

print(aList[0:-1])

############# Tuples - Immutable ###########

aTuple = (4,1,5,3,2)

print(aTuple)

print(aTuple[1:3])

bTuple = (22,33,44)

cTuple=()

cTuple = (aTuple + bTuple)

print(cTuple)

############## cTuple += [100] --------- can't be executed - tuples are immutable ############

########### tuple - list casting - change of type #############

castedList = tuple([1,2,3])

print(castedList)

############ Dictionaries - mapped key:value pairs #############

wordDict = {
    "noun" : "name of anything",
    "pronoun" : "word used for noun",
    "verb" : "action word"
}

print(wordDict)

print(wordDict['noun'])

print(wordDict.keys())

print(wordDict.values())

########check for key or value in dictionary with IN ###########

print('noun' in wordDict)

######## Conditional Statements ##########

if 2 > 1:
    print("True")

num1 = 2
num2 = 6

if num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is greater than {num2}")

val = 100
if val <= 10:
    print("That is a great deal")
elif val > 10:
    print("That's too much")

x = 9
y = 16
if x < 10 or y > 15:
    print("The statement is true..")


x = 9
y = 16
if x < 10 and y > 15:
    print("both are true..")
else:
    print("One of them is false")


myList = [1,2,4,5,6,7]
x = 3
if x not in myList:
    print("x not in the list.")
else:
    print("x is in the list.")

x = 10
if x != 11:
    print("True")
else:
    print("False")

print("I have a \n new line in the middel")

print("I have a \t in the middle ;P")

####### Loopsssssss ##########

loopList = [2,4,6,1,3,9]

for i in loopList:
    print(i)

wordD = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
}

for key in wordD:
    print(key)

wordDD = {
    3 : "three",
    4 : "four",
    1 : "one",
    5 : "five",
    2 : "two",
}

sortedKeys = sorted(wordDD) # both work fine (wordDD.keys())
for key in sortedKeys:
    print(key)

for i in range(10): #print even in loops
    if i % 2 == 0:
        print(i)

for i in range(10): #print odd in loops
    if i % 2 != 0:
        print(i)

######### while loop #########
i = 0
while i < 10:
    print(i)
    i += 1



