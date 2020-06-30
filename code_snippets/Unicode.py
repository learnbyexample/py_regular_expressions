## re.ASCII

re.findall(r'\w+', 'fox:αλεπού')

re.findall(r'\w+', 'fox:αλεπού', flags=re.A)

re.findall(r'[a-zA-Z0-9_]+', 'fox:αλεπού')

bool(re.search(r'[a-zA-Z]', 'İıſK'))

re.search(r'[a-z]+', 'İıſK', flags=re.I)[0]

bool(re.search(r'[a-z]', 'İıſK', flags=re.I|re.A))

## Codepoints and Unicode escapes

[ord(c) for c in 'fox']

[hex(ord(c)) for c in 'fox']

[c.encode('unicode_escape') for c in 'αλεπού']

[c.encode('unicode_escape') for c in 'İıſK']

re.findall(r'[\u0061-\u007a]+', 'fox:αλεπού,eagle:αετός')

## \N escape sequence

'\N{EM DASH}'

'\N{LATIN SMALL LETTER TURNED DELTA}'

