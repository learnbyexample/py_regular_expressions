# Exercise solutions

>![info](../images/info.svg) Try to solve exercises in every chapter using only the features discussed until that chapter. Some of the exercises will be easier to solve with techniques presented in later chapters, but the aim of these exercises is to explore the features presented so far.

<br>

# re introduction

**a)** Check whether the given strings contain `0xB0`. Display a boolean result as shown below.

```ruby
>>> line1 = 'start address: 0xA0, func1 address: 0xC0'
>>> line2 = 'end address: 0xFF, func2 address: 0xB0'

>>> bool(re.search(r'0xB0', line1))
False
>>> bool(re.search(r'0xB0', line2))
True
```

**b)** Replace all occurrences of `5` with `five` for the given string.

```ruby
>>> ip = 'They ate 5 apples and 5 oranges'

>>> re.sub(r'5', 'five', ip)
'They ate five apples and five oranges'
```

**c)** Replace first occurrence of `5` with `five` for the given string.

```ruby
>>> ip = 'They ate 5 apples and 5 oranges'

>>> re.sub(r'5', 'five', ip, count=1)
'They ate five apples and 5 oranges'
```

**d)** For the given list, filter all elements that do *not* contain `e`.

```ruby
>>> items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

>>> [w for w in items if not re.search(r'e', w)]
['goal', 'sit']
```

**e)** Replace all occurrences of `note` irrespective of case with `X`.

```ruby
>>> ip = 'This note should not be NoTeD'

>>> re.sub(r'note', 'X', ip, flags=re.I)
'This X should not be XD'
```

**f)** Check if `at` is present in the given byte input data.

```ruby
>>> ip = b'tiger imp goat'

>>> bool(re.search(rb'at', ip))
True
```

**g)** For the given input string, display all lines not containing `start` irrespective of case.

```ruby
>>> para = '''good start
... Start working on that
... project you always wanted
... stars are shining brightly
... hi there
... start and try to
... finish the book
... bye'''

>>> pat = re.compile(r'start', flags=re.I)
>>> for line in para.split('\n'):
...     if not pat.search(line):
...         print(line)
... 
project you always wanted
stars are shining brightly
hi there
finish the book
bye
```

**h)** For the given list, filter all elements that contains either `a` or `w`.

```ruby
>>> items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

>>> [w for w in items if re.search(r'a', w) or re.search(r'w', w)]
['goal', 'new', 'eat']
```

**i)** For the given list, filter all elements that contains both `e` and `n`.

```ruby
>>> items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

>>> [w for w in items if re.search(r'e', w) and re.search(r'n', w)]
['new', 'dinner']
```

**j)** For the given string, replace `0xA0` with `0x7F` and `0xC0` with `0x1F`.

```ruby
>>> ip = 'start address: 0xA0, func1 address: 0xC0'

>>> re.sub(r'0xC0', '0x1F', re.sub(r'0xA0', '0x7F', ip))
'start address: 0x7F, func1 address: 0x1F'
```

<br>

# Anchors

**a)** Check if the given strings start with `be`.

```ruby
>>> line1 = 'be nice'
>>> line2 = '"best!"'
>>> line3 = 'better?'
>>> line4 = 'oh no\nbear spotted'

>>> pat = re.compile(r'\Abe')

>>> bool(pat.search(line1))
True
>>> bool(pat.search(line2))
False
>>> bool(pat.search(line3))
True
>>> bool(pat.search(line4))
False
```

**b)** For the given input string, change only whole word `red` to `brown`

```ruby
>>> words = 'bred red spread credible'

>>> re.sub(r'\bred\b', 'brown', words)
'bred brown spread credible'
```

**c)** For the given input list, filter all elements that contains `42` surrounded by word characters.

```ruby
>>> words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']

>>> [w for w in words if re.search(r'\B42\B', w)]
['hi42bye', 'nice1423', 'cool_42a']
```

**d)** For the given input list, filter all elements that start with `den` or end with `ly`.

```ruby
>>> items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']

>>> [e for e in items if re.search(r'\Aden', e) or re.search(r'ly\Z', e)]
['lovely', '2 lonely', 'dent']
```

**e)** For the given input string, change whole word `mall` to `1234` only if it is at the start of a line.

```ruby
>>> para = '''\
... ball fall wall tall
... mall call ball pall
... wall mall ball fall
... mallet wallet malls'''

>>> print(re.sub(r'^mall\b', '1234', para, flags=re.M))
ball fall wall tall
1234 call ball pall
wall mall ball fall
mallet wallet malls
```

**f)** For the given list, filter all elements having a line starting with `den` or ending with `ly`.

```ruby
>>> items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']

>>> [e for e in items if re.search(r'^den', e, flags=re.M) or re.search(r'ly$', e, flags=re.M)]
['lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']
```

**g)** For the given input list, filter all whole elements `12\nthree` irrespective of case.

```ruby
>>> items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']
>>> [e for e in items if re.fullmatch(r'12\nthree', e, flags=re.I)]
['12\nThree', '12\nthree']
```

**h)** For the given input list, replace `hand` with `X` for all elements that start with `hand` followed by at least one word character.

```ruby
>>> items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

>>> [re.sub(r'\bhand\B', 'X', w) for w in items]
['Xed', 'hand', 'Xy', 'unhanded', 'Xle', 'hand-2']
```

**i)** For the given input list, filter all elements starting with `h`. Additionally, replace `e` with `X` for these filtered elements.

```ruby
>>> items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

>>> [re.sub(r'e', 'X', w) for w in items if re.search(r'\Ah', w)]
['handXd', 'hand', 'handy', 'handlX', 'hand-2']
```

<br>

# Alternation and Grouping

**a)** For the given input list, filter all elements that start with `den` or end with `ly`

```ruby
>>> items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']

>>> [e for e in items if re.search(r'\Aden|ly\Z', e)]
['lovely', '2 lonely', 'dent']
```

**b)** For the given list, filter all elements having a line starting with `den` or ending with `ly`.

```ruby
>>> items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']

>>> [e for e in items if re.search(r'^den|ly$', e, flags=re.M)]
['lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']
```

**c)** For the given input strings, replace all occurrences of `removed` or `reed` or `received` or `refused` with `X`.

```ruby
>>> s1 = 'creed refuse removed read'
>>> s2 = 'refused reed redo received'

>>> pat = re.compile(r're(mov|ceiv|fus|)ed')

>>> pat.sub('X', s1)
'cX refuse X read'
>>> pat.sub('X', s2)
'X X redo X'
```

**d)** For the given input strings, replace all matches from the list `words` with `A`.

```ruby
>>> s1 = 'plate full of slate'
>>> s2 = "slated for later, don't be late"
>>> words = ['late', 'later', 'slated']

>>> pat = re.compile('|'.join(sorted(words, key=len, reverse=True)))

>>> pat.sub('A', s1)
'pA full of sA'
>>> pat.sub('A', s2)
"A for A, don't be A"
```

**e)** Filter all whole elements from the input list `items` based on elements listed in `words`.

```ruby
>>> items = ['slate', 'later', 'plate', 'late', 'slates', 'slated ']
>>> words = ['late', 'later', 'slated']

>>> pat = re.compile('|'.join(words))

>>> [w for w in items if pat.fullmatch(w)]
['later', 'late']
```

<br>

# Escaping metacharacters

**a)** Transform the given input strings to the expected output using same logic on both strings.

```ruby
>>> str1 = '(9-2)*5+qty/3'
>>> str2 = '(qty+4)/2-(9-2)*5+pq/4'

>>> str1.replace('(9-2)*5', '35')
'35+qty/3'
>>> str2.replace('(9-2)*5', '35')
'(qty+4)/2-35+pq/4'
```

**b)** Replace `(4)\|` with `2` only at the start or end of given input strings.

```ruby
>>> s1 = r'2.3/(4)\|6 foo 5.3-(4)\|'
>>> s2 = r'(4)\|42 - (4)\|3'
>>> s3 = 'two - (4)\\|\n'

>>> pat = re.compile(r'\A\(4\)\\\||\(4\)\\\|\Z')

>>> pat.sub('2', s1)
'2.3/(4)\\|6 foo 5.3-2'
>>> pat.sub('2', s2)
'242 - (4)\\|3'
>>> pat.sub('2', s3)
'two - (4)\\|\n'
```

**c)** Replace any matching element from the list `items` with `X` for given the input strings. Match the elements from `items` literally. Assume no two elements of `items` will result in any matching conflict.

```ruby
>>> items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
>>> pat = re.compile('|'.join(re.escape(e) for e in items))

>>> pat.sub('X', '0a.bcd')
'0Xcd'
>>> pat.sub('X', 'E{n}AMPLE')
'EXAMPLE'
>>> pat.sub('X', r'43+n2 ax\y\ze')
'4X2 aXe'
```

**d)** Replace backspace character `\b` with a single space character for the given input string.

```ruby
>>> ip = '123\b456'
>>> ip
'123\x08456'
>>> print(ip)
12456

>>> re.sub(r'\x08', ' ', ip)
'123 456'
```

**e)** Replace all occurrences of `\e` with `e`.

```ruby
>>> ip = r'th\er\e ar\e common asp\ects among th\e alt\ernations'

>>> re.sub(r'\\e', 'e', ip)
'there are common aspects among the alternations'
```

**f)** Replace any matching item from the list `eqns` with `X` for given the string `ip`. Match the items from `eqns` literally.

```ruby
>>> ip = '3-(a^b)+2*(a^b)-(a/b)+3'
>>> eqns = ['(a^b)', '(a/b)', '(a^b)+2']

>>> eqns_sorted = sorted(eqns, key=len, reverse=True)
>>> pat = re.compile('|'.join(re.escape(s) for s in eqns_sorted))

>>> pat.sub('X', ip)
'3-X*X-X+3'
```

<br>

# Dot metacharacter and Quantifiers

>![info](../images/info.svg) Since `.` metacharacter doesn't match newline character by default, assume that the input strings in the following exercises will not contain newline characters.

**a)** Replace `42//5` or `42/5` with `8` for the given input.

```ruby
>>> ip = 'a+42//5-c pressure*3+42/5-14256'

>>> re.sub(r'42//?5', '8', ip)
'a+8-c pressure*3+8-14256'
```

**b)** For the list `items`, filter all elements starting with `hand` and ending with at most one more character or `le`.

```ruby
>>> items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']

>>> [w for w in items if re.fullmatch(r'hand(.|le)?', w)]
['hand', 'handy', 'hands', 'handle']
```

**c)** Use `re.split` to get the output as shown for the given input strings.

```ruby
>>> eqn1 = 'a+42//5-c'
>>> eqn2 = 'pressure*3+42/5-14256'
>>> eqn3 = 'r*42-5/3+42///5-42/53+a'

>>> pat = re.compile(r'42//?5')

>>> pat.split(eqn1)
['a+', '-c']
>>> pat.split(eqn2)
['pressure*3+', '-14256']
>>> pat.split(eqn3)
['r*42-5/3+42///5-', '3+a']
```

**d)** For the given input strings, remove everything from the first occurrence of `i` till end of the string.

```ruby
>>> s1 = 'remove the special meaning of such constructs'
>>> s2 = 'characters while constructing'

>>> pat = re.compile(r'i.*')

>>> pat.sub('', s1)
'remove the spec'
>>> pat.sub('', s2)
'characters wh'
```

**e)** For the given strings, construct a RE to get output as shown.

```ruby
>>> str1 = 'a+b(addition)'
>>> str2 = 'a/b(division) + c%d(#modulo)'
>>> str3 = 'Hi there(greeting). Nice day(a(b)'

>>> remove_parentheses = re.compile(r'\(.*?\)')

>>> remove_parentheses.sub('', str1)
'a+b'
>>> remove_parentheses.sub('', str2)
'a/b + c%d'
>>> remove_parentheses.sub('', str3)
'Hi there. Nice day'
```

**f)** Correct the given RE to get the expected output.

```ruby
>>> words = 'plink incoming tint winter in caution sentient'
>>> change = re.compile(r'int|in|ion|ing|inco|inter|ink')

# wrong output
>>> change.sub('X', words)
'plXk XcomXg tX wXer X cautX sentient'

# expected output
>>> change = re.compile(r'in(ter|co|t|g|k)?|ion')
>>> change.sub('X', words)
'plX XmX tX wX X cautX sentient'
```

**g)** For the given greedy quantifiers, what would be the equivalent form using `{m,n}` representation?

* `?` is same as `{,1}`
* `*` is same as `{0,}`
* `+` is same as `{1,}`

**h)** `(a*|b*)` is same as `(a|b)*` — True or False?

False. Because `(a*|b*)` will match only sequences like `a`, `aaa`, `bb`, `bbbbbbbb`. But `(a|b)*` can match a mixed sequence like `ababbba` too.

**i)** For the given input strings, remove everything from the first occurrence of `test` (irrespective of case) till end of the string, provided `test` isn't at the end of the string.

```ruby
>>> s1 = 'this is a Test'
>>> s2 = 'always test your RE for corner cases'
>>> s3 = 'a TEST of skill tests?'

>>> pat = re.compile('test.+', flags=re.I)

>>> pat.sub('', s1)
'this is a Test'
>>> pat.sub('', s2)
'always '
>>> pat.sub('', s3)
'a '
```

**j)** For the input list `words`, filter all elements starting with `s` and containing `e` and `t` in any order.

```ruby
>>> words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

>>> [w for w in words if re.search(r'\As.*(e.*t|t.*e)', w)]
['subtle', 'sets', 'site']
```

**k)** For the input list `words`, remove all elements having less than `6` characters.

```ruby
>>> words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

>>> [w for w in words if re.search(r'.{6,}', w)]
['sequoia', 'subtle', 'exhibit']
```

**l)** For the input list `words`, filter all elements starting with `s` or `t` and having a maximum of `6` characters.

```ruby
>>> words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

>>> [w for w in words if re.fullmatch(r'(s|t).{,5}', w)]
['subtle', 'sets', 'tests', 'site']
```

**m)** Can you reason out why this code results in the output shown? The aim was to remove all `<characters>` patterns but not the `<>` ones. The expected result was `'a 1<> b 2<> c'`.

The use of `.+` quantifier after `<` means that `<>` cannot be a possible match to satisfy `<.+?>`. So, after matching `<` (which occurs after `1` and `2` in the given input string) the regular expression engine will look for next occurrence of `>` character to satisfy the given pattern. To solve such cases, you need to use character classes, which is discussed in a later chapter, to specify which particular set of characters should be matched by the `+` quantifier instead of `.` metacharacter.

```ruby
>>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

>>> re.sub(r'<.+?>', '', ip)
'a 1 2'
```

**n)** Use `re.split` to get the output as shown below for given input strings.

```ruby
>>> s1 = 'go there  //   "this // that"'
>>> s2 = 'a//b // c//d e//f // 4//5'
>>> s3 = '42// hi//bye//see // carefully'

>>> pat = re.compile(r' +// +')

>>> pat.split(s1, maxsplit=1)
['go there', '"this // that"']
>>> pat.split(s2, maxsplit=1)
['a//b', 'c//d e//f // 4//5']
>>> pat.split(s3, maxsplit=1)
['42// hi//bye//see', 'carefully']
```

<br>

# Working with matched portions

**a)** For the given strings, extract the matching portion from first `is` to last `t`.

```ruby
>>> str1 = 'This the biggest fruit you have seen?'
>>> str2 = 'Your mission is to read and practice consistently'

>>> pat = re.compile(r'is.*t')

>>> pat.search(str1)[0]
'is the biggest fruit'
>>> pat.search(str2)[0]
'ission is to read and practice consistent'
```

**b)** Find the starting index of first occurrence of `is` or `the` or `was` or `to` for the given input strings.

```ruby
>>> s1 = 'match after the last newline character'
>>> s2 = 'and then you want to test'
>>> s3 = 'this is good bye then'
>>> s4 = 'who was there to see?'

>>> pat = re.compile(r'is|the|was|to')

>>> pat.search(s1).start()
12
>>> pat.search(s2).start()
4
>>> pat.search(s3).start()
2
>>> pat.search(s4).start()
4
```

**c)** Find the starting index of last occurrence of `is` or `the` or `was` or `to` for the given input strings.

```ruby
>>> s1 = 'match after the last newline character'
>>> s2 = 'and then you want to test'
>>> s3 = 'this is good bye then'
>>> s4 = 'who was there to see?'

>>> pat = re.compile(r'.*(is|the|was|to)')

>>> pat.search(s1).start(1)
12
>>> pat.search(s2).start(1)
18
>>> pat.search(s3).start(1)
17
>>> pat.search(s4).start(1)
14
```

**d)** The given input string contains `:` exactly once. Extract all characters after the `:` as output.

```ruby
>>> ip = 'fruits:apple, mango, guava, blueberry'

>>> re.search(r':(.*)', ip)[1]
'apple, mango, guava, blueberry'
```

**e)** The given input strings contains some text followed by `-` followed by a number. Replace that number with its `log` value using `math.log()`.

```ruby
>>> s1 = 'first-3.14'
>>> s2 = 'next-123'

>>> pat = re.compile(r'-(.*)')

>>> import math
>>> pat.sub(lambda m: '-' + str(math.log(float(m[1]))), s1)
'first-1.144222799920162'
>>> pat.sub(lambda m: '-' + str(math.log(float(m[1]))), s2)
'next-4.812184355372417'
```

**f)** Replace all occurrences of `par` with `spar`, `spare` with `extra` and `park` with `garden` for the given input strings.

```ruby
>>> str1 = 'apartment has a park'
>>> str2 = 'do you have a spare cable'
>>> str3 = 'write a parser'

>>> pat = re.compile(r'park?|spare')
>>> d = {'par': 'spar', 'spare': 'extra', 'park': 'garden'}

>>> pat.sub(lambda m: d[m[0]], str1)
'aspartment has a garden'
>>> pat.sub(lambda m: d[m[0]], str2)
'do you have a extra cable'
>>> pat.sub(lambda m: d[m[0]], str3)
'write a sparser'
```

**g)** Extract all words between `(` and `)` from the given input string as a list. Assume that the input will not contain any broken parentheses.

```ruby
>>> ip = 'another (way) to reuse (portion) matched (by) capture groups'

>>> re.findall(r'\((.*?)\)', ip)
['way', 'portion', 'by']
```

**h)** Extract all occurrences of `<` up to next occurrence of `>`, provided there is at least one character in between `<` and `>`.

```ruby
>>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

>>> re.findall(r'<.+?>', ip)
['<apple>', '<> b<bye>', '<> c<cat>']
```

**i)** Use `re.findall` to get the output as shown below for the given input strings. Note the characters used in the input strings carefully.

```ruby
>>> row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
>>> row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

>>> pat = re.compile(r'(.+?),(.+?) ')

>>> pat.findall(row1)
[('-2', '5'), ('4', '+3'), ('+42', '-53'), ('4356246', '-357532354')]
>>> pat.findall(row2)
[('1.32', '-3.14'), ('634', '5.63'), ('63.3e3', '9907809345343.235')]
```

**j)** This is an extension to previous question.

* For `row1`, find the sum of integers of each tuple element. For example, sum of `-2` and `5` is `3`.
* For `row2`, find the sum of floating-point numbers of each tuple element. For example, sum of `1.32` and `-3.14` is `-1.82`.

```ruby
>>> row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
>>> row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

# should be same as previous question
>>> pat = re.compile(r'(.+?),(.+?) ')

>>> [int(m[1]) + int(m[2]) for m in pat.finditer(row1)]
[3, 7, -11, -353176108]

>>> [float(m[1]) + float(m[2]) for m in pat.finditer(row2)]
[-1.82, 639.63, 9907809408643.234]
```

**k)** Use `re.split` to get the output as shown below.

```ruby
>>> ip = '42:no-output;1000:car-truck;SQEX49801'

>>> re.split(r':.+?-(.+?);', ip)
['42', 'output', '1000', 'truck', 'SQEX49801']
```

**l)** For the given list of strings, change the elements into a tuple of original element and number of times `t` occurs in that element.

```ruby
>>> words = ['sequoia', 'attest', 'tattletale', 'asset']

>>> [re.subn(r't', 't', w) for w in words]
[('sequoia', 0), ('attest', 3), ('tattletale', 4), ('asset', 1)]
```

**m)** The given input string has fields separated by `:`. Each field contains four uppercase alphabets followed optionally by two digits. Ignore the last field, which is empty. See [docs.python: Match.groups](https://docs.python.org/3/library/re.html#re.Match.groups) and use `re.finditer` to get the output as shown below. If the optional digits aren't present, show `'NA'` instead of `None`.
```ruby
>>> ip = 'TWXA42:JWPA:NTED01:'

>>> [m.groups(default='NA') for m in re.finditer(r'(.{4})(..)?:', ip)]
[('TWXA', '42'), ('JWPA', 'NA'), ('NTED', '01')]
```

>![info](../images/info.svg) Note that this is different from `re.findall` which will just give empty string instead of `None` when a capture group doesn't participate.

**n)** Convert the comma separated strings to corresponding `dict` objects as shown below.

```ruby
>>> row1 = 'name:rohan,maths:75,phy:89,'
>>> row2 = 'name:rose,maths:88,phy:92,'

>>> pat = re.compile(r'(.+?):(.+?),')

>>> {m[1]:m[2] for m in pat.finditer(row1)}
{'name': 'rohan', 'maths': '75', 'phy': '89'}
>>> {m[1]:m[2] for m in pat.finditer(row2)}
{'name': 'rose', 'maths': '88', 'phy': '92'}
```

<br>

# Character class

**a)** For the list `items`, filter all elements starting with `hand` and ending with `s` or `y` or `le`.

```ruby
>>> items = ['-handy', 'hand', 'handy', 'unhand', 'hands', 'handle']

>>> [w for w in items if re.fullmatch(r'hand([sy]|le)', w)]
['handy', 'hands', 'handle']
```

**b)** Replace all whole words `reed` or `read` or `red` with `X`.

```ruby
>>> ip = 'redo red credible :read: rod reed'

>>> re.sub(r'\bre[ae]?d\b', 'X', ip)
'redo X credible :X: rod X'
```

**c)** For the list `words`, filter all elements containing `e` or `i` followed by `l` or `n`. Note that the order mentioned should be followed.

```ruby
>>> words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

>>> [w for w in words if re.search(r'[ei].*[ln]', w)]
['surrender', 'unicorn', 'eel']
```

**d)** For the list `words`, filter all elements containing `e` or `i` and `l` or `n` in any order.

```ruby
>>> words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

>>> [w for w in words if re.search(r'[ei].*[ln]|[ln].*[ei]', w)]
['surrender', 'unicorn', 'newer', 'eel']
```

**e)** Extract all hex character sequences, with `0x` optional prefix. Match the characters case insensitively, and the sequences shouldn't be surrounded by other word characters.

```ruby
>>> str1 = '128A foo 0xfe32 34 0xbar'
>>> str2 = '0XDEADBEEF place 0x0ff1ce bad'

>>> hex_seq = re.compile(r'\b(0x)?[\da-f]+\b', flags=re.I)

>>> [m[0] for m in hex_seq.finditer(str1)]
['128A', '0xfe32', '34']

>>> [m[0] for m in hex_seq.finditer(str2)]
['0XDEADBEEF', '0x0ff1ce', 'bad']
```

**f)** Delete from `(` to the next occurrence of `)` unless they contain parentheses characters in between.

```ruby
>>> str1 = 'def factorial()'
>>> str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
>>> str3 = 'Hi there(greeting). Nice day(a(b)'

>>> remove_parentheses = re.compile(r'\([^()]*\)')

>>> remove_parentheses.sub('', str1)
'def factorial'
>>> remove_parentheses.sub('', str2)
'a/b + c%d - (e+*4)'
>>> remove_parentheses.sub('', str3)
'Hi there. Nice day(a'
```

**g)** For the list `words`, filter all elements not starting with `e` or `p` or `u`.

```ruby
>>> words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

>>> [w for w in words if re.search(r'\A[^epu]', w)]
['surrender', 'newer', 'door']
```

**h)** For the list `words`, filter all elements not containing `u` or `w` or `ee` or `-`.

```ruby
>>> words = ['p-t', 'you', 'tea', 'heel', 'owe', 'new', 'reed', 'ear']

>>> [w for w in words if not re.search(r'[uw-]|ee', w)]
['tea', 'ear']
```

**i)** The given input strings contain fields separated by `,` and fields can be empty too. Replace last three fields with `WHTSZ323`.

```ruby
>>> row1 = '(2),kite,12,,D,C,,'
>>> row2 = 'hi,bye,sun,moon'

>>> pat = re.compile(r'(,[^,]*){3}\Z')

>>> pat.sub(',WHTSZ323', row1)
'(2),kite,12,,D,WHTSZ323'
>>> pat.sub(',WHTSZ323', row2)
'hi,WHTSZ323'
```

**j)** Split the given strings based on consecutive sequence of digit or whitespace characters.

```ruby
>>> str1 = 'lion \t Ink32onion Nice'
>>> str2 = '**1\f2\n3star\t7 77\r**'

>>> pat = re.compile(r'[\d\s]+')

>>> pat.split(str1)
['lion', 'Ink', 'onion', 'Nice']
>>> pat.split(str2)
['**', 'star', '**']
```

**k)** Delete all occurrences of the sequence `<characters>` where `characters` is one or more non `>` characters and cannot be empty.

```ruby
>>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

>>> re.sub(r'<[^>]+>', '', ip)
'a 1<> b 2<> c'
```

**l)** `\b[a-z](on|no)[a-z]\b` is same as `\b[a-z][on]{2}[a-z]\b`. True or False? Sample input lines shown below might help to understand the differences, if any.

False. `[on]{2}` will also match `oo` and `nn`.

```ruby
>>> print('known\nmood\nknow\npony\ninns')
known
mood
know
pony
inns
```

**m)** For the given list, filter all elements containing any number sequence greater than `624`.

```ruby
>>> items = ['hi0000432abcd', 'car00625', '42_624 0512', '3.14 96 2 foo1234baz']

>>> [e for e in items if any(int(m[0])>624 for m in re.finditer(r'\d+', e))]
['car00625', '3.14 96 2 foo1234baz']
```

**n)** Count the maximum depth of nested braces for the given strings. Unbalanced or wrongly ordered braces should return `-1`. Note that this will require a mix of regular expressions and Python code.

```ruby
>>> def max_nested_braces(ip):
...     count = 0
...     while True:
...         ip, no_of_subs = re.subn(r'\{[^{}]*\}', '', ip)
...         if no_of_subs == 0:
...             break
...         count += 1
...     if re.search(r'[{}]', ip):
...         return -1
...     return count
... 

>>> max_nested_braces('a*b')
0
>>> max_nested_braces('}a+b{')
-1
>>> max_nested_braces('a*b+{}')
1
>>> max_nested_braces('{{a+2}*{b+c}+e}')
2
>>> max_nested_braces('{{a+2}*{b+{c*d}}+e}')
3
>>> max_nested_braces('{{a+2}*{\n{b+{c*d}}+e*d}}')
4
>>> max_nested_braces('a*{b+c*{e*3.14}}}')
-1
```

**o)** By default, `str.split` method will split on whitespace and remove empty strings from the result. Which `re` module function would you use to replicate this functionality?

```ruby
>>> ip = ' \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f  '

>>> ip.split()
['so', 'pole', 'lit', 'in', 'to']
>>> re.findall(r'\S+', ip)
['so', 'pole', 'lit', 'in', 'to']
```

**p)** Convert the given input string to two different lists as shown below.

```ruby
>>> ip = 'price_42 roast^\t\n^-ice==cat\neast'

>>> re.split(r'\W+', ip)
['price_42', 'roast', 'ice', 'cat', 'east']

>>> re.split(r'(\W+)', ip)
['price_42', ' ', 'roast', '^\t\n^-', 'ice', '==', 'cat', '\n', 'east']
```

**q)** Filter all elements whose first non-whitespace character is not a `#` character. Any element made up of only whitespace characters should be ignored as well.

```ruby
>>> items = ['    #comment', '\t\napple #42', '#oops', 'sure', 'no#1', '\t\r\f']

>>> [e for e in items if re.search(r'\A\s*[^#\s]', e)]
['\t\napple #42', 'sure', 'no#1']
```

<br>

# Groupings and backreferences

**a)** Replace the space character that occurs after a word ending with `a` or `r` with a newline character.

```ruby
>>> ip = 'area not a _a2_ roar took 22'

>>> print(re.sub(r'([ar]) ', r'\1\n', ip))
area
not a
_a2_ roar
took 22
```

**b)** Add `[]` around words starting with `s` and containing `e` and `t` in any order.

```ruby
>>> ip = 'sequoia subtle exhibit asset sets tests site'

>>> re.sub(r'\bs\w*(t\w*e|e\w*t)\w*', r'[\g<0>]', ip)
'sequoia [subtle] exhibit asset [sets] tests [site]'
```

**c)** Replace all whole words with `X` that start and end with the same word character. Single character word should get replaced with `X` too, as it satisfies the stated condition.

```ruby
>>> ip = 'oreo not a _a2_ roar took 22'

>>> re.sub(r'\b(\w|(\w)\w*\2)\b', 'X', ip)
'X not X X X took X'
```

**d)** Convert the given **markdown** headers to corresponding **anchor** tag. Consider the input to start with one or more `#` characters followed by space and word characters. The `name` attribute is constructed by converting the header to lowercase and replacing spaces with hyphens. Can you do it without using a capture group?

```ruby
>>> header1 = '# Regular Expressions'
>>> header2 = '## Compiling regular expressions'

>>> anchor = re.compile(r'\w.*')
>>> def hyphenify(m):
...     return f'<a name="{m[0].lower().replace(" ", "-")}"></a>{m[0]}'
... 
>>> anchor.sub(hyphenify, header1)
'# <a name="regular-expressions"></a>Regular Expressions'
>>> anchor.sub(hyphenify, header2)
'## <a name="compiling-regular-expressions"></a>Compiling regular expressions'
```

**e)** Convert the given **markdown** anchors to corresponding **hyperlinks**.

```ruby
>>> anchor1 = '# <a name="regular-expressions"></a>Regular Expressions'
>>> anchor2 = '## <a name="subexpression-calls"></a>Subexpression calls'

>>> hyperlink = re.compile(r'[^"]+"([^"]+)"></a>(.+)')

>>> hyperlink.sub(r'[\2](#\1)', anchor1)
'[Regular Expressions](#regular-expressions)'
>>> hyperlink.sub(r'[\2](#\1)', anchor2)
'[Subexpression calls](#subexpression-calls)'
```

**f)** Count the number of whole words that have at least two occurrences of consecutive repeated alphabets. For example, words like `stillness` and `Committee` should be counted but not words like `root` or `readable` or `rotational`.

```ruby
>>> ip = '''oppressed abandon accommodation bloodless
... carelessness committed apparition innkeeper
... occasionally afforded embarrassment foolishness
... depended successfully succeeded
... possession cleanliness suppress'''

>>> len(re.findall(r'\b(\w*(\w)\2){2}\w*\b', ip))
13
```

**g)** For the given input string, replace all occurrences of digit sequences with only the unique non-repeating sequence. For example, `232323` should be changed to `23` and `897897` should be changed to `897`. If there no repeats (for example `1234`) or if the repeats end prematurely (for example `12121`), it should not be changed.

```ruby
>>> ip = '1234 2323 453545354535 9339 11 60260260'

>>> re.sub(r'\b(\d+)\1+\b', r'\1', ip)
'1234 23 4535 9339 1 60260260'
```

**h)** Replace sequences made up of words separated by `:` or `.` by the first word of the sequence. Such sequences will end when `:` or `.` is not followed by a word character.

```ruby
>>> ip = 'wow:Good:2_two:five: hi-2 bye kite.777.water.'

>>> re.sub(r'(\w+)[:.](\w+[:.])+', r'\1', ip)
'wow hi-2 bye kite'
```

**i)** Replace sequences made up of words separated by `:` or `.` by the last word of the sequence. Such sequences will end when `:` or `.` is not followed by a word character.

```ruby
>>> ip = 'wow:Good:2_two:five: hi-2 bye kite.777.water.'

>>> re.sub(r'((\w+)[:.])+', r'\2', ip)
'five hi-2 bye water'
```

**j)** Split the given input string on one or more repeated sequence of `cat`.

```ruby
>>> ip = 'firecatlioncatcatcatbearcatcatparrot'

>>> re.split(r'(?:cat)+', ip)
['fire', 'lion', 'bear', 'parrot']
```

**k)** For the given input string, find all occurrences of digit sequences with at least one repeating sequence. For example, `232323` and `897897`. If the repeats end prematurely, for example `12121`, it should not be matched.

```ruby
>>> ip = '1234 2323 453545354535 9339 11 60260260'

>>> pat = re.compile(r'\b(\d+)\1+\b')

# entire sequences in the output
>>> [m[0] for m in pat.finditer(ip)]
['2323', '453545354535', '11']

# only the unique sequence in the output
>>> pat.findall(ip)
['23', '4535', '1']
```

**l)** Convert the comma separated strings to corresponding `dict` objects as shown below. The keys are `name`, `maths` and `phy` for the three fields in the input strings.

```ruby
>>> row1 = 'rohan,75,89'
>>> row2 = 'rose,88,92'

>>> pat = re.compile(r'(?P<name>[^,]+),(?P<maths>[^,]+),(?P<phy>[^,]+)')

>>> pat.search(row1).groupdict()
{'name': 'rohan', 'maths': '75', 'phy': '89'}
>>> pat.search(row2).groupdict()
{'name': 'rose', 'maths': '88', 'phy': '92'}
```

**m)** Surround all whole words with `()`. Additionally, if the whole word is `imp` or `ant`, delete them. Can you do it with single substitution?

```ruby
>>> ip = 'tiger imp goat eagle ant important'

>>> re.sub(r'\b(?:imp|ant|(\w+))\b', r'(\1)', ip)
'(tiger) () (goat) (eagle) () (important)'
```

**n)** Filter all elements that contains a sequence of lowercase alphabets followed by `-` followed by digits. They can be optionally surrounded by `{{` and `}}`. Any partial match shouldn't be part of the output.

```ruby
>>> ip = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']

>>> [w for w in ip if re.fullmatch(r'({{)?[a-z]+-\d+(?(1)}})', w)]
['{{apple-150}}', 'grape-87']
```

**o)** The given input string has sequences made up of words separated by `:` or `.` and such sequences will end when `:` or `.` is not followed by a word character. For all such sequences, display only the last word followed by `-` followed by first word.

```ruby
>>> ip = 'wow:Good:2_two:five: hi-2 bye kite.777.water.'

>>> [m.expand(r'\2-\1') for m in re.finditer(r'(\w+)[:.](?:(\w+)[:.])+', ip)]
['five-wow', 'water-kite']
```

<br>

# Lookarounds

>![info](../images/info.svg) Please use lookarounds for solving the following exercises even if you can do it without lookarounds. Unless you cannot use lookarounds for cases like variable length lookbehinds.

**a)** Replace all whole words with `X` unless it is preceded by `(` character.

```ruby
>>> ip = '(apple) guava berry) apple (mango) (grape'

>>> re.sub(r'(?<!\()\b\w+', 'X', ip)
'(apple) X X) X (mango) (grape'
```

**b)** Replace all whole words with `X` unless it is followed by `)` character.

```ruby
>>> ip = '(apple) guava berry) apple (mango) (grape'

>>> re.sub(r'\b\w+\b(?!\))', 'X', ip)
'(apple) X berry) X (mango) (X'
```

**c)** Replace all whole words with `X` unless it is preceded by `(` or followed by `)` characters.

```ruby
>>> ip = '(apple) guava berry) apple (mango) (grape'

>>> re.sub(r'(?<!\()\b\w+\b(?!\))', 'X', ip)
'(apple) X berry) X (mango) (grape'
```

**d)** Extract all whole words that do not end with `e` or `n`.

```ruby
>>> ip = 'at row on urn e note dust n'

>>> re.findall(r'\b\w+\b(?<![en])', ip)
['at', 'row', 'dust']
```

**e)** Extract all whole words that do not start with `a` or `d` or `n`.

```ruby
>>> ip = 'at row on urn e note dust n'

>>> re.findall(r'(?![adn])\b\w+\b', ip)
['row', 'on', 'urn', 'e']
```

**f)** Extract all whole words only if they are followed by `:` or `,` or `-`.

```ruby
>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

>>> re.findall(r'\w+(?=[:,-])', ip)
['poke', 'so', 'ever']
```

**g)** Extract all whole words only if they are preceded by `=` or `/` or `-`.

```ruby
>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

>>> re.findall(r'(?<=[=/-])\w+', ip)
['so', 'is', 'sit']
```

**h)** Extract all whole words only if they are preceded by `=` or `:` and followed by `:` or `.`.

```ruby
>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

>>> re.findall(r'(?<=[=:])\w+(?=[:.])', ip)
['so', 'ink']
```

**i)** Extract all whole words only if they are preceded by `=` or `:` or `.` or `(` or `-` and not followed by `.` or `/`.

```ruby
>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

>>> re.findall(r'(?<=[=:.(-])\w+\b(?![/.])', ip)
['so', 'vast', 'sit']
```

**j)** Remove leading and trailing whitespaces from all the individual fields where `,` is the field separator.

```ruby
>>> csv1 = ' comma  ,separated ,values \t\r '
>>> csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'

>>> remove_whitespace = re.compile(r'(?<![^,])\s+|\s+(?![^,])')

>>> remove_whitespace.sub('', csv1)
'comma,separated,values'
>>> remove_whitespace.sub('', csv2)
'good bad,nice  ice,42,,stall   small'
```

**k)** Filter all elements that satisfy all of these rules:

* should have at least two alphabets
* should have at least 3 digits
* should have at least one special character among `%` or `*` or `#` or `$`
* should not end with a whitespace character

```ruby
>>> pwds = ['hunter2', 'F2H3u%9', '*X3Yz3.14\t', 'r2_d2_42', 'A $B C1234']

>>> rule_chk = re.compile(r'(?=(.*[a-zA-Z]){2})(?=(.*\d){3})(?!.*\s\Z).*[%*#$]')

>>> [p for p in pwds if rule_chk.search(p)]
['F2H3u%9', 'A $B C1234']
```

**l)** For the given string, surround all whole words with `{}` except for whole words `par` and `cat` and `apple`.

```ruby
>>> ip = 'part; cat {super} rest_42 par scatter apple spar'

>>> re.sub(r'\b(?!(?:par|cat|apple)\b)\w+\b', r'{\g<0>}', ip)
'{part}; cat {{super}} {rest_42} par {scatter} apple {spar}'
```

**m)** Extract integer portion of floating-point numbers for the given string. A number ending with `.` and no further digits should not be considered.

```ruby
>>> ip = '12 ab32.4 go 5 2. 46.42 5'

>>> re.findall(r'\d+(?=\.\d+)', ip)
['32', '46']
```

**n)** For the given input strings, extract all overlapping two character sequences.

```ruby
>>> s1 = 'apple'
>>> s2 = '1.2-3:4'

>>> pat = re.compile(r'.(?=(.))')

>>> [m[0]+m[1] for m in pat.finditer(s1)]
['ap', 'pp', 'pl', 'le']
>>> [m[0]+m[1] for m in pat.finditer(s2)]
['1.', '.2', '2-', '-3', '3:', ':4']
```

**o)** The given input strings contain fields separated by `:` character. Delete `:` and the last field if there is a digit character anywhere before the last field.

```ruby
>>> s1 = '42:cat'
>>> s2 = 'twelve:a2b'
>>> s3 = 'we:be:he:0:a:b:bother'

>>> pat = re.compile(r'(.*\d.*):.*')

>>> pat.sub(r'\1', s1)
'42'
>>> pat.sub(r'\1', s2)
'twelve:a2b'
>>> pat.sub(r'\1', s3)
'we:be:he:0:a:b'
```

**p)** Extract all whole words unless they are preceded by `:` or `<=>` or `----` or `#`.

```ruby
>>> ip = '::very--at<=>row|in.a_b#b2c=>lion----east'

>>> re.findall(r'(?<![:#])(?<!<=>)(?<!-{4})\b\w+', ip)
['at', 'in', 'a_b', 'lion']
```

**q)** Match strings if it contains `qty` followed by `price` but not if there is **whitespace** or the string `error` between them.

```ruby
>>> str1 = '23,qty,price,42'
>>> str2 = 'qty price,oh'
>>> str3 = '3.14,qty,6,errors,9,price,3'
>>> str4 = '42\nqty-6,apple-56,price-234,error'
>>> str5 = '4,price,3.14,qty,4'

>>> neg = re.compile(r'qty((?!\s|error).)*price')

>>> bool(neg.search(str1))
True
>>> bool(neg.search(str2))
False
>>> bool(neg.search(str3))
False
>>> bool(neg.search(str4))
True
>>> bool(neg.search(str5))
False
```

**r)** Can you reason out why the output shown is different for these two regular expressions?

`\b` matches both the start and end of word locations. In the below example, `\b..\b` doesn't necessarily mean that first `\b` will match only the start of word location and second `\b` will match only the end of word location. They can be any combination! For example, `I` followed by space in the input string here is using start of word location for both whereas space followed by `2` is using end of word location for both.

In contrast, the negative lookarounds only ensure that there are no word characters around any two characters. And these assertions will always be satisfied at the start of string and the end of string respectively. But `\b` depends on the presence of word characters. So, `!` at the end of the input string here matches the lookaround assertion but not word boundary.

```ruby
>>> ip = 'I have 12, he has 2!'

>>> re.sub(r'\b..\b', '{\g<0>}', ip)
'{I }have {12}{, }{he} has{ 2}!'

>>> re.sub(r'(?<!\w)..(?!\w)', '{\g<0>}', ip)
'I have {12}, {he} has {2!}'
```

<br>

# Flags

**a)** Remove from first occurrence of `hat` to last occurrence of `it` for the given input strings. Match these markers case insensitively.

```ruby
>>> s1 = 'But Cool THAT\nsee What okay\nwow quite'
>>> s2 = 'it this hat is sliced HIT.'

>>> pat = re.compile(r'hat.*it', flags=re.S|re.I)

>>> pat.sub('', s1)
'But Cool Te'
>>> pat.sub('', s2)
'it this .'
```

**b)** Delete from `start` if it is at the beginning of a line up to the next occurrence of the `end` at the end of a line. Match these markers case insensitively.

```ruby
>>> para = '''\
... good start
... start working on that
... project you always wanted
... to, do not let it end
... hi there
... start and end the end
... 42
... Start and try to
... finish the End
... bye'''

>>> pat = re.compile(r'(?ims)^start.*?end$')

>>> print(pat.sub('', para))
good start

hi there

42

bye
```

**c)** For the given input strings, match all of these three patterns:

* `This` case sensitively
* `nice` and `cool` case insensitively

```ruby
>>> s1 = 'This is nice and Cool'
>>> s2 = 'Nice and cool this is'
>>> s3 = 'What is so nice and cool about This?'

>>> pat = re.compile(r'(?i)(?=.*nice)(?=.*cool)(?-i:.*This)')

>>> bool(pat.search(s1))
True
>>> bool(pat.search(s2))
False
>>> bool(pat.search(s3))
True
```

**d)** For the given input strings, match if the string begins with `Th` and also contains a line that starts with `There`.

```ruby
>>> s1 = 'There there\nHave a cookie'
>>> s2 = 'This is a mess\nYeah?\nThereeeee'
>>> s3 = 'Oh\nThere goes the fun'

>>> pat = re.compile(r'\A(?=Th)(?ms:.*^There)')

>>> bool(pat.search(s1))
True
>>> bool(pat.search(s2))
True
>>> bool(pat.search(s3))
False
```

**e)** Explore what the `re.DEBUG` flag does. Here's some example patterns to check out.

* `re.compile(r'\Aden|ly\Z', flags=re.DEBUG)`
* `re.compile(r'\b(0x)?[\da-f]+\b', flags=re.DEBUG)`
* `re.compile(r'\b(?:0x)?[\da-f]+\b', flags=re.I|re.DEBUG)`

<br>

# Unicode

**a)** Output `True` or `False` depending on input string made up of ASCII characters or not. Consider the input to be non-empty strings and any character that isn't part of 7-bit ASCII set should give `False`. Do you need regular expressions for this?

```ruby
>>> str1 = '123—456'
>>> str2 = 'good fοοd'
>>> str3 = 'happy learning!'
>>> str4 = 'İıſK'

>>> str1.isascii()
False
>>> str2.isascii()
False
>>> str3.isascii()
True
>>> str4.isascii()
False
```

**b)** Does `.` quantifier with `re.ASCII` flag enabled match non-ASCII characters?

Yes.

```ruby
>>> re.search(r'.+', 'fox:αλεπού')[0]
'fox:αλεπού'

>>> re.search(r'(?a).+', 'fox:αλεπού')[0]
'fox:αλεπού'
```

**c)** Explore the following Q&A threads.

* [stackoverflow: remove powered number from string](https://stackoverflow.com/questions/57553721/remove-powered-number-from-string-in-python)
* [stackoverflow: regular expression for French characters](https://stackoverflow.com/questions/1922097/regular-expression-for-french-characters)

<br>

# regex module

**a)** Filter all elements whose first non-whitespace character is not a `#` character. Any element made up of only whitespace characters should be ignored as well.

```ruby
>>> items = ['    #comment', '\t\napple #42', '#oops', 'sure', 'no#1', '\t\r\f']

>>> [e for e in items if regex.search(r'\A\s*+[^#]', e)]
['\t\napple #42', 'sure', 'no#1']
```

**b)** Replace sequences made up of words separated by `:` or `.` by the first word of the sequence and the separator. Such sequences will end when `:` or `.` is not followed by a word character.

```ruby
>>> ip = 'wow:Good:2_two:five: hi bye kite.777.water.'

>>> regex.sub(r'(\w+[:.])(?1)+', r'\1', ip)
'wow: hi bye kite.'
```

**c)** The given list of strings has fields separated by `:` character. Delete `:` and the last field if there is a digit character anywhere before the last field.

```ruby
>>> items = ['42:cat', 'twelve:a2b', 'we:be:he:0:a:b:bother']

>>> [regex.sub(r'\d.*\K:.*', '', e) for e in items]
['42', 'twelve:a2b', 'we:be:he:0:a:b']
```

**d)** Extract all whole words unless they are preceded by `:` or `<=>` or `----` or `#`.

```ruby
>>> ip = '::very--at<=>row|in.a_b#b2c=>lion----east'

>>> regex.findall(r'(?<![:#]|<=>|-{4})\b\w+', ip)
['at', 'in', 'a_b', 'lion']
```

**e)** The given input string has fields separated by `:` character. Extract all fields if the previous field contains a digit character.

```ruby
>>> ip = 'vast:a2b2:ride:in:awe:b2b:3list:end'

>>> regex.findall(r'(?<=\d[^:]*:)[^:]+', ip)
['ride', '3list', 'end']
```

**f)** The given input string has fields separated by `:` character. Delete all fields, including the separator, unless the field contains a digit character. Stop deleting once a field with digit character is found.

```ruby
>>> row1 = 'vast:a2b2:ride:in:awe:b2b:3list:end'
>>> row2 = 'um:no:low:3e:s4w:seer'

>>> pat = regex.compile(r'\G[^\d:]+:')

>>> pat.sub('', row1)
'a2b2:ride:in:awe:b2b:3list:end'
>>> pat.sub('', row2)
'3e:s4w:seer'
```

**g)** For the given input strings, extract `if` followed by any number of nested parentheses. Assume that there will be only one such pattern per input string.

```ruby
>>> ip1 = 'for (((i*3)+2)/6) if(3-(k*3+4)/12-(r+2/3)) while()'
>>> ip2 = 'if+while if(a(b)c(d(e(f)1)2)3) for(i=1)'

>>> pat = regex.compile(r'if(\((?:[^()]++|(?1))++\))')

>>> pat.search(ip1)[0]
'if(3-(k*3+4)/12-(r+2/3))'
>>> pat.search(ip2)[0]
'if(a(b)c(d(e(f)1)2)3)'
```

**h)** Read about `POSIX` flag from https://pypi.org/project/regex/. Is the following code snippet showing the correct output?

Yes. Leftmost longest match wins in `POSIX` implementations, so alternation order doesn't matter.

```ruby
>>> words = 'plink incoming tint winter in caution sentient'

>>> change = regex.compile(r'int|in|ion|ing|inco|inter|ink', flags=regex.POSIX)

>>> change.sub('X', words)
'plX XmX tX wX X cautX sentient'
```

Unless two or more patterns match the same portion with the same length. In such cases, left-to-right priority is applied for the alternations. For example:

```ruby
>>> ip = 'tryst,fun,glyph,pity,why,group'

>>> regex.sub(r'\b\w+\b|(\b[gp]\w*y\w*\b)', r'\1', ip)
',,,,,'
>>> regex.sub(r'(\b[gp]\w*y\w*\b)|\b\w+\b', r'\1', ip)
',,glyph,pity,,'
```

**i)** Extract all whole words for the given input strings. However, based on user input `ignore`, do not match words if they contain any character present in the `ignore` variable.

```ruby
>>> s1 = 'match after the last newline character'
>>> s2 = 'and then you want to test'

>>> ignore = 'aty'
>>> regex.findall(r'\b[\w--[' + ignore + r']]+\b', s1)
['newline']
>>> regex.findall(r'\b[\w--[' + ignore + r']]+\b', s2)
[]

>>> ignore = 'esw'
>>> regex.findall(r'\b[\w--[' + ignore + r']]+\b', s1)
['match']
>>> regex.findall(r'\b[\w--[' + ignore + r']]+\b', s2)
['and', 'you', 'to']
```

**j)** Retain only punctuation characters for the given strings (generated from codepoints). Use Unicode character set definition for punctuation for solving this exercise.

```ruby
>>> s1 = ''.join(chr(c) for c in range(0, 0x80))
>>> s2 = ''.join(chr(c) for c in range(0x80, 0x100))
>>> s3 = ''.join(chr(c) for c in range(0x2600, 0x27ec))

>>> pat = regex.compile(r'\P{P}+')

>>> pat.sub('', s1)
'!"#%&\'()*,-./:;?@[\\]_{}'
>>> pat.sub('', s2)
'¡§«¶·»¿'
>>> pat.sub('', s3)
'❨❩❪❫❬❭❮❯❰❱❲❳❴❵⟅⟆⟦⟧⟨⟩⟪⟫'
```

**k)** For the given **markdown** file, replace all occurrences of the string `python` (irrespective of case) with the string `Python`. However, any match within code blocks that start with whole line ` ```python ` and end with whole line ` ``` ` shouldn't be replaced. Consider the input file to be small enough to fit memory requirements.

Refer to [github: exercises folder](https://github.com/learnbyexample/py_regular_expressions/tree/master/exercises) for files `sample.md` and `expected.md` required to solve this exercise.

```ruby
>>> ip_str = open('sample.md', 'r').read()
>>> pat = regex.compile(r'(?ms)^```python$.*?^```$(*SKIP)(*F)|(?i:python)')
>>> with open('sample_mod.md', 'w') as op_file:
...     op_file.write(pat.sub(lambda m: m[0].capitalize(), ip_str))
... 
305
>>> assert open('sample_mod.md').read() == open('expected.md').read()
```

**l)** For the given input strings, construct a word that is made up of last characters of all the words in the input. Use last character of last word as first character, last character of last but one word as second character and so on.

```ruby
>>> s1 = 'knack tic pi roar what'
>>> s2 = '42;rod;t2t2;car'

>>> pat = regex.compile(r'(?r)\w\b')

>>> ''.join(pat.findall(s1))
'trick'
>>> ''.join(pat.findall(s2))
'r2d2'
```

**m)** Replicate `str.rpartition` functionality with regular expressions. Split into three parts based on last match of sequences of digits, which is `777` and `12` for the given input strings.

```ruby
>>> s1 = 'Sample123string42with777numbers'
>>> s2 = '12apples'

>>> regex.split(r'(\d+)(?!.*\d)', s1)
['Sample123string42with', '777', 'numbers']
>>> regex.split(r'(\d+)(?!.*\d)', s2)
['', '12', 'apples']
```

**n)** Read about fuzzy matching on https://pypi.org/project/regex/. For the given input strings, return `True` if they are exactly same as `cat` or there is exactly one character difference. Ignore case when comparing differences. For example, `Ca2` should give `True`. `act` will be `False` even though the characters are same because position should be maintained.

```ruby
>>> pat = regex.compile(r'(?i)(cat){s<=1}')

>>> bool(pat.fullmatch('CaT'))
True
>>> bool(pat.fullmatch('scat'))
False
>>> bool(pat.fullmatch('ca.'))
True
>>> bool(pat.fullmatch('ca#'))
True
>>> bool(pat.fullmatch('c#t'))
True
>>> bool(pat.fullmatch('at'))
False
>>> bool(pat.fullmatch('act'))
False
>>> bool(pat.fullmatch('2a1'))
False
```

