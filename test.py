import tkinter

button_values = [               #listen 
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]  #listen sortiert
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
colum_count = len(button_values[0]) #4 

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white" 

window = tkinter.Tk() #create window
window.title("calculator")
window.resizable(False, False) #width and height 

frame = tkinter.Frame(window) #placing the frame inside the window
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, 
                      foreground=color_white, anchor="e", width=colum_count) #text from east (right) and not centered

label.grid(row=0, column=0, columnspan=colum_count, sticky="we") #columnspan -> how many columns this lable should take, colum_count = 4, so lable should take 4 columns
                                                    #sticky -> colour stretches from west to east (left,right) column

for row in range(row_count):
    for column in range(colum_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),  #set the button inside the frame 
                                 width=colum_count-1, height=1, 
                                 command=lambda value=value: button_clicked(value))

        if value in top_symbols: 
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row=row+1, column=column) #1 to shift row down by 1

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None 

def remove_zero_decimal(num):
    if num % 1 == 0: 
        num = int(num)
    return str(num)


def button_clicked(value): #define the action
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
       if value == "=":
           if A is not None  and A is not None:
               B = label["text"]
               numA = float(A)
               numB = float(B)

               if operator == "+":
                     label["text"] = remove_zero_decimal(numA + numB)
               elif operator == "-":
                     label["text"] = remove_zero_decimal(numA - numB)
               elif operator == "×":
                     label["text"] = remove_zero_decimal(numA * numB)
               elif operator == "÷":
                     label["text"] = remove_zero_decimal(numA / numB)
               clear_all()

       elif value in "+-×÷":
           if operator is None:
               A = label["text"]
               label["text"] = "0"
               B = "0"

           operator = value

    elif value in top_symbols: 
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else: #digits or .
        if value == ".":
             if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0": #0 replaced with 5, not 05, but just 5 
                label["text"] = value
            else:
                label["text"] += value


#center the window
window.update() 
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((window_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop() #window stays open


