from tkinter import *
import math
import tkinter.messagebox
from tkinter import filedialog
from tkinter import Scrollbar

root = Tk()
root.title("SCIENTIFIC CALCULATOR")
root.configure(background = 'powder blue')
root.resizable(width=True, height=True)
root.geometry("480x600+380+90")
calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def asin(self):
        self.result = False
        self.current = math.asin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def acos(self):
        self.result = False
        self.current = math.acos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def atan(self):
        self.result = False
        self.current = math.atan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def power(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()),txtDisplay.get())
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cbrt(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get(),1/3))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(float(txtDisplay.get()))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(float(txtDisplay.get()))
        self.display(self.current) 

    def tanh(self):
        self.result = False
        self.current = math.tanh(float(txtDisplay.get()))
        self.display(self.current) 


    def factorial(self):
        self.result = False
        self.current = math.factorial(float(txtDisplay.get()))
        self.display(self.current)



    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def gamma(self):
        self.result = False
        self.current = math.gamma(float(txtDisplay.get()))
        self.display(self.current)

    def beta(self):
        self.result=False
        self.current = (math.gamma(float(txtDisplay.get()))**2)/(math.gamma(2*float(txtDisplay.get())))
        self.display(self.current)

    def erf(self):
        self.result = False
        self.current = math.erf(float(txtDisplay.get()))
        self.display(self.current)

    def erfc(self):
        self.result = False
        self.current = math.erfc(float(txtDisplay.get()))
        self.display(self.current)


    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def loge(self):
        self.result = False
        self.current = math.loge(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=5, height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1
	
btnClear = Button(calc, text=chr(67),width=5,
                  height=2,bg='powder blue',
                  font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry
                  ).grid(row=1, column= 1, pady = 1)

btnAllClear = Button(calc, text=chr(67)+chr(69),
                     width=5, height=2,
                     bg='powder blue',
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                     ).grid(row=1, column= 0, pady = 1)

btnsq = Button(calc, text="\u221A",width=5, height=2,
               bg='powder blue', font=('Helvetica',
								        20,'bold'),
               bd=4,command=added_value.squared
               ).grid(row=5, column= 0, pady = 1)

btnAdd = Button(calc, text="+",width=5, height=2,
				bg='powder blue',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.operation("add")
				).grid(row=3, column= 3, pady = 1)

btnSub = Button(calc, text="-",width=5,
				height=2,bg='powder blue',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.operation("sub")
				).grid(row=4, column= 3, pady = 1)

btnMul = Button(calc, text="x",width=5,
				height=2,bg='powder blue',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.operation("multi")
				).grid(row=2, column= 3, pady = 1)

btnDiv = Button(calc, text="÷",width=5,
				height=2,bg='powder blue',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.operation("divide")
				).grid(row=1, column= 3, pady = 1)

btnZero = Button(calc, text="0",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.numberEnter(0)
				).grid(row=5, column= 1, pady = 1)

btnDot = Button(calc, text=".",width=5,
				height=2,bg='powder blue',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.numberEnter(".")
				).grid(row=5, column= 2, pady = 1)
btnacos = Button(calc, text='cos^-1',width=5,
			height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),
			bd=4,command=added_value.acos
            ).grid(row=2, column= 6, pady = 1)

btnEquals = Button(calc, text="=",width=5,
				height=2,bg='powder blue',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.sum_of_total
				).grid(row=5, column= 3, pady = 1)
# ROW 1 :
btnPi = Button(calc, text="π",width=5,
			height=2,bg='black',fg='white',
			font=('Helvetica',20,'bold'),
			bd=4,command=added_value.pi
			).grid(row=1, column= 4, pady = 1)

btnCos = Button(calc, text="cos",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.cos
			).grid(row=1, column= 6, pady = 1)

btntan = Button(calc, text="tan",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.tan
			).grid(row=1, column= 7, pady = 1)

btnsin = Button(calc, text="sin",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.sin
			).grid(row=1, column= 5, pady = 1)

# ROW 2 :
btnasin = Button(calc, text="sin^-1",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.asin
			).grid(row=2, column= 5, pady = 1)

btnatan = Button(calc, text="tan^-1",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.atan
				).grid(row=2, column= 7, pady = 1)

btnpow = Button(calc, text="pow",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.power
				).grid(row=3, column= 5, pady = 1)

btncbrt = Button(calc, text="∛",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.cbrt
				).grid(row=3, column= 4, pady = 1)

# ROW 3 :
btnlog = Button(calc, text="log",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.log
			).grid(row=4, column= 4, pady = 1)

btnExp = Button(calc, text="exp",width=5, height=2,
				bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.exp
			).grid(row=5, column= 5, pady = 1)

btnMod = Button(calc, text="%",width=5,
				height=2,bg='powder blue',fg='black',
				font=('Helvetica',20,'bold'),
				bd=4,command=lambda:added_value.operation("mod")
				).grid(row=1, column= 2, pady = 1)

btnE = Button(calc, text="e",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.e
			).grid(row=5, column= 4, pady = 1)

# ROW 4 :
btnlog10 = Button(calc, text="log10",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.log10
				).grid(row=4, column= 5, pady = 1)

btnlog1p = Button(calc, text="log1p",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.log1p
				).grid(row=4, column= 7, pady = 1)

btnexpm1 = Button(calc, text="expm1",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd = 4,command=added_value.expm1
				).grid(row=5, column= 6, pady = 1)

btngamma = Button(calc, text="gamma",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.gamma
				).grid(row=5, column= 7, pady = 1)
# ROW 5 :
btnloge = Button(calc, text="loge",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.loge
				).grid(row=4, column= 6, pady = 1)

btndeg= Button(calc, text="deg",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.degrees
			).grid(row=2, column= 4, pady = 1)

btncosh = Button(calc, text="cosh",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.cosh
				).grid(row=3, column= 7, pady = 1)

btnsinh = Button(calc, text="sinh",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.sinh
				).grid(row=3, column= 6, pady = 1)

btntanh = Button(calc, text="tanh",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.tanh
				).grid(row=3, column= 8, pady = 1)

btnbeta = Button(calc, text="beta",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.tanh
				).grid(row=5, column= 8, pady = 1)

btnerf = Button(calc, text="erf",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.erf
				).grid(row=1, column= 8, pady = 1)

btnerfc= Button(calc, text="erfc",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.erfc
				).grid(row=2, column= 8, pady = 1)
btnfactorial = Button(calc, text="fact",width=5,
				height=2,bg='black',fg='white',
				font=('Helvetica',20,'bold'),
				bd=4,command=added_value.factorial
				).grid(row=4, column= 8, pady = 1)


lblDisplay = Label(calc, text = "SCIENTIFIC CALCULATOR",
				font=('Helvetica',30,'bold'),
				bg='powder blue',fg='black',justify=CENTER)

lblDisplay.grid(row=0, column= 4,columnspan=4)

def iExit():
	iExit = tkinter.messagebox.askyesno("SCIENTIFIC CALCULATOR",
										"DO YOU WANT TO EXIT ?")
	if iExit>0:
		root.destroy()
		return

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("1120x600+0+0")

def Standard():
	root.resizable(width=False, height=False)
	root.geometry("400x400")

def openNewWindow():
    newWindow = tkinter.Toplevel(root)
    newWindow.title("MATH FUNCTION DEFINITIONS")
    newWindow.geometry("400x400")
    newWindow.configure(background="black")

    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()

        text_widget = tkinter.Text(newWindow,wrap = tkinter.WORD)
        text_widget.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

         #Create a Scrollbar for the Text widget
        scrollbar = Scrollbar(newWindow, command=text_widget.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        text_widget.config(yscrollcommand=scrollbar.set)
        text_widget.insert("1.0", file_contents)


menubar = Menu(calc)

# MenuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'MENU', menu = filemenu)
filemenu.add_command(label = "STANDARD", command = Standard)
filemenu.add_command(label = "SCIENTIFIC", command = Scientific)
filemenu.add_command(label = "HELP", command = openNewWindow)
filemenu.add_separator()
filemenu.add_command(label = "EXIT", command = iExit)

root.config(menu=menubar)

root.mainloop()


