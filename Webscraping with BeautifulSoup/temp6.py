import re
"""
s = '28.01'
pattern = re.compile("^[0-9].[0-9]$")
print(pattern.match(s))
"""


pattern = '^[0-9][0-9].[0-9][0-9]$'
test_string = '28.01'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
