# Regular Expression modules

**a)** For the given input file, print all lines containing the string `two`

```ruby
# note that expected output shown here is wrapped to fit pdf width
>>> filename = 'programming_quotes.txt'
>>> word = re.compile()     ##### add your solution here
>>> with open(filename, 'r') as ip_file:
...     for ip_line in ip_file:
...         if word.search(ip_line):
...             print(ip_line, end='')
... 
"Some people, when confronted with a problem, think - I know, I'll use regular expressions.
Now they have two problems" by Jamie Zawinski
"So much complexity in software comes from trying to make one thing do two things" by Ryan Singer
```

**b)** For the given input string, print all lines NOT containing the string `2`

```ruby
>>> purchases = '''\
... apple 24
... mango 50
... guava 42
... onion 31
... water 10'''
>>> num = re.compile()      ##### add your solution here
>>> for line in purchases.split('\n'):
...     if not num.search(line):
...         print(line)
... 
mango 50
onion 31
water 10
```

<br>

# Anchors

**a)** For the given **url**, count the total number of lines that contain `is` or `the` as whole words.
Note that each `line` in the `for` loop will be of `bytes` data type.

```ruby
>>> import urllib.request
>>> scarlet_pimpernel_link = r'https://www.gutenberg.org/cache/epub/60/pg60.txt'
>>> word1 = re.compile()    ##### add your solution here
>>> word2 = re.compile()    ##### add your solution here
>>> count = 0
>>> with urllib.request.urlopen(scarlet_pimpernel_link) as ip_file:
...     for line in ip_file:
...         if word1.search(line) or word2.search(line):
...             count += 1
... 
>>> print(count)
3737
```

**b)** For the given input string, change only whole word `red` to `brown`

```ruby
>>> words = 'bred red spread credible'

>>> re.sub()     ##### add your solution here
'bred brown spread credible'
```

**c)** For the given input list, filter all elements that contains `42` surrounded by word characters.

```ruby
>>> words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']

>>> [w for w in words if re.search()]   ##### add your solution here
['hi42bye', 'nice1423', 'cool_42a']
```

**d)** For the given input list, filter all elements that start with `den` or end with `ly`

```ruby
>>> foo = ['lovely', '1 dentist', '2 lonely', 'eden', 'fly away', 'dent']

>>> [e for e in foo if ]        ##### add your solution here
['lovely', '2 lonely', 'dent']
```

**e)** For the given input string, change whole word `mall` only if it is at start of line.

```ruby
>>> para = '''\
... ball fall wall tall
... mall call ball pall
... wall mall ball fall'''

>>> print(re.sub())    ##### add your solution here
ball fall wall tall
1234 call ball pall
wall mall ball fall
```

<br>

# Alternation and Grouping

**a)** For the given input list, filter all elements that start with `den` or end with `ly`

```ruby
>>> foo = ['lovely', '1 dentist', '2 lonely', 'eden', 'fly away', 'dent']

>>> [e for e in foo if ]     ##### add your solution here
['lovely', '2 lonely', 'dent']
```

**b)** For the given **url**, count the total number of lines that contain `removed` or `rested` or
`received` or `replied` or `refused` or `retired` as whole words. Note that each `line` in the
`for` loop will be of `bytes` data type.

```ruby
>>> import urllib.request
>>> scarlet_pimpernel_link = r'https://www.gutenberg.org/cache/epub/60/pg60.txt'
>>> words = re.compile()   ##### add your solution here
>>> count = 0
>>> with urllib.request.urlopen(scarlet_pimpernel_link) as ip_file:
...     for line in ip_file:
...         if words.search(line):
...             count += 1
... 
>>> print(count)
83
```

<br>

# Escaping metacharacters

**a)** Transform given input strings to expected output using same logic on both strings.

```ruby
>>> str1 = '(9-2)*5+qty/3'
>>> str2 = '(qty+4)/2-(9-2)*5+pq/4'

>>>    ##### add your solution here for str1
'35+qty/3'
>>>    ##### add your solution here for str2
'(qty+4)/2-35+pq/4'
```

**b)** Replace any matching item from given list with `X` for given input strings.

```ruby
>>> items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
>>> alt_re = re.compile()      ##### add your solution here

>>> alt_re.sub(r'X', '0a.bcd')
'0Xcd'
>>> alt_re.sub(r'X', 'E{n}AMPLE')
'EXAMPLE'
>>> alt_re.sub(r'X', r'43+n2 ax\y\ze')
'4X2 aXe'
```

<br>

# Dot metacharacter and Quantifiers

**Note** that some exercises are intentionally designed to be complicated to solve with regular
expressions alone. Try to use normal string methods, break down the problem into multiple steps, etc.
Some exercises will become easier to solve with techniques presented in chapters to come. Going through
the exercises a second time after finishing entire book will be fruitful as well.

**a)** Use regular expression to get the output as shown for the given strings.

```ruby
>>> eqn1 = 'a+42//5-c'
>>> eqn2 = 'pressure*3+42/5-14256'
>>> eqn3 = 'r*42-5/3+42///5-42/53+a'

##### add your solution here for eqn1
['a+', '-c']
##### add your solution here for eqn2
['pressure*3+', '-14256']
##### add your solution here for eqn3
['r*42-5/3+42///5-', '3+a']
```

**b)** For the given strings, construct a RE to get output as shown.

```ruby
>>> str1 = 'a+b(addition)'
>>> str2 = 'a/b(division) + c%d(#modulo)'
>>> str3 = 'Hi there(greeting). Nice day(a(b)'

>>> remove_parentheses = re.compile()     ##### add your solution here
>>> remove_parentheses.sub('', str1)
'a+b'
>>> remove_parentheses.sub('', str2)
'a/b + c%d'
>>> remove_parentheses.sub('', str3)
'Hi there. Nice day'
```

**c)** Remove leading/trailing whitespaces from all the individual fields of these csv strings.

```ruby
>>> csv1 = ' comma  ,separated ,values '
>>> csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'

##### add your solution here for csv1
'comma,separated,values'
##### add your solution here for csv2
'good bad,nice  ice,42,,stall   small'
```

**d)** Correct the given RE to get the expected output.

```ruby
>>> words = 'plink incoming tint winter in caution sentient'
>>> change = re.compile(r'int|in|ion|ing|inco|inter|ink')

# wrong output
>>> change.sub(r'X', words)
'plXk XcomXg tX wXer X cautX sentient'

# expected output
>>> change = re.compile()       ##### add your solution here
>>> change.sub(r'X', words)
'plX XmX tX wX X cautX sentient'
```

**e)** For the given greedy quantifiers, what would be the equivalent form using `{m,n}` representation?

* `?` is same as
* `*` is same as
* `+` is same as

**f)** `(a*|b*)` is same as `(a|b)*` - True or False?

<br>

# Working with matched portions

**a)** For the given strings, extract the matching portion from first `is` to last `t`

```ruby
>>> str1 = 'What is the biggest fruit you have seen?'
>>> str2 = 'Your mission is to read and practice consistently'
>>> expr = re.compile()     ##### add your solution here

>>> expr        ##### add your solution here
'is the biggest fruit'
>>> expr        ##### add your solution here
'ission is to read and practice consistent'
```

**b)** Transform the given input strings to expected output as shown.

```ruby
>>> row1 = '-2,5 4,+3 +42,-53 '
##### add your solution here
[3, 7, -11]

>>> row2 = '1.32,-3.14 634,5.63 '
##### add your solution here
[-1.82, 639.63]
```

<br>

# Character class

**a)** Delete all pair of parentheses, unless they contain a parentheses character.

```ruby
>>> str1 = 'def factorial()'
>>> str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
>>> str3 = 'Hi there(greeting). Nice day(a(b)'

>>> remove_parentheses = re.compile()      ##### add your solution here
>>> remove_parentheses.sub('', str1)
'def factorial'
>>> remove_parentheses.sub('', str2)
'a/b + c%d - (e+*4)'
>>> remove_parentheses.sub('', str3)
'Hi there. Nice day(a'
```

**b)** Extract all hex character sequences, with optional prefix. Match the
characters case insensitively, and the sequences shouldn't be surrounded by
other word characters.

```ruby
>>> hex_seq = re.compile()        ##### add your solution here

>>> str1 = '128A foo 0xfe32 34 0xbar'
##### add your solution here
['128A', '0xfe32', '34']

>>> str2 = '0XDEADBEEF lace 0x0ff1ce bad'
##### add your solution here
['0XDEADBEEF', '0x0ff1ce', 'bad']
```

**c)** Output True/False depending upon input string containing any number sequence
that is greater than `624`

```ruby
>>> str1 = 'hi0000432abcd'
##### add your solution here
False

>>> str2 = '42_624 0512'
##### add your solution here
False

>>> str3 = '3.14 96 2 foo1234baz'
##### add your solution here
True
```

**d)** Split the given strings based on consecutive sequence of digit or whitespace characters.

```ruby
>>> str1 = 'lion \t Ink32onion Nice'
>>> str2 = '**1\f2\n3star\t7 77\r**'
>>> expr = re.compile()       ##### add your solution here

>>> expr.split(str1)
['lion', 'Ink', 'onion', 'Nice']
>>> expr.split(str2)
['**', 'star', '**']
```

<br>

# Groupings and backreferences

**a)** The given string has fields separated by `:` and each field has a floating point
number followed by a `,` and a string. If the floating point number has only one digit
precision, append `0` and swap the strings separated by `,` for that particular field.

```ruby
>>> row = '3.14,hi:42.5,bye:1056.1,cool:00.9,fool'
##### add your solution here
'3.14,hi:bye,42.50:cool,1056.10:fool,00.90'
```

**b)** Count the number of words that have at least two consecutive repeated alphabets,
for ex: words like `stillness` and `Committee` but not words like `root` or `readable` or `rotational`.
Consider word to be as defined in regular expression parlance and word split across two lines as two
different words.

```ruby
>>> import urllib.request
>>> scarlet_pimpernel_link = r'https://www.gutenberg.org/cache/epub/60/pg60.txt'
>>> word_expr = re.compile()      ##### add your solution here
>>> count = 0
>>> with urllib.request.urlopen(scarlet_pimpernel_link) as ip_file:
...     for line in ip_file:
...         for word in re.findall(rb'\w+', line):
...             if word_expr.search(word):
...                 count += 1
... 
>>> print(count)
219
```

**c)** Convert the given **markdown** headers to corresponding **anchor** tag.
Consider the input to start with one or more `#` characters followed by space and word characters.
The `name` attribute is constructed by converting the header to lowercase and replacing spaces
with hyphens. Can you do it without using a capture group?

```ruby
>>> header1 = '# Regular Expressions'
>>> header2 = '## Compiling regular expressions'

##### add your solution here for header1
'# <a name="regular-expressions"></a>Regular Expressions'
##### add your solution here for header2
'## <a name="compiling-regular-expressions"></a>Compiling regular expressions'
```

**d)** Convert the given **markdown** anchors to corresponding **hyperlinks**.

```ruby
>>> anchor1 = '# <a name="regular-expressions"></a>Regular Expressions'
>>> anchor2 = '## <a name="subexpression-calls"></a>Subexpression calls'

##### add your solution here for anchor1
'[Regular Expressions](#regular-expressions)'
##### add your solution here for anchor2
'[Subexpression calls](#subexpression-calls)'
```

**e)** Use appropriate regular expression function to get the expected output for given string.

```ruby
>>> str1 = 'price_42 roast:\t\n:-ice==cat\neast'
##### add your solution here
['price_42', ' ', 'roast', ':\t\n:-', 'ice', '==', 'cat', '\n', 'east']
```

<br>

# Lookarounds

**a)** Remove leading and trailing whitespaces from all the individual fields of these csv strings.

```ruby
>>> csv1 = ' comma  ,separated ,values '
>>> csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'

>>> remove_whitespace = re.compile()     ##### add your solution here
>>> remove_whitespace.sub('', csv1)
'comma,separated,values'
>>> remove_whitespace.sub('', csv2)
'good bad,nice  ice,42,,stall   small'
```

**b)** Filter all elements that satisfy all of these rules:

* should have at least two alphabets
* should have at least 3 digits
* should have at least one special character among `%` or `*` or `#` or `$`
* should not end with a whitespace character

```ruby
>>> pwds = ['hunter2', 'F2H3u%9', '*X3Yz3.14\t', 'r2_d2_42', 'A $B C1234']
##### add your solution here
['F2H3u%9', 'A $B C1234']
```

**c)** Match strings if it doesn't contain whitespace or the string `error` between
the strings `qty` and `price`

```ruby
>>> str1 = '23,qty,price,42'
>>> str2 = 'qty price,oh'
>>> str3 = '3.14,qty,6,errors,9,price,3'
>>> str4 = 'qty-6,apple-56,price-234'

>>> neg = re.compile()       ##### add your solution here
>>> bool(neg.search(str1))
True
>>> bool(neg.search(str2))
False
>>> bool(neg.search(str3))
False
>>> bool(neg.search(str4))
True
```

<br>

# Flags

**a)** Delete from the string `start` if it is at beginning of a line up to
the next occurrence of the string `end` at end of a line. Match these keywords
irrespective of case.

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

>>> expr = re.compile()       ##### add your solution here
>>> print(expr.sub('', para))
good start

hi there

42

bye
```

**b)** Explore what the `re.DEBUG` flag does. Here's some examples, check their output:

* `re.compile(r'\Aden|ly\Z', flags=re.DEBUG)`
* `re.compile(r'\b(0x)?[\da-f]+\b', flags=re.DEBUG)`
* `re.compile(r'\b(?:0x)?[\da-f]+\b', flags=re.I|re.DEBUG)`

<br>

# Unicode

**a)** Output `True` or `False` depending on input string made up of ASCII characters or not.
Consider the input to be non-empty strings and any character that isn't part of 7-bit ASCII
set should give `False`

```ruby
>>> str1 = '123—456'
>>> str2 = 'good fοοd'
>>> str3 = 'happy learning!'
>>> str4 = 'İıſK'

##### add your solution here for str1
False
##### add your solution here for str2
False
##### add your solution here for str3
True
##### add your solution here for str4
False
```

<br>

# Miscellaneous

**a)** Count the maximum depth of nested braces for the given string.
Unbalanced or wrongly ordered braces should return `-1`

```ruby
>>> def max_nested_braces(ip):
##### add your solution here

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

**b)** Replace the string `par` with `spar`, `spare` with `extra` and `park` with `garden`

```ruby
>>> str1 = 'apartment has a park'
##### add your solution here for str1
'aspartment has a garden'

>>> str2 = 'do you have a spare cable'
##### add your solution here for str2
'do you have a extra cable'

>>> str3 = 'write a parser'
##### add your solution here for str3
'write a sparser'
```

**c)** Read about `POSIX` flag from [regex module documentation](https://pypi.org/project/regex/).
Is the following code snippet showing the correct output?

```ruby
>>> words = 'plink incoming tint winter in caution sentient'
>>> change = regex.compile(r'int|in|ion|ing|inco|inter|ink', flags=regex.POSIX)
>>> change.sub(r'X', words)
'plX XmX tX wX X cautX sentient'
```

**d)** For the given **markdown** file, replace all occurrences of the string `python` (irrespective
of case) with the string `Python`. However, any match within code blocks that start with whole line
` ```python ` and end with whole line ` ``` ` shouldn't be replaced.
Consider the input file to be small enough to fit memory requirements.

```ruby
>>> ip_str = open('sample.md', 'r').read()
>>> expr = regex.compile()      ##### add your solution here
>>> with open('sample_mod.md', 'w') as op_file:
...     op_file.write(expr.sub(lambda m: m[0].capitalize(), ip_str))
... 
305
>>> assert open('sample_mod.md').read() == open('expected.md').read()
```

