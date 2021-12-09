#Imports
import PySimpleGUI as sg


#Define 2º degree calculator
def calc2grau(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        x1 = "Não está definido para os reais!"
        x2 = "Não está definido para os reais!"
        sqrtdelta = 'Não está definido para os reais!'
    else:
        sqrtdelta = delta**(1/2) #raiz de edelta
        x1 = (-b + sqrtdelta) / (2 * a) #x'
        x2 = (-b - sqrtdelta) / (2 * a) #x''
    xv = -b/(2*a) #x do vertice
    yv = -delta / (4 * a)  #y do vertice
    return x1, x2, xv, yv, delta, sqrtdelta

#scope
def main():
    #Theme
    sg.theme('LightGrey1')
    
    #layout
    layout = [
        [sg.Text('Digite o coeficiente a: '), sg.InputText(size = (10,20))],
        [sg.Text('Digite o coeficiente b: '), sg.InputText(size = (10,20))],
        [sg.Text('Digite o coeficiente c: '), sg.InputText(size = (10,20))],
        [sg.Button('Calcular'), sg.Cancel('Fechar')],
        [sg.Output( size = (40,9))],
    ]
    
    
    '''This block is for to define the window to be created, 
    including defining the of window with your name and layout.'''
    
    window = sg.Window('Calculadora de segundo grau.    ', layout) #create a window
    
    
    #loop
    while True:
        event, value = window.read()
        if event == 'Fechar'or event == sg.WIN_CLOSED:
            break
        resultado = calc2grau(float(value[0]), float(value[1]), float(value[2]))
        print(f"x' = {resultado[0]}")
        print(f"x'' = {resultado[1]}")
        print(f'x do vertice = {resultado[2]}')
        print(f'y do vertice = {resultado[3]}')
        print(f'delta = {resultado[4]}')
        print(f'raiz de delta = {resultado[5]}')
        print()
        
    return 0

#call main
if __name__ == '__main__':
    main()
