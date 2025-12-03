#!/usr/bin/env python3
n1 = input ("Digite o primeiro numero ")
n2 = input ("Digite o segundo numero ")
n1 = int(n1)
n2 = int(n2)
mult = n1 * n2

print(f"{n1} x {n2}= {mult}")
if mult <0 :
    print ("Esse numero e negativo.")

elif mult == 0:
    print ("Esse numero e positivo e negativo.")
else :
    print ("Esse numero e positivo.") 
     
       