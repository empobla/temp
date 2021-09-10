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

def Frame4():
    t0 = sg.Text("Según las estadísticas que proporciona el gobierno de México, tenemos las siguientes cifras:")
    t1 = sg.Text("Personas confirmadas: 3,465,171 acumulados")
    t2 = sg.Text("Positivos estimados: 3,677,152")
    t3 = sg.Text("Negativos: 6,097,127 acumulados")
    t4 = sg.Text("Sospechosos: 502,142 acumulados")
    t5 = sg.Text("Defunciones: 265,420 acumulados")
    t6 = sg.Text("Defunciones estimadas: 278,592")
    t7 = sg.Text("Recuperado: 2,809,029 acumulados")
    t8 = sg.Text("Activos: 88,964 acumulados")
    t9 = sg.Text("Activos estimados: 97,611")
    b4 = sg.Button("Continuar", key="B4")
    layout = [[t0],[t1],[t2],[t3],[t4],[t5],[t6],[t7],[t8],[t9],[b4]]
    frame = sg.Frame("Cifras", layout, visible=False, key="F4")
    return frame

def Frame5():
    t0 = sg.Text("Nombre")
    i0 = sg.Input(key="NAME")
    t1 = sg.Text("Edad")
    i1 = sg.Input(key="AGE")
    t2 = sg.Text("Sexo")
    i2 = sg.Input(key="SEX")
    t3 = sg.Text("Ciudad")
    i3 = sg.Input(key="CITY")
    b5 = sg.Button("Continuar", key="B5")
    layout = [[t0, i0],[t1, i1],[t2, i2],[t3, i3],[b5]]
    frame = sg.Frame("Datos Personales", layout, visible=False, key="F5")
    return frame

def Frame6():
    t0 = sg.Text("¿Haz tenido COVID-19?")
    i0 = sg.Input(key="HADCOVID")
    t1 = sg.Text("¿Haz tendio contacto con alguien recientemente postivo de covid?")
    i1 = sg.Input(key="SAWCOVID")
    t2 = sg.Text("¿Ya te vacunaste?")
    i2 = sg.Input(key="VACCINATED")
    t3 = sg.Text("¿Primera dosis o segunda dosis?")
    i3 = sg.Input(key="DOSES")
    t4 = sg.Text("¿Que vacuna te fue adminstradas?")
    i4 = sg.Input(key="BRAND")
    b6 = sg.Button("Continuar", key="B6")
    layout = [[t0, i0],[t1, i1],[t2, i2],[t3, i3],[t4, i4],[b6]]
    frame = sg.Frame("Encuesta", layout, visible=False, key="F6")
    return frame
    

if __name__ == "__main__":
    sg.theme("Dark Blue 12")

    fr0 = Frame0()
    fr1 = Frame1()
    fr2 = Frame2()
    fr3 = Frame3()
    fr4 = Frame4()
    fr5 = Frame5()
    fr6 = Frame6()

    layout = [[fr0, fr1, fr2, fr3, fr4, fr5, fr6]]

    window = sg.Window("COVID 19 en México", layout, grab_anywhere=True, resizable=True)

    i=0
    name = ''
    age = ''
    sex = ''
    city = ''
    hadcovid = ''
    contactcovid = ''
    vaccinated = ''
    numdoses = ''
    brandvaccine = ''
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
        
        if event == "B3":
            window["F3"].update(visible = False)
            window["F4"].update(visible = True)
        
        if event == "B4":
            window["F4"].update(visible = False)
            window["F5"].update(visible = True)

        if event == "B5":
            name = values["NAME"]
            age = values["AGE"]
            sex = values["SEX"]
            city = values["CITY"]
            window["F5"].update(visible = False)
            window["F6"].update(visible = True)
        
        if event == "B6":
            hadcovid = values["HADCOVID"]
            contactcovid = values["SAWCOVID"]
            vaccinated = values["VACCINATED"]
            numdoses = values["DOSES"]
            brandvaccine = values["BRAND"]
            window["F6"].update(visible = False)
            sg.popup("Gracias por tu tiempo!")
            break

    with open('datos.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Nombre', 'Edad', 'Sexo', 'Ciudad', 'TuvoCovid', 'ContactoCovid', 'Vacunado', 'Dosis', 'Marca'])
        writer.writerow([name, age, sex, city, hadcovid, contactcovid, vaccinated, numdoses, brandvaccine])