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
            [sg.Text("Chose file first", key="_Text_lable_"), sg.Combo(key= "_ComboBox_", values=l)],
            [sg.Text("Select a column to copy: "), sg.InputText(key="_Column_", size=(10,1)), sg.Button('Copy columns')]
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
            window["_Text_lable_"].Update("Choose file first", text_color="red")
        else:
            print("Folder and file choose:",values["_File_name_"])             
            window["_Text_lable_"].Update("you choosed file")
            log_file = open(values["_File_name_"], "r")
            print(log_file.read())
    elif event == "Copy columns":
        if values["_ComboBox_"] == "":
            print("Choose column first")
        elif values["_Column_"] == "":
            print("Enter a column number")
            window["_Text_lable_"].update("Enter a column number", text_color="red")
        else:
            column_num = int(values["_Column_"]) - 1 # selected columns
            with open("C:\\Users\\Yarik\\Documents\\GitHub\\first_repository\Resault\\test.txt", "w") as output_file:
                with open(values["_File_name_"], "r") as input_file:
                    for line in input_file:
                        columns = line.split()
                        if len(columns) > column_num:
                            output_file.write(columns[column_num] + "\n")
    print("Column copied to output.txt")
    window["_Text_lable_"].update("Column copied to file", text_color="green")
window.close()
