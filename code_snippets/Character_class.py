## Custom character sets

words = ['cute', 'cat', 'cot', 'coat', 'cost', 'scuttle']

[w for w in words if re.search(r'c[ou]t', w)]

re.findall(r'.[aeo]+t', 'meeting cute boat site foot cat net')

## Range of characters

re.findall(r'[0-9]+', 'Sample123string42with777numbers')

re.findall(r'\b[a-z0-9]+\b', 'coat Bin food tar12 best Apple fig_42')

re.findall(r'\b[p-z][a-z]*\b', 'coat tin food put stoop best fig_42 Pet')

re.findall(r'\b[a-fp-t]+\b', 'coat tin food put stoop best fig_42 Pet')

## Negating character sets

re.findall(r'[^0-9]+', 'Sample123string42with777numbers')

re.sub(r'\A([^:]+:){2}', '', 'apple:123:banana:cherry')

re.sub(r'=[^=]+\Z', '', 'apple=42; cherry=123')

dates = '2023/04/25,1986/Mar/02,77/12/31'

re.findall(r'([^/]+)/([^/]+)/([^,]+),?', dates)

words = ['tryst', 'fun', 'glyph', 'pity', 'why']

[w for w in words if re.search(r'\A[^aeiou]+\Z', w)]

[w for w in words if not re.search(r'[aeiou]', w)]

## Matching metacharacters literally

re.findall(r'\b[a-z-]{2,}\b', 'ab-cd gh-c 12-423')

re.findall(r'\b[a-z\-0-9]{2,}\b', 'ab-cd gh-c 12-423')

re.findall(r'a[+^]b', 'f*(a^b) - 3*(a+b)')

re.findall(r'a[\^+]b', 'f*(a^b) - 3*(a+b)')

s = 'words[5] = tea'

re.search(r'[]a-z0-9[]+', s)[0]

re.search(r'[a-z\[\]0-9]+', s)[0]

re.sub(r'[][]', '', s)

print(re.search(r'[a\\b]+', r'5ba\babc2')[0])

## Escape sequence sets

re.split(r'\d+', 'Sample123string42with777numbers')

re.findall(r'\d+', 'apple=5, banana=3; x=83, y=120')

''.join(re.findall(r'\b\w', 'sea eat car rat eel tea'))

re.findall(r'[\w\s]+', 'tea sea-Pit Sit;(lean_2\tbean_3)')

re.sub(r'\D+', '-', 'Sample123string42with777numbers')

re.sub(r'\W+', ':', 'apple=5, banana=3; x=83, y=120')

re.findall(r'\S+', '   7..9  \v\f  fig_tea 42\tzzz   \r\n1-2-3  ')

ip = ['#comment', 'c = "#"', '\t #comment', 'fig', '', ' \t ']

[s for s in ip if re.search(r'\A\s*[^#]', s)]

[s for s in ip if re.search(r'\A\s*+[^#]', s)]

[s for s in ip if re.search(r'\A\s*[^#\s]', s)]

## Numeric ranges

re.findall(r'\b[12]\d\b', '23 154 12 26 98234')

re.findall(r'\b\d{3,}\b', '23 154 12 26 98234')

re.findall(r'\b0*+\d{3,}\b', '0501 035 154 12 26 98234')

m_iter = re.finditer(r'\d+', '45 349 651 593 4 204 350')

[m[0] for m in m_iter if int(m[0]) < 350]

def num_range(s):
    return '1' if 200 <= int(s[0]) <= 650 else '0'

re.sub(r'\d+', num_range, '45 349 651 593 4 204')

