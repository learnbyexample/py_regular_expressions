sentence = 'This is a sample string'

'is' in sentence

'xyz' in sentence

import re

bool(re.search(r'is', sentence))

bool(re.search(r'xyz', sentence))

sentence = 'This is a sample string'

if re.search(r'ring', sentence):
    print('mission success')

if not re.search(r'xyz', sentence):
    print('mission failed')

words = ['cat', 'attempt', 'tattle']

[w for w in words if re.search(r'tt', w)]

all(re.search(r'at', w) for w in words)

any(re.search(r'stat', w) for w in words)

pet = re.compile(r'dog')

type(pet)

bool(pet.search('They bought a dog'))

bool(pet.search('A cat crossed their path'))

sentence = 'This is a sample string'

word = re.compile(r'is')

bool(word.search(sentence, 4))

bool(word.search(sentence, 6))

bool(word.search(sentence, 2, 4))

byte_data = b'This is a sample string'

re.search(r'is', byte_data)

bool(re.search(rb'is', byte_data))

bool(re.search(rb'xyz', byte_data))

import regex

sentence = 'This is a sample string'

bool(regex.search(r'is', sentence))

bool(regex.search(r'xyz', sentence))

