## Backreference

re.sub(r'\[(\d+)\]', r'\1', '[52] apples and [31] mangoes')

re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_')

re.sub(r'(\w+),(\w+)', r'\2,\1', 'good,bad 42,24')

re.sub(r'\[(\d+)\]', r'(\15)', '[52] apples and [31] mangoes')

re.sub(r'\[(\d+)\]', r'(\g<1>5)', '[52] apples and [31] mangoes')

re.sub(r'\[(\d+)\]', r'(\1\065)', '[52] apples and [31] mangoes')

re.sub(r'[a-z]+', r'{\g<0>}', '[52] apples and [31] mangoes')

re.sub(r'.+', r'Hi. \g<0>. Have a nice day', 'Hello world')

re.sub(r'\A([^,]+),.+', r'\g<0>,\1', 'fork,42,nice,3.14')

words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']

[w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]

re.sub(r'\b(\w+)( \1)+\b', r'\1', 'aa a a a 42 f_1 f_1 f_13.14')

s = 'abcdefghijklmna1d'

re.sub(r'(.).*\11', 'X', s)

re.sub(r'(.).*\1\x31', 'X', s)

re.sub(r'(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.).*\11', 'X', s)

re.sub(r'(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)(.).*\1\x31', 'X', s)

## Non-capturing groups

re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run against')

re.split(r'hand(?:y|ful)?', '123hand42handy777handful500')

re.sub(r'\A(([^,]+,){3})([^,]+)', r'\1(\3)', '1,2,3,4,5,6,7')

re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7')

s = 'hi 123123123 bye 456123456'

re.findall(r'(123)+', s)

re.findall(r'(?:123)+', s)

re.sub(r'(123)+', 'X', s)

row = 'one,2,3.14,42,five'

re.sub(r'\A([^,]+,){3}([^,]+)', r'\1"\2"', row)

re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1"\2"', row)

words = 'effort flee facade oddball rat tool'

repeat_char = re.compile(r'\b\w*(\w)\1\w*\b')

repeat_char.findall(words)

m_iter = repeat_char.finditer(words)

[m[0] for m in m_iter]

## Named capture groups

re.sub(r'(?P<fw>\w+),(?P<sw>\w+)', r'\g<sw>,\g<fw>', 'good,bad 42,24')

s = 'aa a a a 42 f_1 f_1 f_13.14'

re.sub(r'\b(?P<dup>\w+)( (?P=dup))+\b', r'\g<dup>', s)

sentence = 'I bought an apple'

m = re.search(r'(?P<fruit>\w+)\Z', sentence)

m[1]

m['fruit']

m.group('fruit')

details = '2018-10-25,car,2346'

re.search(r'(?P<date>[^,]+),(?P<product>[^,]+)', details).groupdict()

re.search(r'(?P<date>[^,]+),([^,]+)', details).groupdict()

s = 'good,bad 42,24'

[m.groupdict() for m in re.finditer(r'(?P<fw>\w+),(?P<sw>\w+)', s)]

## Conditional groups

words = ['"hi"', 'bye', 'bad"', '"good"', '42', '"3']

pat = re.compile(r'(")?\w+(?(1)")')

[w for w in words if pat.fullmatch(w)]

[w for w in words if re.fullmatch(r'"\w+"|\w+', w)]

[w for w in words if re.fullmatch(r'"?\w+"?', w)]

[w for w in words if pat.search(w)]

words = ['(hi)', 'good-bye', 'bad', '(42)', '-oh', 'i-j', '(-)']

pat = re.compile(r'(\()?\w+(?(1)\)|-\w+)')

[w for w in words if pat.fullmatch(w)]

## Match.expand

re.sub(r'w(.*)m', r'[\1]', 'awesome')

re.search(r'w(.*)m', 'awesome').expand(r'[\1]')

dates = '2020/04/25,1986/03/02,77/12/31'

m_iter = re.finditer(r'([^/]+)/([^/]+)/[^,]+,?', dates)

[m.expand(r'Month:\2, Year:\1') for m in m_iter]

