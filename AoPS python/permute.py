def anagrams(string):
    
    #Base Cases
    
    if len(string)==0:#If list is empty
        return []; #Return empty list
    elif len(string) == 1: #If list contains one argument
        return [string] #Return that list
    
    
    #Recursive Case
    
    else: #Otherwise...
        anagram = [] #Create empty list
        
        for letter in range(len(string)): #From 0 to length of string - 1
            remaining = string[:letter] + string[letter+1:] #Remaining letters
            
            for each in anagrams(remaining): #For each anagram
                anagram.append(string[letter]+each) #Add anagram to empty list

        return anagram #Return all anagram

 
def jumble_solve(string):
    
    lst = anagrams(string) #converts "string" to all anagrams of "string"
    valid = [] #creates empty list for text file
    jumbled = [] #creates empty list for accurate jumbled words
    check = open("wordlist.txt","r") #opens and reads the file

    for word in check: #for each word in the file
        valid.append(word.strip()) #append the word to our empty list 
    
    for word in lst: #for each word in our list of anagrams
        word = word.lower() #converts to lower case
        for line in valid: #for each word in the file
            if word == line: #if the both words match
                jumbled.append(word) #add the word to list "jumbled"
    check.close()
    return jumbled #return list "jumbled"


#test cases
print(jumble_solve("CHWAT"))
print(jumble_solve("RAROM"))
print(jumble_solve("CEPLIN"))
print(jumble_solve("YAFLIM"))
