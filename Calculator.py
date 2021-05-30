import PySimpleGUI as sg

sg.theme('DarkBlue9')
#sg.theme_previewer() # uncomment for setting color scheme

start_input = "0"

def button(button_text):
    return sg.Button(button_text, size=(5, 1), font=("Helvetica", 20))

layout =[[sg.Text("Result:"), sg.Text(size=(15,1), key="-OUTPUT-")],
        [sg.InputText(key=("-INPUT-"))],
        [button(t) for t in ("7","8","9","/")],
        [button(t) for t in ("4","5","6","*")],
        [button(t) for t in ("1","2","3","-")],
        [button(t) for t in ("0","C","=","+")]]
         

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
            elif operation == "-":
                final_number = (float(first_number)-float(second_number))
            elif operation == "*":
                final_number = (float(first_number)*float(second_number))
            elif operation == "/":
                final_number = (float(first_number)/float(second_number))

            first_number = final_number
            second_number = 0
            operation = operation2
            operation2 = ""
    
    
    if event.isnumeric() == True:
        if not operation == "" and second_number == 0:
            second_number = event
        elif not operation == "" and eventbefore.isnumeric() == True:
            second_number = second_number + event
        elif first_number == 0:
            first_number = event
        elif not first_number == 0 and operation == "":
            first_number = first_number + event
        if not operation == "":
            window["-OUTPUT-"].update(second_number)
        else:
            window["-OUTPUT-"].update(first_number)

        
    if event == "+" or event =="-" or event =="*" or event=="/" and operation == "":
        window["-OUTPUT-"].update(event)
        operation = event
    elif event == "+" or event =="-" or event =="*" or event=="/" and not operation == "":
        if second_number == 0:
            window["-OUTPUT-"].update(event)
            operation = event
                                                                                           
    if event == "=":
        if operation == "+":
            final_number =(float(first_number)+float(second_number))
        elif operation == "-":
            final_number = (float(first_number)-float(second_number))
        elif operation == "*":
            final_number = (float(first_number)*float(second_number))
        elif operation == "/":
            final_number = (float(first_number)/float(second_number))
        window["-OUTPUT-"].update(final_number)
        operation = ""
        first_number = final_number
        second_number = 0
        final_number = 0

   
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

    eventbefore = event


window.close()


