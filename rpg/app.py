import random
import string 
print("Welcom to Random Password Generator!..")

def main(): 
    while True:  
        userSelection = input("Do you wish to generate a Password?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")  
        if userSelection == 'N' or userSelection == 'n':  
            print("Thank You! See you next time.")  
            break  
        elif userSelection == 'Y' or userSelection == 'y':  
            length = int(input("Enter the length of the Password: "))  
            lower=string.ascii_lowercase
            upper=string.ascii_uppercase
            digit=string.digits
            symbols=string.punctuation
            com=lower+upper+digit+symbols
            x=random.sample(com,length)
            password="".join(x)
            print(password)
        else:  
            print("Invalid Input! Try Again.")  
            print("")
main()