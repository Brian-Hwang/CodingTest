a = "HELLOHELLOHELLO"
b = "HELLO"
list = [1, 2, 3, 4, 5]
print(max(list), len(list))
c = a.split(b)
print(c, len(c))
if any(item for item in c if item != ""):
    print(c)

print(b * 3)
print("HELLOHELLO" / b)
