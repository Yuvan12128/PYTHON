email=input('enter you email : ')
count=0
length = len(email)
i=0
while i<length:
    if email[i]>='a' and email[i]<='z':
        print(email[i])
        count+=1
    i+=1

print(count)