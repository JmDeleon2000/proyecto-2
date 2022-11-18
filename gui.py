
import PySimpleGUI as sg
import os.path
from PIL import Image


# im1 = Image.open("./example.jpg")

# im1.show()
color_base= '#2776c1'
color_fondo_secundario= '#70a7db'
color_secundario= '#fb8300'


layout1 = [
	[
	sg.Text("Seleccionar Imagen"),
	sg.In(size = (21,1), enable_events=True, key="-FOLDER-" ,background_color=color_fondo_secundario),
	sg.FolderBrowse(),


	],
	[
		sg.Listbox(
				values = [] , enable_events=True, size =(40,20),
				key="-FILE_LIST-"
			)

	],
	
]

layout2 = [
	[sg.Text("Seleccionar el modelo")],
	[sg.Image(key="-IMAGE-")],
	[sg.Button("Classify")]


	]	

layout = [
	[
		sg.Column(layout1),
		sg.VSeparator(),
		sg.Column(layout2)

	]


]

mywindow = sg.Window(title="Classifier", layout=layout, margins=(100,50) , background_color=color_base)

while True:
	event, values = mywindow.read()

	if event == "Classify" :
		print("Boton presionado")

	if event == sg.WIN_CLOSED:
		break

	if event == "-FOLDER-":
		folder = values ["-FOLDER-"]
		try:
			file_list = os.listdir(folder)
		except:
			file_list= []

		fnames = [
			f 
			for f in file_list
			if os.path.isfile(os.path.join(folder ,f)) and f.lower().endswith((".png",".gif"))
		]
		mywindow["-FILE_LIST-"].update(fnames)
	if event =="-FILE_LIST-":
		try:
			filename=os.path.join (values["-FOLDER-"], values["-FILE_LIST-"][0])
			mywindow["-IMAGE-"].update(filename=filename)
		except:
			pass



mywindow.close()