with open("demo.txt", "r") as f:
    data = f.read()
print(data)
f = open("demo.txt", "a")
f.write("\nthis line is added")
f.close()
f = open("demo.txt", "r")
print(f.read())
f.close()
a, b, c = 8, 15, 10
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)