def fact(a):
   if a==0 or a==1:
     return 1
   else:
     return a*fact(a-1)
num=5
res=fact(num)
print("The factorial of",num,"is",res)
