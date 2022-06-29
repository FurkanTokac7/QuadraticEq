#Create the class.
class QuadraticEq():
     #Equation --> ax^2 + bx + c = 0
     #Defined a,b,c variables.
     def __init__(self,name,a,b,c):
          self.name = name
          self.a = a
          self.b = b
          self.c = c

     #Calculate the discriminant.
     def disc(self):
          return self.b**2-4*self.a*self.c

     #Calculate the roots.
     def roots(self):
          if self.disc() > 0:
               x_1 = (-self.b + (self.disc())**0.5)/(2*self.a)
               x_2 = (-self.b - (self.disc())**0.5)/(2*self.a)
               return x_1,x_2

          elif self.disc() == 0:
               x_12 = -self.b/(2*self.a)
               return x_12

          else:
               x_1 = complex(-self.b,abs(self.disc())**0.5)/(2*self.a)
               x_2 = complex(-self.b,-abs(self.disc())**0.5)/(2*self.a)
               return x_1,x_2

     #Create graph.
     def graph(self):
          import numpy as np
          import matplotlib.pyplot as plt
          x = list(np.linspace(-100,100,1000))
          y = list(map(lambda x:self.a*x**2+self.b*x+self.c,x))
          plt.xlabel("X - Axis");plt.ylabel("Y - Axis")
          plt.title("Graphs")
          plt.plot(x,y,label = self.name)
          plt.legend()
          plt.show()

     #Create multi graph.
     def multi_graph(self,*equations):
          import numpy as np
          import matplotlib.pyplot as plt
          plt.xlabel("X - Axis");plt.ylabel("Y - Axis")
          plt.title("Graphs")
          for eq in equations:
               x = list(np.linspace(-100,100,1000))
               y = list(map(lambda x:eq.a*x**2+eq.b*x+eq.c,x))
               plt.plot(x,y,label = eq.name)
          self.graph()

#Run!
if __name__ == "__main__":
     eq1 = QuadraticEq("Equation 1",1,-6,8)
     eq2 = QuadraticEq("Equation 2",5,2,3)
     eq3 = QuadraticEq("Equation 3",7,4,10)
     print(eq1.roots(),eq2.roots(),eq3.roots(),sep = "\n")
     eq1.multi_graph(eq2,eq3)

     
