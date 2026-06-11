# Import required libraries
import tkinter as tk
from tkinter import messagebox, ttk
import random, string

# Function to generate a password based on selected criteria
def generate_password():
    # Fetch user-selected options and password length
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    # Ensure at least one character type is selected
    if not(include_upper or include_lower or  include_numbers or include_symbols):
        messagebox.showwarning(
            "Selection Error",
            "Please select at least one character type"
        )
        return
    # Build the character pool based on selected options
    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation
        
    # Generate a ramdom password from pool
    password = "".join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    update_strength_indicator(password)

# Function  to update the password strength indicator
def update_strength_indicator(password):
    strength = calculate_strength(password)
    # Update the label color and text based on strength
    if strength == 'Weak':
        strength_label.config(
            text='Strength: Weak',
            foreground='#e53935'
        )
    elif strength == 'Moderate':      
        strength_label.config(
            text='Strength: Moderate',
            foreground='#E59935'
        )
    elif strength == 'Strong':      
        strength_label.config(
            text='Strength: Strong',
            foreground='#087A19'
        )
        
#Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    # Assign a score based on character diversity
    score = sum([has_upper,
                has_lower,
                has_digit,
                has_symbol
                ])
    
    # Return strength based on length and diversity
    if length >= 12 and score == 4:
        return 'Strong'
    elif length >= 8 and score >= 3:
        return 'Moderate'
    else:
        return 'Weak'
    
# Function to toogle password visibility
def toogle_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toogle_btn.config(text='Show')
    else:
        password_entry.config(show='')
        toogle_btn.config(text='Hide')
        
# Function to update the slider value dynamically
def update_slider_label(event):
    slider_label.config(text=f'Length: {length_var.get()}')
    
# Function to hover effects for buttons
def on_button_hover(event, button):
    button.config(bg='#FCBE05')
    
# Function on button hover
def on_button_leave(event, button):
    button.config(bg='#C1068F')
    
# Main application window setup
root = tk.Tk()
root.title('PassGenPro 1.0.1')
root.geometry('450x550')
root.resizable(False, False) #It depends, you can make it True to resize
root.configure(bg='#FCBE05')

# Initialize variables for user preferences

length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# Setup header section
header_label = tk.Label(
    root,
    text='GenPassPro for secure password',
    font=("Ubuntu", 18, 'bold'),
    bg="#FCBE05",
    fg="#A90779"
)
header_label.pack(pady=15)

# Frame for content
frame = ttk.Frame(root, padding="15")
frame.pack(fill="both", expand=True)

# Password length slider
ttk.Label(
    frame,
    text='Password Length:',
    font=("Ubuntu", 12)
).pack(anchor='w')

length_slider = ttk.Scale(
    frame,
    from_=4,
    to=32,
    variable=length_var,
    orient="horizontal",
    command=update_slider_label,   
)
length_slider.pack(fill='x', pady=5)

slider_label = ttk.Label(
    frame,
    text=f'Length: {length_var.get()}',
    font=("Ubuntu", 10)
)
slider_label.pack()

# Options section with checkboxes
options_frame = ttk.LabelFrame(
    frame,
    text='Options',
    padding="10"   
)

options_frame.pack(fill='x', pady=10)
upper_check = ttk.Checkbutton(
    options_frame,
    text='Include Uppercase Letters',
    variable=upper_var    
)

upper_check.pack(anchor='w')

# Copy the above and modify for remaining check options
lower_check = ttk.Checkbutton(
    options_frame,
    text='Include Lowercase Letters',
    variable=lower_var    
)

lower_check.pack(anchor='w')

numbers_check = ttk.Checkbutton(
    options_frame,
    text='Include Numbers',
    variable=numbers_var  
)

numbers_check.pack(anchor='w')

symbols_check = ttk.Checkbutton(
    options_frame,
    text='Include Special Symbols',
    variable=symbols_var    
)

symbols_check.pack(anchor='w')

# Password entry field
password_label = ttk.Label(
    frame,
    text='Generated Password:',
    font=("Ubuntu", 12)
)
password_label.pack(anchor='w', pady=5)
password_entry = ttk.Entry(
    frame,
    font=("Ubuntu", 12),
    justify='center'
)
password_entry.pack(fill='x', pady=10, ipady=5)

# Buttons for generation and toggling
button_frame = ttk.Frame(frame)
button_frame.pack(fill='x', pady=10)

generate_btn = tk.Button(
    frame,
    text='Generate Password',
    command=generate_password,
    bg='#920664',
    fg='#FFFFFF',
    font=("Ubuntu", 10),
    relief = 'groove'
)
generate_btn.pack(side='left', padx=5)

generate_btn.bind('<Enter>', lambda e: on_button_hover(e, generate_btn))
generate_btn.bind('<Leave>', lambda e: on_button_leave(e, generate_btn))

toogle_btn = tk.Button(
    button_frame,
    text='Hide',
    command=toogle_visibility,
    bg='#920664',
    fg='#ffffff',
    font=("Ubuntu", 10),
    relief = 'groove'
)
toogle_btn.pack(side='left', padx=5)
toogle_btn.bind('<Enter>', lambda e: on_button_hover(e, toogle_btn))
toogle_btn.bind('<Leave>', lambda e: on_button_leave(e, toogle_btn))

# Password strength indicator
strength_label = ttk.Label(
    frame,
    text='Strength: Weak',
    font=("Ubuntu", 12)
)
strength_label.pack(pady=10)

# Footer Section
footer_label = tk.Label(
    root,
    text='Created by: f.Ebrottie',
    font=('Ubuntu', 11),
    bg='#FFC505',
    fg='#4D0333'
)
footer_label.pack(padx=5)

# Run Application

if __name__ == '__main__':
    root.mainloop()