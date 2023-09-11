def fact(n):
  if(n==1) :
    return 1
  return n * fact(n-1)
n= int(input(" enter the value of n :"))
print(" the factorial of given number is",fact(n)) 
