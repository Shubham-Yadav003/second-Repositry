x=input()
y=x.split(",")
print(tuple(y))

value=int(input("value"))
for i in range(len(y)):
    y[i]==int(y[i])


if value in  y:
    print("true")
else:
    print("false")
