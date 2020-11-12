import re

def isPhoneNumber(text, isAll=False):
    phoneNumberRegex = re.compile(r'(\(\d\d\d\)-)?(\d\d\d-\d\d\d\d)')
    matches, allMatches = (None, None)
    if isAll == False:
        matches = phoneNumberRegex.search(text)
        if matches != None:
            print('Phone number found, print by group: %s' % matches.group())
            #area, main = matches.groups()
            #print('Phone number found, print by types: %s' % matches.group())
        else:
            print('Phone number not found')
    else:
        allMatches = phoneNumberRegex.findall(text)
        if allMatches != None:
            print('Phone number found, print all: %s' % allMatches)
    

if __name__ == '__main__':
    isPhoneNumber('Hello. I am Eggy. My number is (025)-555-4242. Thanks.')
    isPhoneNumber('Hello. I am Eggy Brother. My cell number is 555-6666 and work number is (025)-512-6666 Thanks.', True)