print("Assign multiple value to multiple variables:")
num1,num2,num3=10,20,30
print("Number1 value",num1)
print("Number2 value",num2)
print("Number3 value",num3)
print("All variable refferences are:",id(num1),id(num2),id(num3))

print("Assign single value to multiple variables:")
num1,num2,num3=10,10,10
print("Number1 value",num1)
print("Number2 value",num2)
print("Number3 value",num3)
print("All variable refferences are:",id(num1),id(num2),id(num3))


print("swappng two numbers")
a,b=10,20
print("Before swapping")
print(a,b,id(a),id(b))
a,b=b,a
print(a,b,id(a),id(b))


