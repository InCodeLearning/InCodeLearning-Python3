import re


# 1. simple testing example w/o regular exp
print ("*********** Matching w/o Regex    ************")

S = "Regular expressions easily explained"
_yn = "easily" in S

print (_yn)

# 2. Simple Regex

print ("*********** Simple RegEx           ************")
x = re.search("cat", "A cat and a rat can't be friend.")
print (x)

x = re.search("cow", "A cat and a rat can't be friend.")
print (x)

# 3. Combine If logic
print ("*********** If RegEx                ************")
if re.search("cat", "A cat and a rat can't be friend."):
    print('Find the "cat"')
else:
    print('Can\'t find the "cat"')

if re.search("cow", "A cat and a rat can't be friend."):
    print('Find the "cat"')
else:
    print('Can\'t find the "cow"')

# 4. Raw format r"

print ("*********** User Raw format         ************")
if re.search(r"is", "Mayer is a very common Name"):
    print('Find the "is"')
else:
    print('Can\'t find the "is"')

# 5. Add patterns
print ("*********** User Pattern parameters ************")
if re.search(r"M[ae][iy]er", "Mayer is a very common Name"):
    print('Find the Match')
else:
    print('Can\'t find the Match')

# 6. Add param -I ignore case
print ("*********** Add parameters ************")
if re.search(r"mayer", "Mayer is a very common Name\n"):
    print('Find the Mayer')
elif re.search(r"mayer", "Mayer is a very common Name\n", re.I):
    print('Find the Mayer with case insensitive')
else:
    print('Can\'t find the Mayer')

# 7. Grouping and back reference

mo = re.search("([0-9]+).*: (.*)", "Customer number: 2454, Date: Feb 12, 2011")
print ("*********** back reference ************")
print ("Back reference .group():", mo.group())
print ("Back reference group(1):", mo.group(1))
print ("Back reference group(2):", mo.group(2))
