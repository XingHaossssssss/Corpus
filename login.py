import tkinter as tk
from tkinter import messagebox
import random
import mysqlconn as sql
from PIL import Image, ImageTk
from font import *
import re
import home



# 不连接数据库
u_list = ['admin']
pwd_list = ['admin']

# 登录界面
class Login(object):
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.var_user_name = tk.StringVar()
        self.var_user_pwd = tk.StringVar()
        self.var_code = tk.StringVar()
        self.code = self.creat_authcode()

    # 生成有大小写字母、数字组成的6为随机验证码
    def creat_authcode(self):
        res1 = ''
        res2 = ''
        res3 = ''
        for i in range(2):
            num = random.randint(0, 9)
            res1 += str(num)
            big_letter = chr(random.randint(65, 90))
            res2 += str(big_letter)
            low_letter = chr(random.randint(97, 122))
            res3 += str(low_letter)
        string = str(res1+res2+res3)
        return string

    # 登录按钮
    def user_login(self):
        user_name = self.var_user_name.get()
        user_pwd = self.var_user_pwd.get()
        lo_code = self.var_code.get()
        uname_ls = sql.u_name
        upwd_ls = sql.u_password


        # 不连接数据库
        uname_ls = u_list
        upwd_ls = pwd_list

        null = ''
        if user_name == null:
            tk.messagebox.showerror(title='corpus error',
                                    message='输入用户名！')
        elif user_pwd == null:
            tk.messagebox.showerror(title='corpus error',
                                    message='输入密码！')
        elif lo_code == null:
            tk.messagebox.showerror(title='corpus error',
                                    message='输入验证码！')
        else:
            if lo_code == self.code:
                if user_name in uname_ls:
                    if user_pwd in upwd_ls:
                        tk.messagebox.showinfo(title='corpus_user v-text',
                                               message=user_name + ' 欢迎使用!')
                        self.window.destroy()
                        home.home_run()
                    else:
                        tk.messagebox.showerror(title='corpus error',
                                                message='密码错误，请重新输入!')
                else:
                    '''
                    back = tk.messagebox.askyesno(message='未注册，是否注册.')
                    if back:
                        Register().registered()
                    '''
                    tk.messagebox.showerror(title='corpus error',
                                            message='用户名不存在！')
            else:
                tk.messagebox.showwarning(title='Warning！',
                                          message='验证码输入错误！')

    # 注册按钮
    def sign(self):
        self.window.destroy()
        Register().registered()

    # 设置窗口
    # window = tk.Tk()
    def login(self):
        self.window.title('corpus v1.0')
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 400
        window_height = 300
        self.window.geometry('%dx%d+%d+%d' % (window_width, window_height, (screen_width-window_width)/2, (screen_height-window_height)/2))
        '''
        # 创建画布
        canvas = tk.Canvas(window, height=180, width=450)
        # 加载图片
        im = Image.open('image/text.jpg')
        image_file = ImageTk.PhotoImage(im)
        # image_file = tk.photoImage(file='image/text.gif')
        # tkinter.PhotoImage()仅支持 GIF and PGM/PPM 文件格式
        image = canvas.create_image(100, 40, anchor='nw', image=image_file)
        canvas.pack(side='top')
        '''

        # 创建标签
        tk.Label(self.window, text='中 英 对 照 语 料 库', font=('黑体', 24), fg='BlueViolet').place(x=40, y=60)
        tk.Label(self.window, text='用户名', font=font_heiti()).place(x=100, y=140)
        tk.Label(self.window, text='密  码', font=font_heiti()).place(x=100, y=175)
        tk.Label(self.window, text='验证码', font=font_heiti()).place(x=100, y=210)

        # 创建文本框
        entry_user_name = tk.Entry(self.window, textvariable=self.var_user_name)
        entry_user_name.place(x=160, y=140)
        entry_user_pwd = tk.Entry(self.window, textvariable=self.var_user_pwd, show='*')
        entry_user_pwd.place(x=160, y=175)
        entry_code = tk.Entry(self.window, textvariable=self.var_code, width=10)
        entry_code.place(x=160, y=210)

        txt = tk.StringVar()
        txt.set('验证码')

        def click():
            txt.set(self.code)

        codestr = tk.Button(self.window, textvariable=txt, command=click, fg='SeaGreen', bg='#F8F8FF')
        codestr.place(x=240, y=205)

        # 创建注册和登录按钮
        btn_login = tk.Button(self.window, text='登 录', font=font_heiti(), command=self.user_login)
        btn_login.place(x=130, y=250)
        btn_sign_up = tk.Button(self.window, text='注 册', font=font_heiti(), command=self.sign)
        btn_sign_up.place(x=220, y=250)

        self.window.mainloop()


# 注册界面
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
        screen_width = self.window_registered.winfo_screenwidth()
        screen_height = self.window_registered.winfo_screenheight()
        self.window_registered.geometry('300x300+%d+%d' % ((screen_width-300)/2, (screen_height-300)/2))
        self.window_registered.title('corpus 注册')
        y = 30
        y_list = [y, y+40, y+80, y+120, y+160]
        # new_name = tk.StringVar()
        tk.Label(self.window_registered, text='用户名', font=font_heiti()).place(x=50, y=y_list[0])
        entry_new_name = tk.Entry(self.window_registered, textvariable=self.new_name).place(x=120, y=y_list[0])
        # new_pwd = tk.StringVar()
        tk.Label(self.window_registered, text='密  码', font=font_heiti()).place(x=50, y=y_list[1])
        entry_new_pwd = tk.Entry(self.window_registered, textvariable=self.new_pwd, show='*').place(x=120, y=y_list[1])
        # re_new_pwd = tk.StringVar()
        tk.Label(self.window_registered, text='确认密码', font=font_heiti()).place(x=40, y=y_list[2])
        re_entry_new_name = tk.Entry(self.window_registered, textvariable=self.re_new_pwd, show='*').place(x=120, y=y_list[2])
        # new_email = tk.StringVar()
        tk.Label(self.window_registered, text='邮  箱', font=font_heiti()).place(x=50, y=y_list[3])
        entry_email = tk.Entry(self.window_registered, textvariable=self.new_email).place(x=120, y=y_list[3])
        # new_phone = tk.StringVar()
        tk.Label(self.window_registered, text='电  话', font=font_heiti()).place(x=50, y=y_list[4])
        entry_phone = tk.Entry(self.window_registered, textvariable=self.new_phone).place(x=120, y=y_list[4])
        tk.Button(self.window_registered, text='确认注册', font=font_heiti(), command=self.registered_but).place(x=115, y=240)

    def check_email(self, str):
        ans = False
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.match(regex, str):
            ans = True
        return ans

    def check_mobile(self, str):
        ans = False
        list_phone = [139, 138, 137, 136, 135, 134, 159, 158, 157, 150, 151, 152, 147, 188, 187, 182, 183, 184, 178, 170, 196, # 移动号段
                      130, 131, 132, 140, 145, 146, 155, 156, 166, 185, 186, 175, 176, 196,       # 联通号段
                      133, 149, 153, 177, 173, 180, 181, 189, 191, 193, 199,                      # 电信号段
                      162, 165, 167, 170, 171]                                                    # 虚拟运营商号段
        if len(str) == 11 and str.isdigit() and (int(str[:3]) in list_phone):
            ans = True
        return ans

    def creat_uid(self):
        uid = sql.UserInfo().get_uid()
        num = int(uid[-1]) + 1
        if 1 <= num <= 9:
            return str(num).rjust(3, '0')
        elif 10 <= num <=100:
            return str(num).rjust(3, '0')
        else:
            return str(num)


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
        error = 'corpus error'

        # 判断输入框是否为空
        null = ''
        if n_name == null:
            tk.messagebox.showerror(title=error,
                                    message='输入用户名！')
        elif n_name in n_name_ls and n_name in m_name_ls:
            tk.messagebox.showerror(title=error,
                                    message='用户名已经存在！')
        elif n_pwd == null:
            tk.messagebox.showerror(title=error,
                                    message='输入密码！')
        elif re_pwd == null:
            tk.messagebox.showerror(title=error,
                                    message='输入确认密码！')
        elif n_pwd != re_pwd:
            tk.messagebox.showerror(title=error,
                                    message='俩次输入密码不一样！')
        elif n_email == null:
            tk.messagebox.showerror(title=error,
                                    message='输入邮箱！')
        elif n_phone == null:
            tk.messagebox.showerror(title=error,
                                    message='输入电话号码！')
        else:
            if self.check_email(n_email):
                if self.check_mobile(n_phone):
                    tk.messagebox.showinfo(title='corpus',
                                           message='注册成功！')
                    '''
                    # 连数据库
                    id = self.creat_uid()
                    data = (id, '001', n_name, n_pwd, n_email, n_phone, None)
                    sql.registered_insert(data)
                    '''

                    # 不连接数据库
                    u_list.append(n_name)
                    pwd_list.append(n_pwd)

                    self.window_registered.destroy()
                    Login().login()
                else:
                    tk.messagebox.showerror(title=error,
                                            message='电话号码格式不正确')
            else:
                tk.messagebox.showerror(title=error,
                                        message='邮箱格式不正确')
            '''
            tk.messagebox.showinfo(title='corpus',
                                   message='注册成功！')
            self.window_registered.destroy()
            Login().login()
            '''


def run():
    Login().login()