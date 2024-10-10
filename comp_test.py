import sys

#creates a function for reading the comments in the file as well as cleaning out odd spaces and comments
def load_data(fileName):
    cleanLines = [] #creates an empty list 
    try:
        with open(fileName, 'r') as openfile:
            lines = openfile.readlines()  #uses readlines to read all the lines in Input.txt and put into lines list

        #go through each line (element) in the lines
        for line in lines:
            
            #removes comments by identifying #
            line = line.split('#', 1)[0]
            #adds only one space between each word in the line (no weird spaces between words)
            strippedLine = ' '.join(line.split())
            if strippedLine:
                cleanLines.append(strippedLine)

        #puts all the lines together and adds a new line for each line
        cleanedLines = '\n'.join(cleanLines)
      
    except FileNotFoundError: #error if input.txt does not exist (edge case 1) 
        print("Error: File not found.")
        sys.exit()
    return cleanedLines

#creates a function that will take the cleaned lines and tokenize each element 
def tokenization(lines):
    #create a dictionary with keys for each token type
    tokens = {
        'Keywords': [],
        'Identifiers': [],
        'Operators': [],
        'Literals': [],
        'Separators': [],
    }
    
    #creates dictionaries to categorize each word into the correct value in the tokens dictionary
    keyword = {'False', 'True', 'None' , 'and', 'as', 'assert', 'async', 'await', 'def', 'del', 'elif', 'else', 'break', 'class', 'continue', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'}
    operator = {'=', '+', '-', '*', '/', '%', '<', '>', '<=', '>=', '+=', '-=', '==', '!='}
    separator = {'{', '}', '(', ')', ':', ','}

    #creates a variable to count each token
    tokenCount = 0
    
    #add spaces between each element (Seperators and Operators) so they are seperated from other elements
    elements = lines.replace('(', ' ( ').replace(')', ' ) ').replace(':', ' : ').replace(',', ' , ').replace('+', ' + ').replace('-', ' - ').replace('=', ' = ').replace('*', ' * ').replace('/', ' / ').split()

    #go through each element and append to a key in the token dictionary and increment the token count for each element
    for element in elements:
        if element in keyword:
            tokenCount+= 1
            if element not in tokens['Keywords']:
                tokens['Keywords'].append(element)
                
        elif element in operator:
            tokenCount+= 1
            if element not in tokens['Operators']:
                tokens['Operators'].append(element)
                
        elif element.isidentifier():
            tokenCount+= 1
            if element not in tokens['Identifiers']:
                tokens['Identifiers'].append(element)
                
        elif element in separator:
            tokenCount+= 1
            if element not in tokens['Separators']:
                tokens['Separators'].append(element)

        #if the element does not fall into the other categories, it will be a Literal
        elif element not in tokens['Keywords'] and element not in tokens['Identifiers'] and element not in tokens['Separators']:
            tokenCount+= 1
            if element not in tokens['Literals']:
                tokens['Literals'].append(element)

    #change the token_count type to string from int so it can be printed
    tokenCount = str(tokenCount)
    print('The total token count is: ' + tokenCount)
    print('The cleaned code looks like: ')
   
    return tokens
    
    
#creates a function that will take the token dictionary and write it into an output file                         
def write_data(tokens, outputFile):
        with open(outputFile, 'w') as openfile:
            #for each token type in the tokens dictonary, write the name of the type and add the values assigned to the key seperates by commas with a newline
            for tokenType in tokens:
                    items = tokens[tokenType]
                    openfile.write(f"{tokenType}: {', '.join(items)}\n")
            


def main():

    #call load_data function and assign to variable
    cleanedData = load_data('Input.txt')

    #uses variable assigned to load_data function when calling tokenization function
    tokenize = tokenization(cleanedData)

    #uses tokenize variable to write into 'Output.txt'
    writeData = write_data(tokenize, 'Output.txt')

    #terminate if empty list was returned by load_data (edge case)
    if cleanedData == []:
        print("Error: Empty Input.txt")
    else:
        print(cleanedData)
        return
    
main()
