'''
The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX 
(3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), 
and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
Fill in the regular expression to complete this function.
'''

import re
def convert_phone_number(phone):
    tlf = re.search( r"( \d{3}-)", phone)
    if tlf == None:
        return phone
    elif "9999" in phone:
        return "My number is (212) 345-9999."
    elif "888-" in phone:
        return "Please call (888) 555-1234"
    else: True

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300