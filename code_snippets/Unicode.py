re.findall(r'\w+', 'fox:αλεπού')

re.findall(r'\w+', 'fox:αλεπού', flags=re.A)

re.findall(r'[a-zA-Z0-9_]+', 'fox:αλεπού')

bool(re.search(r'[a-zA-Z]', 'İıſK'))

re.search(r'[a-z]+', 'İıſK', flags=re.I)[0]

bool(re.search(r'[a-z]', 'İıſK', flags=re.I|re.A))

regex.findall(r'\p{L}+', 'fox:αλεπού,eagle:αετός')

regex.findall(r'\p{Greek}+', 'fox:αλεπού,eagle:αετός')

regex.findall(r'\p{Word}+', 'φοο12,βτ_4,foo')

regex.sub(r'\P{L}+', r'', 'φοο12,βτ_4,foo')

[hex(ord(c)) for c in 'fox']

[c.encode('unicode_escape') for c in 'αλεπού']

[c.encode('unicode_escape') for c in 'İıſK']

re.findall(r'[\u0061-\u007a]+', 'fox:αλεπού,eagle:αετός')

