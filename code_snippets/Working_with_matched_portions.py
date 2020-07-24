## re.Match object

re.search(r'ab*c', 'abc ac adc abbbc')

re.fullmatch(r'1(2|3)*4', '1233224')

sentence = 'that is quite a fabricated tale'

m = re.search(r'q.*?t', sentence)

m.span()

m.span()[0]

re.search(r'q.*?t', sentence).span()

re.search(r'b.*d', 'abc ac adc abbbc')

re.search(r'b.*d', 'abc ac adc abbbc')[0]

re.search(r'b.*d', 'abc ac adc abbbc').group(0)

m = re.fullmatch(r'a(.*?) (.*)d(.*)c', 'abc ac adc abbbc')

m[2]

m.group(3, 1)

m.groups()

m = re.search(r'w(.*)me', 'awesome')

m.span()

m.span(1)

m.start()

m.end(1)

pat = re.compile(r'hi.*bye')

m = pat.search('This is goodbye then', 1, 15)

m.pos

m.endpos

m.re

m.string

## Assignment expressions

if m := re.search(r'(.*)s', 'oh!'):
    print(m[1])

if m := re.search(r'(.*)s', 'awesome'):
    print(m[1])

text = ['type: fruit', 'date: 2020/04/28']

for ip in text:
    if m := re.search(r'type: (.*)', ip):
        print(m[1])
    elif m := re.search(r'date: (.*?)/(.*?)/', ip):
        print(f'month: {m[2]}, year: {m[1]}')

## Using functions in replacement section

re.sub(r'(a|b)\^2', lambda m: m[0].upper(), 'a^2 + b^2 - C*3')

re.sub(r'2|3', lambda m: str(int(m[0])**2), 'a^2 + b^2 - C*3')

## Using dict in replacement section

d = { '1': 'one', '2': 'two', '4': 'four' }

re.sub(r'1|2|4', lambda m: d[m[0]], '9234012')

re.sub(r'0|1|2|3|4|5|6|7|8|9', lambda m: d.get(m[0], 'X'), '9234012')

swap = { 'cat': 'tiger', 'tiger': 'cat' }

words = 'cat tiger dog tiger cat'

re.sub(r'cat|tiger', lambda m: swap[m[0]], words)

d = { 'hand': '1', 'handy': '2', 'handful': '3', 'a^b': '4' }

words = sorted(d.keys(), key=len, reverse=True)

pat = re.compile('|'.join(re.escape(s) for s in words))

pat.pattern

pat.sub(lambda m: d[m[0]], 'handful hand pin handy (a^b)')

## re.findall

re.findall(r'ab*c', 'abc ac adc abbbc')

re.findall(r'ab+c', 'abc ac adc abbbc')

s = 'PAR spar apparent SpArE part pare'

re.findall(r'\bs?pare?\b', s, flags=re.I)

re.findall(r't.*a', 'that is quite a fabricated tale')

re.findall(r't.*?a', 'that is quite a fabricated tale')

re.findall(r'ab*c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')

re.findall(r'a(b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')

re.findall(r'(.*?)/(.*?)/(.*?),', '2020/04/25,1986/Mar/02,77/12/31')

## re.finditer

re.finditer(r'ab+c', 'abc ac adc abbbc')

m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')

for m in m_iter:
    print(m)

m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')

for m in m_iter:
    print(m[0].upper(), m.span(), sep='\t')

d = '2020/04/25,1986/Mar/02,77/12/31'

m_iter = re.finditer(r'(.*?)/(.*?)/(.*?),', d)

[m.groups() for m in m_iter]

d = '2020/04/25,1986/Mar/02,77/12/31'

m_iter = re.finditer(r'(.*?),', d)

[m[1] for m in m_iter]

[m[1] for m in m_iter]

## re.split with capture groups

re.split(r'1*4?2', '31111111111251111426')

re.split(r'(1*4?2)', '31111111111251111426')

re.split(r'(1*)4?2', '31111111111251111426')

re.split(r'(a+)b+(c+)', '3.14aabccc42')

re.split(r'(1*)(4)?2', '31111111111251111426')

re.split(r'(a+b+c+)', '3.14aabccc42abc88', maxsplit=1)

## re.subn

greeting = 'Have a nice weekend'

re.sub(r'e', 'E', greeting)

re.subn(r'e', 'E', greeting)

word = 'coffining'

while True:
    word, cnt = re.subn(r'fin', '', word)
    if cnt == 0:
        break

word

