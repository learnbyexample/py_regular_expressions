bool(re.search(r'b^2', 'a^2 + b^2 - C*3'))

bool(re.search(r'b\^2', 'a^2 + b^2 - C*3'))

re.sub(r'\(|\)', r'', '(a*b) + c')

re.sub(r'\\', r'/', r'\learn\by\example')

eqn = 'f*(a^b) - 3*(a^b)'

eqn.replace('(a^b)', 'c')

expr = '(a^b)'

print(re.escape(expr))

re.sub(re.escape(expr) + r'\Z', r'c', eqn)

terms = ['foo_baz', expr]

print('|'.join(re.escape(w) for w in terms))

