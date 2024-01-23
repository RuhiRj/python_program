"""Write a recursive python function to calculate sum of squares of first N natural
numbers"""
print("enter the number")
n=int(input())
def sumev(n):
    if n==1:
        return 1
    return (n*n)+sumev(n-1)
s=sumev(n)
print(s)
