## Escaping with \

bool(re.search(r'b^2', 'a^2 + b^2 - C*3'))

bool(re.search(r'b\^2', 'a^2 + b^2 - C*3'))

re.sub(r'\(|\)', '', '(a*b) + c')

re.sub(r'\\', '/', r'\learn\by\example')

eqn = 'f*(a^b) - 3*(a^b)'

eqn.replace('(a^b)', 'c')

## re.escape

expr = '(a^b)'

print(re.escape(expr))

eqn = 'f*(a^b) - 3*(a^b)'

re.sub(re.escape(expr) + r'\Z', 'c', eqn)

terms = ['a_42', '(a^b)', '2|3']

pat1 = re.compile('|'.join(re.escape(s) for s in terms))

pat2 = re.compile('|'.join(terms))

print(pat1.pattern)

print(pat2.pattern)

s = 'ba_423 (a^b)c 2|3 a^b'

pat1.sub('X', s)

pat2.sub('X', s)

## Escape sequences

re.sub(r'\t', ':', 'a\tb\tc')

re.sub(r'\n', ' ', '1\n2\n3')

re.search(r'\e', 'hello')

re.sub(r'\x20', '', 'h e l l o')

re.sub(r'2\x7c3', '5', '12|30')

re.sub(r'2|3', '5', '12|30')

