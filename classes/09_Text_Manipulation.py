sentence = "Curso em Video Python"

# slicing
print("\nSlicing")
print(sentence[9])  # only
print(sentence[9:13])  # interval
print(sentence[9:])  # x=9 until the end
print(sentence[:5])  # start to x = 5
print(sentence[9:21:2])  # jumps two by two until x =21
print(sentence[9::3])  # jumps three by three until the end

# analysis
print("\nAnalysis")
print(len(sentence))  # number of characters
print(sentence.count("o"))  # how many o there are in the sentence
print(sentence.count("o", 0, 13)) # how many o there is in the interval of the sentence
print(sentence.find("deo")) # find where start this string, returns 11 in this case
print(sentence.find("android")) # returns -1 to show that the method doesnt found the string
print('Curso' in sentence) # if this text exist in the sentence it will returns true, otherwise false

# transformation
print("\nTransformation")
print(sentence.replace('Python', 'Android'))  # replace
print(sentence.upper())  # high case letter
print(sentence.lower())  # low case letter
print(sentence.capitalize()) # it makes the first letter capitalized and the other letters lower
print(sentence.title())  # it makes ever first letter of all words capitilized

phrase = "   Aprenda Python  "
print(phrase.strip()) # remove excess spaces at the beginning and end of the chain
print(phrase.lstrip())  # remove excess spaces at the left side of the chain
print(phrase.rstrip())  # remove excess spaces at the right side of the chain

#division
print("\nDivision")
print(phrase.split()) # its like a generation list with all the words, divide a string in a list
txt = "hello, my name is Lorenzo, I am 19 years old"
x = txt.split(", ")
print(x)
txt = "apple#banana#cherry#orange"
y = txt.split("#", 1) # setting the maxsplit parameter to 1, will return a list with 2 elements!
print(y)
txt = "hello, my name is Lorenzo, I am 19 years old"
g = txt.split()
print(g [0]) # it takes the first position of the split
print(g [4] [3]) # the first parameter takes a slice of the list created by split and the second parameter takes the corresponding letter of this slice

#junction
print("\nJunction")
v = sentence.split()
print('-'.join(v))
print('.'.join(sentence))