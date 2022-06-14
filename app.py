class Rectangle:
    def __init__(self, width, height):
        self.h = height
        self.w = width

    def calculate_area(self):
        return self.w * self.h
  
class Carre :
    def __init__ (self,width):
        self.w = width

    def calculate_area(self):
        return self.w ** 2

i = input('carré ou rectangle')
if i == 'carré':
    w = int(input('entrer la longueur ou la largeur'))
    h = w
    calcul = Carre(w)
    resultat = calcul.calculate_area()
    print('le resultat est :' , resultat )

if i == 'rectangle':
    w = int(input('entrer la largeur'))
    h = int(input('entrer la longueur '))
    calcul = Rectangle(w, h)
    resultat = calcul.calculate_area()
    print ('le resultat est :' , resultat)

else :
    print('Veuillez entrer une ou plusieur valeurs')