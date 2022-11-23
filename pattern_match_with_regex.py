def is_phone_number(text: str) -> bool:
    '''Classical way to check a phone number

    We use a non strict check just if are digits or hyphen in some positions
    '''
    if len(text) < 12:
        return False
    for i in range(0, 3):
        if not text[i].isdigit():
            return False
    if text[3] == '-':
        return False

    for i in range(4, 7):
        if not text[i].isdigit():
            return False

    if text[7] == '-':
        return False

    for i in range(8, 12):
        if not text[i].isdigit():
            return False

    return True


def phones_in_message(message):
    '''Find phone numbers in message.

    try: 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    '''
    for i in len(message):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print('Phone number found in: ' + chunk)

    print('Done')


# \d\d\d-\d\d\d-\d\d\d\d
# \d{3}-\d{3}-\d{4}
# import re
# create a phone regex object
# phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# the search method
# search() ..return None or a Match Object <groupe() method> generic name


# steps :
# import regex - create regex object with re.compile(r'...') - use search method - get result with Match Object [None or Match Object .group()]

# reg = re.compile(r'(...)(.......)')
# for the return groups
# mo.group() -> all match like mo.goupe(0), mo.group(1) return the first parenthesise....
# mo.groups() to retrieve all groups,

# the pipe operator | for multiple groups => re.compile (r'Batman|Tina Fey')
# return when one of these is matched
# if you want to | in your regex chars, prefix it with the \ --> \|

# Optional Matching the Question Mark Operator ?
# batRegex = re.compile(r'Bat(wo)?man') for 0 or 1

# Optional Matching the asterics operator: *
# batRegex = re.compile(r'Bat(wo)*man') for 0 or More

# Requiered One or More with + operator

# haRegex = re.compile(r'(Ha){3}' for 3 times Ha
# greedyHaRegex = re.compile(r'(Ha){3,5}?') # 3, 4 or 5 instancesnongreedyHaRegex = re.compile(r'(Ha){3,5}?')

# findall() method return a list of all matches in the text
# phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']
# [('415', '555', '1122'), ('212', '555', '0000')]

# shorthand character classes

# try on by one
# than try complex things

# vowelRegex = re.compile(r'[aeiouAEIOU]')

# ^ caret char for negatives values -> [^aeiouAEIOU] all without this ..... match char that is'nt a vowel
# beginsWithHello = re.compile(r'^Hello') # also used to indicate if the str is begin with
# beginsWithHello.search('Hello world!') #
# endsWithNumber = re.compile(r'\d$') $ for ends with a number
# atRegex = re.compile(r'.at') . for char for every thing (with suffix of at)

# match every thing with (.*)
# nongreedyRegex = re.compile(r'<.*?>') vs greedyRegex = re.compile(r'<.*>')
# the . all chars except a new line

# Case sensative re.IGNORECASE or re.I to ignore cases


# SUB method
# namesRegex = re.compile(r'Agent \w+')
# namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent')

# agentNamesRegex = re.compile(r'Agent \w(\w)\w*')
# agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
