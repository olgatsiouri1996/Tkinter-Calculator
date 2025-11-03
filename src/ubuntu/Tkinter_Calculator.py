#==============================#
#      Tkinter Calculator      #
#------------------------------#
#      Konstantinos Thanos     #
#      Mathematician, MSc      #
#------------------------------#
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

def trig_sinh():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.sinh(math.radians(value)))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

def trig_cosh():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.cosh(math.radians(value)))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

def trig_tanh():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.tanh(math.radians(value)))
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

# degrees2radiant function
def radfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.radians(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# degrees2radiant function
def degfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.degrees(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# x^2 function
def squarefunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str((value)**2)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# x^3 function
def cubefunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str((value)**3)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# 1/x function
def invfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str((value)**(-1))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# 10^x function
def base10func():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(10**(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# 2^x function
def base2func():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(2**(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

#pi^x function
def basepifunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(math.pi**(value))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Celsius to Fahrenheit
def ctoffunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str((9/5)*value + 32)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Fahrenheit to Celsius
def ftocfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str((5/9)*(value - 32))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Celsius to Kelvin
def ctokfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value + 273.15)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Kelvin to Celsius
def ktocfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value - 273.15)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Fahrenheit to Kelvin
def ftokfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str((value + 459.67)*(5/9))
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Kelvin to Fahrenheit
def ktoffunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(((value*5)/9) - 459.67)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Meter to Feet
def mtoffunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value*3.2808399)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Feet to Meter
def ftomfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value/3.2808399)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Kg to Pounds
def ktopfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value*2.20462262)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# Pounds to Kg
def ptokfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value/2.20462262)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# ml to oz
def ozfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value*29.5735296)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# oz to ml
def mlfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value/29.5735296)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# cal to joule
def c2jfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value*4.184)
        text_input.set(result)
        calc_operator = result
    except Exception:
        text_input.set("ERROR")
        calc_operator = ""

# cal to joule
def j2cfunc():
    global calc_operator
    try:
        value = float(text_input.get())
        result = str(value/4.184)
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

text_display = Entry(tk_calc,  textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right', width= 80).grid(columnspan=10, padx = 20, pady = 20)

button_params = {'bd':2, 'fg':'#BBB', 'bg':'#3C3636'}
button_params_main = {'bd':2, 'fg':'#000', 'bg':'#BBB'}

'''
Buttons
'''
#--1st row--
# tau constant
tau_value = Button(tk_calc, button_params, text='tau',
                   command=lambda:button_click(str(math.tau))).grid(row=1, column=0, sticky="nsew")
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
# Sine of an angle in degrees
sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=1, column=5, sticky="nsew")
# Cosine of an angle in degrees
cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=1, column=6, sticky="nsew")
# Tangent of an angle in degrees
tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=1, column=7, sticky="nsew")
# Powers of 2
two_powers = Button(tk_calc, button_params, text='2^x', 
                     command=base2func).grid(row=1, column=8, sticky="nsew")
# Pi(3.10...) number 
pi_num = Button(tk_calc, button_params, text='pi',
                command=lambda:button_click(str(math.pi))).grid(row=1, column=9, sticky="nsew")

#--2nd row--
# Power of 2
second_power = Button(tk_calc, button_params, text='x^2',
             command=squarefunc).grid(row=2, column=0, sticky="nsew")
# Power of 3
third_power = Button(tk_calc, button_params, text='x^3',
             command=cubefunc).grid(row=2, column=1, sticky="nsew")
# Power of n
nth_power = Button(tk_calc, button_params, text='x^n',
             command=lambda:button_click('**')).grid(row=2, column=2, sticky="nsew")
# Inverse number
inv_power = Button(tk_calc, button_params, text='1/x',
             command=invfunc).grid(row=2, column=3, sticky="nsew")
# Powers of 10
tens_powers = Button(tk_calc, button_params, text='10^x', 
                     command=base10func).grid(row=2, column=4, sticky="nsew")
# Square root of a number
sq_root = Button(tk_calc, button_params, text='sqrt',
                     command=square_root).grid(row=2, column=5, sticky="nsew")
# Third root of a number
trd_root = Button(tk_calc, button_params, text='cbrt',
                    command=third_root).grid(row=2, column=6, sticky="nsew")
# nth root of a number
nth_root = Button(tk_calc, button_params, text='nthrt',
                  command=lambda:button_click('**(1/')).grid(row=2, column=7, sticky="nsew")
# Logarithm of a number with base 10
log_base10 = Button(tk_calc, button_params, text='log10', 
                   command=log10func).grid(row=2, column=8, sticky="nsew")
# Logarithm of a number with base e (ln)
log_basee = Button(tk_calc, button_params, text='ln',
                   command=lnfunc).grid(row=2, column=9, sticky="nsew")

#--3nd row--
# pi^x
pi_power = Button(tk_calc, button_params, text='pi^x',
                  command=basepifunc).grid(row=3, column=0, sticky="nsew")
# Golden ratio
golden_ratio = Button(tk_calc, button_params, text='phi',
                   command=lambda:button_click(str(1.618033988749894))).grid(row=3, column=1, sticky="nsew")   
# Plastic ratio
r_value = Button(tk_calc, button_params, text='rho',
                   command=lambda:button_click(str(1.324717957244746))).grid(row=3, column=2, sticky="nsew")

# Transform number to percentage
percentage = Button(tk_calc, button_params, text='%',
               command=percent).grid(row=3, column=3, sticky="nsew")

# Logarithm of a number with base 2
log_base2 = Button(tk_calc, button_params, text='log2', 
                   command=log2func).grid(row=3, column=4, sticky="nsew")
# Silver ratio
s_value = Button(tk_calc, button_params, text='ds',
                   command=lambda:button_click(str(2.41421356237309504880))).grid(row=3, column=5, sticky="nsew")

# Golden angle in radians
g_value = Button(tk_calc, button_params, text='g',
                   command=lambda:button_click(str(2.39996322972865332223))).grid(row=3, column=6, sticky="nsew")

# Van der Pauw constant
v_value = Button(tk_calc, button_params, text='VdP',
                   command=lambda:button_click(str(4.53236014182719380962))).grid(row=3, column=7, sticky="nsew")

# Universal parabolic constant
par_value = Button(tk_calc, button_params, text='P',
                   command=lambda:button_click(str(2.29558714939263807403))).grid(row=3, column=8, sticky="nsew")

# Supersilver ratio
supers_value = Button(tk_calc, button_params, text='s',
                   command=lambda:button_click(str(2.20556943040059031170))).grid(row=3, column=9, sticky="nsew")

#--4th row--
# Supergolden ratio
button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=4, column=0, sticky="nsew")
button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=4, column=1, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=4, column=2, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=4, column=3, sticky="nsew")
button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=4, column=4, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=4, column=5, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=4, column=6, sticky="nsew")
button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=4, column=7, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=4, column=8, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=4, column=9, sticky="nsew")

#--5th row--
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=5, column=0, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=5, column=1, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=5, column=2, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=5, column=3, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=5, column=4, sticky="nsew")
exp = Button(tk_calc, button_params_main, text='EXP', 
             command=lambda:button_click(E)).grid(row=5, column=5, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=5, column=6, sticky="nsew")
delete_one = Button(tk_calc, bd=2, fg='#000', 
              text='DEL', command=button_delete, bg='#db701f').grid(row=5, column=7, sticky="nsew")
delete_all = Button(tk_calc, bd=2, fg='#000', 
              text='AC', command=button_clear_all, bg='#db701f').grid(row=5, column=8, sticky="nsew")
superg_value = Button(tk_calc, button_params, text='psi',
                   command=lambda:button_click(str(1.46557103187676802665))).grid(row=5, column=9, sticky="nsew")
#--6th row--
# Fibonacci function
fib = Button(tk_calc, button_params_main, text='fibo', fg= '#BBB', bg= '#3C3636', 
               command=fibonacci).grid(row=6, column=0, sticky="nsew")
# Error function
erf = Button(tk_calc, button_params_main, text='erf', fg= '#BBB', bg= '#3C3636', 
               command=erfunc).grid(row=6, column=1, sticky="nsew")
# Calculate the function e^x
ex = Button(tk_calc, button_params, text='e^x', fg= '#BBB', bg= '#3C3636', command=expfunc).grid(row=6, column=2, sticky="nsew")
# Gamma function
gam = Button(tk_calc, button_params_main, text='gamma', fg= '#BBB', bg= '#3C3636', 
               command=gamma_func).grid(row=6, column=3, sticky="nsew")
# ln Gamma function
lgam = Button(tk_calc, button_params_main, text='lngamma', fg= '#BBB', bg= '#3C3636', 
               command=lgamma_func).grid(row=6, column=4, sticky="nsew")
# Hyperbolic sine of an angle in degrees
sineh = Button(tk_calc, button_params, text='sinh', fg= '#BBB', bg= '#3C3636',
             command=trig_sinh).grid(row=6, column=5, sticky="nsew")
# Hyperbolic cosine of an angle in degrees
cosineh = Button(tk_calc, button_params, text='cosh', fg= '#BBB', bg= '#3C3636',
             command=trig_cosh).grid(row=6, column=6, sticky="nsew")
# Hyperbolic tangent of an angle in degrees
tangenth = Button(tk_calc, button_params, text='tanh', fg= '#BBB', bg= '#3C3636',
             command=trig_tanh).grid(row=6, column=7, sticky="nsew")

# Hyperbolic tangent of an angle in degrees
degs = Button(tk_calc, button_params, text='deg', fg= '#BBB', bg= '#3C3636',
             command=degfunc).grid(row=6, column=8, sticky="nsew")

# Hyperbolic tangent of an angle in degrees
rads = Button(tk_calc, button_params, text='rad', fg= '#BBB', bg= '#3C3636',
             command=radfunc).grid(row=6, column=9, sticky="nsew")

#--7th row--

# Celsius to Fahrenheit
c2f_value = Button(tk_calc, button_params, text='C2F',
                   command=ctoffunc).grid(row=7, column=0, sticky="nsew")
# Celsius to Kelvin
c2k_value = Button(tk_calc, button_params, text='C2K',
                   command=ctokfunc).grid(row=7, column=1, sticky="nsew")
# Fahrenheit to Celsius
f2c_value = Button(tk_calc, button_params, text='F2C',
                   command=ftocfunc).grid(row=7, column=2, sticky="nsew")
# Fahrenheit to Kelvin
f2k_value = Button(tk_calc, button_params, text='F2K',
                   command=ftokfunc).grid(row=7, column=3, sticky="nsew")
# Kelvin to Celsius
k2c_value = Button(tk_calc, button_params, text='K2C',
                   command=ktocfunc).grid(row=7, column=4, sticky="nsew")
# Kelvin to Fahrenheit
k2f_value = Button(tk_calc, button_params, text='K2F',
                   command=ktoffunc).grid(row=7, column=5, sticky="nsew")
# Meter to Feet
m2f_value = Button(tk_calc, button_params, text='M2F',
                   command=mtoffunc).grid(row=7, column=6, sticky="nsew")
# Feet to Meter
f2m_value = Button(tk_calc, button_params, text='F2M',
                   command=ftomfunc).grid(row=7, column=7, sticky="nsew")
# Kg to Pounds
k2p_value = Button(tk_calc, button_params, text='K2P',
                   command=ktopfunc).grid(row=7, column=8, sticky="nsew")
p2k_value = Button(tk_calc, button_params, text='P2K',
                   command=ptokfunc).grid(row=7, column=9, sticky="nsew")
#--8th row--
# Pounds to Kg
# ml to oz
oz_value = Button(tk_calc, button_params, text='oz',
                   command=ozfunc).grid(row=8, column=0, sticky="nsew")
# oz to ml
ml_value = Button(tk_calc, button_params, text='ml',
                   command=mlfunc).grid(row=8, column=1, sticky="nsew")
# Gas constants
rsi_value = Button(tk_calc, button_params, text='R(SI)',
                   command=lambda:button_click(str(8.31446261815324))).grid(row=8, column=2, sticky="nsew")
rcal_value = Button(tk_calc, button_params, text='R(cal)',
                   command=lambda:button_click(str(1.98720425864083))).grid(row=8, column=3, sticky="nsew")
rlatm_value = Button(tk_calc, button_params, text='R(L*atm)',
                   command=lambda:button_click(str(0.082057366080960))).grid(row=8, column=4, sticky="nsew")
rlbar_value = Button(tk_calc, button_params, text='R(L*bar)',
                   command=lambda:button_click(str(0.0831446261815324))).grid(row=8, column=5, sticky="nsew")
rltorr_value = Button(tk_calc, button_params, text='R(L*torr)',
                   command=lambda:button_click(str(554.984319180))).grid(row=8, column=6, sticky="nsew")
rm3atm_value = Button(tk_calc, button_params, text='R(m³·atm)',
                   command=lambda:button_click(str(0.0000820573660809596))).grid(row=8, column=7, sticky="nsew")
rm3bar_value = Button(tk_calc, button_params, text='R(m³·bar)',
                   command=lambda:button_click(str(0.0000831446261815324))).grid(row=8, column=8, sticky="nsew")
rm3torr_value = Button(tk_calc, button_params, text='R(m³·torr)',
                   command=lambda:button_click(str(0.062363598418483226))).grid(row=8, column=9, sticky="nsew")

#--9th row--
rerg_value = Button(tk_calc, button_params, text='R(erg)',
                   command=lambda:button_click(str(0.000000831446261815324))).grid(row=9, column=0, sticky="nsew")
# Speed of light in a vacuum
c_value = Button(tk_calc, button_params, text='C',
                   command=lambda:button_click(str(299792458))).grid(row=9, column=1, sticky="nsew")
# 1 second definition as the duration of 9192631770 periods with transitions between the two hyperfine levels of the ground state of the caesium-133 atom
dtcs_value = Button(tk_calc, button_params, text='DtCs',
                   command=lambda:button_click(str(9192631770))).grid(row=9, column=2, sticky="nsew")
# Faraday constant
fara_value = Button(tk_calc, button_params, text='F',
                   command=lambda:button_click(str(96485.3321233100184))).grid(row=9, column=3, sticky="nsew")
# Standard acceleration of gravity
gas_value = Button(tk_calc, button_params, text='g(m/s²)',
                   command=lambda:button_click(str(9.80665))).grid(row=9, column=4, sticky="nsew")
# von Klitzing constant
vonkli_value = Button(tk_calc, button_params, text='Rk',
                   command=lambda:button_click(str(25812.80745))).grid(row=9, column=5, sticky="nsew")
# Calories to Joule conversion
c2j_value = Button(tk_calc, button_params, text='cal2joule',
                   command=c2jfunc).grid(row=9, column=6, columnspan=2, sticky="nsew")
# Joule to Calories conversion
j2c_value = Button(tk_calc, button_params, text='joule2cal',
                   command=j2cfunc).grid(row=9, column=8, columnspan=2, sticky="nsew")
tk_calc.mainloop()
