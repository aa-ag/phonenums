#-- Pure Python --#
import re

def validPhoneNumber(phoneNumber):
    pattern = re.compile("^\([\dA-Z]{3}\)\s[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    print( pattern.match(phoneNumber) is not None )

### alternatively
def validPhoneNumber(phoneNumber):
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))


#-- API --#


#-- Python library "phonenumbers" --#
# Documentation: https://pypi.org/project/phonenumbers/

