"""Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary par"""
x=complex(input("enter the imaginary number"))
print(x.real) if x.real>x.imag else print(x.imag)
t1=tuple([int(e) for e in input("enter the number sepatater by comma").split(' ,')])
print(t1)