## re.search

sentence = 'This is a sample string'

'is' in sentence

'xyz' in sentence

import re

bool(re.search(r'is', sentence))

bool(re.search(r'xyz', sentence))

sentence = 'This is a sample string'

bool(re.search(r'this', sentence))

bool(re.search(r'this', sentence, flags=re.I))

## re.search in conditional expressions

sentence = 'This is a sample string'

if re.search(r'ring', sentence):
    print('mission success')

if not re.search(r'xyz', sentence):
    print('mission failed')

words = ['cat', 'attempt', 'tattle']

[w for w in words if re.search(r'tt', w)]

all(re.search(r'at', w) for w in words)

any(re.search(r'stat', w) for w in words)

## re.sub

greeting = 'Have a nice weekend'

re.sub(r'e', 'E', greeting)

re.sub(r'e', 'E', greeting, count=2)

word = 'cater'

re.sub(r'cat', 'wag', word)

word

word = re.sub(r'cat', 'wag', word)

word

## Compiling regular expressions

pet = re.compile(r'dog')

type(pet)

bool(pet.search('They bought a dog'))

bool(pet.search('A cat crossed their path'))

pet.sub('cat', 'They bought a dog')

sentence = 'This is a sample string'

word = re.compile(r'is')

bool(word.search(sentence, 4))

bool(word.search(sentence, 6))

bool(word.search(sentence, 2, 4))

## bytes

byte_data = b'This is a sample string'

re.search(r'is', byte_data)

bool(re.search(rb'is', byte_data))

bool(re.search(rb'xyz', byte_data))

