import sqlite3
import pandas as pd
import tkinter as tk                   #匯入tkinter模組
import tkinter.font as tkFont            # 匯入字型模組
import tkinter.messagebox
from datetime import date, time, datetime
from tkinter import *                  # tkinter 模組
from pprint import pprint              
from tkinter import ttk                  # 匯入下拉選單模組
from tkcalendar import *


# 互動式介面視窗設計

app = tk.Tk()                          # 建立主視窗物件
app.geometry('1200x800')                # 設定主視窗預設尺寸為1200x800
app.resizable(True,True)             # 設定主視窗的寬跟高皆不可縮放
app.title("Ricky's Data Notebook Side Project")  # 設定主視窗標題
app.iconbitmap('瑞奇的數據筆記標誌(調整後).ico')          # 設定主視窗 icon
logo = tk.PhotoImage(file='瑞奇的數據筆記標誌(橫)黑色(調整大小後).png')  # 讀取Logo
ricky_logo = tk.Label(app, image=logo)  # 放置Logo圖案
ricky_logo.place(relx=0.72,rely=0.85)    # 指定Logo放置的位置
Time_Range_title = tk.Label(app, text="1.Time Range：", font=("Courier", 14))    # 左側欄位
Time_Range_title.place(relx=0.05,rely=0.27)
Product_line_title = tk.Label(app, text="2.Product Line：", font=("Courier", 14))   # 左側欄位
Product_line_title.place(relx=0.05,rely=0.6)
Branch_title = tk.Label(app, text="3.Branch：", font=("Courier", 14))   # 左側欄位
Branch_title.place(relx=0.05,rely=0.75)
title = tk.Label(app, text="SQL數據撈取工具", font=("Courier", 20))   # 左側欄位
title.place(relx=0.4,rely=0.03)

# 視窗底部狀態列
statusbar = tk.Label(app, text="   This system was designed by Ricky.    If there is any question, please contact me.    E-mail : rickydatanotebook@gmail.com", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)


# 日曆設置：

# 1.起始日期日曆
# 日歷預設狀態設定：
current_year = int(datetime.now().strftime("%Y"))
current_month = int(datetime.now().strftime("%m"))
current_day = int(datetime.now().strftime("%d"))
cal_from = Calendar(app, selectmode="day", year=current_year, month=current_month, day=current_day, date_pattern='y-mm-dd')
cal_from.place(relx=0.25,rely=0.2)
cal_from_title = tk.Label(app, text="起始日期：", font=("Courier", 18))
cal_from_title.place(relx=0.25,rely=0.14)


# 3.擷取起始日期的函數
def grab_date_from(): 
    date_from_select = tk.Label(app,text=cal_from.get_date(),font=("Courier", 12))
    date_from_select.place(relx=0.35,rely=0.145)
    result = date_from_select.cget("text")
    return result 

# 4.確認起始日期的按鈕
confirm_button_from = Button(app,text='確定',command=grab_date_from)
confirm_button_from.place(relx=0.32,rely=0.46)

# 5.結束日期日曆
cal_to = Calendar(app, selectmode="day", year=int(datetime.now().strftime("%Y")) , month=int(datetime.now().strftime("%m")), day=int(datetime.now().strftime("%d")), date_pattern='y-mm-dd')
cal_to.place(relx=0.55,rely=0.2)
cal_to_title = tk.Label(app, text="結束日期：", font=("Courier", 18))
cal_to_title.place(relx=0.55,rely=0.14)


# 6.擷取結束日期的函數
def grab_date_to(): 
    date_to_select = tk.Label(app,text=cal_to.get_date(),font=("Courier", 12))
    date_to_select.place(relx=0.65,rely=0.145)
    result = date_to_select.cget("text")
    return result

# 8.確認結束日期的按鈕
confirm_button_to = Button(app,text='確定',command=grab_date_to)
confirm_button_to.place(relx=0.62,rely=0.46)



# 其他條件複選框：


# 全選函式
def select_all():
     Electronic_accessories_checkbox.select()
     Fashion_accessories_checkbox.select()
     Food_and_beverages_checkbox.select()
     Health_and_beauty_checkbox.select()
     Home_and_lifestyle_checkbox.select()
     Sports_and_travel_checkbox.select()

# 取消全選函式

def deselect_all():
     Electronic_accessories_checkbox.deselect()
     Fashion_accessories_checkbox.deselect()
     Food_and_beverages_checkbox.deselect()
     Health_and_beauty_checkbox.deselect()
     Home_and_lifestyle_checkbox.deselect()
     Sports_and_travel_checkbox.deselect()

# 全選按鈕
All_select_button = Button(app,text='全選',command=select_all)
All_select_button.place(relx=0.258,rely=0.57)

# 取消全選按鈕
All_select_button = Button(app,text='取消全選',command=deselect_all)
All_select_button.place(relx=0.3,rely=0.57)


# 產品線複選框：
EC_Var = tk.StringVar()
Electronic_accessories_checkbox = tk.Checkbutton(app, text="  Electronic accessories", onvalue="Electronic accessories", offvalue="", variable=EC_Var , height=1, width=20)
Electronic_accessories_checkbox.place(relx=0.25,rely=0.62)

FACC_Var = tk.StringVar()
Fashion_accessories_checkbox = tk.Checkbutton(app, text="  Fashion accessories", onvalue="Fashion accessories", offvalue="", variable=FACC_Var, height=1, width=20)
Fashion_accessories_checkbox.place(relx=0.4,rely=0.62)

FB_Var = tk.StringVar()
Food_and_beverages_checkbox = tk.Checkbutton(app, text="  Food_and_beverages", onvalue="Food_and_beverages", offvalue="", variable=FB_Var, height=1, width=20)
Food_and_beverages_checkbox.place(relx=0.55,rely=0.62)

HB_Var = tk.StringVar()
Health_and_beauty_checkbox = tk.Checkbutton(app, text="  Health_and_beauty", onvalue="Health_and_beauty", offvalue="", variable=HB_Var, height=1, width=20)
Health_and_beauty_checkbox.place(relx=0.2445,rely=0.65)

HL_Var = tk.StringVar()
Home_and_lifestyle_checkbox = tk.Checkbutton(app, text="  Home and lifestyle", onvalue="Home and lifestyle", offvalue="", variable=HL_Var , height=1, width=20)
Home_and_lifestyle_checkbox.place(relx=0.3985,rely=0.65)

ST_Var = tk.StringVar()
Sports_and_travel_checkbox = tk.Checkbutton(app, text="  Sports and travel", onvalue="Sports and travel", offvalue="", variable=ST_Var ,height=1, width=20)
Sports_and_travel_checkbox.place(relx=0.5395,rely=0.65)


# 分店複選框：

A_Var = tk.StringVar()
BranchA_checkbox = tk.Checkbutton(app, text="  Branch A", onvalue="A", offvalue="", variable=A_Var,height=1, width=20)
BranchA_checkbox.place(relx=0.2445,rely=0.755)

B_Var = tk.StringVar()
BranchB_checkbox = tk.Checkbutton(app, text="  Branch B", onvalue="B", offvalue="", variable=B_Var ,height=1, width=20)
BranchB_checkbox.place(relx=0.3985,rely=0.755)

C_Var = tk.StringVar()
BranchC_checkbox = tk.Checkbutton(app, text="  Branch C", onvalue="C", offvalue="", variable=C_Var,height=1, width=20)
BranchC_checkbox.place(relx=0.5395,rely=0.755)




# 匯出CSV：

# 根據日期篩選條件Query資料庫函數
def download_data(date_from,date_to):
    connection = sqlite3.connect('supermarket_dataset.db')
    sql_code = f'''
    SELECT * FROM supermarket_dataset 
    WHERE Date >= '{date_from}' AND  Date <= '{date_to}' 
    AND Product_line In('{EC_Var.get()}','{FACC_Var.get()}','{FB_Var.get()}','{HB_Var.get()}','{HL_Var.get()}','{ST_Var.get()}')
    AND Branch IN('{A_Var.get()}','{B_Var.get()}','{C_Var.get()}')
    ; '''
    result = pd.read_sql_query(sql_code, connection)
    result.to_csv(grab_date_from() + " to " + grab_date_to() + ".csv",encoding='utf-8',index=False)

# 執行完成的通知訊息 
def success_info():
    result = tkinter.messagebox.showinfo(title = '執行完成！',message='下載成功！')
    print(result)


# 匯出按鈕
download_button = Button(app,text='下載csv至資料夾',font=("Courier", 12),command=lambda:[download_data(grab_date_from()+" 00:00:00",grab_date_to()+ " 00:00:00"),success_info()])
download_button.place(relx=0.415,rely=0.87)




app.mainloop()