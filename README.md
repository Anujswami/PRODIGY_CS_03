# Password Strength Checker

A Python script to check the strength of a password based on multiple criteria including length, uppercase letters, alphabets, numbers, and special characters.

## Features

- **Length Check**: Ensures the password is at least 12 characters long.
- **Uppercase Letter Check**: Ensures the password contains at least one uppercase letter.
- **Alphabet Check**: Ensures the password contains at least one alphabetic character.
- **Number Check**: Ensures the password contains at least one numeric character.
- **Special Character Check**: Ensures the password contains at least one special character.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Script

1. Clone the repository or download the script file.

git clone https://github.com/Anujswami/PRODIGY_CS_03.git
cd PRODIGY_CS_03


Run the script.


python Password_Strength_Checker.py


Enter your password when prompted.


Enter Your Password: <your_password_here>

Example Output

Enter Your Password: Password123!
Your password is good.

Or

Enter Your Password: pass
Password is too short, it should be at least 12 characters long.
Password does not have any uppercase letters.
Password does not have any special character.


### Code Explanation
The script defines several functions to check different aspects of password strength:

length_checker(password): Checks if the password is at least 12 characters long.

upper_case_checker(password): Checks if the password contains at least one uppercase letter.

alphabet_checker(password): Checks if the password contains at least one alphabetic character.

number_checker(password): Checks if the password contains at least one numeric character.

special_character_checker(password): Checks if the password contains at least one special character.

These functions are called by password_checker(password), which collects and prints any issues. If no problems are found, it prints that the password is good.
