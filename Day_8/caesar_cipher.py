
from arts_pro import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    cipher_text = ''
    for letter in text:
        index = alphabet.index(letter) + shift
        cipher_text += alphabet[index]
       
    print(f"The encoded text is {cipher_text}") 
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    
def decrypt(cipher_text, shift):
	text = ''
	for letter in cipher_text:
		index = alphabet.index(letter) - shift
		text += alphabet[index]
       
	print(f"The decoded text is {text}") 

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == 'encode':
    encrypt(text = text, shift = shift)
else:
    decrypt(cipher_text = text, shift = shift)
#TODO-4 resume the 2 functions into one function a resume all the code u can(name function caesar ) and ask a use if wants restart program