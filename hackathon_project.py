import requests
from tkinter import *
from tkinter import filedialog
from ocr import *
from youtube import *
from articles import *
from ai_api import *
import customtkinter
from testofcomplex import *

customtkinter.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# from tkinter.ttk import *

def accessYoutube(content, newWindow):
    #print(content)
    content_list = []
   # print(content)
    # for i in content.keys():
    #     content_list.append(i)

    videos = search_videos_by_keywords(content)
    print(videos)
    #anotherWindow = Toplevel()
    #anotherWindow.title("Answer:")
    #anotherWindow.geometry("800x300")
   # label = Label(newWindow, text=videos, font=('Arial', 12)).pack()
    counter = 0
    label = customtkinter.CTkLabel(newWindow, text=videos[counter], font=('Calibri', 22))
    label.pack(padx=20, pady=20)
    counter += 1

    # for item in videos:
    #     label = Label(newWindow, text= item, font=('Arial', 18))
    #     label.pack(padx=20, pady=20)

    print(videos)



def give_info_desired(question):
    newWindow = Toplevel()
    newWindow.title("Minerva")
    newWindow.geometry("800x300")
    customtkinter.CTkLabel(newWindow, text="Choose The Type of Information", font=('Calibri', 28)).pack()
    customtkinter.CTkLabel(newWindow, text="User Input: ", font=('Calibri', 18)).pack()
    buttonframe = Frame(newWindow)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    btn1 = customtkinter.CTkButton(buttonframe, text="Youtube Videos", font=('Calibri', 22), command=lambda: accessYoutube(question, newWindow))
    btn1.grid(row=0, column=0, sticky=W + E, pady=20)
    btn2 = customtkinter.CTkButton(buttonframe, text="Conceptual Summary", font=('Calibri', 22), command=lambda: accessSummary(question, newWindow))
    btn2.grid(row=0, column=1, sticky=W + E, pady=20)
    btn3 = customtkinter.CTkButton(buttonframe, text="Articles", font=('Calibri', 22), command=lambda: accessArticles(question, newWindow))
    btn3.grid(row=0, column=2, sticky=W + E, pady=20)
    customtkinter.CTkLabel(newWindow, text=question, font=('Calibri', 22)).pack()
    buttonframe.pack(fill='x')


def uploadimage():
    filename = filedialog.askopenfilename()
    returned_text = detect_text(filename)
    print(returned_text)
    give_info_desired(returned_text)
    # print('Selected:', filename)
    #### GO THROUGHT THE API TO READ THE QUESTION OUT!!!
    # readquestion= ###
    # give_info_desired(readquestion)

def retrieve_input(textBox):
    inputValue=textBox.get("1.0","end-1c")
    #print(inputValue)
    return inputValue
    # inputValue = txt.get("1.0","end-1c")
    # return inputValue

def type_out_the_question():
    typeWindow = Toplevel()
    typeWindow.title("Type your question out")
    typeWindow.geometry("800x300")
    customtkinter.CTkLabel(typeWindow, text="Type Out Your Question", font=('Calibri', 22)).pack()
    textBox = Text(typeWindow, height=5, width=52, font=('Calibri', 18))
    textBox.pack(padx=20, pady=20)

    button = customtkinter.CTkButton(typeWindow, text="Submit", font=('Calibri', 22), command=lambda: give_info_desired(retrieve_input(textBox)))
    button.pack(padx=10, pady=10)


def primary():
    aFunction()
    customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    root = Tk()
    root.geometry("800x400")
    root.title("MINERVA")
    label = customtkinter.CTkLabel(root, text="Choose What You Want to Input:", font=('Calibri', 28))
    label.pack(padx=20, pady=20)

    buttonframe = Frame(root)
    buttonframe.columnconfigure(0, weight=20)
    buttonframe.columnconfigure(1, weight=20)


    btn1 = customtkinter.CTkButton(buttonframe, text="Upload Your Screenshot", font=('Calibri', 22), command=uploadimage)
    btn1.grid(row=0, column=0, padx=20, pady=10, sticky= W+E)

    btn2 = customtkinter.CTkButton(buttonframe, text="Type the Question", font=('Calibri', 22), command=type_out_the_question)
    btn2.grid(row=0, column=1, padx=20, sticky= W+E)

    buttonframe.pack(fill='x')
    label2 = customtkinter.CTkLabel(root, text="MINERVA - HACKNYU2023", font=('Calibri', 30))
    label2.pack(padx=20, pady=20)
    label2.place(relx = 0.0,
                 rely = 1.0,
                 anchor ='sw')
    root.mainloop()


def accessSummary(content, newWindow):
    ans = get_answer(content)
    string1 = ''
    for i in ans:
        if i != ".":
            if ('{"message":"' in string1):
                string1 = ''
            string1 = string1 + i
        else:
            break

    label = customtkinter.CTkLabel(newWindow, text= string1, font=('Calibri', 22))
    label.pack(padx=20, pady=20)

    # print(type(ans), 'typesjakfnsajkfnlaslafka;lsfk')
    # label = Label(newWindow, text='hello sir', font=('Arial', 18)).pack()


def accessArticles(content, newWindow):
    for i in getArticles(content):
        label = customtkinter.CTkLabel(newWindow, text= getArticles(content), font=('Calibri', 22))
        label.pack(padx=20, pady=20)
    print(getArticles(content))

primary()




