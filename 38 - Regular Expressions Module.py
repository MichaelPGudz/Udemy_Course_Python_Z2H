# Regular Expressions

import re

patterns = ['term1', 'term2']
text = 'This is a string with term1 but not ther other term'

re.search('hello', 'hello world!')

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"'%(pattern, text)),

    #Check for match
    if re.search(pattern, text):
        print('\n')
        print('Match was found. \n')

    else:
        print('\n')
        print('No match was found.\n')

print(re.search('h','n'))

match = re.search(patterns[0], text)
print(type(match))

print(match.start())
print(match.end())
print(match.span())

split_term = '@'

phrase = 'What is your eamil, is it hello@gamil.com'

re.split(split_term,phrase)

print(re.findall('match','Here is one match, here is another match'))

def multi_re_find(patterns,phrase):
    '''
    akes in a list of regex patterns
    Prints a list of all matches
    '''

    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern,phrase))
        print('\n')


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

test_phrase_second = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns_second = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns_second,test_phrase_second)

test_phrase_third = 'This is a string! But it has punctuation. How can we remove it?'

print(re.findall('[^!.? ]+',test_phrase_third))


test_phrase_fourth = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns_fourth = ['[a-z]+',  # sequences of lower case letters
                 '[A-Z]+',  # sequences of upper case letters
                 '[a-zA-Z]+',  # sequences of lower or upper case letters
                 '[A-Z][a-z]+']  # one upper case letter followed by lower case letters

multi_re_find(test_patterns_fourth, test_phrase_fourth)

test_phrase_fifth = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns_fifth=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns_fifth,test_phrase_fifth)