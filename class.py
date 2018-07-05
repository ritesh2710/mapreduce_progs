class CalArea:
    def __init__(self):
        print("This class calculates area of different shapes")
    
    def AreaRect(self,length, width):
        area = length*width
        return area
            
    def AreaSqr(self,length):
        area = length*length
        return area
    
    
x = CalArea()

print(x.AreaRect(2,2))
print(x.AreaSqr(2))