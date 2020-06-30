## CommonRegex

from commonregex import ip

data = 'hello 255.21.255.22 okay'

ip.findall(data)

data = '23.14.2.4.2 255.21.255.22 567.12.2.1'

ip.findall(data)

[e for e in data.split() if ip.fullmatch(e)]

