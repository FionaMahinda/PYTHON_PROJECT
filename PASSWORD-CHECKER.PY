import string
import getpass #ma platform-independent way to enter a password in a command-line program


def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0
#enter the password characters
   for char in list(password):
       if char in string.ascii_lowercase: #lowercase letters
           lower_count += 1
       elif char in string.ascii_uppercase: #uppercase letter
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1 #program to count the number of spaces in string
       else:
           special_count += 1 #program to count the number of special characters in String

   if lower_count >= 1: # the number of times lowercase letters appears
       strength += 1
   if upper_count >= 1:  # the number of times uppercase letters appear
       strength += 1
   if num_count >= 1:   # the number of times numerals appear
       strength += 1
   if wspace_count >= 1: ##program to count the number of spaces in string
       strength += 1
   if special_count >= 1: ##program to count the number of special characters in String
       strength += 1

   if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')# the response if the password does not meet any of the requirements
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')# the response if the password is below average
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'# the response if the password is not strong enough
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')# the response if the password meets some of the requirements, its average.
   elif strength == 5:
       remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')# response if the password meets all the requirements for a strong password

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False): # check the current issued password
   valid = False
   if another_pw:# if you choose to check another password for its strength input 'y'for yes or 'n' for no
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')# command to allow checking of the password strnghth

   while not valid:
       if choice.lower() == 'y':# use a lowercase letter 'y'
           return True
       elif choice.lower() == 'n': # use a lowercase letter 'n'
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')


if __name__ == '__main__':# Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()# the process starts from the beginning
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)
