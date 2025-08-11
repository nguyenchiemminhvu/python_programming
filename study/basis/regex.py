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

x = re.match(r"([\w ]+)(\d+)", txt)
print(x)  # <re.Match object; span=(0, 20), match='The rain in Spain 123'>