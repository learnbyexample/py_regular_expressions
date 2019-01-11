re.search(r'ab*c', 'abc ac adc abbbc')

re.search(r'b.*d', 'abc ac adc abbbc')

re.search(r'b.*d', 'abc ac adc abbbc')

re.search(r'b.*d', 'abc ac adc abbbc')[0]

re.search(r'b.*d', 'abc ac adc abbbc').group(0)

m = re.search(r'a(.*)d(.*a)', 'abc ac adc abbbc')

m[2]

m.groups()

re.sub(r'(a|b)\^2', lambda m: m[0].upper(), 'a^2 + b^2 - C*3')

re.findall(r'ab*c', 'abc ac adc abbbc')

re.findall(r'ab+c', 'abc ac adc abbbc')

re.findall(r'\bs?pare?\b', 'par spar apparent spare part pare')

re.findall(r't.*a', 'that is quite a fabricated tale')

re.findall(r't.*?a', 'that is quite a fabricated tale')

re.findall(r'a(b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')

re.findall(r'(x*):(y*)', 'xx:yyy x: x:yy :y')

re.finditer(r'ab+c', 'abc ac adc abbbc')

m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')

for m in m_iter:
    print(m)

m_iter = re.finditer(r'(x*):(y*)', 'xx:yyy x: x:yy :y')

[(m[1], m[2]) for m in m_iter]

m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')

for m in m_iter:
    print(m[0].upper())

m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')

for m in m_iter:
    print(m.span())

