def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str encodes plaintext using
    the railfence cipher numRails is the number of rails'''
    
    plaintext = list(plaintext) #converts input to a list
    end = len(plaintext) #stores length in variable end
    cypher = "" #empty string
    
    for start in range(numRails - 1, -1, -1): #numRails - 1 to 0 inclusive
        for letter in range(start,end,numRails): #for letter from current numRail to length of text, skipping by numRails
            cypher += plaintext[letter] #add letter to empty string cypher
    return(cypher) #return cypher

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    ciphertext = list(ciphertext) #converts input to list
    length = len(ciphertext) #stores length in variable length
    decipher = [[]]*length #creates empty array of the same length
    z = 0 #creates a variable z

    for i in range (1,numRails+1): #runs from 1 to numRails+1 inclusive (length of NumRails)
        railLen = (length + numRails - i)//numRails #gets the length of the rail
        z += railLen  #adds railLen to z
        r = ciphertext[length-z:length-z+railLen] #splits string into enciphered rail
        for letter in range(railLen): #from 0-railLen
            decipher[i-1 + (numRails*letter)] = r[letter] #attaches the deciphered letter to corresponding loaction in array decipher
    decipher = "".join(decipher) #joins the list into a string
    return decipher #returns whole value
          

def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    
    inputFile = open(wordfilename, "r") #reads in file
    punctuations = ''';:'",.?!@#$%&_~'''#string for punctuation
    mostAccurate = 0; #creates variable mostAccurate
    valid =[] #creates empty array vaild
    actualWord = "" #creates empty string actualWord
    
    for line in inputFile: #for each line in the file
        valid.append(line.strip()) #add the line to our array valid (without the newline character)
        
    for numRails in range(1,11): #from 1 to 10 inclusive
        words = decipher_fence(ciphertext,numRails).split() #deciphers ciphertext with numRails amount of rails
        count = 0; #creates count
        for word in words: #for each word in deciphered string
            for char in word: #for each character in word
                if char in punctuations: #if it is a punctuation
                    word = word.replace(char, "")#replace it with empty string
            for arg in valid: #for each argument/word in valid
                if word == arg: #if the word in deciphered string is the same as the argument
                   count+=1 #increase count by 1
            if count>mostAccurate: #if count > mostAccurate
                mostAccurate = count #change mostAccurate to match
                actualWord = " ".join(words) #converts the words into a string
    inputFile.close()
    return actualWord


# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!


# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
