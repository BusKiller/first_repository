# test project 1th. Writing values to file  
import PySimpleGUI as sg
import os
working_directory = os.getcwd()
sg.theme('DarkGrey1')   # Add a touch of color
# All the stuff inside your window.
l = []
l.append("1 values")
l.append("2 values")
l.append("3 values")
l.append("4 values")
layout = [  [sg.Text("File: "),sg.InputText(key = "_File_name_", default_text= "Choose file"),  sg.FileBrowse(initial_folder=working_directory, file_types = [("TXT Files", "*.txt")])],
            [sg.Button("Open file")],
            [sg.Text("Chose file first", key="_Text_lable_"), sg.Combo(key= "_ComboBox_", values=l)]
            ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    elif event == "Open file":
        if values["_File_name_"] == "Choose file":
            print("Choose file first")
            window["_Text_lable_"].TextColor = "red"
            window["_Text_lable_"].Update()
        else:
            print("Folder and file choose:",values["_File_name_"])             
            window["_Text_lable_"].Update("you choosed file")
            log_file = open(values["_File_name_"], "r")
            print(log_file.read())
window.close()
