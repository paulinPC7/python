b= int (input("digite o valor da base da Base:"))

e= int (input("digite o valor da base do expoente:"))
r= b

for g in range(1,e):
    r =r * b
print ("resultado:", "{:.2f}".format(r))
