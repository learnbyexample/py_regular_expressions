re.sub(r'foo(?!\d)', r'baz', 'hey food! foo42 foot5 foofoo')

re.sub(r'(?<!_)foo', r'baz', 'foo _foo 42foofoo')

re.sub(r'(?<!_)foo.', r'baz', 'food _fool 42foo_foot')

re.sub(r'(?<![:-])\b\w+\b', r'X', ':cart <apple -rest ;tea')

re.sub(r'(?<!\A)\b(?!\Z)', r' ', 'foo_baz=num1+35*42/num2')

re.findall(r'\d+(?=,)', '42 foo-5, baz3; x-83, y-20: f12')

re.findall(r'(?<=-)\d+(?=[:;])', '42 foo-5, baz3; x-83, y-20: f12')

re.findall(r'(?<=,)[^,]+(?=,)', '1,two,3,four,5')

re.sub(r'(?<![^,])(?![^,])', r'NA', ',1,,,two,3,,,')

print(re.sub(r'(\S+\s+)(?=(\S+)\s)', r'\1\2\n', 'a b c d e'))

re.findall(r'(?<=(po|ca)re)\d+', 'pore42 car3 pare7 care5')

re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5')

words = ['sequoia', 'subtle', 'questionable', 'exhibit', 'equation']

[w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)]

[w for w in words if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u', w)]

re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5')

re.findall(r'(?<=\b[a-z]{4})\d+', 'pore42 car3 pare7 care5')

re.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5')

re.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5')

re.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,')

import regex

regex.sub(r'\b\w\K\w*\W*', r'', 'sea eat car rat eel tea')

regex.sub(r'(cat.*?){2}\Kcat', r'X', 'cat scatter cater scat', count=1)

regex.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5')

regex.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,')

regex.sub(r'(?<=(cat.*?){2})cat', r'X', 'cat scatter cater scat', count=1)

regex.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5')

bool(regex.search(r'(?<!cat.*)dog', 'fox,cat,dog,parrot'))

bool(regex.search(r'(?<!parrot.*)dog', 'fox,cat,dog,parrot'))

bool(re.search(r'\A((?!cat).)*dog', 'fox,cat,dog,parrot'))

bool(re.search(r'\A((?!parrot).)*dog', 'fox,cat,dog,parrot'))

re.search(r'\A((?!cat).)*', 'fox,cat,dog,parrot')[0]

re.search(r'\A((?!parrot).)*', 'fox,cat,dog,parrot')[0]

re.search(r'\A((?!(.)\2).)*', 'fox,cat,dog,parrot')[0]

bool(re.search(r'at((?!do).)*par', 'fox,cat,dog,parrot'))

bool(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot'))

re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')[0]

