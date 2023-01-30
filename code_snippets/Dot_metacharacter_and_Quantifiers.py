## Dot metacharacter

re.sub(r'c.t', 'X', 'tac tin cat abc;tuv acute')

re.sub(r'r..d', 'X', 'breadth markedly reported overrides')

re.sub(r'2.3', '8', '42\t35')

bool(re.search(r'a.b', 'a\nb'))

re.sub(r'a.e', 'o', 'cag̈ed')

re.sub(r'a..e', 'o', 'cag̈ed')

## re.split()

re.split(r'-', 'apple-85-mango-70')

re.split(r'-', 'apple-85-mango-70', maxsplit=1)

re.split(r':.:', 'bus:3:car:-:van')

## Greedy quantifiers

re.sub(r'e?ar', 'X', 'far feat flare fear')

re.sub(r'\bpart?\b', 'X', 'par spare part party')

words = ['red', 'read', 'ready', 're;d', 'road', 'redo', 'reed', 'rod']

[w for w in words if re.search(r'\bre.?d\b', w)]

re.sub(r'par(ro)?t', 'X', 'par part parrot parent')

re.sub(r'par(en|ro)?t', 'X', 'par part parrot parent')

re.sub(r'ta*r', 'X', 'tr tear tare steer sitaara')

re.sub(r't(e|a)*r', 'X', 'tr tear tare steer sitaara')

re.sub(r'1*2', 'X', '3111111111125111142')

re.split(r'1*2', '3111111111125111142')

re.split(r'1*2', '3111111111125111142', maxsplit=1)

re.split(r'u*', 'cloudy')

re.sub(r'ta+r', 'X', 'tr tear tare steer sitaara')

re.sub(r't(e|a)+r', 'X', 'tr tear tare steer sitaara')

re.sub(r'1+2', 'X', '3111111111125111142')

re.split(r'1+', '3111111111125111142')

re.split(r'u+', 'cloudy')

repeats = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']

[w for w in repeats if re.search(r'ab{1,4}c', w)]

[w for w in repeats if re.search(r'ab{3,}c', w)]

[w for w in repeats if re.search(r'ab{,2}c', w)]

[w for w in repeats if re.search(r'ab{3}c', w)]

re.sub(r'a\{5}', 'a{6}', 'a{5} = 10')

re.sub(r'_{a,b}', '-{c,d}', 'report_{a,b}.txt')

## Conditional AND

bool(re.search(r'Error.*valid', 'Error: not a valid input'))

bool(re.search(r'Error.*valid', 'Error: key not found'))

s1 = 'cat and dog and parrot'

s2 = 'dog and cat and parrot'

pat = re.compile(r'cat.*dog|dog.*cat')

pat.sub('X', s1)

pat.sub('X', s2)

s1 = 'cat and dog and parrot'

s2 = 'dog and cat and parrot'

patterns = (r'cat', r'dog')

all(re.search(p, s1) for p in patterns)

all(re.search(p, s2) for p in patterns)

## What does greedy mean?

re.sub(r'f.?o', 'X', 'foot')

print(re.sub(r'\\?<', r'\<', r'table \< fig < bat \< box < cake'))

re.sub(r'hand(y|ful)?', 'X', 'hand handy handful')

sentence = 'that is quite a fabricated tale'

re.sub(r't.*a', 'X', sentence)

re.sub(r't.*a', 'X', 'star')

re.sub(r't.*a.*q.*f', 'X', sentence)

re.sub(r't.*a.*u', 'X', sentence)

## Non-greedy quantifiers

re.sub(r'f.??o', 'X', 'foot')

re.sub(r'f.??o', 'X', 'frost')

re.sub(r'.{2,5}?', 'X', '123456789', count=1)

re.split(r':.*:', 'green:3.14:teal::brown:oh!:blue')

re.split(r':.*?:', 'green:3.14:teal::brown:oh!:blue')

## Possessive quantifiers

ip = 'fig:mango:pineapple:guava:apples:orange'

re.sub(r':.*+', 'X', ip)

bool(re.search(r':.*+apple', ip))

numbers = '42 314 001 12 00984'

re.findall(r'0*\d{3,}', numbers)

re.findall(r'0*+\d{3,}', numbers)

re.findall(r'0*[1-9]\d{2,}', numbers)

## Catastrophic Backtracking

from timeit import timeit

greedy = re.compile(r'(a+|\w+)*:')

possessive = re.compile(r'(a+|\w+)*+:')

s1 = 'aaaaaaaaaaaaaaaa:123'

s2 = 'aaaaaaaaaaaaaaaa-123'

timeit('greedy.search(s1)', number=10000, globals=globals())

timeit('possessive.search(s1)', number=10000, globals=globals())

timeit('greedy.search(s2)', number=10, globals=globals())

timeit('possessive.search(s2)', number=10, globals=globals())

