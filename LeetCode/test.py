a = "HELLOHELLOHELLO"
b = "HELLO"
list = [1, 2, 3, 4, 5]
print(list[0:])
print(max(list), len(list))
c = a.split(b)
print(c, len(c))
if any(item for item in c if item != ""):
    print(c)

print(b * 3)

list = ["a", "b", "c", "d", "e"]
it = iter(list)
for item in it:
    print(item)

print("ASDF")
for item in range(1, len(list) + 1, 1):
    print(list[-item])


for i in range(-5):
    print(i)

print(float(13) / 3)
