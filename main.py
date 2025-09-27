import math

print(math.gcd(120,200))
no1, no2=120,200
div =2
if no1<no2:
    small=no1
elif no2<no1:
    small=no2
while div<=small:
    if no1%div==0 and no2%div==0:
        last=div
    div+=1
else:
        print(last)
