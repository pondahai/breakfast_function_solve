from numpy import linspace,power,cos
sum = 0
for x in linspace(-2,2,1000000):
    sum = sum + (((power(x,3))*cos(x/2)+0.5)*power(4-power(x,2),0.5))*((4/1000000))
print (sum)


from scipy import integrate
f1=lambda x:(((x**3)*cos(x/2)+0.5)*((4-x**2)**0.5))
print (integrate.quad(f1,-2,2))
