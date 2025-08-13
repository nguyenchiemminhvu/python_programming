import re

txt = "The rain in Spain 123"

# search
x = re.search(r"^The.*ain$", txt)
print(x)  # <re.Match object; span=(5, 8), match='ain'>

x = re.search(r"ain", txt)
print(x)  # <re.Match object; span=(5, 8), match='ain'>

x = re.findall(r"ain", txt)
print(x)  # ['ain', 'ain']

x = re.split(r"\s", txt)
print(x)  # ['The', 'rain', 'in', 'Spain']

x = re.sub(r"ain", "XXX", txt)
print(x)  # The rXXX in SpXXX

# grouping
x = re.match(r"([\w ]+)(\d+)", txt)
print(x)  # <re.Match object; span=(0, 20), match='The rain in Spain 123'>

x = re.sub(r"([\w ]+) (\d+)", r"\2 \1", txt)
print(x)  # 123 The rain in Spain

txt = "aaaaaaaaaaa b"
x = re.search(r"a{3,5}", txt)
print(x)

x = re.search(r"a{3,5}?", txt)
print(x)

x = re.search(r"\bb", txt)
print(x)

x = re.search(r"(\w+) (\w+)", txt)
print(x.groups())

txt = "ab ab ab"
x = re.search(r"(\b\w+\b) \1 \1", txt)
print(x)

x = re.search(r"(?P<g1>\w+) (?P<g2>\w+)", txt)
print(x)
print(x.group('g1'), x.group('g2'))

x = re.search(r"(?P<g1>\w+) (?P=g1)", txt)
print(x)

txt = "ab ac ad"

x = re.search(r"(?P<g1>\w+) (?:\w+) (?P<g2>\w+)", txt)
print(x)
print(x.group('g1'), x.group('g2'))

x = re.search(r"(ab|ac|ad)", txt)
print(x)