import tkinter as tk
import os
#import  genai
from tkinter import ttk, messagebox
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(API_KEY=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-exp")
 #========= constant =========== 
app_title = "Chatbot developed by WAJAHAT WAKEEL"
window_size = "900X750"
bg_color = "#ffe6e66" 
font_meta = ("Arial Black", 24 , "bold")
font_sub = ("papyrus", 18, "bold")
text_color= "#000000"
input_bg = "#ffffcc"
btn_color = "#ffd700"
btn_hover = "#fff8dc"
font_main = ("segog UI", 14)
font_log = ("Couier New",12,"bold")
# valid ids
valid_ids = [f"{i:03}" for i in range(1,93)]    
#=========functions==========
def on_enter(e):
    generate_btn.config(bg=btn_hover)
def on_leave(e):
    generate_btn.config(bg=btn_color)   
def validate_student_id(sid):
    return sid in valid_ids

def log_message(message):
    log_output.config(state=tk.NORMAL)
    log_output.insert(tk.END , message + "\n")
    log_output.see(tk.END)
    log_output.config(state=tk.DISABLED)

def call_gemini_api(student_id , quetion):
    try:
        prompt = f"student id:  {student_id}. question: {quetion}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error:  {e}"
    
    def generate_script():
        student_id = student_id_entry.get().strip()
        quetion = quetion_input.get("1.0", tk.END).strip()                                                  


    if not validate_student_id(student_id):
        messagebox.showerror("invalid id", "student id must be between 001 and 092")
        return
    
    if not quetion:
        messagebox.showerror("missing question", "please enter question")
        return
    
    log_message(f"asking for student id{student_id}... \n   {quetion}")
    response = call_gemini_api(student_id , quetion)
    log_message(f"response:\n {response}")

    #============= GUI ==============

    app = tk.Tk()
    app.title(app_title)
    app.geometry(window_size)
    app.configure(bg = bg_color)


  # TITLE SECTION 

title_frame = tk.Frame(app, bg= bg_color)
title_frame.pack(pady=(10,0))

meta_label = tk.Label(title_frame, text="meta" , font=font_meta, fg="blue", bg=bg_color)
meta_label.pack(side=tk.LEFT)
learn_label = tk.Label(title_frame, text= "learn", font=font_meta, fg= "#b8860b", bg= bg_color)
learn_label.pack(side=tk.LEFT)
sub_lable = tk.Label(app , text= " developed by dr. mantashah", font=font_sub , fg= "black", bg = bg_color)
  
main_frame= tk.Frame(app, bg= bg_color)
main_frame.pack(fill=tk.BOTH , expand=True)
    
# id input 
tk.Label(main_frame, text="enter student id (001 to 092):" , font=font_main, bg=bg_color).pack(anchor="w", padx = 40)
student_id_entry = tk.Entry(main_frame, font=font_main, bg = input_bg, fg= text_color)
student_id_entry.pack(fill=tk.X,padx= 40 , pady= (0,20))

# question input
tk.Label(main_frame, text= " enter ypur question :", font= font_main, bg=bg_color).pack(anchor="w",padx= 40)
question_input= tk.Text(main_frame, height=6, font= font_main, bg = input_bg, fg= text_color)
question_input.pack(fill=tk.X, padx=40, pady= (0,20))

#send button
generate_btn= tk.Button(main_frame, text= "send" , font= ("Comic Sans MS", 14, "bold"),
                        bg=bg_color, fg= "navy", relief=tk.FLAT,command=generate_script)
generate_btn.pack(pady= (0,20), ipadx=10)
generate_btn.bind("<enter>",on_enter)
generate_btn.bind("<leave>",on_leave)
 
#log section
tk.Label(main_frame, text="conversation log:", font= ("Comic Sans MS", 14 , "bold"),
                         fg="darkgreen" , bg= bg_color).pack(anchor="w", padx=40)
log_output = tk.Text(main_frame, height=12, font=font_log, bg= "#f4f4f4",
                     fg= "#444444", state=tk.DISABLED, wrap=tk.WORD)
log_output.pack(fill=tk.BOTH,padx=40 , pady= (5,20), expand=True)

app.mainloop()

