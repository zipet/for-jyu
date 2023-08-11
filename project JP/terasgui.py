import PySimpleGUI as sg
from equations import *
from equations import *
from properties import *

sg.theme('SandyBeach')

valueColumn = [
    [sg.Text("Arvot: ")],
    [sg.Text("Massa"), sg.In(size=(9, 1), enable_events=True, key="-MASS-")],
    [sg.Text("Varmuuskerroin"), sg.In(size=(9, 1), enable_events=True, key="-SAFETY-")],
    [sg.Text("Koko pituus"), sg.In(size=(9, 1), enable_events=True, key="-LENGTH-")],
    [sg.Text("Montako voimaa?: "), sg.In(size=(9, 1), enable_events=True, key="-FX_X-")],
    [sg.Text("fx_1"), sg.In(size=(9, 1))],
    # [sg.Text("fx_'juokseva numero'"), sg.In(size=(9, 1))],
    # [sg.Text("fx_'juokseva numero'"), sg.In(size=(9, 1))],
    [sg.Button('Päivitä voimat', enable_events=True, key="-UPFORCE-")],
    [sg.Button("Poistu", enable_events=True, key="-EXIT-"), sg.Button("laske", enable_events=True, key="-CALC-")]
]

drawColumn = [
    [sg.Text("piirtoikkuna.")],
    [sg.Graph(
        canvas_size=(700, 300),
        graph_bottom_left=(0, 0),
        graph_top_right=(100, 50),
        background_color="lightblue"
    )],
    [sg.Text("Tähän tulisi kaavoja/vastauksia/arvoja mitälie olisi hyvä olla"), sg.Multiline("Tulos: ", key="-ANSWER-",size=(45,5))]
]

layout = [
    [
        sg.Column(valueColumn),
        sg.VSeparator(),
        sg.Column(drawColumn)
    ]
]

window = sg.Window("Teräspalkkiperkele", layout)

while True:
    event, values = window.read()
    if event == "-EXIT-" or event == sg.WIN_CLOSED:
        break
    if event == "-CALC-":
        mass = int(values["-MASS-"])
        varmuus = int(values["-SAFETY-"])
        kok_pituus = int(values["-LENGTH-"])
        voimia = int(values["-FX_X-"])
        if voimia > 1:
            count = 2 
            for i in range(voimia):
                valueColumn.append([[sg.Text(f"fx_{count}"), sg.In(size=(9, 1), key=f"-FX_{count}")]])
                count += 1
        _fxdict = setFx_x(voimia)
        addFx_x(**_fxdict)
        calcVoimaF = voimaF(mass, grav, varmuus)
        calcVoimaB = voimaB(kok_pituus, _fxdict["fx_1"], calcVoimaF)
        # print(f"voimaF = {calcVoimaF}")
        # print(f"voimaB = {calcVoimaB}")
        window["-ANSWER-"].print(f"voimaF = {calcVoimaF}") # kuinka tulostaa output asioille. window[Multiline element key].print()
        window["-ANSWER-"].print(f"voimaB = {calcVoimaB}")
        for k, v in _fxdict.items():
            window["-ANSWER-"].print(k,v)
    if event == "-UPFORCE-":
        voimia = int(values["-FX_X-"])
        if voimia > 1:
            count = 2 
            for i in range(voimia):
                valueColumn.append([[sg.Text(f"fx_{count}"), sg.In(size=(9, 1), key=f"-FX_{count}")]])
                # window[valueColumn].update(f"-FX_X{count}")
                count += 1
        
        # window['-TEXT-'].update('My new text value') TODO: update key täysin oma column, funktion sisään?
window.close()