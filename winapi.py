# - **********************************************************
# - Author: Suchin T
# - Date: 2024-09-30 (YYYY-MM-DD)
# - Version: 0.1
# - Function: API Window Application 
# - **********************************************************

from tkinter import *
import json
import requests

Version = "0.1"

window = Tk()
window.title(f"Win api ... ver {Version}")
window.geometry("500x500")
window.config(bg="lightgray")

m_frame_main = Frame(window,bg="white",height=500,width=500)
m_frame_main.pack(expand=True)

m_frame_get = Frame(m_frame_main, height=250, width=500, bg="skyblue")
m_frame_get.grid(row=0,column=0,columnspan=4,rowspan=2, padx=10, pady=10)

m_label_get = Label(master=m_frame_get, text="GET Request", bg="gray")
m_label_get.grid(row=0,column=0,rowspan=1, columnspan=1,sticky=W, padx=10, pady=10)

m_button_get = Button(master=m_frame_get, text="Send GET")
m_button_get.grid(row=0,column=1,rowspan=1,columnspan=1, padx=10,pady=10)

m_button_get_clear = Button(master=m_frame_get, text="Clear GET")
m_button_get_clear.grid(row=0,column=2, rowspan=1, columnspan=1, padx=10, pady=10)

m_label_get_result = Label(master=m_frame_get, text="NULL", bg="white")
m_label_get_result.grid(row=1,column=0,rowspan=1,columnspan=4,padx=10,pady=10, sticky=W)
# -- Design Frame of Post Request ----------------------------------------------------

m_frame_post = Frame(m_frame_main, height=250, width=500, bg="pink")
m_frame_post.grid(row=2,column=0,rowspan=4,columnspan=8, padx=10,pady=10)

m_label_post = Label(master=m_frame_post, text="POST Request", bg="gray")
m_label_post.grid(row=2,column=0,rowspan=1,columnspan=1,sticky=W,padx=10,pady=10)

m_button_post = Button(master=m_frame_post,text="Send POST")
m_button_post.grid(row=2,column=1,rowspan=1,columnspan=1,padx=10,pady=10)

m_button_post_clear = Button(master=m_frame_post,text="Clear POST")
m_button_post_clear.grid(row=2,column=3,rowspan=1,columnspan=1,padx=10,pady=10)

m_label_aItem = Label(master=m_frame_post, text="a item", bg="gray")
m_label_aItem.grid(row=3,column=0, rowspan=1, columnspan=1, padx=10, pady=10, sticky=W)

m_textbox_aItem = Entry(master=m_frame_post, textvariable="")
m_textbox_aItem.grid(row=3,column=1,rowspan=1,columnspan=2,padx=10,pady=10,sticky=W)

m_label_bItem = Label(master=m_frame_post, text="b item",bg="gray")
m_label_bItem.grid(row=4,column=0, rowspan=1, columnspan=1, padx=10, pady=10, sticky=W)

m_textbox_bItem = Entry(master=m_frame_post, textvariable="")
m_textbox_bItem.grid(row=4,column=1,rowspan=1,columnspan=2,padx=10,pady=10,sticky=W)

m_label_post_result = Label(master=m_frame_post, text = "NULL", bg="white")
m_label_post_result.grid(row=5,column=0,rowspan=1,columnspan=2, padx=10, pady=10,sticky=W)

# -- Function ----------------------------------------------------------------------------
def Send_Get_Req(event):
    url = 'http://127.0.0.1:8000/api/get'
    try:
      response = requests.get(url)
      data = response.text
      m_label_get_result.config(text=data)
    except Exception as err:
      m_label_get_result.config(text=err)
      print(err)

def Clear_Get(event):
    if m_label_get_result['text'] != "NULL":
       m_label_get_result.config(text="NULL")

def Send_Post_Req(event):
    url = 'http://127.0.0.1:8000/api/post'
    try:
       data_send = {}
       data_send["aItem"] = m_textbox_aItem.get()
       data_send["bItem"] = m_textbox_bItem.get()
       response = requests.post(url,json=data_send)
       m_label_post_result.config(text=response.text)
    except Exception as err:
       m_label_post_result.config(text=err)
       print(err)

def Clear_Post(event):
    if m_label_post_result['text'] != "NULL":
       m_label_post_result.config(text="NULL")
       m_textbox_aItem.delete(0,END)
       m_textbox_bItem.delete(0,END)

m_button_get.bind('<Button-1>',Send_Get_Req)
m_button_get_clear.bind('<Button-1>',Clear_Get)
m_button_post.bind('<Button-1>',Send_Post_Req)
m_button_post_clear.bind('<Button-1>',Clear_Post)
window.mainloop()