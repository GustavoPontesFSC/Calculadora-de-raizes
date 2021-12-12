def root2deg(a1=0, b1=0, c1=0):
    variavel = {'a':a1, 'b':b1, 'c':c1}
    delta = (variavel['b']**2) - (4*variavel['a']*variavel['c'])
    if delta < 0:
        x1 = "Não está definido para os reais!"
        x2 = "Não está definido para os reais!"
        sqrtdelta = 'Não está definido para os reais!'
    else:
        sqrtdelta = delta**(1/2) #raiz de edelta
        x1 = (-variavel['b'] + sqrtdelta) / (2 * variavel['a']) #x'
        x2 = (-variavel['b'] - sqrtdelta) / (2 * variavel['a']) #x''
    xv = -variavel['b']/(2*variavel['a']) #x do vertice
    yv = -delta / (4 * variavel['a'])  #y do vertice
    return x1, x2, xv, yv, delta, sqrtdelta
print(root2deg(1,1,-1))