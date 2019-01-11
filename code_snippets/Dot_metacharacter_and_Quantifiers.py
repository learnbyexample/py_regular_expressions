re.sub(r'c.t', r'X', 'tac tin cat abc;tuv acute')

re.sub(r'r..d', r'X', 'breadth markedly reported overrides')

re.sub(r'2.3', r'8', '42\t33')

re.sub(r'e?ar', r'X', 'far feat flare fear')

re.sub(r'\bpart?\b', r'X', 'par spare part party')

words = ['red', 'read', 'ready', 're;d', 'redo', 'reed']

[w for w in words if re.search(r'\bre.?d\b', w)]

re.sub(r'par(ro)?t', r'X', 'par part parrot parent')

re.sub(r'par(en|ro)?t', r'X', 'par part parrot parent')

re.sub(r'ta*r', r'X', 'tr tear tare steer sitaara')

re.sub(r't(e|a)*r', r'X', 'tr tear tare steer sitaara')

re.sub(r'1*2', r'X', '3111111111125111142')

re.split(r'1*2', '3111111111125111142')

re.split(r'1*2', '3111111111125111142', maxsplit=1)

re.split(r'u*', 'cloudy')

re.sub(r'ta+r', r'X', 'tr tear tare steer sitaara')

re.sub(r't(e|a)+r', r'X', 'tr tear tare steer sitaara')

re.sub(r'1+2', r'X', '3111111111125111142')

re.split(r'1+', '3111111111125111142')

re.split(r'u+', 'cloudy')

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']

[w for w in demo if re.search(r'ab{1,4}c', w)]

[w for w in demo if re.search(r'ab{3,}c', w)]

[w for w in demo if re.search(r'ab{,2}c', w)]

[w for w in demo if re.search(r'ab{3}c', w)]

bool(re.search(r'Error.*valid', 'Error: not a valid input'))

bool(re.search(r'Error.*valid', 'Error: key not found'))

seq1 = 'cat and dog'

seq2 = 'dog and cat'

bool(re.search(r'cat.*dog|dog.*cat', seq1))

bool(re.search(r'cat.*dog|dog.*cat', seq2))

patterns = (r'cat', r'dog')

all(re.search(p, seq1) for p in patterns)

all(re.search(p, seq2) for p in patterns)

re.sub(r'f.?o', r'X', 'foot')

print(re.sub(r'\\?<', r'\<', r'blah \< foo < bar \< blah < baz'))

re.sub(r'hand(y|ful)?', r'X', 'hand handy handful')

sentence = 'that is quite a fabricated tale'

re.sub(r't.*a', r'X', sentence, count=1)

re.sub(r't.*a', r'X', 'star', count=1)

re.sub(r't.*a.*q.*f', r'X', sentence, count=1)

re.sub(r't.*a.*u', r'X', sentence, count=1)

re.sub(r'f.??o', r'X', 'foot', count=1)

re.sub(r'f.??o', r'X', 'frost', count=1)

re.sub(r'.{2,5}?', r'X', '123456789', count=1)

sentence = 'that is quite a fabricated tale'

re.sub(r't.*?a', r'X', sentence, count=1)

re.sub(r't.*?a.*?f', r'X', sentence, count=1)

import regex

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']

[w for w in demo if regex.search(r'ab*c', w)]

[w for w in demo if regex.search(r'ab*+c', w)]

regex.sub(r'f(a|e)*at', r'X', 'feat ft feaeat')

regex.sub(r'f(a|e)*+at', r'X', 'feat ft feaeat')

regex.sub(r'(?>(b|o)+)', r'X', 'abbbc foooooot')

regex.sub(r'f(?>(a|e)*)at', r'X', 'feat ft feaeat')

