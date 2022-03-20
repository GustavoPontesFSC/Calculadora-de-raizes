def root1deg(a, b):
    x =-b/a
    return x
class root2deg():
    def __init__(self, a=0, b=0, c=0):
        self.delta = b**2 - 4*a*c
        self.sqrtdelta = self.delta**(1/2)
        if self.delta < 0:
            self.x1 = "Não está definido para os reais!"
            self.x2 = "Não está definido para os reais!"
            self.sqrtdelta = 'Não está definido para os reais!'
        else:
            self.sqrtdelta = self.delta**(1/2) #raiz de edelta
            self.x1 = (-b + self.sqrtdelta) / (2 * a) #x'
            self.x2 = (-b - self.sqrtdelta) / (2 * a) #x''     
        self.xv = -b/(2*a) #x do vertice
        self.yv = -self.delta / (4 * a)  #y do vertice              
        pass
    
    pass