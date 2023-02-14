# I literlaly don't know how to make this efficient 
# converts lowercase to uppercase 
alph = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function to ignore symbols, can only be used in stringToList()
def filterSymbols(character):
    filteredChar = ''.join(filter(str.isalnum, character))
    return filteredChar

# checks character index of given string, converts it to lowercase
def charsAQ(charstoConv):
    lowerChars = charstoConv.lower()
    convertedStr = alph.index(lowerChars)        
    return convertedStr

#convets a string to list using literal magic
def stringToList(string):
    list1 = []
    filStr = filterSymbols(string)
    list1[:0] = filStr.replace(" ", "")
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

AQmain()
