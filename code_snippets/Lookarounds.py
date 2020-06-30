## Conditional expressions

items = ['1,2,3,4', 'a,b,c,d', '#foo 123']

[s for s in items if re.search(r'\d', s) and '#' in s]

for s in items:
    if s[0] != '#':
        print(re.sub(r',.+,', ' ', s))

## Negative lookarounds

re.sub(r'foo(?!\d)', 'baz', 'hey food! foo42 foot5 foofoo')

re.sub(r'(?<!_)foo', 'baz', 'foo _foo 42foofoo')

re.sub(r'(?<!_)foo.', 'baz', 'food _fool 42foo_foot')

re.sub(r'(?<![:-])\b\w+\b', 'X', ':cart <apple -rest ;tea')

re.sub(r'(?<!\A)\b(?!\Z)', ' ', 'foo_baz=num1+35*42/num2')

re.sub(r'(?<![pr]).', '*', 'spare')

re.sub(r'.(?<![pr].)', '*', 'spare')

re.sub(r'par(?!.*s)', 'X', 'par spare part party')

re.sub(r'(?!.*s)par', 'X', 'par spare part party')

re.sub(r'(?!\Z)\b(?<!\A)', ' ', 'foo_baz=num1+35*42/num2')

## Positive lookarounds

re.findall(r'\d+(?=,)', '42 foo-5, baz3; x-83, y-20: f12')

re.findall(r'(?<=-)\d+(?=[:;])', '42 foo-5, baz3; x-83, y-20: f12')

re.sub(r'par(?=.*\bpart\b)', 'X', 'par spare part party')

re.findall(r'(?<=,)[^,]+(?=,)', '1,two,3,four,5')

re.sub(r'(?<![^,])(?![^,])', 'NA', ',1,,,two,3,,,')

## Capture groups inside positive lookarounds

print(re.sub(r'(\S+\s+)(?=(\S+)\s)', r'\1\2\n', 'a b c d e'))

re.findall(r'(?<=(po|ca)re)\d+', 'pore42 car3 pare7 care5')

re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5')

## Conditional AND with lookarounds

words = ['sequoia', 'subtle', 'questionable', 'exhibit', 'equation']

[w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)]

[w for w in words if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u', w)]

[w for w in words if re.search(r'(?=.*a)(?=.*q)(?!.*n\Z)', w)]

## Variable length lookbehind

s = 'pore42 tar3 dare7 care5'

re.findall(r'(?<=(?:po|da)re)\d+', s)

re.findall(r'(?<=\b[a-z]{4})\d+', s)

re.findall(r'(?<!tar|dare)\d+', s)

re.findall(r'(?<=\b[pd][a-z]*)\d+', s)

re.sub(r'(?<=\A|,)(?=,|\Z)', 'NA', ',1,,,two,3,,,')

s = 'pore42 tar3 dare7 care5'

re.findall(r'(?<!tar)(?<!dare)\d+', s)

re.findall(r'(?:(?<=tar)|(?<=dare))\d+', s)

re.sub(r'((?<=\A)|(?<=,))(?=,|\Z)', 'NA', ',1,,,two,3,,,')

s = 'pore42 tar3 dare7 care5'

re.findall(r'(?:tar|dare)(\d+)', s)

re.sub(r'(tar|dare)\d+', r'\1', s)

re.findall(r'\b[pd][a-z]*(\d+)', s)

re.sub(r'(\b[pd][a-z]*)\d+', r'\1', s)

## Negated groups

bool(re.search(r'\A((?!cat).)*dog', 'fox,cat,dog,parrot'))

bool(re.search(r'\A((?!parrot).)*dog', 'fox,cat,dog,parrot'))

bool(re.search(r'((?!cat).)*dog', 'fox,cat,dog,parrot'))

re.search(r'\A((?!cat).)*', 'fox,cat,dog,parrot')[0]

re.search(r'\A((?!parrot).)*', 'fox,cat,dog,parrot')[0]

re.search(r'\A((?!(.)\2).)*', 'fox,cat,dog,parrot')[0]

bool(re.search(r'at((?!do).)*par', 'fox,cat,dog,parrot'))

bool(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot'))

re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')[0]

re.findall(r'a(?:(?!\d).)*z', 'at,baz,a2z,bad-zoo')

