from datetime import datetime
now = datetime.now()
print(now)

from datetime import datetime
today = datetime.now().date()
print(today)

from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y"))

import glob
file = glob.glob("*.txt")
print(file)

import os

files = os.listdir()

print(files)

import glob
python_files = glob.glob("*.py")
print(python_files)

import re
text = "Python is easy to learn"
result = re.findall("Python", text)
print(result)

import re
test = "english speaking in my style is good"
result = re.findall("speaking",test)
print(result)

import re
text = "Age 21, Score 95"
numbers = re.findall(r"\d+", text)
print(numbers)

import re
team = "age 50 & 60 is just a number"
numbers = re.findall(r"\d+",team)
print(numbers)

import re
text = "Python Programming Practice"
words = re.findall(r'P\w+', text)
print(words)

import re
sentence = "python programming language is best practice language"
words = re.findall(r'p\w+', sentence)
print(words)
