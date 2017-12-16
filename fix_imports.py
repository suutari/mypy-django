#!/usr/bin/env python
import re
import sys


dont_reexport = ['collections', 'typing', 'datetime', 'django.utils.datastructures']

pattern1 = r'(from +[a-zA-Z_\.0-9]+ +import +\()((?:\s|#)*(?:[a-zA-Z_0-9]+(?:\s|#)*,?(?:\s|#)*)+)(\))'
pattern2 = r'(from +[a-zA-Z_\.0-9]+ +import +)((?:[a-zA-Z_0-9]+ *,? *)+)()$'


def fix_import(match):
    if any([i in match.group(1) for i in dont_reexport]) or ' as ' in match.group(2):
        inner = match.group(2)
    else:
        inner = re.sub(r'([a-zA-Z_0-9]+)', r'\1 as \1', match.group(2))
    return match.group(1) + inner + match.group(3)


def main():
    """Usage: find | grep __init__.pyi | xargs ./fix_imports.py"""
    for filename in sys.argv[1:]:
        print('fixing: ' + filename)
        with open(filename, 'r') as f:
            code = f.read()
        code = re.sub(pattern1, fix_import, code)
        code = re.sub(pattern2, fix_import, code, flags=re.MULTILINE)
        with open(filename, 'w') as f:
            f.write(code)


main()
