import regex

regex.DEFAULT_VERSION = regex.VERSION1

sentence = 'This is a sample string'

bool(regex.search(r'is', sentence))

## Possessive quantifiers

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']

[w for w in demo if regex.search(r'ab*c', w)]

[w for w in demo if regex.search(r'ab*+c', w)]

regex.findall(r'\b0*\d{3,}\b', '0501 035 154 12 26 98234')

regex.findall(r'\b0*+\d{3,}\b', '0501 035 154 12 26 98234')

regex.sub(r'(?>[bo]+)', 'X', 'abbbc foooooot')

regex.findall(r'\b(?>0*)\d{3,}\b', '0501 035 154 12 26 98234')

## Subexpression calls

row = 'today,2008-03-24,food,2012-08-12,nice,5632'

re.search(r'\d{4}-\d{2}-\d{2}.*\d{4}-\d{2}-\d{2}', row)[0]

regex.search(r'(\d{4}-\d{2}-\d{2}).*(?1)', row)[0]

row = 'today,2008-03-24,food,2012-08-12,nice,5632'

regex.search(r'(?P<date>\d{4}-\d{2}-\d{2}).*(?&date)', row)[0]

## Positive lookbehind with \K

regex.sub(r'\b\w\K\w*\W*', '', 'sea eat car rat eel tea')

regex.sub(r'(cat.*?){2}\Kcat', 'X', 'cat scatter cater scat', count=1)

row = '421,foo,2425,42,5,foo,6,6,42'

while True:
    row, cnt = regex.subn(r'(?<![^,])([^,]++).*\K,\1(?![^,])', r'', row)
    if cnt == 0:
        break

row

## Variable length lookbehind

s = 'pore42 tar3 dare7 care5'

regex.findall(r'(?<!tar|dare)\d+', s)

regex.findall(r'(?<=\b[pd][a-z]*)\d+', s)

regex.sub(r'(?<=\A|,)(?=,|\Z)', 'NA', ',1,,,two,3,,,')

regex.sub(r'(?<=(cat.*?){2})cat', 'X', 'cat scatter cater scat', count=1)

bool(regex.search(r'(?<!cat.*)dog', 'fox,cat,dog,parrot'))

bool(regex.search(r'(?<!parrot.*)dog', 'fox,cat,dog,parrot'))

bool(regex.search(r'at(?<!go.*)par', 'fox,cat,dog,parrot'))

bool(regex.search(r'at((?!go).)*par', 'fox,cat,dog,parrot'))

## \G anchor

regex.findall(r'\G\S', '123-87-593 42 foo')

regex.sub(r'\G\S', '*', '123-87-593 42 foo')

regex.findall(r'\G\d+-?', '123-87-593 42 foo')

regex.sub(r'\G(\d+)(-?)', r'(\1)\2', '123-87-593 42 foo')

regex.findall(r'\G\w(?=\w)', 'cat12 bat pin')

regex.sub(r'\G\w(?=\w)', r'\g<0>:', 'cat12 bat pin')

regex.sub(r'\G[a-z ]', r'(\g<0>)', 'par tar-den hen-food mood')

## Recursive matching

eqn0 = 'a + (b * c) - (d / e)'

regex.findall(r'\([^()]++\)', eqn0)

eqn1 = '((f+x)^y-42)*((3-g)^z+2)'

regex.findall(r'\([^()]++\)', eqn1)

eqn1 = '((f+x)^y-42)*((3-g)^z+2)'

regex.findall(r'\((?:[^()]++|\([^()]++\))++\)', eqn1)

eqn2 = 'a + (b) + ((c)) + (((d)))'

regex.findall(r'\((?:[^()]++|\([^()]++\))++\)', eqn2)

lvl2 = regex.compile('''
         \(              #literal (
           (?:           #start of non-capturing group
            [^()]++      #non-parentheses characters
            |            #OR
            \([^()]++\)  #level-one RE
           )++           #end of non-capturing group, 1 or more times
         \)              #literal )
         ''', flags=regex.X)

lvl2.findall(eqn1)

lvl2.findall(eqn2)

lvln = regex.compile('''
         \(           #literal (
           (?:        #start of non-capturing group
            [^()]++   #non-parentheses characters
            |         #OR
            (?0)      #recursive call
           )++        #end of non-capturing group, 1 or more times
         \)           #literal )
         ''', flags=regex.X)

lvln.findall(eqn0)

lvln.findall(eqn1)

lvln.findall(eqn2)

eqn3 = '(3+a) * ((r-2)*(t+2)/6) + 42 * (a(b(c(d(e)))))'

lvln.findall(eqn3)

## Named character sets

regex.split(r'[[:digit:]]+', 'Sample123string42with777numbers')

regex.sub(r'[[:alpha:]]+', ':', 'Sample123string42with777numbers')

regex.findall(r'[[:word:][:space:]]+', 'tea sea-pit sit-lean\tbean')

regex.findall(r'[[:^space:]]+', 'tea sea-pit sit-lean\tbean')

regex.findall(r'(?<![[:punct:]])\b\w+\b(?![[:punct:]])', 'tie. ink eat;')

## Set operations

regex.findall(r'\b[^aeiou]+\b', 'tryst glyph pity why')

regex.findall(r'\b[a-z&&[^aeiou]]+\b', 'tryst glyph pity why')

regex.findall(r'\b[[a-l]~~[g-z]]+\b', 'gets eat top sigh')

para = '"Hi", there! How *are* you? All fine here.'

regex.sub(r'[[:punct:]--[.!?]]+', '', para)

## Unicode character sets

regex.findall(r'\p{L}+', 'fox:αλεπού,eagle:αετός')

regex.findall(r'\p{Greek}+', 'fox:αλεπού,eagle:αετός')

regex.findall(r'\p{Word}+', 'φοο12,βτ_4,foo')

regex.sub(r'\P{L}+', '', 'φοο12,βτ_4,foo')

## Skipping matches

words = 'tiger imp goat eagle rat'

regex.sub(r'\b(?:imp|rat)\b(*SKIP)(*F)|[a-z]++', r'(\g<0>)', words)

row = '1,"cat,12",nice,two,"dog,5"'

regex.sub(r'"[^"]++"(*SKIP)(*F)|,', '|', row)

## \m and \M word anchors

regex.sub(r'\b', ':', 'hi log_42 12b')

regex.sub(r'\m', ':', 'hi log_42 12b')

regex.sub(r'\M', ':', 'hi log_42 12b')

regex.sub(r'\b..\b', r'[\g<0>]', 'I have 12, he has 2!')

regex.sub(r'\m..\M', r'[\g<0>]', 'I have 12, he has 2!')

## Overlapped matches

words = 'on vast ever road lane at peak'

regex.findall(r'\b\w+ \w+\b', words)

regex.findall(r'\b\w+ \w+\b', words, overlapped=True)

regex.findall(r'\w{2}', 'apple', overlapped=True)

## regex.REVERSE flag

words = 'par spare lion part cool'

regex.sub(r'par', 'co', words, count=1)

regex.sub(r'par', 'co', words, count=1, flags=regex.R)

regex.findall(r'(?r)\w+', words)

## \X vs dot metacharacter

[c.encode('unicode_escape') for c in 'g̈']

regex.sub(r'a.e', 'o', 'cag̈ed')

regex.sub(r'a..e', 'o', 'cag̈ed')

regex.sub(r'a\Xe', 'o', 'cag̈ed')

regex.sub(r'e.a', 'ea', 'he\nat', flags=regex.S)

regex.sub(r'e\Xa', 'ea', 'he\nat')

