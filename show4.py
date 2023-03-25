from math import sqrt
class dot():
    def __init__(self, x=0, y=0):
      self._x=x
      self._y=y
    def move_to(self,x,y):
        self._x=x
        self._y=y
    def move_by(self,addx,addy):
        self._x+=addx
        self._y+=addy
    def distance(self,other):
        subx=self._x-other._x
        suby=self._y-other._y
        lenth=sqrt(subx*subx+suby*suby)
        print(f"{lenth}")
    def now(self):
        print(f"x={self._x},y={self._y}")
        
def main():
    dot1=dot(0,0)
    dot2=dot(10,10)
    dot1.move_by(3,4)
    dot1.distance(dot2)
    
if __name__=='__main__':
    main()