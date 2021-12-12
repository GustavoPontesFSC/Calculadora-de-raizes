#Imports
import PySimpleGUI as sg
from rootndeg import root1deg, root2deg
#Define 1º degree calculator

#scope
def main():
    #Theme
    sg.theme('LightGrey1')
    
    #layout
    tab2_layout = [
        [sg.Text('Digite o coeficiente a: '), sg.InputText(size = (10,20), key = 'eq2ga')],
        [sg.Text('Digite o coeficiente b: '), sg.InputText(size = (10,20), key = 'eq2gb')],
        [sg.Text('Digite o coeficiente c: '), sg.InputText(size = (10,20), key = 'eq2gc')],
        [sg.Button('Calcular', key = 'root2deg')],
    ]
    tab1_layout = [
        [sg.Text('Digite o coeficiente a: '), sg.InputText(size=(10,20), key = 'eq1ga')],
        [sg.Text('Digite o coeficiente b: '), sg.InputText(size=(10,20), key = 'eq1gb')],
        [sg.Button('Calcular', key = 'root1deg')],
    ]
    
    layout = [
        [sg.TabGroup([[sg.Tab('Calculadora de 1º grau', tab1_layout), sg.Tab('Calculadora de 2º grau', tab2_layout)]])],
        [sg.Cancel('Fechar')],
        [sg.Output( size = (40,9))],
    ]
    
    '''This block is for to define the window to be created, 
    including defining the of window with your name and layout.'''
    
    window = sg.Window('Calculadora de raizes', layout) #create a window
    
    
    #loop
    while True:
        event, value = window.read()
        if event == 'Fechar' or event == sg.WIN_CLOSED:
            break
        elif event == 'root1deg':
            try:
                print(root1deg(float(value['eq1ga']), float(value['eq1gb'])))#Necessário que não tenha as 3 linhas escritas na cacluladora de segundo grau
            except:
                print('Você deve colocar todas as variaveis')
        elif event == 'root2deg':
            try:
                resultado = root2deg(float(value['eq2ga']), float(value['eq2gb']), float(value['eq2gc']))
                print(f"x' = {resultado[0]}")
                print(f"x'' = {resultado[1]}")
                print(f'x do vertice = {resultado[2]}')
                print(f'y do vertice = {resultado[3]}')
                print(f'delta = {resultado[4]}')
                print(f'raiz de delta = {resultado[5]}')
                print()
            except:
                print('Você deve colocar todas as variaveis')
                
        
    return 0

#call main
if __name__ == '__main__':
    main()
