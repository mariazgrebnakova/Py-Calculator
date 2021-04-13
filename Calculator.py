import PySimpleGUI as sg

start_input = "0"
layout = [[sg.Text("Result:"), sg.Text(size=(15,1), key="-OUTPUT-")],[sg.Input(start_input)],
          [sg.Button("CLOSE"), sg.Button("1"),sg.Button("2"),sg.Button("3"),sg.Button("4"),sg.Button("5"),
                                                sg.Button("6"),sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("0"), sg.Button("+"),
                                                sg.Button("-"),sg.Button("*"),sg.Button("/"),sg.Button("="), sg.Button("C")]]

# Create the window
window = sg.Window("Calculator", layout, margins=(100,100))

x = 0 #first number
y = 0 #second number
z = 0 #final number
operation = ""
operation2 = ""
eventbefore = ""

# Create an event loop
while True:
    event, values = window.read()
    
    if event == "+" or event =="-" or event =="*" or event=="/" :
        if not operation == "" and not y == 0:
            operation2 = event
        
            if operation == "+":
                window["-OUTPUT-"].update(float(x)+float(y))
                z =(float(x)+float(y))
                print (z)
            elif operation == "-":
                z = (float(x)-float(y))
            elif operation == "*":
                z = (float(x)*float(y))
            elif operation == "/":
                z = (float(x)/float(y))

            print (z)

            x = z
            y = 0
            operation = operation2
            operation2 = ""
    
    
    if event.isnumeric() == True:
        if not operation == "" and y == 0:
            y = event
            print (y)
        elif not operation == "" and eventbefore.isnumeric() == True:
            y = y + event
            print (y)
        elif x == 0:
            x = event
            print (x)
        elif not x == 0 and operation == "":
            x = x + event
            print (x)
        if not operation == "":
            window["-OUTPUT-"].update(y)
        else:
            window["-OUTPUT-"].update(x)

        
    if event == "+" or event =="-" or event =="*" or event=="/" and operation == "":
        window["-OUTPUT-"].update(event)
        operation = event
        print(operation)
    elif event == "+" or event =="-" or event =="*" or event=="/" and not operation == "":
        if y == 0:
            window["-OUTPUT-"].update(event)
            operation = event
            print(operation)
    
    if event == "=":
        if operation == "+":
            window["-OUTPUT-"].update(float(x)+float(y))
            z =(float(x)+float(y))
            print (z)
        elif operation == "-":
            window["-OUTPUT-"].update(float(x)-float(y))
            z = (float(x)-float(y))
            print (z)
        elif operation == "*":
            window["-OUTPUT-"].update(float(x)*float(y))
            z = (float(x)*float(y))
            print (z)
        elif operation == "/":
            window["-OUTPUT-"].update(float(x)/float(y))
            z = (float(x)/float(y))
            print (z)
        operation = ""
        x = z
        y = 0
        z = 0

    if event == "C":
        x = 0
        y = 0
        operation = ""
        window["-OUTPUT-"].update(start_input)

        
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

    eventbefore = event
    print (eventbefore)


window.close()


