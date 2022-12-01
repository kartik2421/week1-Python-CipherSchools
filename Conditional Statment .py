# 1 indent  = 2 spaces, 4 spaces ,tab , 9 spaces user defined

a = True
if True:
    print("A")

a = False

if a:
    print("the value is true")
print("end")

a = False
if a:
    print("this value is true")
elif a == 5:
    print("this value is 5")
else:
    print("this value is false")

# if x<0:
#     sign=-1
# if x == 0:
#     sign=0
# if x>0:
#     sign = 1

# x = int(-inf, inf)
# G -> x 

# a= x < 0
# b = x == 0
# c = x > 0

# a int b = b int c = a int c = phi
# a u b u c != 0 then else statement
# conditions are mutually exclusive

# q = can profile A access profile B

# a = isFriend
# b = isBlocked
# c = isAdmin
# d = isMarkZuckerberg

# a b c d q
# 0 0 0 0 0   
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 0
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1
# 1 0 0 0 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 0
# 1 1 0 1 1
# 1 1 1 0 0
# 1 1 1 1 1

if ___:
    print("has access")
else:
    print("access denied")