from Tuesday02.ArrayStack import arrayStack

s = arrayStack(30)

str = input("Enter String: ")
for c in str:
    s.push(c)

print("Print String: ", end="")
while not