import re

string = '檢視另1000則回覆'
regex = re.compile(r"檢視另(\d+)則回覆")
match = regex.search(string)
print(match.group(0))

a = None
if not a:
    print('yes')