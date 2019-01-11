bool(re.search(r'\t', 'cat\tdog'))

bool(re.search(r'\c', 'cat\tdog'))

print(re.sub(r'(?m)^', r'foo ', '1\n2\n'))

print(re.sub(r'(?m)$', r' baz', '1\n2\n'))

re.sub(r'[^,]*', r'{\g<0>}', ',cat,tiger')

regex.sub(r'[^,]*+', r'{\g<0>}', ',cat,tiger')

re.sub(r'(?<![^,])[^,]*', r'{\g<0>}', ',cat,tiger')

re.sub(r'\A([^,]+,){3}([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7', count=1)

re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7', count=1)

re.findall(r'([^,]+,){3}', '1,2,3,4,5,6,7')

re.findall(r'(?:[^,]+,){3}', '1,2,3,4,5,6,7')

re.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=re.A)

regex.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=re.A)

regex.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=regex.A)

