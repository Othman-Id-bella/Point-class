class Point:
    def __init__(self,abscisse=0,ordonne=0):
       self.abscisse=abscisse
       self.ordonne=ordonne

    def Distance(self,point):
        distance=((self.abscisse-point.abscisse)**2+(self.ordonne-point.ordonne)**2)
        return distance**0.5
    
    def Norme(self):
        return(self.abscisse**2 + self.ordonne**2)**0.5
    
point1 = Point(1, 2)
point2 = Point(4, 6)

distance = point1.Distance(point2)
norme = point1.Norme()

print("Distance between points:",distance)
print("Norm of point1: ",norme)
