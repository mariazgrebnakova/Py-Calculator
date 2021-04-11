import PySimpleGUI as sg

start_input = "0"
layout = [[sg.Text("Result:"), sg.Text(size=(15,1), key="-OUTPUT-")],[sg.Input(start_input)],
          [sg.Button("CLOSE"), sg.Button("1"),sg.Button("2"),sg.Button("3"),sg.Button("4"),sg.Button("5"),
                                                sg.Button("6"),sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("0"), sg.Button("+"),
                                                sg.Button("-"),sg.Button("*"),sg.Button("/"),sg.Button("="), sg.Button("C")]]

# Create the window
window = sg.Window("Calculator", layout, margins=(100,100))

x = 0
y = 0
operation = ""

# Create an event loop
while True:
    event, values = window.read()
    if event.isnumeric() == True:
        if not operation == "":
            y = event
            print (y)
        else:
            x = event
            print (x)
        window["-OUTPUT-"].update(event)

        
    if event == "+" or event =="-" or event =="*" or event=="/":
        window["-OUTPUT-"].update(event)
        operation = event
        print(operation)
        
    
    if event == "=":
        if operation == "+":
            window["-OUTPUT-"].update(int(x)+int(y))
            print (int(x)+int(y))
        elif operation == "-":
            window["-OUTPUT-"].update(int(x)-int(y))
            print (int(x)-int(y))
        elif operation == "*":
            window["-OUTPUT-"].update(int(x)*int(y))
            print (int(x)*int(y))
        elif operation == "/":
            window["-OUTPUT-"].update(float(x)/float(y))
            print (float(x)/float(y))
        operation = ""

    if event == "C":
        x = 0
        y = 0
        operation = ""
        window["-OUTPUT-"].update(start_input)

        
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break


window.close()


