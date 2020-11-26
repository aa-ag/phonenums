import re
import phonenumbers

#-- Pure Python --#

def validPhoneNumber(phoneNumber):
    pattern = re.compile("^\([\dA-Z]{3}\)\s[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    print( pattern.match(phoneNumber) is not None )

### alternatively
def validPhoneNumber(phoneNumber):
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))


#-- API --#


#-- Python library "phonenumbers" --#
# Documentation: https://pypi.org/project/phonenumbers/

n = "+17792301817"

x = phonenumbers.parse(f"{n}", None)
print(type(x)) # <class 'phonenumbers.phonenumber.PhoneNumber'>
print(x) # Country Code: 1 National Number: 7792301817
print(phonenumbers.is_possible_number(x)) # True
print(phonenumbers.is_valid_number(x)) # True

print()

n2 = "+3477923018192020"

y = phonenumbers.parse(f"{n2}", "GB")
print(type(x))
print(y)
print(phonenumbers.is_possible_number(y)) # False
print(phonenumbers.is_valid_number(y)) # False