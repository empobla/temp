import PySimpleGUI as sg
import csv

def Frame0():
    t0 = sg.Text("Contraseña: ")
    i0 = sg.Input(password_char="*", key="PW")
    b0 = sg.Button("Ingresar", key="B0")
    layout = [[t0, i0], [b0]]
    frame = sg.Frame("Ingreso", layout, key="F0")
    return frame

def Frame1():
    t0 = sg.Text("El coronavirus SARS-Cov-2 es un virus que apareció en China. Después se extendió a todos los continentes del mundo provocando una pandemia. Actualmente Europa y América son los más afectados.")
    t1 = sg.Text("Este nuevo virus, provoca la enfermedad conocida con el nombre de COVID-19.")
    im0 = sg.Image(filename="images/covidmexico.png", key="IMG0")
    b1 = sg.Button("Continuar", key="B1")
    layout = [[t0],[t1], [im0],[b1]]
    frame = sg.Frame("¿Qué Es?", layout, visible=False, key="F1")
    return frame

def Frame2():
    t0 = sg.Text("*Tos y/o fiebre y/o dolor de cabeza.")
    t1 = sg.Text("*Y se acompaña de al menos uno de los siguientes: dolor o ardor de garganta, ojos rojos, dolores en músculos o articulaciones (malestar general).")
    t2 = sg.Text("*Los casos más graves tienen dificultades para respirar o falta de aire en sus pulmones.")
    b2 = sg.Button("Continuar", key="B2")
    layout = [[t0],[t1],[t2],[b2]]
    frame = sg.Frame("¿Cuáles son los síntomas?", layout, visible=False, key="F2")
    return frame

def Frame3():
    t0 = sg.Text("*Lavar las manos con jabón")
    t1 = sg.Text("*Mantener la sana distancia con las demás personas")
    t2 = sg.Text("*Al salir a calles usar el cubrebocas y evitar quitárselo")
    b3 = sg.Button("Continuar", key="B3")
    layout = [[t0],[t1],[t2],[b3]]
    frame = sg.Frame("¿Cómo prevenirlo?", layout, visible=False, key="F3")
    return frame

    

if __name__ == "__main__":
    sg.theme("Dark Blue 12")

    fr0 = Frame0()
    fr1 = Frame1()
    fr2 = Frame2()
    fr3 = Frame3()

    layout = [[fr0, fr1, fr2, fr3]]

    window = sg.Window("COVID 19 en México", layout, grab_anywhere=True, resizable=True)

    i=0
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == "B0":
            if values["PW"] != "password":
                sg.popup("Contraseña Incorrecta")
            else:
                sg.popup("Contraseña Correcta")
                window["F0"].update(visible = False)
                window["F1"].update(visible = True)
        
        if event == "B1":
            window["F1"].update(visible = False)
            window["F2"].update(visible = True)
        
        if event == "B2":
            window["F2"].update(visible = False)
            window["F3"].update(visible = True)