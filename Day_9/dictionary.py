#basic dictionary
programming_dictionary = {

    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

#add new key and value
programming_dictionary['loop'] = 'The action to doing something over and over again'

#create a empty dictionary
empty_dictionary = {}

#read a item into empty_dictionary
print(programming_dictionary['Bug'])

#edit a item into dictionary
programming_dictionary['Bug'] = 'A moth in your computer'

#wipe(clear) a empty_dictionary
#programming_dictionary = {}

#loop into a dictionary
for think in programming_dictionary:
    print(think)#print the key
    print(programming_dictionary[think])#print the value