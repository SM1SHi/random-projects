# I literlaly don't know how to make this efficient 
# converts lowercase to uppercase 
alph = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def charsAQ(charstoConv):
    lowerChars = charstoConv.lower()
    convertedStr = alph.index(lowerChars)
    return convertedStr

def stringToList(string):
    list1 = []
    list1[:0] = string.replace(" ", "")
    return list1

# map charsAQ to all elements in list1 
# numerize letters of a string 
def AQmain():
    words = input("Please enter words that you wish to encode in AQ: ")
    convertedWords = stringToList(words)
    result = list(map(charsAQ, convertedWords))
    sumElements = sum(result)
    print(sumElements)

AQmain()
