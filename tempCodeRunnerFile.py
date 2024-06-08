#Python script to check Password Strength
import string
def Length_Checker(password):
    length=len(password)
    if(length<12):
        res=False
    else:
        res=True
        
    if(res!=True):
        print("Password Is too Short, Password should be alteast 12 characters long")
        
def Upper_Case_Checker(password):
    for letters in password:
        if(letters.isupper()):
            res=True
            break
        else:
            res=False
    if(res!=True):
        print("Password do not have any Uppercase Letter")
        
def Alphabet_Checker(password):
    for letters in password:
        if(letters.isalpha()):
            res=True
            break
        else:
            res=False
    if(res!=True):
        print("Password do not have any Alphabet")
        
def Number_Checker(password):
    for letters in password:
        if(letters.isalpha()):
            res=False
            break
        else:
            res=True
    if(res!=True):
        print("Password do not have any Number Character")

def Special_Character_Checker(password):
    symbols=( '[' ,'@','_' ,'!','#','$','%','^','&' ,'/',"\'","'",'"','|','(',')','`','~')
    for letter in password:
        for character in symbols:
            if(letter==character):
                res=True
                break
            else:
                res=False
                
    if(res!=True):
        print("Password do not have any SpecialCharacter")
    
def password_checker(password):
    if len(password) == 0:
        print("The input was empty.")
    else:
            Length_Checker(password)
            Upper_Case_Checker(password)
            Alphabet_Checker(password)
            Number_Checker(password)
            Special_Character_Checker(password)
                    

user_input=input("Enter Your Password:-\t")    
password_checker(user_input)
        