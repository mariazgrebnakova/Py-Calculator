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

operations = ["+", "-", "*", "/"]

def calculate_result (f_operation, f_first_number, f_second_number):
    result = 0
    f_first_number = float(f_first_number)
    f_second_number = float(f_second_number)
    if f_operation == "+":
        result = (f_first_number + f_second_number)
    elif operation == "-":
        result = (f_first_number - f_second_number)
    elif operation == "*":
        result = (f_first_number * f_second_number)
    elif operation == "/":
        result = (f_first_number / f_second_number)

    return result

# Create an event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # reset state
    if (event.isnumeric() == True and eventbefore == "=") or event == "C":
        first_number = 0
        second_number = 0
        operation = ""
        window["-OUTPUT-"].update(start_input)

    # handle operation buttons
    if event in operations:
        if not operation == "" and not second_number == 0:
            operation2 = event

            final_number = calculate_result(operation, first_number, second_number)
            first_number = final_number
            second_number = 0
            operation = operation2
            operation2 = ""
    
    # handle numeric buttons
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

    # handle operation buttons
    if (event in operations) and operation == "":
        window["-OUTPUT-"].update(event)
        operation = event
    elif (event in operations) and not operation == "":
        if second_number == 0:
            window["-OUTPUT-"].update(event)
            operation = event

    # handle equals button
    if event == "=":
        final_number = calculate_result(operation, first_number, second_number)
        window["-OUTPUT-"].update(final_number)
        operation = ""
        first_number = final_number
        second_number = 0
        final_number = 0

    eventbefore = event


window.close()


