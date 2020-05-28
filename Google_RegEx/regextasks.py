'''
Fill in the code to check if the text passed contains the vowels a, e and i,
 with exactly one occurrence of any other character in between.
'''
import re
def check_aei (text):
  result = re.search(r"a+.+e+.+i+", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


'''
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
 (including letters, numbers, and underscores)
 separated by one or more whitespace characters.
'''

import re
def check_character_groups(text):
  result = re.search(r"\w+\d", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

'''
Find countries
'''

print(re.findall(r"A.*a", "Argentina, Argelia, Armenia, Alemania, Azerbaiyán"))
print(re.search(r"A.*a", "Argentina, Argelia, Armenia, Alemania, Azerbaiyán"))
print(re.search(r"^A.*a$", "Argentina"))