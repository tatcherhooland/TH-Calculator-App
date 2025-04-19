# === CALCULATOR APPLICATION ===

# Import the required modules from tkinter for GUI creation
import tkinter as tk
from tkinter import StringVar

# Create the main window for the application
main_window = tk.Tk()

# Set up the size of the window to be 312x324 pixels
main_window.geometry('312x324')

# Set the title of the main window
main_window.title("Thatcher's Calculator")

# Global variables for storing the mathematical expression
expression = ""  # Keeps track of the current expression
input_text = StringVar()  # StringVar is used to update the input field

# Define function to handle the number/operation button clicks
def btn_click(item):
    global expression
    expression = expression + str(item)  # Add clicked item to the current expression
    input_text.set(expression)  # Update the input field with the new expression

# Define function to clear the input field and reset the expression
def btn_clear():
    global expression
    expression = ""  # Reset the expression
    input_text.set("")  # Clear the input

# Define function to evaluate the expression when the '=' button is clicked
def btn_equal():
    global expression
    try:
        # Evaluate the mathematical expression and update the input field with the result
        result = str(eval(expression))
        input_text.set(result)  # Display the result
        expression = ""  # Clear the expression after evaluation
    except:
        # In case of an error, display 'Error'
        input_text.set('Error')
        expression = ""  # Reset the expression

# Creating a frame to organize widgets (Top frame for input field)
input_frame = tk.Frame(main_window, width=312, height=50, bd=0, highlightbackground='black',
                       highlightcolor='black', highlightthickness=1)
input_frame.pack(side='top')  # Pack the frame to the top of the window

# Create an Entry widget (input field) within the input frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                       textvariable=input_text, width=50, bg="#eee", bd=0, justify='right')
input_field.grid(row=0, column=0)  # Position the input field in the frame
input_field.pack(ipady=10)  # Add padding inside the input field for better appearance

# Create another frame to hold the calculator buttons (Button frame)
btns_frame = tk.Frame(main_window, width=312, height=272.5, bg="grey")
btns_frame.pack()  # Pack the button frame below the input field

# The next part creates buttons for the calculator layout, starting with the first row:

# Create a 'Clear' button to clear the expression
btn_clearing = tk.Button(btns_frame, text="Clear", fg="Black", width=32, height=3, bd=0, bg="#eee",
                         cursor="hand2", command=btn_clear)
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)  # Position the 'Clear' button
# Create a 'Divide' button
btn_div = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                    cursor="hand2", command=lambda: btn_click("/"))
btn_div.grid(row=0, column=3, padx=1, pady=1)  # Position the division button

# The second row includes buttons for numbers 7, 8, 9, and the multiplication operator '*':
tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# The third row includes buttons for numbers 4, 5, 6, and the subtraction operator '-':
tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# The fourth row includes buttons for numbers 1, 2, 3, and the addition operator '+':
tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# The final (fifth) row includes buttons for '0', the decimal point ('.'), and the equal sign ('='):
tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff",
          cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)

# Start the main event loop to run the calculator
main_window.mainloop()
