
from math import pi

print("==================")
print("Area Calculator 📐")
print("==================")

print("              ")

#Forms
print(" 1) Triangulo ")
print(" 2) Retângulo ")
print(" 3) Quadrado ")
print(" 4) Circulo ")
print(" 5) Exit ")

print("             ")

#Where start to work

area = int(input(" Which Shape: "))

if area == 1:
    altura = int(input( " Altura: " ))
    base = int(input( " Base: "))
    print( "                 ")
    print( " The Triangle area is: " + str((altura*base)/2) + " Cm")

elif area == 2:
    comprimento = int(input( " Comprimento: "))
    largura = int(input( " Largura: "))
    print( "                 ")
    print(" The Rectangle area is: " + str(comprimento*largura) + " Cm")

elif area == 3:
    lado = int(input( "Lado: "))
    print( "                 ")
    print(" The Square area is: " + str(lado**2) + " Cm")

elif area == 4:
    raio = int(input( " Raio: "))
    print( "                 ")
    print(" The Circle area is: " + str(pi*raio**2) + " Cm")

else:
    print( "                 ")
    print( " Don´t Have this Option!! ")