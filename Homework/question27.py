#what are the regular expressions in python


import re

txt1 = 'The rain in the spain'

value =re.search('^The.*spain$',txt1)

if value:
    print('Txt is found to be matching')
else:
    print('No text is found to be matching')
