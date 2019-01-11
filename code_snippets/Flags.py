bool(re.search(r'cat', 'Cat'))

bool(re.search(r'cat', 'Cat', flags=re.IGNORECASE))

re.findall(r'c.t', 'Cat cot CATER ScUtTLe', flags=re.I)

re.findall(r'[a-z]+', 'Sample123string42with777numbers', flags=re.I)

re.sub(r'the.*ice', r'X', 'Hi there\nHave a Nice Day')

re.sub(r'the.*ice', r'X', 'Hi there\nHave a Nice Day', flags=re.S)

re.sub(r'the.*day', r'Bye', 'Hi there\nHave a Nice Day', flags=re.S|re.I)

bool(re.search(r'^top', "hi hello\ntop spot", flags=re.M))

bool(re.search(r'ar$', "spare\npar\ndare", flags=re.M))

rex = re.compile(r'''
        \A(                 # group-1, captures first 3 columns
            (?:[^,]+,){3}   # non-capturing group to get the 3 columns
          )
        ([^,]+)             # group-2, captures 4th column
        ''', flags=re.X)

rex.sub(r'\1(\2)', '1,2,3,4,5,6,7', count=1)

bool(re.search(r't a', 'cat and dog', flags=re.X))

bool(re.search(r't\ a', 'cat and dog', flags=re.X))

bool(re.search(r't[ ]a', 'cat and dog', flags=re.X))

bool(re.search(r't\x20a', 'cat and dog', flags=re.X))

re.search(r'a#b', 'foo a#b 123', flags=re.X)[0]

re.search(r'a\#b', 'foo a#b 123', flags=re.X)[0]

rex = re.compile(r'\A((?:[^,]+,){3})(?#3-cols)([^,]+)(?#4th-col)')

rex.sub(r'\1(\2)', '1,2,3,4,5,6,7', count=1)

re.findall(r'Cat[a-z]*\b', 'Cat SCatTeR CATER cAts')

re.findall(r'Cat(?i:[a-z]*)\b', 'Cat SCatTeR CATER cAts')

re.findall(r'Cat[a-z]*\b', 'Cat SCatTeR CATER cAts', flags=re.I)

re.findall(r'(?i)Cat[a-z]*\b', 'Cat SCatTeR CATER cAts')

re.findall(r'(?-i:Cat)[a-z]*\b', 'Cat SCatTeR CATER cAts', flags=re.I)

