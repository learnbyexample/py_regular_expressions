## Dot metacharacter

re.sub(r'c.t', 'X', 'tac tin cat abc;tuv acute')

re.sub(r'r..d', 'X', 'breadth markedly reported overrides')

re.sub(r'2.3', '8', '42\t35')

bool(re.search(r'a.b', 'a\nb'))

## re.split

re.split(r'-', 'apple-85-mango-70')

re.split(r'-', 'apple-85-mango-70', maxsplit=1)

re.split(r':.:', 'bus:3:car:5:van')

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

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']

[w for w in demo if re.search(r'ab{1,4}c', w)]

[w for w in demo if re.search(r'ab{3,}c', w)]

[w for w in demo if re.search(r'ab{,2}c', w)]

[w for w in demo if re.search(r'ab{3}c', w)]

## Conditional AND

bool(re.search(r'Error.*valid', 'Error: not a valid input'))

bool(re.search(r'Error.*valid', 'Error: key not found'))

seq1 = 'cat and dog'

seq2 = 'dog and cat'

bool(re.search(r'cat.*dog|dog.*cat', seq1))

bool(re.search(r'cat.*dog|dog.*cat', seq2))

patterns = (r'cat', r'dog')

all(re.search(p, seq1) for p in patterns)

all(re.search(p, seq2) for p in patterns)

## What does greedy mean?

re.sub(r'f.?o', 'X', 'foot')

print(re.sub(r'\\?<', r'\<', r'blah \< foo < bar \< blah < baz'))

re.sub(r'hand(y|ful)?', 'X', 'hand handy handful')

sentence = 'that is quite a fabricated tale'

re.sub(r't.*a', 'X', sentence, count=1)

re.sub(r't.*a', 'X', 'star', count=1)

re.sub(r't.*a.*q.*f', 'X', sentence, count=1)

re.sub(r't.*a.*u', 'X', sentence, count=1)

## Non-greedy quantifiers

re.sub(r'f.??o', 'X', 'foot', count=1)

re.sub(r'f.??o', 'X', 'frost', count=1)

re.sub(r'.{2,5}?', 'X', '123456789', count=1)

re.split(r':.*?:', 'green:3.14:teal::brown:oh!:blue')

sentence = 'that is quite a fabricated tale'

re.sub(r't.*?a', 'X', sentence, count=1)

re.sub(r't.*?a.*?f', 'X', sentence, count=1)

