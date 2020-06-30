## Alternation

bool(re.search(r'cat|dog', 'I like cats'))

bool(re.search(r'cat|dog', 'I like dogs'))

bool(re.search(r'cat|dog', 'I like parrots'))

re.sub(r'\Acat|cat\b', 'X', 'catapults concatenate cat scat')

re.sub(r'cat|dog|fox', 'mammal', 'cat dog bee parrot fox')

'|'.join(['car', 'jeep'])

words = ['cat', 'dog', 'fox']

'|'.join(words)

re.sub('|'.join(words), 'mammal', 'cat dog bee parrot fox')

## Grouping

re.sub(r'reform|rest', 'X', 'red reform read arrest')

re.sub(r're(form|st)', 'X', 'red reform read arrest')

re.sub(r'\bpar\b|\bpart\b', 'X', 'par spare part party')

re.sub(r'\b(par|part)\b', 'X', 'par spare part party')

re.sub(r'\bpar(|t)\b', 'X', 'par spare part party')

words = ['cat', 'par']

'|'.join(words)

re.sub('|'.join(words), 'X', 'cater cat concatenate par spare')

alt = re.compile(r'\b(' + '|'.join(words) + r')\b')

alt.sub('X', 'cater cat concatenate par spare')

alt.pattern

alt.pattern == r'\b(cat|par)\b'

terms = ['no', 'ten', 'it']

items = ['dip', 'nobody', 'it', 'oh', 'no', 'bitten']

pat = re.compile('|'.join(terms))

[w for w in items if(pat.fullmatch(w))]

[w for w in items if(pat.search(w))]

## Precedence rules

words = 'lion elephant are rope not'

re.search(r'on', words)

re.search(r'ant', words)

re.sub(r'on|ant', 'X', words, count=1)

re.sub(r'ant|on', 'X', words, count=1)

mood = 'best years'

re.search(r'year', mood)

re.search(r'years', mood)

re.sub(r'year|years', 'X', mood, count=1)

re.sub(r'years|year', 'X', mood, count=1)

words = 'ear xerox at mare part learn eye'

re.sub(r'ar|are|art', 'X', words)

re.sub(r'are|ar|art', 'X', words)

re.sub(r'are|art|ar', 'X', words)

words = ['hand', 'handy', 'handful']

alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))

alt.pattern

alt.sub('X', 'hands handful handed handy')

re.sub('|'.join(words), 'X', 'hands handful handed handy')

