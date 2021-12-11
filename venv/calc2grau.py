#Imports
import PySimpleGUI as sg

#Define 1º degree calculator
def calc1grau(a, b):
    x =-b/a
    return x
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
    tab2_layout = [
        [sg.Text('Digite o coeficiente a: '), sg.InputText(size = (10,20), key = 'eq2ga')],
        [sg.Text('Digite o coeficiente b: '), sg.InputText(size = (10,20), key = 'eq2gb')],
        [sg.Text('Digite o coeficiente c: '), sg.InputText(size = (10,20), key = 'eq2gc')],
        [sg.Button('Calcular', key = 'calc2g')],
    ]
    tab1_layout = [
        [sg.Text('Digite o coeficiente a: '), sg.InputText(size=(10,20), key = 'eq1ga')],
        [sg.Text('Digite o coeficiente b: '), sg.InputText(size=(10,20), key = 'eq1gb')],
        [sg.Button('Calcular',key='calc2g')],
    ]
    
    layout = [
        [sg.TabGroup([[sg.Tab('Calculadora de 1º grau', tab1_layout), sg.Tab('Calculadora de 2º grau', tab2_layout)]])],
        [sg.Output( size = (40,9))],
        [sg.Cancel('Fechar')],
    ]
    
    '''This block is for to define the window to be created, 
    including defining the of window with your name and layout.'''
    
    window = sg.Window('Calculadora de raizes', layout) #create a window
    
    
    #loop
    while True:
        event, value = window.read()
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
        try:
            resultado = calc2grau(float(value['eq2ga']), float(value['eq2gb']), float(value['eq2gc']))
            print(f"x' = {resultado[0]}")
            print(f"x'' = {resultado[1]}")
            print(f'x do vertice = {resultado[2]}')
            print(f'y do vertice = {resultado[3]}')
            print(f'delta = {resultado[4]}')
            print(f'raiz de delta = {resultado[5]}')
            print()
        except:
            print(calc1grau(float(value['eq1ga']), float(value['eq1gb'])))
        
    return 0

#call main
if __name__ == '__main__':
    main()
