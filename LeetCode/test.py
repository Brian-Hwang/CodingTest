a = "HELLOHELLOHELLO"
b = "HELLO"
c = a.split(b)
print(c, len(c))
if any(item for item in c if item != ""):
    print(c)

print(b * 3)
