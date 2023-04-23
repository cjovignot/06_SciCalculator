#!/usr/bin/python3
from tkinter import *
import re
import math

window = Tk()

# DISPLAY CONFIG
# buttons
default_button_style = {
    "bg": "#595959", "fg": "white", "highlightthickness": 0,
    "font": ("Arial", 25, "bold"),
    "width": 3,
    "borderwidth": 2
}
equal_button_style = default_button_style | {
    "width": 3,
    "bg": "#f05a2D"
}
default_button_grid = {
    "sticky": "nsew"
}
close_button_style = default_button_style | {
    "width": 16,
    "bg": "#333333"
}
# window grid
window.configure(bg="#333333")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0, minsize=90)
window.rowconfigure(3, weight=0)
window.rowconfigure(4, weight=0)
window.rowconfigure(5, weight=0)
window.rowconfigure(6, weight=0)
window.columnconfigure(0, weight=1, uniform="same_group")
window.columnconfigure(1, weight=1, uniform="same_group")
window.columnconfigure(2, weight=1, uniform="same_group")
window.columnconfigure(3, weight=1, uniform="same_group")

calc_input = ""
calc_input_text = ""
result_text = ""
calculation = ""
string = ""



# INPUT
def input_key(value):
    global calc_input
    global string
    calc_input += value
    calc_input_text.set(calc_input)

# RESET FUNCTION
def reset():
    global calc_input
    calc_input = ""
    calc_input_text.set("")
    result_text.set("")

# TEMP FUNCTION
def defineInput():
    global calc_input
    global calculation
    calculation = calc_input
    print("string:", calculation)

    try:
        if "/0" in calculation:
            raise Exception("Division by zero forbidden")
    except Exception as e:
        print(e)
        exit(84)

    if "cos(" in calculation:
        cosinus()
    elif "sin(" in calculation:
        sinus()
    elif "tan(" in calculation:
        tan()
    elif "^" in calculation:
        exp()
    else:
        equal(calculation)

# COS FUNCTION
def cosinus():
    global calc_input
    if "cos(" in calculation:
        regex = r'(?<=cos\()\d+(?=\))'
        cos = re.search(regex, calculation)
        cos_result = math.cos(int(cos.group()))
        print("cos_result:", cos_result)
        result_text.set(cos_result)
        calc_input = str(cos_result)

# SIN FUNCTION
def sinus():
    global calc_input
    if "sin(" in calculation:
        print("sin:", calculation)
        regex = r'(?<=sin\()\d+(?=\))'
        sin = re.search(regex, calculation)
        sin_result = math.sin(int(sin.group()))
        print("sin:", sin_result)
        result_text.set(sin_result)
        calc_input = str(sin_result)

# TAN FUNCTION
def tan():
    global calc_input
    if "tan(" in calculation:
        print("tan:", calculation)
        regex = r'(?<=tan\()\d+(?=\))'
        tan = re.search(regex, calculation)
        tan_result = math.tan(int(tan.group()))
        print(calculation,":", tan_result)
        result_text.set(tan_result)
        calc_input = str(tan_result)

# EXPONENTIAL
def exp():
    global calc_input
    if "^" in calculation:
        print("exp:", calculation)

        regex = r"(\d+)\^(\d+)"
        exp = re.match(regex, calculation)
        if regex:
            base = int(exp.group(1))
            exponent = int(exp.group(2))
            exp_result = base ** exponent
            print(calculation,":", exp_result)
            result_text.set(exp_result)
            calc_input = str(exp_result)

# EQUAL FUNCTION
def equal(calculation):
    global calc_input
    global calc_input_text
    inner = []

    if calculation[0] == '-':
        calculation = '0' + calculation

    # Replace '+-' or '-+' with '-'
    pattern1 = r"[+-]-|[+-]-"
    calculation = re.sub(pattern1, "-", calculation)
    # Replace '--' with '-'
    pattern2 = r"--"
    calculation = re.sub(pattern2, "-", calculation)
    # Replace '++' with '+'
    pattern3 = r"\+\+"
    calculation = re.sub(pattern3, "+", calculation)
    # "*-" case
    if "*-" in calculation:
        calculation = '-{}*{}'.format(calculation[3:], calculation[0])


    print("signs solved", calculation)

    if "cos(" in calculation:
        cosinus()
    elif "sin(" in calculation:
        sinus()
    elif "tan(" in calculation:
        tan()
    elif "^" in calculation:
        exp()

    elif "(" in calculation:

        regex = r"\(([^\(\)]+)\)"
        match = re.search(regex, calculation)
        if match:
            print("to calculate:", match.group(1))
            inner = match.group(1)

    else:
        # "*-" case
        if "*-" in calculation:
            calculation = '-{}*{}'.format(calc_input[3:], calc_input[0])
        inner = calculation

    array = re.split('(\W)', inner)


    while len(array)>1:
            
        if "*" in array or "/" in array:
            for i in range(len(array)):
                if array[i] == "*":
                    array[i] = int(array[i-1])*int(array[i+1])
                    array.pop(i-1)
                    array.pop(i)
                    calc_input_text.set(array)
                    print("***", array)
                    if array[0] == "" and array[1] == "-":
                        array = ''.join(str(i) for i in array).strip()
                        print(array)

                    calc_input_text.set(array)
                    break
                elif array[i] == "/":
                    array[i] = int(array[i-1])/int(array[i+1])
                    array.pop(i-1)
                    array.pop(i)
                    print("///", array)
                    calc_input_text.set(array)
                    
                    calc_input_text.set(array)
                    break
        else: 
            for i in range(len(array)):
                if array[i] == "+":
                    array[i] = int(array[i-1])+int(array[i+1])
                    array.pop(i-1)
                    array.pop(i)
                    print("+++", array)

                    calc_input_text.set(array)
                    break
                elif array[i] == "-":
                    array[i] = int(array[i-1])-int(array[i+1])
                    array.pop(i-1)
                    array.pop(i)
                    calc_input_text.set(array)
                    print("---", array)

                    calc_input_text.set(array)
                    break

    regex = r"\(([^\(\)]+)\)"
    match = re.search(regex, calc_input)
    print("last check:", calc_input)
    if match:
        print("result:", array[0])
        inner = match.group(1)
        calc_input = calc_input.replace('({})'.format(inner), str(array[0]))
        equal(calc_input)
    else:
        print("final result:", array[0])
        calc_input = str(array[0])
        result_text.set(array[0])



# BUTTONS
# ROW 0
Button(window, text="Fermer", command=window.quit, **close_button_style).grid(row=0, column=0, columnspan=4)

# ROW 1
calc_input_text = StringVar()
Label(window, textvariable=calc_input_text, anchor='e',
                        bg="#a2af77", fg="black", font=("Arial", 25)).grid(column=0, row=1, columnspan=4, **default_button_grid)

# ROW 2
result_text = StringVar()
Label(window, textvariable=result_text, anchor='e',
                        bg="#a2af77", fg="black", font=("Arial", 30, "bold")).grid(column=0, row=2, columnspan=4, **default_button_grid)

# ROW 3
Button(window, text=" sin ", command=lambda: input_key("sin("), **default_button_style).grid(row=3, column=0)
Button(window, text=" cos ", command=lambda: input_key("cos("), **default_button_style).grid(row=3, column=1)
Button(window, text=" tan ", command=lambda: input_key("tan("), **default_button_style).grid(row=3, column=2)
Button(window, text=" ^ ", command=lambda: input_key("^"), **default_button_style).grid(row=3, column=3)

# ROW 4
Button(window, text="   ", command=lambda: input_key(""), **default_button_style).grid(row=4, column=0)
Button(window, text=" ( ", command=lambda: input_key("("), **default_button_style).grid(row=4, column=1)
Button(window, text=" ) ", command=lambda: input_key(")"), **default_button_style).grid(row=4, column=2)
Button(window, text=" / ", command=lambda: input_key("/"), **default_button_style).grid(row=4, column=3)

# ROW 5
Button(window, text=" 7 ", command=lambda: input_key("7"), **default_button_style).grid(row=5, column=0)
Button(window, text=" 8 ", command=lambda: input_key("8"), **default_button_style).grid(row=5, column=1)
Button(window, text=" 9 ", command=lambda: input_key("9"), **default_button_style).grid(row=5, column=2)
Button(window, text=" * ", command=lambda: input_key("*"), **default_button_style).grid(row=5, column=3)

# ROW 6
Button(window, text=" 4 ", command=lambda: input_key("4"), **default_button_style).grid(row=6, column=0)
Button(window, text=" 5 ", command=lambda: input_key("5"), **default_button_style).grid(row=6, column=1)
Button(window, text=" 6 ", command=lambda: input_key("6"), **default_button_style).grid(row=6, column=2)
Button(window, text=" - ", command=lambda: input_key("-"), **default_button_style).grid(row=6, column=3)

# ROW 7
Button(window, text=" 1 ", command=lambda: input_key("1"), **default_button_style).grid(row=7, column=0)
Button(window, text=" 2 ", command=lambda: input_key("2"), **default_button_style).grid(row=7, column=1)
Button(window, text=" 3 ", command=lambda: input_key("3"), **default_button_style).grid(row=7, column=2)
Button(window, text=" + ", command=lambda: input_key("+"), **default_button_style).grid(row=7, column=3)

# ROW 8
Button(window, text=" 0 ", command=lambda: input_key("0"), **default_button_style).grid(row=8, column=0)
Button(window, text=" . ", command=lambda: input_key("."), **default_button_style).grid(row=8, column=1)
Button(window, text=" C ", command=lambda: reset(), **default_button_style).grid(row=8, column=2)
Button(window, text=" = ", command=lambda: defineInput(), **equal_button_style).grid(row=8, column=3)

# ROW 9


window.mainloop()