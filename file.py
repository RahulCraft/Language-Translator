#Project 5:

"""This is Google Language Translator """


#pip install googletrans==3.1.0a0
#pip insall googletrans


from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from gtts import gTTS


root=Tk()
root.geometry("1080x400")
root.resizable(0,0)
root.title(" Google Translator")
root.config(bg="aqua")
#heading


# create a label 1
Label(root,text="Google Language Translator",font=("arial 20 bold"),
      bg="aqua",fg="blue").pack()

Label(root,text="Made by Rahul Sharma",font=("Arial 20 bold"),
      bg="aqua",fg="gray",width="20",).pack(side="bottom")


Label(root,text="Enter Text",font="arial 17 bold",
      bg="aqua").place(x=180,y=60)

# create a Input Text 
Input_text=Text(root,font="arial 10", height=11,
                wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30,y=100)

# create a lebel 2
Label(root,text="Output",font=("arial 17 bold"),
      bg="aqua").place(x=760,y=60)

#create a output text2
Output_text=Text(root,font="arial 10",height=11,wrap=WORD,padx=5,pady=5,width=60)
Output_text.place(x=600,y=100)


#day 2
language=list(LANGUAGES.values())

src_lang=ttk.Combobox(root,values=language,width=20)
src_lang.place(x=30,y=70)
src_lang.set("Choose input language")
                    

dest_lang=ttk.Combobox(root,values=language,width=22)
dest_lang.place(x=600,y=70)
dest_lang.set("Choose output language")
                    

# create a function
def Translate():
    translator=Translator()
    translated=translator.translate(text=Input_text.get(1.0,END),
                                  src=src_lang.get(),dest=dest_lang.get())
    Output_text.delete(1.0,END)
    Output_text.insert(END,translated.text)

def speak():

    language="hi"
    t=Output_text.get()
    myobj=gTTS(text=t,lang=language,slow=False)
    myobj.save("E://welcome.mp3")
    os.system("E://welcome.mp3")
    


#create Translate Button
trans_btn=Button(root, text="Translate", font="arial 12 bold",
                 pady=5,command=Translate,
                 bg="royal blue1",
                 activebackground="sky blue")
trans_btn.place(x=490,y=180)


#create speak Button 
speak_btn=Button(root, text="Speak", font="arial 12 bold",
                 pady=5,command=speak,
                 bg="royal blue1",
                 activebackground="sky blue")
speak_btn.place(x=780,y=300)

 

