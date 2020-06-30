## Escape sequences

bool(re.search(r'\t', 'cat\tdog'))

bool(re.search(r'\c', 'cat\tdog'))

re.sub(r',', r'\x7c', '1,2')

re.sub(r',', r'\174', '1,2')

re.sub(r',', '\x7c', '1,2')

## Line anchors with \n as last character

print(re.sub(r'(?m)^', 'foo ', '1\n2\n'))

print(re.sub(r'(?m)$', ' baz', '1\n2\n'))

## Zero length matches

re.sub(r'[^,]*', r'{\g<0>}', ',cat,tiger')

regex.sub(r'[^,]*+', r'{\g<0>}', ',cat,tiger')

re.sub(r'(?<![^,])[^,]*', r'{\g<0>}', ',cat,tiger')

## Capture group with quantifiers

re.sub(r'\A([^,]+,){3}([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7')

re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7')

re.findall(r'([^,]+,){3}', '1,2,3,4,5,6,7')

re.findall(r'(?:[^,]+,){3}', '1,2,3,4,5,6,7')

## Converting re to regex module

re.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=re.A)

regex.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=re.A)

regex.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=regex.A)

regex.findall(r'(?a)[[:word:]]+', 'fox:αλεπού,eagle:αετός')

## Optional arguments syntax

+re.I

re.findall(r'key', 'KEY portkey oKey Keyed', re.I)

re.sub(r'key', 'X', 'KEY portkey oKey Keyed', re.I)

re.sub(r'key', 'X', 'KEY portkey oKey Keyed', flags=re.I)

