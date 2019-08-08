d = { '1': 'one', '2': 'two', '4': 'four' }

re.sub(r'[124]', lambda m: d[m[0]], '9234012')

re.sub(r'\d', lambda m: d.get(m[0], 'X'), '9234012')

swap = { 'cat': 'tiger', 'tiger': 'cat' }

words = 'cat tiger dog tiger cat'

re.sub(r'\w+', lambda m: swap.get(m[0], m[0]), words)

re.sub(r'cat|tiger', lambda m: swap[m[0]], words)

d = { 'hand': 1, 'handy': 2, 'handful': 3, 'a^b': 4 }

words = [re.escape(k) for k in d.keys()]

'|'.join(sorted(words, key=len, reverse=True))

word = 'coffining'

while True:
    word, cnt = re.subn(r'fin', r'', word)
    if cnt == 0:
        break

word

row = '421,foo,2425,42,5,foo,6,6,42'

while True:
    row, cnt = regex.subn(r'(?<=\A|,)([^,]++).*\K,\1(?=,|\Z)', r'', row)
    if cnt == 0:
        break

row

regex.findall(r'\G\S', '123-87-593 42 foo')

regex.sub(r'\G\S', r'*', '123-87-593 42 foo')

regex.findall(r'\G\d+-?', '123-87-593 42 foo')

regex.sub(r'\G(\d+)(-?)', r'(\1)\2', '123-87-593 42 foo')

regex.findall(r'\G\w(?=\w)', 'cat12 bat pin')

regex.sub(r'\G\w(?=\w)', r'\g<0>:', 'cat12 bat pin')

regex.sub(r'\G[a-z ]', r'(\g<0>)', 'par tar-den hen-food mood')

eqn0 = 'a + (b * c) - (d / e)'

regex.findall(r'\([^()]++\)', eqn0)

eqn1 = '((f+x)^y-42)*((3-g)^z+2)'

regex.findall(r'\([^()]++\)', eqn1)

eqn1 = '((f+x)^y-42)*((3-g)^z+2)'

regex.findall(r'\((?:[^()]++|\([^()]++\))++\)', eqn1)

eqn2 = 'a + (b) + ((c)) + (((d)))'

regex.findall(r'\((?:[^()]++|\([^()]++\))++\)', eqn2)

lvl2 = regex.compile('''
         \(              #literal (
           (?:           #start of non-capturing group
            [^()]++      #non-parentheses characters
            |            #OR
            \([^()]++\)  #level-one RE
           )++           #end of non-capturing group, 1 or more times
         \)              #literal )
         ''', flags=regex.X)

lvl2.findall(eqn1)

lvl2.findall(eqn2)

lvln = regex.compile('''
         \(           #literal (
           (?:        #start of non-capturing group
            [^()]++   #non-parentheses characters
            |         #OR
            (?0)      #recursive call
           )++        #end of non-capturing group, 1 or more times
         \)           #literal )
         ''', flags=regex.X)

lvln.findall(eqn0)

lvln.findall(eqn1)

lvln.findall(eqn2)

eqn3 = '(3+a) * ((r-2)*(t+2)/6) + 42 * (a(b(c(d(e)))))'

lvln.findall(eqn3)

regex.split(r'[[:digit:]]+', 'Sample123string42with777numbers')

regex.sub(r'[[:alpha:]]+', r':', 'Sample123string42with777numbers')

regex.findall(r'[[:word:][:space:]]+', 'tea sea-pit sit-lean\tbean')

regex.findall(r'[[:^space:]]+', 'tea sea-pit sit-lean\tbean')

regex.findall(r'(?<![[:punct:]])\b\w+\b(?![[:punct:]])', 'tie. ink eat;')

re.findall(r'\b[^aeiou]+\b', 'tryst glyph pity why')

regex.findall(r'(?V1)\b[a-z&&[^aeiou]]+\b', 'tryst glyph pity why')

regex.findall(r'(?V1)\b[[a-l]~~[g-z]]+\b', 'gets eat top sigh')

para = '"Hi", there! How *are* you? All fine here.'

regex.sub(r'(?V1)[[:punct:]--[.!?]]+', r'', para)

words = 'tiger imp goat eagle rat'

regex.sub(r'\b(?:imp|rat)\b(*SKIP)(*F)|[a-z]++', r'(\g<0>)', words)

row = '1,"cat,12",nice,two,"dog,5"'

regex.sub(r'"[^"]++"(*SKIP)(*F)|,', r'|', row)

