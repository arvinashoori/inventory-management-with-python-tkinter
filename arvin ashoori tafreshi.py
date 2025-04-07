import os
from tkinter import *
import tkinter as tk
import pandas as pd
import numpy as np
import sqlite3 as sql
from time import strftime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
import tksheet
from tksheet import Sheet
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PyPDF2 import PdfReader


#------------------------------------------------------------------------------------------------------------------

class value_digit :

    def __set_name__(self , instance , key):
        self.key = key

        
    def __get__(self , instance , owner):
        return instance.__dict__[self.key]

    
    def __set__(self , instance , value):
        if value.isdigit():
            instance.__dict__[self.key] = value
        else:
            instance.__dict__[self.key] = ''


class Gui(Tk):


    def __init__(self):
        Tk.__init__(self)
        
        self.lst_date01 = []
        self.lstt1 = []
        self.lstt2 = []
        self.lst_pro_code = []
        self.lst100 = []
        self.date_string = strftime('%Y/%d/%B')
        self.shomare_sefaresh = 1


        self.main()


#-------------------------------------------------
#----------------------------------------------------
    def inventory(self):
        if not self.frm1.winfo_ismapped():
            self.frm1.grid(row=1,column=1)
        else:
            self.frm1.grid_forget()

            

            
    def new_product(self):
                
        self.frm4 = LabelFrame(self, width=700 , height=600 , text= 'تعریف کالای جدید' , 
                               font = ('calibri' , 11) , relief='groove', padx=2 , pady=2 ,
                               borderwidth=2 , labelanchor='n',bg ='darkgray')

        self.lbl1 = Label(self.frm4 , **self.d4 , text='نام کالا' , padx = 7 , pady = 7).place(x = 530, y = 20)
        self.lbl2 = Label(self.frm4 , **self.d4 , text='نوع بسته بندی', padx = 7 , pady = 7).place(x = 530, y = 80)
        self.lbl3 = Label(self.frm4 , **self.d4 , text='گروه کالا', padx = 7 , pady = 7).place(x = 530, y = 140)
        self.lbl4 = Label(self.frm4 , **self.d4 , text='کد کالا', padx = 7 , pady = 7).place(x = 530, y = 200)
        self.lbl5 = Label(self.frm4 , **self.d4 , text='مشخصات فنی', padx = 7 , pady = 7).place(x = 530, y = 280)
        self.lbl6 = Label(self.frm4 , **self.d4 , text='عکس کالا' , padx = 7 , pady = 7).place(x = 530, y = 390)
        
        self.img2 = PhotoImage(file = '03.png')
        self.ilbl2= Label (self.frm4 , image = self.img2)
        self.ilbl2.place(x = 260 , y = 380)
 
        #self.lbl7 = Label(self.frm4 , **self.d4 , text='عکس کالا' , padx = 7 , pady = 7).place(x = 396, y = 390)
        
        self.ent1 = Entry(self.frm4 , **self.d2 )
        self.ent1.focus()
        self.ent1.place(x=180 , y=21)
        
        self.combo1 = ttk.Combobox(self.frm4 , values = self.v1 , width=30 , height=1)
        self.combo1.set('نوع بسته بندی')
        self.combo1.place(x=180 , y=88)
        
        self.combo2 = ttk.Combobox(self.frm4 , values = self.v2 , width=30 , height=5)
        self.combo2.set('گروه کالا')
        self.combo2.place(x=180 , y=148)
        
        self.ent2 = Entry(self.frm4 , **self.d2 )
        self.ent2.place(x=180 , y=201)

        self.btn18 = Button (self.frm4, **self.d5 ,text = 'بارگذاری' , command = self.callback).place(x=530 , y=315)
        self.btn19 = Button (self.frm4, **self.d5 ,text = 'بارگذاری' , command = self.ax).place(x=530 , y=425)
        self.btn20 = Button (self.frm4, **self.d1 ,text = 'ثبت'     , command = self.record1).place(x=260 , y=520)
        
        
        self.command1 = '''CREATE TABLE IF NOT EXISTS emp(product_code INTEGER PRIMARY KEY ,
                                                          product_name TEXT NOT NULL ,
                                                          package_type TEXT NOT NULL ,
                                                          product_group TEXT NOT NULL ,
                                                          number INTEGER ,
                                                          picture BLOB)'''
        
        self.cur.execute(self.command1) 
        self.con.commit()

        
        
        if not self.frm4.winfo_ismapped():
            self.frm4.place(x = 190 , y = 3)
            self.ent1.focus()
        else:
            self.frm4.grid_forget()

            
#------------------------------------------------------------------
    
    def registration(self):
        
        
        self.frm5 = LabelFrame(self, width=700 , height=600 , text= 'ثبت ورود کالا' , 
                               font = ('calibri' , 11) , relief='groove', padx=2 , pady=2 ,
                               borderwidth=2 , labelanchor='n',bg ='darkgray')

        self.lbl7  = Label(self.frm5 , **self.d9 , text='کد کالا'      , padx = 4 , pady = 4).place(x = 550, y = 20)
        self.lbl8  = Label(self.frm5 , **self.d9 , text='نام کالا'      , padx = 4 , pady = 4).place(x = 550, y = 70)
        self.lbl9  = Label(self.frm5 , **self.d9 , text='نوع بسته بندی' , padx = 4 , pady = 4).place(x = 550, y = 120)
        self.lbl10 = Label(self.frm5 , **self.d9 , text='گروه کالا'    , padx = 4 , pady = 4).place(x = 550, y = 170)
        self.lbl11 = Label(self.frm5 , **self.d9 , text='تعداد کالا'    , padx = 4 , pady = 4).place(x = 160, y = 20)
        self.lbl12 = Label(self.frm5 , **self.d9 , text='عکس کالا'   , padx = 4 , pady = 4).place(x = 160, y = 100)
        
        self.lbl13 = Label(self.frm5 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl13.place(x = 350, y = 20)
        self.lbl14 = Label(self.frm5 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl14.place(x = 350, y = 70)
        self.lbl15 = Label(self.frm5 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl15.place(x = 350, y = 120)
        self.lbl16 = Label(self.frm5 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl16.place(x = 350, y = 170)
        
        self.img3 = PhotoImage(file = '03.png')
        self.ilbl3 = Label (self.frm5 , image = self.img3)
        self.ilbl3.place(x = 30 , y = 80)
        
        
        self.ent3 = Entry(self.frm5 , **self.d8 )
        self.ent3.focus()
        self.ent3.place(x=30 , y=20)
        
        
        self.btn21 = Button(self.frm5, **self.d1 ,text = 'ثبت نهایی'  , command = self.record22).place(x=190 , y=530)
        self.btn22 = Button(self.frm5, **self.d1 ,text = 'جستجو'    , command = self.search1).place(x=350 , y=530)
        self.btn23 = Button(self.frm5, **self.d10,text = 'ثبت'      , command = self.record3).place(x=160 , y=50)
                
       
        if not self.frm5.winfo_ismapped():
            self.frm5.place(x = 190 , y = 3)
            
            self.lst1 = []
            self.row = self.cur.execute('SELECT product_code , product_name , package_type , product_group FROM emp')
            for i in self.row :
                self.lst1.append(i)
            
            self.headers = ['product_code','product_name','package_type','product_group','number']    
                       
            self.sheet1 = Sheet(self.frm5 , data = [[f'{j}' for j in i] for i in self.lst1] ,
                                width=670, height=280, total_columns=5, total_rows=20 ,
                                show_x_scrollbar=True, show_y_scrollbar=True ,
                                headers = ['product_code','product_name','package_type','product_group','number'] ,
                                header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                                table_bg = 'seashell' , index_bg = 'lavender' )
        
            self.sheet1.place(x=10 , y=230)
        
            
            self.sheet1.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                         'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                         'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                         'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                         'rc_delete_row','copy','cut','paste','delete','undo','edit_cell'))
            
            
            
        else:
            self.frm5.grid_forget()
            

#--------------------------------------------------------------------
    
    def orders(self):
        
        self.frm6 = LabelFrame(self, width=700 , height=600 , text= 'سفارشات',
                               font = ('calibri' , 11) , relief='groove',
                               padx=2 , pady=2 ,borderwidth=2 , labelanchor='n',bg ='darkgray')
        
        
        self.btn24 = Button(self.frm6, **self.d11 ,text = 'ثبت  تغییر  وضعیت  کالا'  , command = self.change_status).place(x=270 , y=520)
        
        

        self.command5 = '''CREATE TABLE IF NOT EXISTS sef(order_number    INTEGER PRIMARY KEY UNIQUE ,
                                                          orders_name     TEXT  NOT NULL ,
                                                          order_date      TEXT  NOT NULL ,
                                                          product_name    TEXT  NOT NULL ,
                                                          product_group   TEXT  NOT NULL ,
                                                          product_code    INTEGER  UNIQUE NOT NULL ,
                                                          howmany_orders  INTEGER  NOT NULL ,
                                                          status          TEXT NOT NULL )'''
        
        self.cur.execute(self.command5) 
        self.con.commit()
        
        
        self.lst_1 = []
        self.command_1 = 'SELECT order_number,orders_name,order_date,product_name,product_group,product_code,howmany_orders,status  FROM sef'
        self.row_1 = self.cur.execute(self.command_1)
        
        for i in self.row_1 :
            self.lst_1.append(i)
                
        
        self.headers = ['Order_Number','Orders_Name','Order_Date','Product_Name',
                        'Product_Group','Product_Code','Howmany_Orders','Status']    
                       
        self.sheet2 = Sheet(self.frm6 , data = [[f'{j}' for j in i] for i in self.lst_1] ,
                            width=670, height=490, total_columns=8, total_rows=100 ,
                            show_x_scrollbar=True, show_y_scrollbar=True ,
                            headers = self.headers ,
                            header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                            table_bg = 'seashell' , index_bg = 'lavender' )
        
        self.sheet2.place(x=5 , y=5)
        
            
        self.sheet2.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                     'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                     'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                     'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                     'rc_delete_row','copy','cut','paste','delete','undo'))
            
        
        
        self.sheet2.bind("<Double-Button-1>" , self.double_click)
        
       

        
        
        if not self.frm6.winfo_ismapped():
            self.frm6.place(x = 190 , y = 3)
            
            
           
        else:
            self.frm6.grid_forget()

#-------------------------------------------------------------------------------------------------------            
            
            
#-------------------------------------------------------------------------------------------------------            
            
    def double_click(self , event=None):
        
        self.row1     = self.sheet2.identify_row(event, exclude_index = False, allow_end = True)
        self.column1  = self.sheet2.identify_column(event, exclude_header = False, allow_end = True)    
        self.lst_m1   = [self.row1 , self.column1]
        
        if self.column1 == 7 :
            messagebox.askokcancel(title = 'هشدار' , message = 'آیا از تغییر وضعیت کالا اطمینان دارید؟')
            self.sheet2.set_cell_data(self.row1 , self.column1 , value = 'آماده تحویل' , set_copy = True, redraw = False)


#-----------------------------------------------------------------------------------------------------------        


    def change_status(self):
        
        lst_10 = []
        str1 = 'آماده تحویل'
        
        self.sheet2_data = self.sheet2.get_sheet_data(return_copy = False, get_header = False, get_index = False)
        
        
        
        command_insert_ch_st = '''INSERT INTO ch_status (order_number , orders_name , order_date , product_name , product_group , product_code , howmany_orders , status) VALUES (?,?,?,?,?,?,?,?) '''
        
        for i in self.sheet2_data :
            if i[len(i)-1] == 'آماده تحویل' :
                self.cur.execute(command_insert_ch_st , i)
                self.con.commit()
                lst_10.append(i[0])
                
                
        if len(lst_10) != 0 :
            for i in lst_10 :
                
                command_update_sef = ''' UPDATE sef SET status="{}"  WHERE order_number={} ''' .format(str1 , i)
                self.cur.execute(command_update_sef)
                self.con.commit()
        
        
        command_delet = ''' DELETE FROM sef WHERE status="{}" ''' .format(str1)
        self.cur.execute(command_delet)
        self.con.commit()

        

        self.lst_11 = []
        self.command_11 = 'SELECT order_number,orders_name,order_date,product_name,product_group,product_code,howmany_orders,status  FROM sef'
        self.row_11 = self.cur.execute(self.command_11)

        for i in self.row_11 :
            self.lst_11.append(i)
        
        
        self.sheet22 = Sheet(self.frm6 , data = [[f'{j}' for j in i] for i in self.lst_11] ,
                             width=670, height=490, total_columns=8, total_rows=100 ,
                             show_x_scrollbar=True, show_y_scrollbar=True ,
                             headers = self.headers ,
                             header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                             table_bg = 'seashell' , index_bg = 'lavender' )
        
        self.sheet22.place(x=5 , y=5)
        
            
        self.sheet22.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                     'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                     'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                     'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                     'rc_delete_row','copy','cut','paste','delete','undo'))
            
        

        self.sheet22.bind("<Double-Button-1>" , self.double_click)
        
        
        if not self.frm6.winfo_ismapped():
            self.frm6.place(x = 147 , y = 3)
            
            
           
        else:
            self.frm6.grid_forget()
       
        
#-----------------------------------------------------------------------------------------------------


    def Product_departure(self):
        
        self.frm7 = LabelFrame(self, width=700 , height=600 , text= 'ثبت خروج کالا',
                               font = ('calibri' , 11) , relief='groove',
                               padx=2 , pady=2 ,borderwidth=2 , labelanchor='n',bg ='darkgray')
        
        
        
        
        self.btn30 = Button(self.frm7, **self.d11 ,text = 'ثبت خروج کالا'  , command = self.final_record).place(x=270 , y=520)
                
        
        self.lst_3 = []
        self.command_3 = 'SELECT order_number,orders_name,order_date,product_name,product_group,product_code,howmany_orders,status  FROM ch_status'
        self.row_3 = self.cur.execute(self.command_3)
        
        for i in self.row_3 :
            self.lst_3.append(i)
                
        
        self.headers_3 = ['Order_Number','Orders_Name','Order_Date','Product_Name',
                        'Product_Group','Product_Code','Howmany_Orders','Status']    
                       
        self.sheet_4 = Sheet(self.frm7 , data = [[f'{j}' for j in i] for i in self.lst_3] ,
                            width=670, height=490, total_columns=8, total_rows=100 ,
                            show_x_scrollbar=True, show_y_scrollbar=True ,
                            headers = self.headers_3 ,
                            header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                            table_bg = 'seashell' , index_bg = 'lavender' )
        
        self.sheet_4.place(x=5 , y=5)
        
            
        self.sheet_4.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                     'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                     'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                     'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                     'rc_delete_row','copy','cut','paste','delete','undo'))
            
        
        
        self.sheet_4.bind("<Double-Button-1>" , self.double_click_2)
        
       

        
        
        if not self.frm7.winfo_ismapped():
            self.frm7.place(x = 190 , y = 3)
            
            
           
        else:
            self.frm7.grid_forget()
    
        
#---------------------------------------------------------------------------------------------------       
        
        
    def double_click_2(self , event=None) :
        
        
        self.row2     = self.sheet_4.identify_row(event, exclude_index = False, allow_end = True)
        self.column2  = self.sheet_4.identify_column(event, exclude_header = False, allow_end = True)    
        self.lst_m2   = [self.row2 , self.column2]
        
        if self.column2 == 7 :
            messagebox.askokcancel(title = 'هشدار' , message = 'آیا از تغییر وضعیت کالا اطمینان دارید؟')
            self.sheet_4.set_cell_data(self.row2 , self.column2 , value = 'تحویل داده شد' , set_copy = True, redraw = False)
        
#---------------------------------------------------------------------------------------------------       
        
        
    def final_record(self) :
        
        lst_101 = []
        str2 = 'تحویل داده شد'
        
        self.sheet_4_data = self.sheet_4.get_sheet_data(return_copy = False, get_header = False, get_index = False)
        
        
        
        command_insert_order_date = '''INSERT INTO order_date (order_number , orders_name , order_date , product_name , product_group , product_code , howmany_orders , status) VALUES (?,?,?,?,?,?,?,?) '''
        
        for i in self.sheet_4_data :
            if i[len(i)-1] == 'تحویل داده شد' :
                self.cur.execute(command_insert_order_date , i)
                self.con.commit()
                lst_101.append(i[0])
                
                
        if len(lst_101) != 0 :
            for i in lst_101 :
                
                command_update_ch_status = ''' UPDATE ch_status SET status="{}"  WHERE order_number={} ''' .format(str2 , i)
                self.cur.execute(command_update_ch_status)
                self.con.commit()
        
        
        command_delet_2 = ''' DELETE FROM ch_status WHERE status="{}" ''' .format(str2)
        self.cur.execute(command_delet_2)
        self.con.commit()

        

        self.lst_102 = []
        self.command_102 = 'SELECT order_number,orders_name,order_date,product_name,product_group,product_code,howmany_orders,status  FROM sef'
        self.row_102 = self.cur.execute(self.command_102)
        
        for i in self.row_102 :
            self.lst_102.append(i)

        
        
        
        self.sheet_4 = Sheet(self.frm7 , data = [[f'{j}' for j in i] for i in self.lst_102] ,
                             width=530, height=490, total_columns=8, total_rows=100 ,
                             show_x_scrollbar=True, show_y_scrollbar=True ,
                             headers = self.headers_3 ,
                             header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                             table_bg = 'seashell' , index_bg = 'lavender' )
        
        self.sheet_4.place(x=5 , y=5)
        
            
        self.sheet_4.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                     'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                     'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                     'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                     'rc_delete_row','copy','cut','paste','delete','undo'))
            
        

        self.sheet_4.bind("<Double-Button-1>" , self.double_click_2)
        
        
        if not self.frm7.winfo_ismapped():
            self.frm7.place(x = 147 , y = 3)
            
            
           
        else:
            self.frm7.grid_forget()
            
            
#------------------------------------------------------------------------------------------------------

    def reporting(self):
        
        self.frm8 = LabelFrame(self, width=700 , height=640 , text= 'گزارش گيري',
                               font = ('calibri' , 11) , relief='groove',
                               padx=2 , pady=2 ,borderwidth=2 , labelanchor='n',bg ='darkgray')
        
        
        self.lst50 = []
        self.row50 = self.cur.execute('SELECT product_code , product_name , orders_name , order_date , product_group , howmany_orders FROM order_date')
        for i in self.row50 :
            self.lst50.append(i)
           
                       
        self.sheet_6 = Sheet(self.frm8 , data = [[f'{j}' for j in i] for i in self.lst50] ,
                             width=670, height=140, total_columns=5, total_rows=20 ,
                             show_x_scrollbar=True, show_y_scrollbar=True ,
                             headers = ['product_code' , 'product_name' , 'order_name' , 'orders_date' , 'product_group' , 'howmany_orders'] ,
                             header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                             table_bg = 'seashell' , index_bg = 'lavender')
        
        self.sheet_6.place(x=5 , y=5)
        
            
        self.sheet_6.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                         'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                         'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                         'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                         'rc_delete_row','copy','cut','paste','delete','undo'))
        
        
        self.sheet_6.bind('<Button-1>' , self.on_click)
        self.sheet_6.bind("<Double-Button-1>" ,self.plot)
        
#----------------------------- 

        self.total = self.sheet_6.get_sheet_data(return_copy = False, get_header = False, get_index = False)
        self.lst_total = list(self.total)

            
        
        
        if not self.frm8.winfo_ismapped():
            self.frm8.place(x = 190 , y = 3)
            
        else:
            self.frm8.grid_forget()


#--------------------------------------------------------------------------------------------------------------------            
            
    def on_click(self , event=None):        
        
        self.row00     = self.sheet_6.identify_row(event, exclude_index = False, allow_end = True)
        self.column00  = self.sheet_6.identify_column(event, exclude_header = False, allow_end = True)    
        self.lst_m00   = [self.row00 , self.column00]
        
        self.row00_data = self.sheet_6.get_row_data(self.row00 , return_copy = True)
        self.a = self.row00_data[0]
        
        
        for i in self.lst_total :
            if i[0] == self.a :
                self.lst_pro_code.append(i)
        
        #self.lst100 = []
        for i in self.lst_pro_code :
            if i not in self.lst100 :
                self.lst100.append(i)
        
        
        self.sheet_7 = Sheet(self.frm8 , data = [[f'{j}' for j in i] for i in self.lst100] ,
                             width=670, height=140, total_columns=5, total_rows=20 ,
                             show_x_scrollbar=True, show_y_scrollbar=True ,
                             headers = ['product_code' , 'product_name' , 'orders_name' , 'order_date' , 'product_group' , 'howmany_orders'] ,
                             header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                             table_bg = 'seashell' , index_bg = 'lavender' )
        
        self.sheet_7.place(x=5 , y=161)
        
            
        self.sheet_7.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                         'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                         'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                         'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                         'rc_delete_row','copy','cut','paste','delete','undo'))
        
        
        self.dataa_lst = self.sheet_7.get_sheet_data(return_copy = False, get_header = False, get_index = False)
        for i in self.dataa_lst :
            self.lstt1.append(i[3])
            self.lstt2.append(i[5])
        
        self.lstt1_date = pd.to_datetime(self.lstt1)
        for i in self.lstt1_date :
            self.lst_date01.append(i.month_name())
            
            
        self.lst_nahayi = list(zip(self.lst_date01 , self.lstt2))
        
        self.lst_x_plot = ['January','February','March','April','May','June',
                           'July','August','September','October','November','December']
        
        self.lst_y_plot = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        
        for i in self.lst_nahayi :
            
            for j in range(len(self.lst_x_plot)) :
                
                if self.lst_x_plot[j] == i[0] :
                    
                    self.lst_y_plot[j] = self.lst_y_plot[j] + int(i[1])
                
    def plot(self, event = None):
        
        plt.bar(self.lst_x_plot,self.lst_y_plot)
        frm = LabelFrame(self.frm8,text='نمودار')
        frm.place(x=0,y=240)

        fig = plt.figure(figsize = (6.7,3.5))
        plt.bar(self.lst_x_plot,self.lst_y_plot,color='b',fill = True , width =0.5 , edgecolor = 'g',linewidth = 1)
                 
        
        plt.xticks(rotation=45)
        bar = FigureCanvasTkAgg(fig,frm)
        bar.get_tk_widget().pack(side = RIGHT ,fill = BOTH)

           
            
#-------------------------------------------------------------------------------------------------------

    def staff(self):
        if not self.frm2.winfo_ismapped():
            self.frm2.grid(row=3,column=1)
        else:
            self.frm2.grid_forget()

            
            
    def traffic_report(self):
        pass

    
    
    def leave_registration(self):
        pass

    
    def pay_slip(self):
        pass

#--------------------------------------------------------------------------------------------------------    
    

    def ordering_goods(self,event = None):
        
        
        self.frm9 = LabelFrame(self, width=700 , height=600 , text= 'ثبت سفارش' , 
                               font = ('calibri' , 11) , relief='groove', padx=2 , pady=2 ,
                               borderwidth=2 , labelanchor='n',bg ='darkgray')

        self.lbl17  = Label(self.frm9 , **self.d9 , text='کد کالا'      , padx = 4 , pady = 4).place(x = 550, y = 20)
        self.lbl18  = Label(self.frm9 , **self.d9 , text='نام کالا'      , padx = 4 , pady = 4).place(x = 550, y = 70)
        self.lbl19  = Label(self.frm9 , **self.d9 , text='نوع بسته بندی' , padx = 4 , pady = 4).place(x = 550, y = 120)
        self.lbl20 = Label(self.frm9 , **self.d9 , text='گروه کالا'    , padx = 4 , pady = 4).place(x = 550, y = 170)
        
        self.lbl23 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl23.place(x = 380, y = 20)
        self.lbl24 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl24.place(x = 380, y = 70)
        self.lbl25 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl25.place(x = 380, y = 120)
        self.lbl26 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl26.place(x = 380, y = 170)

        self.ent27 = Entry(self.frm9 , **self.d8 )
        self.ent27.focus()
        self.ent27.place(x=22 , y=23)
        
        self.lbl21 = Label(self.frm9 , **self.d9 , text='تعداد کالا'    , padx = 4 , pady = 4).place(x = 180, y = 20)
        self.lbl28  = Label(self.frm9 , **self.d9 , text='شماره سفارش'    , padx = 4 , pady = 4).place(x = 180 , y = 70)
        self.lbl29  = Label(self.frm9 , **self.d9 , text='سفارش دهنده'    , padx = 4 , pady = 4).place(x = 180, y = 120)
        self.lbl30  = Label(self.frm9 , **self.d9 , text='تاریخ سفارش'    , padx = 4 , pady = 4).place(x = 180, y = 170)
        
        self.lbl31 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl31.place(x = 18, y = 70)
        self.lbl32 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl32.place(x = 18, y = 120)
        self.lbl33 = Label(self.frm9 , **self.d7 , text='- - - -'    , padx = 4 , pady = 4)
        self.lbl33.place(x = 18, y = 170)
        
        
        
        
        
        #self.img4 = PhotoImage(file = '03.png')
        #self.ilbl4 = Label (self.frm9 , image = self.img4)
        #self.ilbl4.place(x = 216 , y = 57)
        
        
        self.btn26 = Button(self.frm9, **self.d1 ,text = 'ثبت سفارش' , command = self.record4).place(x=130 , y=520)
        self.btn27 = Button(self.frm9, **self.d1 ,text = 'جستجو'    , command = self.search2).place(x=270 , y=520)

        
        command_0 = '''SELECT order_number FROM sef'''
        self.row_2 = self.cur.execute(command_0)
        self.lst_row_2 = list(self.row_2)
        
        if len(self.lst_row_2) == 0 :
            self.final_sh_sefaresh = 0
        else :
            self.final_sh = list(self.lst_row_2[-1])
            self.final_sh_sefaresh = self.final_sh[0]
            
        
        
       
        if not self.frm9.winfo_ismapped():
            self.frm9.place(x = 190 , y = 3)
            
            self.lst10 = []
            self.row10 = self.cur.execute('SELECT product_code , product_name , package_type , product_group ,number FROM emp1')
            for i in self.row10 :
                self.lst10.append(i)
            
            self.headers_1 = ['product_code','product_name','package_type','product_group','number']    
                       
            self.sheet3 = Sheet(self.frm9 , data = [[f'{j}' for j in i] for i in self.lst10] ,
                                width=670, height=280, total_columns=5, total_rows=20 ,
                                show_x_scrollbar=True, show_y_scrollbar=True ,
                                headers = self.headers_1 ,
                                header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                                table_bg = 'seashell' , index_bg = 'lavender' )
        
            self.sheet3.place(x=5 , y=220)
        
            
            self.sheet3.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                         'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                         'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                         'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                         'rc_delete_row','copy','cut','paste','delete','undo','edit_cell'))
            
            
            
        else:
            self.frm9.grid_forget()
        
        
#------------------------------------------------------------------------------------------------------------        


    def orders_history(self):

        self.frm10 = LabelFrame(self, width=700 , height=600 , text= 'تاريخچه سفارشات',
                                font = ('calibri' , 11) , relief='groove',
                                padx=2 , pady=2 ,borderwidth=2 , labelanchor='n',bg ='darkgray')

                
        
        self.lst_31 = []
        self.command_31 = 'SELECT order_number,orders_name,order_date,product_name,product_group,product_code,howmany_orders,status  FROM order_date'
        self.row_31 = self.cur.execute(self.command_31)
        
        for i in self.row_31 :
            self.lst_31.append(i)
                
        
        self.headers_31 = ['Order_Number','Orders_Name','Order_Date','Product_Name',
                          'Product_Group','Product_Code','Howmany_Orders','Status']    
                       
        self.sheet_5 = Sheet(self.frm10 , data = [[f'{j}' for j in i] for i in self.lst_31] ,
                            width=670, height=520, total_columns=8, total_rows=100 ,
                            show_x_scrollbar=True, show_y_scrollbar=True ,
                            headers = self.headers_31 ,
                            header_bg = 'lightgray' , header_border_fg = 'black' , header_grid_fg = 'black' ,
                            table_bg = 'seashell' , index_bg = 'lavender' )
        
        self.sheet_5.place(x=5 , y=5)
        
            
        self.sheet_5.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                     'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                     'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                     'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                     'rc_delete_row','copy','cut','paste','delete','undo'))
            

        
        
        if not self.frm10.winfo_ismapped():
            self.frm10.place(x = 190 , y = 3)
            
            
           
        else:
            self.frm10.grid_forget()
               
        
#--------------------------------------------------------------------------------------------------------          
            
    def sale(self):
        if not self.frm3.winfo_ismapped():
            self.frm3.grid(row=5,column=1)
        else:
            self.frm3.grid_forget()

            
            
    def customers_management(self):
        pass

    
    
    def Sales_registration(self):
        pass
    
    
#---------------------------------------------------------------------------------------------------           
            
    def exit(self):
        
        if messagebox.askyesno("انبارداري","آيا از خروج اطمينان داريد؟") >0 :
            
            self.destroy()
            return




    
#----------------------------------------------------------------------------------------------------

    def callback(self):
        
        self.name  = fd.askopenfilename(filetypes=(('pdf files', '*.pdf*'),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        
        self.aa=('File name :    ', os.path.basename(self.name))
        self.bb=('Directory Name:     ', os.path.dirname(self.name))
        
        self.lbl1x  = Label(self.frm4 , text=self.aa, padx = 0 , pady = 0).place(x = 180, y = 285)
        self.lbl1xx = Label(self.frm4 , text=self.bb, padx = 0 , pady = 0).place(x = 180, y = 315)
        

        
#-------------------------------------------------------------------------------------------------------

    def ax(self):
        self.ax = fd.askopenfilename(title ='select an Image',
                                            filetypes=(('png files','*.png'),('gif files','*.gif'),('jpeg files','*.jpg')))
        self.img2['file'] = self.ax

    
#------------------------------------------------------------------------------------------------------

    def record1(self):
        
        product_name1  = self.ent1.get()
        package_type1  = self.combo1.get()
        product_group1 = self.combo2.get()
        product_code1  = self.ent2.get()
        with open(self.ax , mode='rb') as f:
            self.blob_ax = f.read()
        
        
        if len(product_name1)!=0 and len(package_type1)!=0 and len(product_group1)!=0 and len(product_code1)!=0:
            data1 = [product_code1 , product_name1 , package_type1 , product_group1 , self.blob_ax]
            self.con = sql.connect('mydb.db')
            self.cur = self.con.cursor()
            command2 = 'INSERT INTO emp (product_code , product_name , package_type , product_group , picture) VALUES (?,?,?,?,?)'
            self.cur.execute(command2 , data1)
            self.con.commit()
            
        else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')
            
#-------------------------------------------------------------------------------------------------------------------



    def record22(self):
        
        self.lst_my_data = self.sheet1.get_sheet_data(return_copy = False, get_header = False, get_index = False)
        
        for i in self.lst_my_data :
            self.command3 = ''' INSERT INTO anbar (product_code , product_name , package_type , product_group , number ) VALUES (?,?,?,?,?) '''
            self.cur.execute(self.command3 , i)
            self.con.commit()
            
#------------------
            
        for i in range(len(self.lst_my_data)):
            self.command33 = ''' UPDATE emp SET product_code={} , product_name="{}" ,
                                                package_type="{}" , product_group="{}" ,
                                                number={} WHERE product_code = {} '''.format(self.lst_my_data[i][0] ,
                                                                                             self.lst_my_data[i][1] ,
                                                                                             self.lst_my_data[i][2] ,
                                                                                             self.lst_my_data[i][3] ,
                                                                                             self.lst_my_data[i][4] ,
                                                                                             self.lst_my_data[i][0])
            
            self.cur.execute(self.command33)
            self.con.commit()
            
#------------------ 

        self.row_20 = self.cur.execute('''SELECT * FROM emp''')
        self.lst_20 = list(self.row_20)
        
        for i in self.lst_20 :
            lst = list(i)
            self.command20 = ' INSERT INTO emp1 (product_code , product_name , package_type , product_group , number , picture) VALUES (?,?,?,?,?,?)'
            self.cur.execute(self.command20 , lst)
            self.con.commit()
        

            
        command51 = ''' DELETE FROM emp '''
        self.cur.execute(command51) 
        self.con.commit()
            


#-------------------------------------------------------------------------------------------------------------------

    def search1(self):
        
        self.cell_select = self.sheet1.get_cell_data(0,0, return_copy = True)
        self.row_select  = self.sheet1.get_row_data(0, return_copy = True)
        self.lbl13['text'] = self.row_select[0]
        self.lbl14['text'] = self.row_select[1]
        self.lbl15['text'] = self.row_select[2]
        self.lbl16['text'] = self.row_select[3]
        
        command4 = '''SELECT * FROM emp WHERE product_code={}'''.format(self.row_select[0])
        rowx = self.cur.execute(command4)
        
        lst2 = list(rowx)
        self.picture1 = lst2[0][5]
        
        with open('0333.png' , mode='wb') as f:
            f.write(self.picture1)
        
        self.imgxx = PhotoImage(file='0333.png')
        self.ilbl3['image'] = self.imgxx
        
        
#------------------------------------------------------------------------------------------------------------------

    def search2(self):
           
        self.cell_select2 = self.sheet3.get_cell_data(0,0, return_copy = True)
        self.row_select2  = self.sheet3.get_row_data(0, return_copy = True)
        self.lbl23['text'] = self.row_select2[0]
        self.lbl24['text'] = self.row_select2[1]
        self.lbl25['text'] = self.row_select2[2]
        self.lbl26['text'] = self.row_select2[3]
    
        self.lbl33['text'] = self.date_string
        self.lbl32['text'] = 'آروين عشوري'
        self.lbl31['text'] = self.final_sh_sefaresh + 1
        
        command5 = '''SELECT * FROM emp1 WHERE product_code={}'''.format(self.row_select2[0])
        row5 = self.cur.execute(command5)
        
        lst_s2 = list(row5)
        self.picture2 = lst_s2[0][5]
            

            
 
        #with open('search2.png' , mode='wb') as f:
            #f.write(self.picture2)
        
        #self.img_s2 = PhotoImage(file='search2.png')
        #self.ilbl4['image'] = self.img_s2

         
#------------------------------------------------------------------------------------------------------------------        
                
    def record3(self):
        
        code1   = self.lbl13['text']
        name1   = self.lbl14['text']
        type1   = self.lbl15['text']
        group1  = self.lbl16['text']
        number1 = self.ent3.get()
        
        t1 = (code1 , name1 , type1 , group1 , number1)
        
        t2 = self.sheet1.get_column_data(0, return_copy = True)
        
        for i in range(len(t2)):
            if t2[i] == code1 :
                self.sheet1.set_row_data(int(t2[i])-1 , values = t1 , add_columns = True, redraw = False)
            
#--------------------------------------------------------------------------------------------------------------


    def record4(self):
        
        sh_sefaresh             = self.lbl31['text']
        name_sefaresh_dahande   = self.lbl32['text']
        tarikhe_sefaresh        = self.lbl33['text']
        name_kala               = self.lbl24['text']
        goroohe_kala            = self.lbl26['text']
        kode_kala               = self.lbl23['text']
        tedaad_kala             = self.ent27.get()
        #tedaad_kala             = self.lbl27['text']
        vaziyat_kala            = 'در حال بررسی'
        
        data2 = [sh_sefaresh , name_sefaresh_dahande , tarikhe_sefaresh , name_kala , goroohe_kala , kode_kala , tedaad_kala , vaziyat_kala]
        
        command_r4 = '''INSERT INTO sef (order_number , orders_name , order_date , product_name , product_group , product_code , howmany_orders , status) VALUES (?,?,?,?,?,?,?,?) '''
        self.cur.execute(command_r4 , data2)
        self.con.commit()
        
        
        self.command6 = '''CREATE TABLE IF NOT EXISTS sh_sef(sh_sefaresh  INTEGER PRIMARY KEY UNIQUE)'''
        self.cur.execute(self.command6) 
        self.con.commit()
        
        self.lst_sef = [sh_sefaresh]
        command7 = '''INSERT INTO sh_sef (sh_sefaresh) VALUES (?)'''
        self.cur.execute(command7 , self.lst_sef) 
        self.con.commit()
        
        
#========================================================================================================================




    def main(self):

        self.d1 = {'width' : 18  , 'font' : ('calibri' ,12) , 'bd' : 3 , 'relief' : 'groove' , 'bg' : 'snow'}               # Btn
        self.d2 = {'width' : 18  , 'font' : ('calibri' ,16) , 'bd' : 3 , 'relief' : 'sunken' , 'justify' : 'center', 'bg' : 'snow'}# Ent
        self.d3 = {'width' : 18  , 'font' : ('calibri' , 13 , 'bold') , 'bd' : 2 , 'relief' : 'groove' , 'bg' : 'darkgray', 'fg' : 'white'} # Btn
        self.d4 = {'width' : 15  , 'font' : ('calibri' ,12) , 'bd' : 2 , 'relief' : 'groove' , 'bg' : 'lightgray'}          # Lbl
        self.d5 = {'width' : 18  , 'font' : ('calibri' , 10) , 'bd' : 2 , 'relief' : 'groove' ,'bg' : 'snow'}               # Btn
        self.d6 = {'width' : 25  , 'font' : ('calibri' ,12) , 'bd' : 2 , 'relief' : 'groove' }                              # Lbl
        self.d7 = {'width' : 18  , 'font' : ('calibri' , 9) , 'bd' : 3 , 'relief' : 'groove', 'bg' : 'darkgray' }           # Lbl
        self.d8 = {'width' : 19  , 'font' : ('calibri' , 9) , 'bd' : 2 , 'relief' : 'sunken' , 'justify' : 'center', 'bg' : 'snow'}# Ent
        self.d9 = {'width' : 18  , 'font' : ('calibri' , 9) , 'bd' : 2 , 'relief' : 'ridge' , 'bg' : 'lightgray'}           # Lbl
        self.d10= {'width' : 18  , 'font' : ('calibri' , 8) , 'bd' : 2 , 'relief' : 'groove' ,'bg' : 'snow'}                # Btn
        self.d11= {'width' : 20  , 'font' : ('calibri' ,12) , 'bd' : 2 , 'relief' : 'groove' }                              # Lbl
        
        self.v1 = ['تکی','بسته 8 عددی','بسته 16 عددی','بسته 32 عددی' , 'بسته 64 عددی']
        self.v2 = ['تجهیزات نهایی','مصرفی','نمونه کار','وارداتی']

        self.title('انبارداري')
        self.configure(bg='lightblue4')
        self.geometry('900x650+400+50')
        self.resizable(False , False)
        #self.iconbitmap('0.ico')
        self.state('normal')
        
        
        

        
        self.frm1 = LabelFrame(self , relief = 'flat' , padx = 4 , pady = 4,bg ='lightblue4')
        
        self.btn5 = Button(self.frm1,**self.d1,text='تعریف کالای جدید',command = self.new_product).grid(row=1,column=1)
        self.btn6 = Button(self.frm1,**self.d1,text='ثبت ورود کالا'  ,command = self.registration).grid(row=2,column=1)
        self.btn7 = Button(self.frm1,**self.d1,text='سفارشات'      ,command = self.orders).grid(row=3,column=1)
        self.btn8 = Button(self.frm1,**self.d1,text='ثبت خروج کالا'  ,command = self.Product_departure).grid(row=4,column=1)
        self.btn9 = Button(self.frm1,**self.d1,text='گزارش گیری'   ,command = self.reporting).grid(row=5,column=1)

#------------------------------------------------------------------------------------------------------------------------
        
        
        self.frm2 = LabelFrame(self , relief = 'flat' , padx = 4 , pady = 4,bg ='lightblue4')
        
        self.btn10 = Button(self.frm2,**self.d1,text='گزارش تردد'    ,command = self.traffic_report).grid(row=1,column=1)
        self.btn11 = Button(self.frm2,**self.d1,text='ثبت مرخصی'    ,command = self.leave_registration).grid(row=2,column=1)
        self.btn12 = Button(self.frm2,**self.d1,text='فیش حقوقی'     ,command = self.pay_slip).grid(row=3,column=1)
        self.btn13 = Button(self.frm2,**self.d1,text='سفارش کالا'     ,command = self.ordering_goods).grid(row=4,column=1)
        self.btn14 = Button(self.frm2,**self.d1,text='تاریخچه سفارشات'  ,command = self.orders_history).grid(row=5,column=1)

#------------------------------------------------------------------------------------------------------------------------
        
        
        self.frm3 = LabelFrame(self , relief = 'flat' , padx = 4 , pady = 4,bg ='lightblue4')
        
        self.btn15 = Button(self.frm3,**self.d1,text='مدیریت امور مشتریان',command = self.customers_management).grid(row=1,column=1)
        self.btn16 = Button(self.frm3,**self.d1,text='ثبت فروش'       ,command = self.Sales_registration).grid(row=2,column=1)
        
        
        
        
        self.img1 = PhotoImage(file = '02.png')
        ilbl1  = Label (self , image = self.img1)
        ilbl1.place(x = 180 , y = 0)

       
                
        self.btn1 = Button (self, **self.d3 ,text = 'انبار داري'  , command = self.inventory).grid(row =0,column=1,padx=8,pady=2)
        self.btn2 = Button (self, **self.d3 ,text = 'پنل همکاران' , command = self.staff).grid(row =2,column=1,padx=8,pady=2)
        self.btn3 = Button (self, **self.d3 ,text = 'پنل فروش'  , command = self.sale).grid(row =4,column=1,padx=8,pady=2)
        self.btn4 = Button (self, **self.d3 ,text = 'خروج'     , command = self.exit).grid(row =6,column=1,padx=8,pady=2)
        

#------------------------------------------------------------------------------------------------------------------------

        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        
        self.command1 = '''CREATE TABLE IF NOT EXISTS emp(product_code INTEGER PRIMARY KEY ,
                                                          product_name TEXT NOT NULL ,
                                                          package_type TEXT NOT NULL ,
                                                          product_group TEXT NOT NULL ,
                                                          number INTEGER ,
                                                          picture BLOB)'''
        
        self.cur.execute(self.command1) 
        self.con.commit()
        
        
        self.command5 = '''CREATE TABLE IF NOT EXISTS sef(order_number    INTEGER PRIMARY KEY UNIQUE ,
                                                          orders_name     TEXT  NOT NULL ,
                                                          order_date      TEXT  NOT NULL ,
                                                          product_name    TEXT  NOT NULL ,
                                                          product_group   TEXT  NOT NULL ,
                                                          product_code    INTEGER  UNIQUE NOT NULL ,
                                                          howmany_orders  INTEGER  NOT NULL ,
                                                          status          TEXT NOT NULL )'''
        
        self.cur.execute(self.command5) 
        self.con.commit()
        
        
        
        self.command50 = '''CREATE TABLE IF NOT EXISTS anbar(product_code  INTEGER PRIMARY KEY ,
                                                             product_name  TEXT    NOT NULL ,
                                                             package_type  TEXT    NOT NULL ,
                                                             product_group TEXT    NOT NULL ,
                                                             number        INTEGER NOT NULL )'''
        
        self.cur.execute(self.command50) 
        self.con.commit()
        
        
        
        
        

        
        self.command6 = '''CREATE TABLE IF NOT EXISTS sh_sef(sh_sefaresh  INTEGER PRIMARY KEY UNIQUE)'''
        
        self.cur.execute(self.command6) 
        self.con.commit()
        
        

        
        self.command1_1 = '''CREATE TABLE IF NOT EXISTS emp1(product_code INTEGER PRIMARY KEY ,
                                                             product_name TEXT NOT NULL ,
                                                             package_type TEXT NOT NULL ,
                                                             product_group TEXT NOT NULL ,
                                                             number INTEGER ,
                                                             picture BLOB)'''
        
        self.cur.execute(self.command1_1) 
        self.con.commit()
        

        
        
        
        self.command1_2 = '''CREATE TABLE IF NOT EXISTS ch_status(order_number    INTEGER PRIMARY KEY UNIQUE ,
                                                                  orders_name     TEXT  NOT NULL ,
                                                                  order_date      TEXT  NOT NULL ,
                                                                  product_name    TEXT  NOT NULL ,
                                                                  product_group   TEXT  NOT NULL ,
                                                                  product_code    INTEGER  NOT NULL ,
                                                                  howmany_orders  INTEGER  NOT NULL ,
                                                                  status          TEXT     NOT NULL )'''
        
        self.cur.execute(self.command1_2) 
        self.con.commit()
        

        
        
        
        
        self.command1_3 = '''CREATE TABLE IF NOT EXISTS order_date(order_number    INTEGER PRIMARY KEY UNIQUE ,
                                                                   orders_name     TEXT  NOT NULL ,
                                                                   order_date      TEXT  NOT NULL ,
                                                                   product_name    TEXT  NOT NULL ,
                                                                   product_group   TEXT  NOT NULL ,
                                                                   product_code    INTEGER  NOT NULL ,
                                                                   howmany_orders  INTEGER  NOT NULL ,
                                                                   status          TEXT     NOT NULL )'''
        
        self.cur.execute(self.command1_3) 
        self.con.commit()
        


o = Gui()
o.mainloop()
