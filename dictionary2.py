from tkinter import *
import json
from tkinter import *
import tkinter.messagebox

data = json.load(open("data.json"))

from difflib import get_close_matches
class Dictionary:
    def __init__(self,master):
        master=master
        master.title("Panda Dictionary 2.0")
        master.title="Panda Dictionary 2.0"
        master.geometry("800x400")


    # def buttons(self,master,text,fun,row=0,col=0):
    #     self.button=Button(master,text=text)
    #     self.button.place(x=row,y=col)


    def titlebar(self,text):
        main_menu.add_cascade(label=text)
    def label(self,where,text,row=0,col=0):

        self.label=Label(where,text=text)
        self.label.place(x=row,y=col)




class Buttons:
    def __init__(self,master,text,row=0,col=0):
        self.button=Button(master,text=text)
        self.button.place(x=row,y=col)


class functions:
    def message_prompt():
        ourMessage = 'SORRY !! currently there is no such word in the english dictionary'
        tkinter.messagebox.showinfo("WTF!!", ourMessage)

    def search(event):
        try:
            pic_label3.place_forget()
            yes_button.place_forget()
            no_button.place_forget()
            text_label.place_forget()
        except:
            pass
        word=word_input_field.get()

        meaning=functions.give_meaning(word)
        functions.give_output(meaning)
    def search2(event):
        try:
            pic_label3.place_forget()
            yes_button.place_forget()
            no_button.place_forget()
            text_label.place_forget()
        except:
            pass

        word=get_close_matches(word_input_field.get(), data.keys())[0]
        meaning = functions.give_meaning(word)
        functions.give_output(meaning)

    def give_meaning(w):
        w = w.lower()
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys())) > 0:
            return (2)

        else:
            
            try:
                pic_label3.place_forget()
                yes_button.place_forget()
                no_button.place_forget()
                text_label.place_forget()
            except:
                pass
            word = word_input_field.get()
    def give_output(text):

        if (type(text)==list):
            global output_box
            pic_label1.place_forget()
            pic_label2.place(x=50, y=70)
            output_box = Listbox(root, width=200)
            output_box.place(x=350,y=80)
            for item in range(len(text)):
                meaning = str(item + 1) + ")" + text[item]
                output_box.insert(END, meaning)
        elif text==2:
            global yes_button
            global no_button
            global text_label
            text2="Did you mean "+get_close_matches(word_input_field.get(), data.keys())[0]+" ?"
            pic_label2.place_forget()
            pic_label3.place(x=50, y=70)
            try:
                output_box.place_forget()
            except:
                pass


            text_label=Label(root,text=text2)
            text_label.place(x=190,y=110)
            yes_button = Button(root, text="YES")
            yes_button.bind("<Button-1>", functions.search2)
            yes_button.place(x=350,y=110)
            no_button = Button(root, text="NO", command=lambda: functions.message_prompt())
            no_button.place(x=400,y=110)

        else:
            functions.message_prompt()
#MAIN
root = Tk()
app= Dictionary(root)

#Declaring main menu
main_menu=Menu(root)
root.config(menu=main_menu)

#Making the tiles in menu
app.titlebar("Help")
app.titlebar("About")

#Adding Labels
app.label(root,"          ENTER WORD      ",30,20)


#Making Input Text Field
word_entered=StringVar()
word_input_field=Entry(root,textvariable=word_entered)
word_input_field.place(x=200,y=20)



#adding Buttons
button_search=Buttons(root,"Search",330,20)
button_search.button.bind("<Button-1>", functions.search)
# app.buttons(root,"byee")

#adding image

welcome_image= PhotoImage(file="panda hello.png")
search_image= PhotoImage(file="panda dictionary.png")
speak_image= PhotoImage(file="panda speak.png")

pic_label1=Label(root,image=welcome_image)
pic_label1.place(x=50,y=70)

pic_label2=Label(root,image=search_image)

pic_label3=Label(root,image=speak_image)

# functions.give_output()




root.mainloop()