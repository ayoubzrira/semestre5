#!/usr/bin/env python3
from random import randint
class Point:
  """ création d'un objet Point
  """

  def __init__(self):
      self.cordonnees = (randint(1,50),randint(1,50))


  def svg(self):
      print('<svg width="100" height="100">\
  <circle cx={} cy={} r="5" stroke="green" stroke-width="4" fill="yellow" />'.format(self.cordonnees[0],self.cordonnees[1]))





def triangle():
    triangle = [Point(),Point(),Point()]
    print("<svg height={} width={}>".format(800,500))
    triangle[0].svg()    
    triangle[1].svg()
    triangle[2].svg()


    #print("<polygon points=\"{}\" \"{}\" \"{}\" />".format(,,triangle[2].svg()))
    print("</svg>")
triangle()
