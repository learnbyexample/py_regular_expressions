re.sub(r'\[(\d+)\]', r'\1', '[52] apples and [31] mangoes')

re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_')

re.sub(r'\d+', r'(\g<0>0)', '52 apples and 31 mangoes')

re.sub(r'.*', r'Hi. \g<0>. Have a nice day', 'Hello world', count=1)

re.sub(r'(\w+),(\w+)', r'\2,\1', 'a,b 42,24')

words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']

[w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]

re.sub(r'\b(\w+)( \1)+\b', r'\1', 'a a a walking for for a cause')

re.split(r'\d+', 'Sample123string42with777numbers')

re.split(r'(\d+)', 'Sample123string42with777numbers')

re.split(r'(1*2)', '3111111111125111142', maxsplit=1)

re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run against')

re.split(r'hand(?:y|ful)?', '123hand42handy777handful500')

re.sub(r'\A(([^,]+,){3})([^,]+)', r'\1(\3)', '1,2,3,4,5,6,7', count=1)

re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7', count=1)

words = 'effort flee facade oddball rat tool'

repeat_char = re.compile(r'\b\w*(\w)\1\w*\b')

repeat_char.findall(words)

m_iter = repeat_char.finditer(words)

[m[0] for m in m_iter]

re.sub(r'(?P<fw>\w+),(?P<sw>\w+)', r'\g<sw>,\g<fw>', 'a,b 42,24')

sentence = 'I bought an apple'

m = re.search(r'(?P<fruit>\w+)\Z', sentence)

m[1]

m['fruit']

m.group('fruit')

import re, regex

row = 'today,2008-03-24,food,2012-08-12,nice,5632'

re.search(r'\d{4}-\d{2}-\d{2}.*\d{4}-\d{2}-\d{2}', row)[0]

regex.search(r'(\d{4}-\d{2}-\d{2}).*(?1)', row)[0]

import regex

row = 'today,2008-03-24,food,2012-08-12,nice,5632'

regex.search(r'(?P<date>\d{4}-\d{2}-\d{2}).*(?&date)', row)[0]

