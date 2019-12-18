import re


def to_camel_case(text):
    string = re.split('-|, |_', text)
    for s in string[0]:
        if s.isupper():
            pass



to_camel_case('hi-hello')
to_camel_case('by_bye')