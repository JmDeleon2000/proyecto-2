
import PySimpleGUI as sg
import os.path


layout = [
	[
	sg.Text("Seleccionar Imagen"),
	sg.In(size = (21,1), enable_events=True, key="-FOLDER-"),
	sg.FolderBrowse(),


	]
	
]


mywindow = sg.Window(title="Classifier", layout=layout, margins=(300,200))

while True:
	event, values = mywindow.read()

	if event == "Select" :
		print("Boton presionado")

	if event == sg.WIN_CLOSED:
		break
mywindow.close()