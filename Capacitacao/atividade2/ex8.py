class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
def dentroRet(v1: int, v2: int, p: int) -> bool:
    if v1.x <= p.x <= v2.x and v1.y <= p.y <= v2.y:
        return True
    else:
        return False

v1 = Ponto(0, 0)
v2 = Ponto(10, 10)
p1 = Ponto(5, 5) 
p2 = Ponto(15, 15)  

print(dentroRet(v1, v2, p1))  
print(dentroRet(v1, v2, p2))  
