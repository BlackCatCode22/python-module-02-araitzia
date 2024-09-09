x = input("Enter First Integer: ")
y = input ("Enter Second Integer: ")
z = input ("Enter Third Integer: ")
xi = int (x)
yi = int (y)
zi = int (z)

if xi > yi:
    if xi > zi:
        l = xi
    else:
        l = zi
else:
    if yi > zi:
        l = yi
    else:
        l = zi

print ("Largest Integer = ", l)