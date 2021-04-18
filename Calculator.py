import PySimpleGUI as sg

start_input = "0"
layout = [[sg.Text("Result:"), sg.Text(size=(15,1), key="-OUTPUT-")],[sg.Input(start_input)],
          [sg.Button("CLOSE"), sg.Button("1"),sg.Button("2"),sg.Button("3"),sg.Button("4"),sg.Button("5"),
                                                sg.Button("6"),sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("0"), sg.Button("+"),
                                                sg.Button("-"),sg.Button("*"),sg.Button("/"),sg.Button("="), sg.Button("C")]]

# Create the window
window = sg.Window("Calculator", layout, margins=(100,100))

first_number = 0
second_number = 0
final_number = 0
operation = ""
operation2 = ""
eventbefore = ""

# Create an event loop
while True:
    event, values = window.read()
    
    if event.isnumeric() == True and eventbefore == "=" or event == "C":
        first_number = 0
        second_number = 0
        operation = ""
        window["-OUTPUT-"].update(start_input)

    if event == "+" or event =="-" or event =="*" or event=="/" :
        if not operation == "" and not second_number == 0:
            operation2 = event
        
            if operation == "+":
                window["-OUTPUT-"].update(float(first_number)+float(second_number))
                final_number =(float(first_number)+float(second_number))
                print (final_number)
            elif operation == "-":
                final_number = (float(first_number)-float(second_number))
            elif operation == "*":
                final_number = (float(first_number)*float(second_number))
            elif operation == "/":
                final_number = (float(first_number)/float(second_number))

            print (final_number)

            first_number = final_number
            second_number = 0
            operation = operation2
            operation2 = ""
    
    
    if event.isnumeric() == True:
        if not operation == "" and second_number == 0:
            second_number = event
            print (second_number)
        elif not operation == "" and eventbefore.isnumeric() == True:
            second_number = second_number + event
            print (second_number)
        elif first_number == 0:
            first_number = event
            print (first_number)
        elif not first_number == 0 and operation == "":
            first_number = first_number + event
            print (first_number)
        if not operation == "":
            window["-OUTPUT-"].update(second_number)
        else:
            window["-OUTPUT-"].update(first_number)

        
    if event == "+" or event =="-" or event =="*" or event=="/" and operation == "":
        window["-OUTPUT-"].update(event)
        operation = event
        print(operation)
    elif event == "+" or event =="-" or event =="*" or event=="/" and not operation == "":
        if second_number == 0:
            window["-OUTPUT-"].update(event)
            operation = event
            print(operation)

                                                                                           
    if event == "=":
        if operation == "+":
            final_number =(float(first_number)+float(second_number))
            print (final_number)
        elif operation == "-":
            final_number = (float(first_number)-float(second_number))
            print (final_number)
        elif operation == "*":
            final_number = (float(first_number)*float(second_number))
            print (final_number)
        elif operation == "/":
            final_number = (float(first_number)/float(second_number))
            print (final_number)
        window["-OUTPUT-"].update(final_number)
        operation = ""
        first_number = final_number
        second_number = 0
        final_number = 0

   
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

    eventbefore = event


window.close()


