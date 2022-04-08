import PySimpleGUI as sg

facesCount = 0

layout = [
    [sg.Text("Faces tracked: {}".format(facesCount))]
]

window = sg.Window("", layout)

while True:
    (event, values) = window.read()

    if event == sg.WIN_CLOSED:
        break

print("App closed!")
window.close()
