print("Enter the first number:\n")
x = int(input())
print("Enter the second number:\n")
y = int(input())
print("Enter the third number:\n")
z = int(input())

k = 0
o = 0

if x%2 ==0:
 k = k+1
else:
  o = 0+1
if y%2 ==0:
  k = k+1
else:
  o = 0+1
if z%2 ==0:
   k = k+1
else:
  o = 0+1

print(f"there are {k} even and {o} odd numbers")