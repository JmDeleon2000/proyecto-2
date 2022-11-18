
import PySimpleGUI as sg
import os.path
from PIL import Image


# im1 = Image.open("./example.jpg")

# im1.show()
color_base= '#2776c1'
color_fondo_secundario= '#70a7db'
color_secundario= '#fb8300'
button1text= "Classify Using model 1"
button2text= "Classify Using model 2"
globalfile=""

layout1 = [
	[
	sg.Text("Seleccionar Imagen"),
	sg.In(size = (21,1), enable_events=True, key="-FILE-" ,background_color=color_fondo_secundario),
	# sg.FolderBrowse(),
	sg.FileBrowse(key="-FILE-"),

	],[sg.HSeparator()],
	[sg.Image(key="-IMAGE-")]
	
	
]

layout2 = [
	[sg.Text("Seleccionar el modelo")],
	# [sg.Text("Seleccionar el modelo" , key="filename")],
	[sg.Text("Modelo 1: 85% Accuracy")],
	[sg.Button(button1text)],
	[sg.Text("Modelo 2: 52% Accuracy")],
	[sg.Button(button2text)],

	[sg.Text("OUTPUT:")],
	[sg.Text("",key="-OUTPUT-")],




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

	if event == button1text:
		print("Boton 1 presionado")
		print("Enviare este file al modelo 1 : " +globalfile)
		mywindow["-OUTPUT-"].update("resultado del modelo1") 
	if event == button2text :
		print("Boton 2 presionado")
		print("Enviare este file al modelo 2 : " +globalfile)
		mywindow["-OUTPUT-"].update("resultado del modelo2") 


	if event == "-FILE-" :
		print("Se selecciono una archivo")
		file= values["-FILE-"]
		print(file)
		globalfile=file
		#mywindow["filename"].update(file)
		mywindow["-IMAGE-"].update(filename=file)



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
			filename = values["-FILE-"]
			#mywindow["filename"].update(filename)
			mywindow["-IMAGE-"].update(filename=filename)
		except:
			pass



mywindow.close()