xA = int(input("Введите координату x точки А"))
yA = int(input("Введите координату y точки А"))
xB = int(input("Введите координату x точки B"))
yB = int(input("Введите координату x точки B"))
A = (yA-yB)
B = (xB-xA)
C = (xA*yB - xB*yA)
print ("{}x+{}y+{}=0".format(A,B,C))
