

file = open("stop-words.txt")
stopwords = file.readlines() #This reads through each line in the stop-words file 

def removeWords(item): #this creates a variable in order to cut word from the text
    for word in stopwords: #This loop will go through all of the words in the stop-words file and compare them to words inputted into the chatbot 
        next = word.strip() 
        item = item.replace(" " + next + " ", " ") #replaces the removed words with empty spaces (deletes them if they are found in stop-words file
    return item
    


while True:
    input = raw_input("Hello, my name is Chat Bot 3000 - what is your name? ") #whilst the chatbot is running it will print the text in speech marks 
    input = " " + input
    name = removeWords(input) #This states the name is the one element that has not been removed from the input by the word strip
    #filtered = removeWords(input)
    print("Hello " + name + " How are you today?") #prints the speech marked text along with the word stored in the variable 'name' (which should be the users name) 
    
    