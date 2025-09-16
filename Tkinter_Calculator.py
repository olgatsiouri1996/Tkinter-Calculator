#==============================#
#      Tkinter Calculator      #
#------------------------------#
#      Konstantinos Thanos     #
#      Mathematician, MSc      #
#      Olga Tsiouri, MSc       #
# Biochemist & Biotechnologist #
#==============================#

# Import packages
from tkinter import *
import math
'''
Functions
'''
# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Function to calculate the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    try:
        value = int(float(text_input.get()))
        result = str(factorial(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.sin(math.radians(value)))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

def trig_cos():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.cos(math.radians(value)))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

def trig_tan():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.tan(math.radians(value)))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

def trig_cot():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(1 / math.tan(math.radians(value)))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function to find the square root of a number
def square_root():
    global calc_operator
    try:
        value = float(text_input.get())
        if value < 0:
            text_input.set("ERROR")
        result = str(math.sqrt(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function to find the third root of a number
def third_root():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value ** (1/3))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function to change the sign of number
def sign_change():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(-value)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function to calculate the percentage of a number
def percent():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value / 100)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Funtion to find the result of an operation
def button_equal():
    global calc_operator
    try:
        expression = text_input.get()   # always use what's actually in the Entry
        result = str(eval(expression))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Fibonnaci for positive and negative integers
def fibo(n):
    if n == 0:
        return 0
    elif n > 0:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b
    else:  # negative n (Negafibonacci)
        a, b = 0, 1
        for _ in range(abs(n)-1):
            a, b = b, a + b
        return (-1)**(abs(n)+1) * b

# Function for fibonacci button that rounds non integers
def fibonacci():
    global calc_operator
    try:
        value = round(float(text_input.get()))
        result = str(fibo(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function for error function button
def erfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.erf(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Function for gamma function button
def gamma_func():
    global calc_operator
    try:
        value = float(text_input.get())
        if value <= 0 and value.is_integer():
            text_input.set("ERROR")
        result = str(math.gamma(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""


# Function for ln(gamma(x)) function button
def lgamma_func():
    global calc_operator
    try:
        value = float(text_input.get())
        if value <= 0 and value.is_integer():
            text_input.set("ERROR")
        result = str(math.lgamma(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# e^x function
def expfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.exp(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# ln(x) function
def lnfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        if value <= 0:
            text_input.set("ERROR")
        result = str(math.log(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# log2(x) function
def log2func():
    global calc_operator
    try:
        value = float(text_input.get())
        if value <= 0:
            text_input.set("ERROR")
        result = str(math.log2(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# log10(x) function
def log10func():
    global calc_operator
    try:
        value = float(text_input.get())
        if value <= 0:
            text_input.set("ERROR")
        result = str(math.log10(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan
e = math.e
p = math.pi
E = '*10**'

tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=6, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

'''
Buttons
'''
#--1st row--
# Absolute value of a number
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs(')).grid(row=1, column=0, sticky="nsew")
# Remainder of a division
modulo = Button(tk_calc, button_params, text='mod',
                command=lambda:button_click('%')).grid(row=1, column=1, sticky="nsew")
# Integer division quotient
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda:button_click('//')).grid(row=1, column=2, sticky="nsew")
# Factorial of a number
factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func).grid(row=1, column=3, sticky="nsew")
# Euler's number e
eulers_num = Button(tk_calc, button_params, text='e',
                    command=lambda:button_click(str(math.e))).grid(row=1, column=4, sticky="nsew")

#--2nd row--
# Sine of an angle in degrees
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=2, column=0, sticky="nsew")
# Cosine of an angle in degrees
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=2, column=1, sticky="nsew")
# Tangent of an angle in degrees
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=2, column=2, sticky="nsew")
# Cotangent of an angle in degrees
cotangent = Button(tk_calc, button_params, text='cot',
             command=trig_cot).grid(row=2, column=3, sticky="nsew")
# Pi(3.14...) number 
pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

#--3rd row--
# Power of 2
second_power = Button(tk_calc, button_params, text='x\u00B2',
             command=lambda:button_click('**2')).grid(row=3, column=0, sticky="nsew")
# Power of 3
third_power = Button(tk_calc, button_params, text='x\u00B3',
             command=lambda:button_click('**3')).grid(row=3, column=1, sticky="nsew")
# Power of n
nth_power = Button(tk_calc, button_params, text='x^n',
             command=lambda:button_click('**')).grid(row=3, column=2, sticky="nsew")
# Inverse number
inv_power = Button(tk_calc, button_params, text='x\u207b\xb9',
             command=lambda:button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
# Powers of 10
tens_powers = Button(tk_calc, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                     command=lambda:button_click('10**')).grid(row=3, column=4, sticky="nsew")

#--4th row--
# Square root of a number
square_root = Button(tk_calc, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=4, column=0, sticky="nsew")
# Third root of a number
third_root = Button(tk_calc, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=4, column=1, sticky="nsew")
# nth root of a number
nth_root = Button(tk_calc, button_params, text='\u221A',
                  command=lambda:button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
# Logarithm of a number with base 10
log_base10 = Button(tk_calc, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                   command=log10func).grid(row=4, column=3, sticky="nsew")
# Logarithm of a number with base e (ln)
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lnfunc).grid(row=4, column=4, sticky="nsew")

#--5th row--
# Add a left parentheses
left_par = Button(tk_calc, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=5, column=0, sticky="nsew")
# Add a right parentheses
right_par = Button(tk_calc, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=5, column=1, sticky="nsew")   
# Change the sign of a number
signs = Button(tk_calc, button_params, text='\u00B1',
               command=sign_change).grid(row=5, column=2, sticky="nsew")
# Transform number to percentage
percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=5, column=3, sticky="nsew")

# Logarithm of a number with base 10
log_base2 = Button(tk_calc, button_params, text='log\u2082', font=('sans-serif', 16, 'bold'),
                   command=log2func).grid(row=5, column=4, sticky="nsew")

#--6th row--
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")

#--7th row--
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")

#--8th row--
button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")

#--9th row--
button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")
exp = Button(tk_calc, button_params_main, text='EXP', font=('sans-serif', 16, 'bold'),
             command=lambda:button_click(E)).grid(row=9, column=2, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")

Fibo = Button(tk_calc, button_params_main, text='Fibo(x)', fg= '#db701f', bg= '#3C3636', font=('sans-serif', 15, 'bold'),
               command=fibonacci).grid(row=10, column=0, sticky="nsew")

erf = Button(tk_calc, button_params_main, text='erf(x)', fg= '#db701f', bg= '#3C3636', font=('sans-serif', 15, 'bold'),
               command=erfunc).grid(row=10, column=1, sticky="nsew")

# Calculate the function e^x
ex = Button(tk_calc, button_params, text='e^x', command=expfunc).grid(row=10, column=2, sticky="nsew")

gam = Button(tk_calc, button_params_main, text='gamma(x)', fg= '#db701f', bg= '#3C3636', font=('sans-serif', 15, 'bold'),
               command=gamma_func).grid(row=10, column=3, sticky="nsew")

lgam = Button(tk_calc, button_params_main, text='ln(gamma(x))', fg= '#db701f', bg= '#3C3636', font=('sans-serif', 15, 'bold'),
               command=lgamma_func).grid(row=10, column=4, sticky="nsew")


tk_calc.mainloop()
