bool(re.search(r'cat|dog', 'I like cats'))

bool(re.search(r'cat|dog', 'I like dogs'))

bool(re.search(r'cat|dog', 'I like parrots'))

re.sub(r'\Acat|cat\b', r'X', 'catapults concatenate cat scat')

re.sub(r'cat|dog|fox', r'mammal', 'cat dog bee parrot fox')

'|'.join(['car', 'jeep'])

words = ['cat', 'dog', 'fox']

'|'.join(words)

re.sub('|'.join(words), r'mammal', 'cat dog bee parrot fox')

re.sub(r'reform|rest', r'X', 'red reform read arrest')

re.sub(r're(form|st)', r'X', 'red reform read arrest')

re.sub(r'\bpar\b|\bpart\b', r'X', 'par spare part party')

re.sub(r'\b(par|part)\b', r'X', 'par spare part party')

re.sub(r'\bpar(|t)\b', r'X', 'par spare part party')

words = ['cat', 'par']

'|'.join(words)

re.sub('|'.join(words), r'X', 'cater cat concatenate par spare')

alt = re.compile(r'\b(' + '|'.join(words) + r')\b')

alt.sub(r'X', 'cater cat concatenate par spare')

alt.pattern

alt.pattern == r'\b(cat|par)\b'

words = 'lion elephant are rope not'

re.search(r'on', words)

re.search(r'ant', words)

re.sub(r'on|ant', r'X', words, count=1)

re.sub(r'ant|on', r'X', words, count=1)

mood = 'best years'

re.search(r'year', mood)

re.search(r'years', mood)

re.sub(r'year|years', r'X', mood, count=1)

re.sub(r'years|year', r'X', mood, count=1)

words = 'ear xerox at mare part learn eye'

re.sub(r'ar|are|art', r'X', words)

re.sub(r'are|ar|art', r'X', words)

re.sub(r'are|art|ar', r'X', words)

words = ['hand', 'handy', 'handful']

alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))

alt.pattern

alt.sub(r'X', 'hands handful handed handy')

re.sub('|'.join(words), r'X', 'hands handful handed handy')

