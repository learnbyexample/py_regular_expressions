## Custom character sets

words = ['cute', 'cat', 'cot', 'coat', 'cost', 'scuttle']

[w for w in words if re.search(r'c[ou]t', w)]

re.sub(r'[aeo]+t', 'X', 'meeting cute boat site foot')

## Range of characters

re.findall(r'[0-9]+', 'Sample123string42with777numbers')

re.findall(r'\b[a-z0-9]+\b', 'coat Bin food tar12 best')

re.findall(r'\b[p-z][a-z]*\b', 'coat tin food put stoop best')

re.findall(r'\b[a-fp-t]+\b', 'coat tin food put stoop best')

## Negating character sets

re.findall(r'[^0-9]+', 'Sample123string42with777numbers')

re.sub(r'\A([^:]+:){2}', '', 'foo:123:bar:baz', count=1)

re.sub(r'=[^=]+\Z', '', 'foo=42; baz=123', count=1)

dates = '2020/04/25,1986/Mar/02,77/12/31'

re.findall(r'([^/]+)/([^/]+)/([^/,]+),?', dates)

words = ['tryst', 'fun', 'glyph', 'pity', 'why']

[w for w in words if re.search(r'\A[^aeiou]+\Z', w)]

[w for w in words if not re.search(r'[aeiou]', w)]

## Matching metacharacters literally

re.findall(r'\b[a-z-]{2,}\b', 'ab-cd gh-c 12-423')

re.findall(r'\b[a-z\-0-9]{2,}\b', 'ab-cd gh-c 12-423')

re.findall(r'a[+^]b', 'f*(a^b) - 3*(a+b)')

re.findall(r'a[\^+]b', 'f*(a^b) - 3*(a+b)')

re.search(r'[]a-z0-9[]+', 'words[5] = tea')[0]

re.search(r'[a-z\[\]0-9]+', 'words[5] = tea')[0]

print(re.search(r'[a\\b]+', r'5ba\babc2')[0])

## Escape sequence sets

re.split(r'\d+', 'Sample123string42with777numbers')

re.findall(r'\d+', 'foo=5, bar=3; x=83, y=120')

''.join(re.findall(r'\b\w', 'sea eat car rat eel tea'))

re.findall(r'[\w\s]+', 'tea sea-pit sit-lean\tbean')

re.sub(r'\D+', '-', 'Sample123string42with777numbers')

re.sub(r'\W+', '', 'foo=5, bar=3; x=83, y=120')

re.findall(r'\S+', '   1..3  \v\f  foo_baz 42\tzzz   \r\n1-2-3  ')

## Numeric ranges

re.findall(r'\b[12]\d\b', '23 154 12 26 98234')

re.findall(r'\b\d{3,}\b', '23 154 12 26 98234')

re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234')

m_iter = re.finditer(r'\d+', '45 349 651 593 4 204')

[m[0] for m in m_iter if int(m[0]) < 350]

def num_range(s):
    return '1' if 200 <= int(s[0]) <= 650 else '0'

re.sub(r'\d+', num_range, '45 349 651 593 4 204')

