#Swap two variables (without using a third variable if you want a challenge).
a=5
b=6
print(f"Before swapping: a={a}, b={b}")
a,b=b,a
print(f"After swapping: a={a}, b={b}")
#Python evaluates the right side first, 
#so it builds a pair containing the current values of b and a. 
# Then it assigns those values back to the left side variables in order. 
# So if a = 5 and b = 6, after this line a = 6 and b = 5.
# This works because Python supports tuple unpacking, 
# so you do not need a temporary third variable.