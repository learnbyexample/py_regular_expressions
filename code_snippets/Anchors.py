## String anchors

bool(re.search(r'\Acat', 'cater'))

bool(re.search(r'\Acat', 'concatenation'))

bool(re.search(r'\Ahi', 'hi hello\ntop spot'))

bool(re.search(r'\Atop', 'hi hello\ntop spot'))

bool(re.search(r'are\Z', 'spare'))

bool(re.search(r'are\Z', 'nearest'))

words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

[w for w in words if re.search(r'er\Z', w)]

[w for w in words if re.search(r't\Z', w)]

re.sub(r'\A', 're', 'live')

re.sub(r'\A', 're', 'send')

re.sub(r'\Z', 'er', 'cat')

re.sub(r'\Z', 'er', 'hack')

word_pat = re.compile(r'\Aat')

bool(word_pat.search('cater', 1))

bool(word_pat.search('cater'[1:]))

## re.fullmatch

word_pat = re.compile(r'\Acat\Z')

bool(word_pat.search('cat'))

bool(word_pat.search('concatenation'))

word_pat = re.compile(r'cat', flags=re.I)

bool(word_pat.fullmatch('Cat'))

bool(word_pat.fullmatch('Scatter'))

## Line anchors

pets = 'cat and dog'

bool(re.search(r'^cat', pets))

bool(re.search(r'^dog', pets))

bool(re.search(r'dog$', pets))

bool(re.search(r'^dog$', pets))

greeting = 'hi there\nhave a nice day\n'

bool(re.search(r'day$', greeting))

bool(re.search(r'day\n$', greeting))

bool(re.search(r'day\Z', greeting))

bool(re.search(r'day\n\Z', greeting))

bool(re.search(r'^top', 'hi hello\ntop spot', flags=re.M))

bool(re.search(r'ar$', 'spare\npar\ndare', flags=re.M))

elements = ['spare\ntool', 'par\n', 'dare']

[e for e in elements if re.search(r'are$', e, flags=re.M)]

bool(re.search(r'^par$', 'spare\npar\ndare', flags=re.M))

ip_lines = 'catapults\nconcatenate\ncat'

print(re.sub(r'^', '* ', ip_lines, flags=re.M))

print(re.sub(r'$', '.', ip_lines, flags=re.M))

## Word anchors

words = 'par spar apparent spare part'

re.sub(r'par', 'X', words)

re.sub(r'\bpar', 'X', words)

re.sub(r'par\b', 'X', words)

re.sub(r'\bpar\b', 'X', words)

words = 'par spar apparent spare part'

print(re.sub(r'\b', '"', words).replace(' ', ','))

re.sub(r'\b', ' ', '-----hello-----')

re.sub(r'\b', ' ', 'foo_baz=num1+35*42/num2')

re.sub(r'\b', ' ', 'foo_baz=num1+35*42/num2').strip()

words = 'par spar apparent spare part'

re.sub(r'\Bpar', 'X', words)

re.sub(r'\Bpar\b', 'X', words)

re.sub(r'par\B', 'X', words)

re.sub(r'\Bpar\B', 'X', words)

re.sub(r'\b', ':', 'copper')

re.sub(r'\B', ':', 'copper')

re.sub(r'\b', ' ', '-----hello-----')

re.sub(r'\B', ' ', '-----hello-----')

