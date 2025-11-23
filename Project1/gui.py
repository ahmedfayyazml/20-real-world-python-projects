import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in Todo")
input_text = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")
window = sg.Window("My Todo-App",layout=[[label],[input_text,add_button]])
window.read()
window.close()