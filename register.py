# 注册界面 没用

import tkinter as tk
from tkinter import messagebox
import mysqlconn as sql
from font import *


class Register(object):
    def __init__(self):
        super().__init__()
        self.window_registered = tk.Tk()
        self.new_name = tk.StringVar()
        self.new_pwd = tk.StringVar()
        self.re_new_pwd = tk.StringVar()
        self.new_email = tk.StringVar()
        self.new_phone = tk.StringVar()

    def registered(self):
        # window_registered = tk.Toplevel(login.window)
        self.window_registered.geometry('300x300')
        self.window_registered.title('corpus 注册')
        y = 30
        y_list = [y, y+40, y+80, y+120, y+160]
        # new_name = tk.StringVar()
        tk.Label(self.window_registered, text='用户名', font=font_heiti()).place(x=50, y=y_list[0])
        entry_new_name = tk.Entry(self.window_registered, textvariable=self.new_name).place(x=120, y=y_list[0])
        # new_pwd = tk.StringVar()
        tk.Label(self.window_registered, text='密  码', font=font_heiti()).place(x=50, y=y_list[1])
        entry_new_pwd = tk.Entry(self.window_registered, textvariable=self.new_pwd).place(x=120, y=y_list[1])
        # re_new_pwd = tk.StringVar()
        tk.Label(self.window_registered, text='确认密码', font=font_heiti()).place(x=40, y=y_list[2])
        re_entry_new_name = tk.Entry(self.window_registered, textvariable=self.re_new_pwd).place(x=120, y=y_list[2])
        # new_email = tk.StringVar()
        tk.Label(self.window_registered, text='邮  箱', font=font_heiti()).place(x=50, y=y_list[3])
        entry_email = tk.Entry(self.window_registered, textvariable=self.new_email).place(x=120, y=y_list[3])
        # new_phone = tk.StringVar()
        tk.Label(self.window_registered, text='电  话', font=font_heiti()).place(x=50, y=y_list[4])
        entry_phone = tk.Entry(self.window_registered, textvariable=self.new_phone).place(x=120, y=y_list[4])
        tk.Button(self.window_registered, text='确认注册', font=font_heiti(), command=self.registered_but).place(x=115, y=240)

    def registered_but(self):
        # 获取输入框输入内容
        n_name = self.new_name.get()
        n_pwd = self.new_pwd.get()
        re_pwd = self.re_new_pwd.get()
        n_email = self.new_email.get()
        n_phone = self.new_phone.get()

        # 获取数据库内容
        n_name_ls = sql.u_name
        m_name_ls = sql.m_name
        name_ls = n_name_ls.append(m_name_ls)

        error = 'corpus error'

        # 判断输入框是否为空
        null = ''
        if n_name == null:
            tk.messagebox.showerror(title=error,
                                    message='输入用户名！')
        elif n_pwd == null:
            tk.messagebox.showerror(title=error,
                                    message='输入密码！')
        elif re_pwd == null:
            tk.messagebox.showerror(title=error,
                                    message='输入密码！')
        elif n_email == null:
            tk.messagebox.showerror(title=error,
                                    message='输入邮箱！')
        elif n_phone == null:
            tk.messagebox.showerror(title=error,
                                    message='输入电话号码！')
        else:
            ask = tk.messagebox.askyesno(title='corpus',
                                         message='注册成功！')
            if ask:
                self.window_registered.quit()



