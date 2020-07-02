#This is a Python Application to Perform Fast Fourier Transform (FFT) on a given Signal Sequence 
#App Name => DSP Toolkit v1.0
#Release Date => 7/7/2020
#Developer Name => Anshuman Biswal
#Platforms Available => Windows 10, MacOS, Linux
#Written in => Python 3.8.3 
#Institution Name => New Horizon College of Engineering, Bangalore,India
#Applications/Use => DFT and IDFT of 4Point,8Point signal sequence in Frequency and Time Domain using Radix Algorithm. 
#Linear Convolution and Circular Convolution using Radix Algorithm.
#GitHub:- https://github.com/anshumanbiswal14 

from tkinter import *
import numpy as np
import webbrowser
import math
import cmath
root = Tk()
url1 = "https://www.linkedin.com/in/anshumanbiswal/"
url2 = "https://www.youtube.com/channel/UC-2mHXYbkhoNim94TQqFgrw?view_as=subscriber"
root.title("DSP ToolKit Version 1.0 // Developed By Anshuman Biswal")
root.geometry("1100x650")
root.iconbitmap("Mainapp.ico")
root.configure(background = '#393939')

# Main Application "Exit" and "About Developer Menu" opens a new tab on your default browser 
def main_exit():
    root.quit()    
def openweb1():
    webbrowser.open_new(url1)
def openweb2():
    webbrowser.open_new(url2)
    
# New Window for 4 Point - (DIT) - FFT    
def open1():
    new_window = Toplevel()
    new_window.title("4 - POINT (DIT) FFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')

# Calculation/Math               
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=350,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=670,y=140) 
               
        s_0 = int(x_2.get()) + int(x_0.get())
        s_1 = int(x_0.get()) - int(x_2.get())
        s_2 = int(x_3.get()) + int(x_1.get())
        s_3 = int(x_1.get()) - int(x_3.get())        
        s_1_0 = s_0
        s_2_1 = s_1
        s_3_2 = s_2
        s_4_3 = s_3
        s_1_com = complex(s_1_0)
        s_2_com = complex(s_2_1)
        s_3_com = complex(s_3_2)
        s_4_com = complex(s_4_3)
        sf_1 =  s_3_2 + s_1_0
        sf_2 =  ((-1j*s_4_com) + s_2_com )
        sf_3 =  s_1_0 - s_3_2
        sf_4 =  (s_2_com - (-1j*s_4_com))
              
        stage_1_0=Label(new_window,text=str(s_1_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=400,y=180)        
        stage_1_1=Label(new_window,text=str(s_2_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=400,y=260)    
        stage_1_2=Label(new_window,text=str(s_3_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=400,y=340)        
        stage_1_3=Label(new_window,text=str(s_4_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=400,y=420)
                
        stage_2_0=Label(new_window,text=str(sf_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=700,y=180)        
        stage_2_1=Label(new_window,text=str(sf_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=700,y=260)    
        stage_2_2=Label(new_window,text=str(sf_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=700,y=340)        
        stage_2_3=Label(new_window,text=str(sf_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=700,y=420)
            
    # Sub-Application-1 Layout                                                    
    Poster_1 = Label(new_window,text="___ 4 - POINT (DIT) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)
        
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=260)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=260)
       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=340)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=340)
    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=420)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=420)
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300) 
    
# New Window for 4 Point - (DIF) - FFT      
def open2():
    new_window = Toplevel()
    new_window.title("4 - POINT (DIF) FFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
# Calculation/Math     
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=350,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=670,y=140)
        
        s_0 = int(x_2.get()) + int(x_0.get())
        s_1 = int(x_3.get()) + int(x_1.get())
        s_2 = int(x_0.get()) - int(x_2.get())
        s_3 = int(x_1.get()) - int(x_3.get())
        ss_0 = s_1 + s_0
        ss_1 = s_0 - s_1
        ss_2 = (complex(s_3)*(-1j)) + s_2
        ss_3 = s_2 - (complex(s_3)*(-1j)) 
        
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=400,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=400,y=260)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=400,y=340)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=400,y=420) 
               
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=700,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=700,y=260)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=700,y=340)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=700,y=420)     
    
    # Sub-Application-2 Layout                                                    
    Poster_1 = Label(new_window,text="___ 4 - POINT (DIF) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100) 
       
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)        
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=260)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=260)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=340)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=340)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=420)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=420)
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300) 
    
# New Window for 8 Point - (DIT) - FFT     
def open3():
    new_window = Toplevel()
    new_window.title("8 - POINT (DIT) FFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
# Calculation/Math    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=280,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=450,y=140)
        sub3=Label(new_window,text='(Stage - 3)',font=('Calibri',18),bg='#393939',fg='white')
        sub3.place(x=640,y=140)
        
        s_0 = int(x_4.get()) + int(x_0.get())
        s_1 = int(x_0.get()) - int(x_4.get())
        s_2 = int(x_6.get()) + int(x_2.get())
        s_3 = int(x_2.get()) - int(x_6.get())
        s_4 = int(x_5.get()) + int(x_1.get())
        s_5 = int(x_1.get()) - int(x_5.get())
        s_6 = int(x_7.get()) + int(x_3.get())
        s_7 = int(x_3.get()) - int(x_7.get())
        
        ss_0 = s_2 + s_0
        ss_1 = ((complex(s_3))*(-1j)) + s_1
        ss_2 = s_0 - s_2
        ss_3 = s_1 - ((complex(s_3))*(-1j))
        ss_4 = s_6 + s_4
        ss_5 = ((complex(s_7))*(-1j)) + s_5
        ss_6 = s_4 - s_6
        ss_7 = s_5 - ((complex(s_7))*(-1j)) 
        
        sss_0 = ss_4 + ss_0
        sss_1 = ((0.7071067812-0.7071067812j)*(complex(ss_5))) + ss_1
        sss_2 = ((complex(ss_6))*(-1j)) + ss_2
        sss_3 = ((-0.7071067812-0.7071067812j)*(complex(ss_7))) + ss_3
        sss_4 = ss_0 - ss_4
        sss_5 = ss_1 - ((0.7071067812-0.7071067812j)*(complex(ss_5)))
        sss_6 = ss_2 - ((complex(ss_6))*(-1j))
        sss_7 = ss_3 - ((-0.7071067812-0.7071067812j)*(complex(ss_7)))
        
        round_sss1=(round(sss_1.real,3)+round(sss_1.imag,3) * 1j)
        round_sss3=(round(sss_3.real,3)+round(sss_3.imag,3) * 1j)
        round_sss5=(round(sss_5.real,3)+round(sss_5.imag,3) * 1j)
        round_sss7=(round(sss_7.real,3)+round(sss_7.imag,3) * 1j)
        
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=310,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=310,y=220)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=310,y=260)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=310,y=300)
        stage_1_4=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_4.place(x=310,y=340)        
        stage_1_5=Label(new_window,text=str(s_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_5.place(x=310,y=380)    
        stage_1_6=Label(new_window,text=str(s_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_6.place(x=310,y=420)        
        stage_1_7=Label(new_window,text=str(s_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_7.place(x=310,y=460) 
        
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=470,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=470,y=220)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=470,y=260)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=470,y=300)
        stage_2_4=Label(new_window,text=str(ss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_4.place(x=470,y=340)        
        stage_2_5=Label(new_window,text=str(ss_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_5.place(x=470,y=380)    
        stage_2_6=Label(new_window,text=str(ss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_6.place(x=470,y=420)        
        stage_2_7=Label(new_window,text=str(ss_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_7.place(x=470,y=460)  
        
        stage_3_0=Label(new_window,text=str(sss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_0.place(x=660,y=180)        
        stage_3_1=Label(new_window,text=str(round_sss1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_1.place(x=660,y=220)    
        stage_3_2=Label(new_window,text=str(sss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_2.place(x=660,y=260)        
        stage_3_3=Label(new_window,text=str(round_sss3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_3.place(x=660,y=300)
        stage_3_4=Label(new_window,text=str(sss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_4.place(x=660,y=340)        
        stage_3_5=Label(new_window,text=str(round_sss5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_5.place(x=660,y=380)    
        stage_3_6=Label(new_window,text=str(sss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_6.place(x=660,y=420)        
        stage_3_7=Label(new_window,text=str(round_sss7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_7.place(x=660,y=460)   
      
    Poster_1 = Label(new_window,text="___ 8 - POINT (DIT) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    #Sub-Application-3 Layout  
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)    
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=220)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=260)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=300)    
    num_4 = Label(new_window, text='X(4) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=340)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=90,y=340)        
    num_5 = Label(new_window, text='X(5) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=380)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=90,y=380)      
    num_6 = Label(new_window, text='X(6) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=420)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=90,y=420)    
    num_7 = Label(new_window, text='X(7) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=30,y=460)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=90,y=460) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)
    
# New Window for 8 Point (DIF) FFT     
def open4():
    new_window = Toplevel()
    new_window.title("8 - POINT (DIF) FFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=280,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=450,y=140)
        sub3=Label(new_window,text='(Stage - 3)',font=('Calibri',18),bg='#393939',fg='white')
        sub3.place(x=640,y=140)
        
        s_0 = int(x_4.get()) + int(x_0.get())
        s_1 = int(x_5.get()) + int(x_1.get())
        s_2 = int(x_6.get()) + int(x_2.get())
        s_3 = int(x_7.get()) + int(x_3.get())
        s_4 = int(x_0.get()) - int(x_4.get())
        s_5 = int(x_1.get()) - int(x_5.get())
        s_6 = int(x_2.get()) - int(x_6.get())
        s_7 = int(x_3.get()) - int(x_7.get())
        
        ss_0 = s_2 + s_0
        ss_1 = s_3 + s_1
        ss_2 = s_0 - s_2
        ss_3 = s_1 - s_3
        ss_4 = (((complex(s_6))*(-1j)) + (s_4))
        ss_5 = (((-0.7071067812-0.7071067812j)*(complex(s_7))) + ((0.7071067812-0.7071067812j)*(complex(s_5))))
        ss_6 = ((s_4) -  ((complex(s_6))*(-1j)))
        ss_7 = (((0.7071067812-0.7071067812j)*(complex(s_5))) - ((-0.7071067812-0.7071067812j)*(complex(s_7))))
        round_ss5=(round(ss_5.real,3)+round(ss_5.imag,3) * 1j)
        round_ss7=(round(ss_7.real,3)+round(ss_7.imag,3) * 1j)

        sss_0 = ss_1 + ss_0
        sss_1 = ss_0 - ss_1
        sss_2 = (complex(ss_3)*(-1j)) + ss_2
        sss_3 = ss_2 - (complex(ss_3)*(-1j))
        sss_4 = ss_5 + ss_4 
        sss_5 = ss_4 - ss_5
        sss_6 = (complex(ss_7)*(-1j)) + ss_6
        sss_7 = ss_6 - (complex(ss_7)*(-1j))
        round_sss4=(round(sss_4.real,3)+round(sss_4.imag,3) * 1j)
        round_sss5=(round(sss_5.real,3)+round(sss_5.imag,3) * 1j)
        round_sss6=(round(sss_6.real,3)+round(sss_6.imag,3) * 1j)
        round_sss7=(round(sss_7.real,3)+round(sss_7.imag,3) * 1j)
        
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=310,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=310,y=220)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=310,y=260)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=310,y=300)
        stage_1_4=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_4.place(x=310,y=340)        
        stage_1_5=Label(new_window,text=str(s_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_5.place(x=310,y=380)    
        stage_1_6=Label(new_window,text=str(s_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_6.place(x=310,y=420)        
        stage_1_7=Label(new_window,text=str(s_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_7.place(x=310,y=460) 
        
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=470,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=470,y=220)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=470,y=260)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=470,y=300)
        stage_2_4=Label(new_window,text=str(ss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_4.place(x=470,y=340)        
        stage_2_5=Label(new_window,text=str(round_ss5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_5.place(x=470,y=380)    
        stage_2_6=Label(new_window,text=str(ss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_6.place(x=470,y=420)        
        stage_2_7=Label(new_window,text=str(round_ss7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_7.place(x=470,y=460)  
        
        stage_3_0=Label(new_window,text=str(sss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_0.place(x=660,y=180)        
        stage_3_1=Label(new_window,text=str(round_sss4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_1.place(x=660,y=220)    
        stage_3_2=Label(new_window,text=str(sss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_2.place(x=660,y=260)        
        stage_3_3=Label(new_window,text=str(round_sss6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_3.place(x=660,y=300)
        stage_3_4=Label(new_window,text=str(sss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_4.place(x=660,y=340)        
        stage_3_5=Label(new_window,text=str(round_sss5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_5.place(x=660,y=380)    
        stage_3_6=Label(new_window,text=str(sss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_6.place(x=660,y=420)        
        stage_3_7=Label(new_window,text=str(round_sss7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_7.place(x=660,y=460)      
        
    Poster_1 = Label(new_window,text="___ 8 - POINT (DIF) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    #Sub-Application-4 Layout  
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)    
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=220)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=260)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=300)    
    num_4 = Label(new_window, text='X(4) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=340)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=90,y=340)        
    num_5 = Label(new_window, text='X(5) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=380)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=90,y=380)      
    num_6 = Label(new_window, text='X(6) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=420)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=90,y=420)    
    num_7 = Label(new_window, text='X(7) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=30,y=460)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=90,y=460) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)
    
#New Window for Circular Convolution 
def open5():
    new_window = Toplevel()
    new_window.title("Circular Convolution Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')

#Calculation/Math    
    def submit():
        s_1 = int(x_2.get()) + int(x_0.get())
        s_2 = int(x_0.get()) - int(x_2.get())
        s_3 = int(x_3.get()) + int(x_1.get())
        s_4 = int(x_1.get()) - int(x_3.get())
        s_1_0 = s_1
        s_2_1 = s_2
        s_3_2 = s_3
        s_4_3 = s_4
        s_1_com = complex(s_1_0)
        s_2_com = complex(s_2_1)
        s_3_com = complex(s_3_2)
        s_4_com = complex(s_4_3)        
        sf_1 =  s_3_2 + s_1_0
        sf_2 =  ((-1j*s_4_com) + s_2_com )
        sf_3 =  s_1_0 - s_3_2
        sf_4 =  (s_2_com - (-1j*s_4_com))
        s_11 =  int(x_6.get()) + int(x_4.get())
        s_22 =  int(x_4.get()) - int(x_6.get())
        s_33 =  int(x_7.get()) + int(x_5.get())
        s_44 =  int(x_5.get()) - int(x_7.get())
        s_1_00 = s_11
        s_2_11 = s_22
        s_3_22 = s_33
        s_4_33 = s_44
        s_1_comm = complex(s_1_00)
        s_2_comm = complex(s_2_11)
        s_3_comm = complex(s_3_22)
        s_4_comm = complex(s_4_33)
        sf_11 =  s_3_22 + s_1_00
        sf_22 =  ((-1j*s_4_comm) + s_2_comm )
        sf_33 =  s_1_00 - s_3_22
        sf_44 =  (s_2_comm - (-1j*s_4_comm))
        mul_0 = sf_1 * sf_11
        mul_1 = sf_2 * sf_22
        mul_2 = sf_3 * sf_33
        mul_3 = sf_4 * sf_44  
        last_0 = mul_2 + mul_0
        last_1 = mul_3 + mul_1
        last_2 = mul_0 - mul_2 
        last_3 = mul_1 - mul_3
        last_00 = last_1 + last_0
        last_11 = last_0 - last_1
        last_22 = (complex(last_3)*(-1j)) + last_2
        last_33 = last_2 - (complex(last_3)*(-1j))
        x_f   = (last_00)*(1/4)
        x_ff  = (last_22)*(1/4)
        x_fff = (last_11)*(1/4)
        x_ffff = (last_33)*(1/4)        
        sub1=Label(new_window,text='Answer :- X3 (n) = '+'{}, {}, {}, {}'.format(x_f,x_ff,x_fff,x_ffff),font=('Calibri',28),bg='#393939',fg='#FAF848')
        sub1.place(x=80,y=400)
                    
    Poster_1 = Label(new_window,text="Circular Convolution Calculator",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=210,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X1(n)' & 'X2(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=180,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=140,y=100)
    
    #Sub-Application-5 Layout  
    num_0 = Label(new_window, text='X1 (0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=40,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=140,y=180)    
    num_1 = Label(new_window, text='X1 (1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=40,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=140,y=220)       
    num_2 = Label(new_window, text='X1 (2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=40,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=140,y=260)    
    num_3 = Label(new_window, text='X1 (3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=40,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=140,y=300)        
    num_4 = Label(new_window, text='X2 (0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=490,y=180)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=600,y=180)        
    num_5 = Label(new_window, text='X2 (1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=490,y=220)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=600,y=220)      
    num_6 = Label(new_window, text='X2 (2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=490,y=260)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=600,y=260)    
    num_7 = Label(new_window, text='X2 (3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=490,y=300)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=600,y=300) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)

#New Window for Linear Convolution     
def open6():
    new_window = Toplevel()
    new_window.title("Linear Convolution Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
#Calculation/Math    
    def submit():
        aa=int(x_0.get())
        bb=int(x_1.get())
        cc=int(x_2.get())
        dd=int(x_3.get())
        ee=int(x_4.get())
        ff=int(x_5.get())
        gg=int(x_6.get())
        hh=int(x_7.get())
        calc_0 = (ee*aa)
        calc_1 = (ff*aa)+(ee*bb)
        calc_2 = (gg*aa)+(ff*bb)+(ee*cc)
        calc_3 = (hh*aa)+(gg*bb)+(ff*cc)+(ee*dd)
        calc_4 = (hh*bb)+(gg*cc)+(ff*dd)
        calc_5 = (hh*cc)+(gg*dd)
        calc_6 = (hh*dd)
        sub1=Label(new_window,text='Answer:- Y(n) = {}, {}, {}, {}, {}, {}, {}'.format(calc_0,calc_1,calc_2,calc_3,calc_4,calc_5,calc_6),font=('Calibri',28),bg='#393939',fg='#FAF848')
        sub1.place(x=80,y=400)

    Poster_1 = Label(new_window,text="Linear Convolution Calculator",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=210,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(n)' & 'H(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=180,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=140,y=100)
    
    #Sub-Application-6 Layout  
    num_0 = Label(new_window, text='X (0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=40,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=140,y=180)    
    num_1 = Label(new_window, text='X (1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=40,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=140,y=220)       
    num_2 = Label(new_window, text='X (2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=40,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=140,y=260)    
    num_3 = Label(new_window, text='X (3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=40,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=140,y=300)        
    num_4 = Label(new_window, text='H (0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=490,y=180)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=600,y=180)        
    num_5 = Label(new_window, text='H (1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=490,y=220)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=600,y=220)      
    num_6 = Label(new_window, text='H (2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=490,y=260)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=600,y=260)    
    num_7 = Label(new_window, text='H (3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=490,y=300)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=600,y=300) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)

# New Window for 8 Point (DIT) IDFT    
def open7():
    new_window = Toplevel()
    new_window.title("8 - Point (DIT) IDFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939') 

# Calculation/Math    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=280,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=450,y=140)
        sub3=Label(new_window,text='(Stage - 3)',font=('Calibri',18),bg='#393939',fg='white')
        sub3.place(x=640,y=140)
        
        cc_val_0 = complex(x_0.get())
        c_val_0 = np.conj(cc_val_0)
        cc_val_1 = complex(x_1.get())
        c_val_1 = np.conj(cc_val_1)
        cc_val_2 = complex(x_2.get())
        c_val_2 = np.conj(cc_val_2)
        cc_val_3 = complex(x_3.get())
        c_val_3 = np.conj(cc_val_3)
        cc_val_4 = complex(x_4.get())
        c_val_4 = np.conj(cc_val_4)
        cc_val_5 = complex(x_5.get())
        c_val_5 = np.conj(cc_val_5)
        cc_val_6 = complex(x_6.get())
        c_val_6 = np.conj(cc_val_6)
        cc_val_7 = complex(x_7.get())
        c_val_7 = np.conj(cc_val_7)        
        s_0 = c_val_4 + c_val_0
        s_1 = c_val_0 - c_val_4
        s_2 = c_val_6 + c_val_2
        s_3 = c_val_2 - c_val_6
        s_4 = c_val_5 + c_val_1
        s_5 = c_val_1 - c_val_5
        s_6 = c_val_7 + c_val_3
        s_7 = c_val_3 - c_val_7
        round_s_5 = (round(s_5.real,2)+round(s_5.imag,2))
        round_s_7 = (round(s_7.real,2)+round(s_7.imag,2))
        ss_0 = s_2 + s_0
        ss_1 = ((complex(s_3))*(-1j)) + s_1
        ss_2 = s_0 - s_2
        ss_3 = s_1 - ((complex(s_3))*(-1j))
        ss_4 = s_6 + s_4
        ss_5 = ((complex(s_7))*(-1j)) + s_5
        ss_6 = s_4 - s_6
        ss_7 = s_5 - ((complex(s_7))*(-1j))
        round_ss_5 = (round(ss_5.real,2)+round(ss_5.imag,2))
        round_ss_7 = (round(ss_7.real,2)+round(ss_7.imag,2))
        sss_0 = ss_4 + ss_0
        sss_1 = ((0.7071067812-0.7071067812j)*(complex(ss_5))) + ss_1
        sss_2 = ((complex(ss_6))*(-1j)) + ss_2
        sss_3 = ((-0.7071067812-0.7071067812j)*(complex(ss_7))) + ss_3
        sss_4 = ss_0 - ss_4
        sss_5 = ss_1 - ((0.7071067812-0.7071067812j)*(complex(ss_5)))
        sss_6 = ss_2 - ((complex(ss_6))*(-1j))
        sss_7 = ss_3 - ((-0.7071067812-0.7071067812j)*(complex(ss_7)))
        
        fin_0 = sss_0.real
        fin_1 = sss_1.real
        fin_2 = sss_2.real
        fin_3 = sss_3.real
        fin_4 = sss_4.real
        fin_5 = sss_5.real
        fin_6 = sss_6.real
        fin_7 = sss_7.real
        fin_00 = (round(fin_0,0)/8)
        fin_11 = (round(fin_1,0)/8)
        fin_22 = (round(fin_2,0)/8)
        fin_33 = (round(fin_3,0)/8)
        fin_44 = (round(fin_4,0)/8)
        fin_55 = (round(fin_5,0)/8)
        fin_66 = (round(fin_6,0)/8)
        fin_77 = (round(fin_7,0)/8)
            
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=310,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=310,y=220)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=310,y=260)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=310,y=300)
        stage_1_4=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_4.place(x=310,y=340)        
        stage_1_5=Label(new_window,text=str(round_s_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_5.place(x=310,y=380)    
        stage_1_6=Label(new_window,text=str(s_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_6.place(x=310,y=420)        
        stage_1_7=Label(new_window,text=str(round_s_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_7.place(x=310,y=460) 
        
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=470,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=470,y=220)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=470,y=260)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=470,y=300)
        stage_2_4=Label(new_window,text=str(ss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_4.place(x=470,y=340)        
        stage_2_5=Label(new_window,text=str(round_ss_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_5.place(x=470,y=380)    
        stage_2_6=Label(new_window,text=str(ss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_6.place(x=470,y=420)        
        stage_2_7=Label(new_window,text=str(round_ss_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_7.place(x=470,y=460)  
        
        stage_3_0=Label(new_window,text=str(fin_00),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_0.place(x=660,y=180)        
        stage_3_1=Label(new_window,text=str(fin_11),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_1.place(x=660,y=220)    
        stage_3_2=Label(new_window,text=str(fin_22),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_2.place(x=660,y=260)        
        stage_3_3=Label(new_window,text=str(fin_33),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_3.place(x=660,y=300)
        stage_3_4=Label(new_window,text=str(fin_44),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_4.place(x=660,y=340)        
        stage_3_5=Label(new_window,text=str(fin_55),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_5.place(x=660,y=380)    
        stage_3_6=Label(new_window,text=str(fin_66),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_6.place(x=660,y=420)        
        stage_3_7=Label(new_window,text=str(fin_77),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_7.place(x=660,y=460)      
                  
    Poster_1 = Label(new_window,text="___ 8 - POINT (DIT) IDFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(k)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    #Sub-Application-7 Layout  
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)    
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=220)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=260)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=300)    
    num_4 = Label(new_window, text='X(4) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=340)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=90,y=340)        
    num_5 = Label(new_window, text='X(5) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=380)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=90,y=380)      
    num_6 = Label(new_window, text='X(6) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=420)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=90,y=420)    
    num_7 = Label(new_window, text='X(7) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=30,y=460)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=90,y=460) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)


# New Window for 8 Point (DIF) IDFT    
def open8():
    new_window = Toplevel()
    new_window.title("8 - Point (DIF) IDFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939') 

# Calculation/Math    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=280,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=450,y=140)
        sub3=Label(new_window,text='(Stage - 3)',font=('Calibri',18),bg='#393939',fg='white')
        sub3.place(x=640,y=140)
    
        cc_val_0 = complex(x_0.get())
        c_val_0 = np.conj(cc_val_0)
        cc_val_1 = complex(x_1.get())
        c_val_1 = np.conj(cc_val_1)
        cc_val_2 = complex(x_2.get())
        c_val_2 = np.conj(cc_val_2)
        cc_val_3 = complex(x_3.get())
        c_val_3 = np.conj(cc_val_3)
        cc_val_4 = complex(x_4.get())
        c_val_4 = np.conj(cc_val_4)
        cc_val_5 = complex(x_5.get())
        c_val_5 = np.conj(cc_val_5)
        cc_val_6 = complex(x_6.get())
        c_val_6 = np.conj(cc_val_6)
        cc_val_7 = complex(x_7.get())
        c_val_7 = np.conj(cc_val_7) 
        
        s_0 = c_val_4 + c_val_0
        s_1 = c_val_5 + c_val_1
        s_2 = c_val_6 + c_val_2
        s_3 = c_val_7 + c_val_3
        s_4 = c_val_0 - c_val_4
        s_5 = c_val_1 - c_val_5
        s_6 = c_val_2 - c_val_6
        s_7 = c_val_3 - c_val_7 
        round_s_5 = (round(s_5.real,2)+round(s_5.imag,2))
        round_s_7 = (round(s_7.real,2)+round(s_7.imag,2))
        
        ss_0 = s_2 + s_0
        ss_1 = s_3 + s_1
        ss_2 = s_0 - s_2
        ss_3 = s_1 - s_3
        ss_4 = (((complex(s_6))*(-1j)) + (s_4))
        ss_5 = (((-0.7071067812-0.7071067812j)*(complex(s_7))) + ((0.7071067812-0.7071067812j)*(complex(s_5))))
        ss_6 = ((s_4) -  ((complex(s_6))*(-1j)))
        ss_7 = (((0.7071067812-0.7071067812j)*(complex(s_5))) - ((-0.7071067812-0.7071067812j)*(complex(s_7))))
        round_ss_5 = (round(ss_5.real,2)+round(ss_5.imag,2))
        round_ss_7 = (round(ss_7.real,2)+round(ss_7.imag,2))
        sss_0 = ss_1 + ss_0
        sss_1 = ss_0 - ss_1
        sss_2 = (complex(ss_3)*(-1j)) + ss_2
        sss_3 = ss_2 - (complex(ss_3)*(-1j))
        sss_4 = ss_5 + ss_4 
        sss_5 = ss_4 - ss_5
        sss_6 = (complex(ss_7)*(-1j)) + ss_6
        sss_7 = ss_6 - (complex(ss_7)*(-1j))
        
        fin_0 = sss_0.real
        fin_1 = sss_1.real
        fin_2 = sss_2.real
        fin_3 = sss_3.real
        fin_4 = sss_4.real
        fin_5 = sss_5.real
        fin_6 = sss_6.real
        fin_7 = sss_7.real
        fin_00 = (round(fin_0,0)/8)
        fin_11 = (round(fin_1,0)/8)
        fin_22 = (round(fin_2,0)/8)
        fin_33 = (round(fin_3,0)/8)
        fin_44 = (round(fin_4,0)/8)
        fin_55 = (round(fin_5,0)/8)
        fin_66 = (round(fin_6,0)/8)
        fin_77 = (round(fin_7,0)/8)

        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=310,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=310,y=220)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=310,y=260)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=310,y=300)
        stage_1_4=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_4.place(x=310,y=340)        
        stage_1_5=Label(new_window,text=str(round_s_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_5.place(x=310,y=380)    
        stage_1_6=Label(new_window,text=str(s_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_6.place(x=310,y=420)        
        stage_1_7=Label(new_window,text=str(round_s_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_7.place(x=310,y=460) 
        
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=470,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=470,y=220)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=470,y=260)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=470,y=300)
        stage_2_4=Label(new_window,text=str(ss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_4.place(x=470,y=340)        
        stage_2_5=Label(new_window,text=str(round_ss_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_5.place(x=470,y=380)    
        stage_2_6=Label(new_window,text=str(ss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_6.place(x=470,y=420)        
        stage_2_7=Label(new_window,text=str(round_ss_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_7.place(x=470,y=460)  
        
        stage_3_0=Label(new_window,text=str(fin_00),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_0.place(x=660,y=180)        
        stage_3_1=Label(new_window,text=str(fin_44),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_1.place(x=660,y=220)    
        stage_3_2=Label(new_window,text=str(fin_22),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_2.place(x=660,y=260)        
        stage_3_3=Label(new_window,text=str(fin_66),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_3.place(x=660,y=300)
        stage_3_4=Label(new_window,text=str(fin_11),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_4.place(x=660,y=340)        
        stage_3_5=Label(new_window,text=str(fin_55),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_5.place(x=660,y=380)    
        stage_3_6=Label(new_window,text=str(fin_33),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_6.place(x=660,y=420)        
        stage_3_7=Label(new_window,text=str(fin_77),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_7.place(x=660,y=460)      
                  
    Poster_1 = Label(new_window,text="___ 8 - POINT (DIF) IDFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(k)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100) 

#Sub-Application-8 Layout  
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)    
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=220)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=260)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=300)    
    num_4 = Label(new_window, text='X(4) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=340)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=90,y=340)        
    num_5 = Label(new_window, text='X(5) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=380)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=90,y=380)      
    num_6 = Label(new_window, text='X(6) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=420)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=90,y=420)    
    num_7 = Label(new_window, text='X(7) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=30,y=460)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=90,y=460) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)
    
# New Window for 4 Point (DIT) IDFT    
def open9():
    new_window = Toplevel()
    new_window.title("4 - Point (DIT) IDFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939') 
    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=370,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=670,y=140)   
        cc_val_0 =complex(x_0.get())
        c_val_0 = np.conj(cc_val_0)
        cc_val_1 =complex(x_1.get())
        c_val_1 = np.conj(cc_val_1)
        cc_val_2 =complex(x_2.get())
        c_val_2 = np.conj(cc_val_2)
        cc_val_3 =complex(x_3.get())
        c_val_3 = np.conj(cc_val_3)        
        s_1 = c_val_2 + c_val_0
        s_2 = c_val_0 - c_val_2
        s_3 = c_val_3 + c_val_1
        s_4 = c_val_1 - c_val_3        
        s_1_0 = s_1
        s_2_1 = s_2
        s_3_2 = s_3
        s_4_3 = s_4
        ss_0 = s_3_2 + s_1_0
        ss_1 = ((-1j*s_4_3) + s_2_1 )
        ss_2 = s_1_0 - s_3_2
        ss_3 = (s_2_1 - (-1j*s_4_3))
        fin_0 = ss_0.real
        fin_1 = ss_1.real
        fin_2 = ss_2.real
        fin_3 = ss_3.real
        fin_00 =(round(fin_0)/4)
        fin_11 =(round(fin_1)/4) 
        fin_22 =(round(fin_2)/4) 
        fin_33 =(round(fin_3)/4)  
        
        stage_1_0=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=400,y=180)        
        stage_1_1=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=400,y=260)    
        stage_1_2=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=400,y=340)        
        stage_1_3=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=400,y=420)
                
        stage_2_0=Label(new_window,text=str(fin_00),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=700,y=180)        
        stage_2_1=Label(new_window,text=str(fin_11),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=700,y=260)    
        stage_2_2=Label(new_window,text=str(fin_22),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=700,y=340)        
        stage_2_3=Label(new_window,text=str(fin_33),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=700,y=420)
                
    # Sub-Application-9 Layout                                                    
    Poster_1 = Label(new_window,text="___ 4 - POINT (DIT) IDFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(k)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)
        
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=260)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=260)
       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=340)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=340)
    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=420)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=420)
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300) 
    
    
# New Window for 4 Point (DIF) IDFT    
def open10():
    new_window = Toplevel()
    new_window.title("4 - Point (DIF) IDFT Calculator // Developed By Anshuman Biswal")
    new_window.iconbitmap('Subapp.ico')
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')

# Calculation/Math    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=370,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=670,y=140)
        cc_val_0 =complex(x_0.get())
        c_val_0 = np.conj(cc_val_0)
        cc_val_1 =complex(x_1.get())
        c_val_1 = np.conj(cc_val_1)
        cc_val_2 =complex(x_2.get())
        c_val_2 = np.conj(cc_val_2)
        cc_val_3 =complex(x_3.get())
        c_val_3 = np.conj(cc_val_3)         
        s_0 = c_val_2 + c_val_0
        s_1 = c_val_3 + c_val_1
        s_2 = c_val_0 - c_val_2 
        s_3 = c_val_1 - c_val_3
        ss_0 = s_1 + s_0
        ss_1 = s_0 - s_1
        ss_2 = (complex(s_3)*(-1j)) + s_2
        ss_3 = s_2 - (complex(s_3)*(-1j))
        fin_0 = ss_0.real
        fin_1 = ss_1.real
        fin_2 = ss_2.real
        fin_3 = ss_3.real
        fin_00 =(round(fin_0)/4)
        fin_11 =(round(fin_2)/4) 
        fin_22 =(round(fin_1)/4) 
        fin_33 =(round(fin_3)/4)  
       
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=400,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=400,y=260)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=400,y=340)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=400,y=420)                
        stage_2_0=Label(new_window,text=str(fin_00),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=700,y=180)        
        stage_2_1=Label(new_window,text=str(fin_11),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=700,y=260)    
        stage_2_2=Label(new_window,text=str(fin_22),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=700,y=340)        
        stage_2_3=Label(new_window,text=str(fin_33),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=700,y=420)
                
    # Sub-Application-10 Layout                                                    
    Poster_1 = Label(new_window,text="___ 4 - POINT (DIT) IDFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(k)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Note:- No Need of  'Bit Reversal', Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)       
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=260)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=260)      
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=340)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=340)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=420)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=420)
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)                    
 
#Main Application Layout        
Posterlabel = Label(root, text = "_______ Fast Fourier Transform (FFT) Calculator _______",font=("Arial Rounded MT Bold", 22),bg ='#393939',fg = 'white')
Posterlabel.place(x=140,y=20)

Optionlabel = Label(root, text = "|| Choose the Operation you want to Perform ||",font=("Calibri", 20),bg ='#393939',fg = 'white')
Optionlabel.place(x=270,y=70)

numlabel1 = Label(root, text='(1)', font=('Calibri',18),bg='#393939',fg='white')
numlabel1.place(x=50,y=180)
button1 = Button(root, text = "4 - Point (DIT) FFT",font=("Aachen", 18), bg ='#FF643B', fg = 'black',relief = RAISED,command=open1)
button1.place(x=90,y=180)

numlabel2 = Label(root, text='(2)', font=('Calibri',18),bg='#393939',fg='white')
numlabel2.place(x=50,y=270)
button2 = Button(root, text = "8 - Point (DIT) FFT",font=("Aachen", 18), bg ='#3ED6F6', fg = 'black',relief = RAISED,command=open3)
button2.place(x=90,y=270)

numlabel3 = Label(root, text='(3)', font=('Calibri',18),bg='#393939',fg='white')
numlabel3.place(x=50,y=360)
button3 = Button(root, text = "4 - Point (DIT) IDFT",font=("Aachen", 18), bg ='#D78AF9', fg = 'black',relief = RAISED,command=open9)
button3.place(x=90,y=360)

numlabel4 = Label(root, text='(4)', font=('Calibri',18),bg='#393939',fg='white')
numlabel4.place(x=50,y=450)
button4 = Button(root, text = "8 - Point (DIT) IDFT",font=("Aachen", 18), bg ='#91F96D', fg = 'black',relief = RAISED,command=open7)
button4.place(x=90,y=450)

numlabel5 = Label(root, text='(8)', font=('Calibri',18),bg='#393939',fg='white')
numlabel5.place(x=410,y=450)
button5 = Button(root, text = "4 - Point (DIF) FFT",font=("Aachen", 18), bg ='#FF643B', fg = 'black',relief = RAISED,command=open2)
button5.place(x=450,y=180)

numlabel6 = Label(root, text='(5)', font=('Calibri',18),bg='#393939',fg='white')
numlabel6.place(x=410,y=180)
button6 = Button(root, text = "8 - Point (DIF) FFT",font=("Aachen", 18), bg ='#3ED6F6', fg = 'black',relief = RAISED,command=open4)
button6.place(x=450,y=270)

numlabel7 = Label(root, text='(6)', font=('Calibri',18),bg='#393939',fg='white')
numlabel7.place(x=410,y=270)
button7 = Button(root, text = "4 - Point (DIF) IDFT",font=("Aachen", 18), bg ='#D78AF9', fg = 'black',relief = RAISED,command=open10)
button7.place(x=450,y=360)

numlabel8 = Label(root, text='(7)', font=('Calibri',18),bg='#393939',fg='white')
numlabel8.place(x=410,y=360)
button8 = Button(root, text = "8 - Point (DIF) IDFT",font=("Aachen", 18), bg ='#91F96D', fg = 'black',relief = RAISED,command=open8)
button8.place(x=450,y=450)

button9 = Button(root, text = "Linear Convolution  ",font=("Aachen", 18), bg ='#F1FA2B', fg = 'black',relief = RAISED,command=open6)
button9.place(x=810,y=180)

button10 = Button(root, text = "Circular Convolution",font=("Aachen", 18), bg ='#F1FA2B', fg = 'black',relief = RAISED,command=open5)
button10.place(x=810,y=270)

button11 = Button(root, text = " About Developer     ",font=("Aachen", 18), bg ='#A0C2C2', fg = 'black',relief = RAISED,command=openweb1)
button11.place(x=810,y=360)

button12 = Button(root, text = " User Manual          ",font=("Aachen", 18), bg ='#A0C2C2', fg = 'black',relief = RAISED,command=openweb2)
button12.place(x=810,y=450)

exitbutton = Button(root, text = "Exit Application",font=("Aachen", 18), bg ='#A0C2C2', fg = 'black',relief = RAISED,command=main_exit)
exitbutton.place(x=90,y=550,width=950)
root.mainloop()

#-------------------------- © copyrights owned by Anshuman Biswal ----------------------------------------------------#
