# a=int(input("enter the number "))
# len=len(str(a))
# i=a
# sum=0
# while a>0:
#     b=(a%10)**len
#     sum=sum+b
#     a=a//10
# if sum==i:
#     print("armstrong number",i)
# else:
#     print("not armstrong number ",i)

# a=int(input("enter the number"))
# len=len(str(a))
# i=a
# sum=0
# while a>0:
#    b=(a%10)**len
#    sum=sum+b
#    a=a//10
# if sum==i:
#    print("amstrong number",i)
# else:
#    print("not amstrong number",i)



a=int(input("enter the number"))
len=len(str(a))
i=a
sum=0
while a>0:
   b=(a%10)**len
   sum=sum+b
   a=a//10
if sum==i:
   print("amstrong number",i)
else:
   print("not amstrong",i)        
    
    

        