import re
import phonenumbers
import requests
import config

#-- Pure Python --#

def validPhoneNumber(phoneNumber):
    pattern = re.compile("^\([\dA-Z]{3}\)\s[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    print( pattern.match(phoneNumber) is not None )

### alternatively
def validPhoneNumber(phoneNumber):
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))

#-- Python library "phonenumbers" --#
# Documentation: https://pypi.org/project/phonenumbers/

n = "+17792301817"

x = phonenumbers.parse(f"{n}", None)
type(x) # <class 'phonenumbers.phonenumber.PhoneNumber'>
# print(x) # Country Code: 1 National Number: 7792301817
phonenumbers.is_possible_number(x) # True
phonenumbers.is_valid_number(x) # True

n2 = "+3477923018192020"

y = phonenumbers.parse(f"{n2}", "GB")
type(x)
phonenumbers.is_possible_number(y) # False
phonenumbers.is_valid_number(y) # False

#-- API --#
# Documentation: https://numverify.com/documentation
# Data set: https://www.kaggle.com/juanumusic/countries-iso-codes

number = '4158586273'
res = requests.get(f'http://apilayer.net/api/validate?access_key={config.KEY}&number={number}&format=1').json()

print(res)