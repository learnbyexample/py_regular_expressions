bool(re.search(r'\Acat', 'cater'))

bool(re.search(r'\Acat', 'concatenation'))

bool(re.search(r'\Ahi', 'hi hello\ntop spot'))

bool(re.search(r'\Atop', 'hi hello\ntop spot'))

bool(re.search(r'are\Z', 'spare'))

bool(re.search(r'are\Z', 'nearest'))

words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

[w for w in words if re.search(r'er\Z', w)]

[w for w in words if re.search(r't\Z', w)]

pat = re.compile(r'\Acat\Z')

bool(pat.search('cat'))

bool(pat.search('cater'))

bool(pat.search('concatenation'))

pat = re.compile(r'\Aat\Z')

bool(pat.search('cat', 1))

bool(pat.search('cat'[1:]))

re.sub(r'\A', r're', 'live')

re.sub(r'\A', r're', 'send')

re.sub(r'\Z', r'er', 'cat')

re.sub(r'\Z', r'er', 'hack')

word = 'cater'

re.sub(r'\Acat', r'hack', word)

word

word = re.sub(r'\Acat', r'hack', word)

word

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

bool(re.search(r'^tap', "hi hello\ntop spot", flags=re.M))

bool(re.search(r'ar$', "spare\npar\ndare", flags=re.M))

elements = ['spare\n', 'par\n', 'dare']

[e for e in elements if re.search(r'are$', e, flags=re.M)]

bool(re.search(r'^par$', "spare\npar\ndare", flags=re.M))

ip_lines = "catapults\nconcatenate\ncat"

print(re.sub(r'^', r'* ', ip_lines, flags=re.M))

print(re.sub(r'$', r'.', ip_lines, flags=re.M))

words = 'par spar apparent spare part'

re.sub(r'par', r'X', words)

re.sub(r'\bpar', r'X', words)

re.sub(r'par\b', r'X', words)

re.sub(r'\bpar\b', r'X', words)

print(re.sub(r'\b', r'"', words).replace(' ', ','))

re.sub(r'\b', r' ', '-----hello-----')

re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2')

re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2').strip()

words = 'par spar apparent spare part'

re.sub(r'\Bpar', r'X', words)

re.sub(r'\Bpar\b', r'X', words)

re.sub(r'par\B', r'X', words)

re.sub(r'\Bpar\B', r'X', words)

re.sub(r'\b', r':', 'copper')

re.sub(r'\B', r':', 'copper')

re.sub(r'\b', r' ', '-----hello-----')

re.sub(r'\B', r' ', '-----hello-----')

