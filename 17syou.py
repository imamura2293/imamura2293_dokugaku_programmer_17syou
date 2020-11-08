$ export GREP_OPTIONS="--color=always"

$ grep Beautiful zen.txt

$ grep Beautiful zen.txt

$ grep -i Beautiful zen.txt

$ grep -o Beautiful zen.txt

import  re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

import  re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l, re.IGNORECASE )

print(matches)


$ grep ^IF zen.txt

$ grep idea. zen.txt

$ grep idea.$ zen.txt


import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""


m = re.findall("^If", zen, re.MULTILINE)
print(m)

$ echo Two too. | grep -i t[ow]o

import re
string ="Two too"
m = re.findball("t[ow]o", string, re.IGNORECASE)
print(m)


$ echo 123 hi 34 hello. | grep [[:didit:]]

import re

line = "123 hi 34 hello."
m = re.findball("\de", line, re.IGNORECASE)
print(m)

$ echo two twoo not too. | grep -o two*


$ echo __hello__there | grep -o __.*__

$