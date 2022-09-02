import tkinter as tk
from tkinter import messagebox
import random
import mysqlconn as sql
from PIL import Image, ImageTk

# 登录界面


# 生成有大小写字母、数字组成的6为随机验证码
def creat_authcode():
    res1 = ''
    res2 = ''
    # res3 = ''
    for i in range(2):
        num = random.randint(0, 9)
        res1 += str(num)
        big_letter = chr(random.randint(65, 90))
        res2 += str(big_letter)
        # low_letter = chr(random.randint(97, 122))
        # res3 += str(low_letter)
    # string = str(res1+res2+res3)
    string = str(res1 + res2)
    return string



# 设置窗口
window = tk.Tk()
window.title('corpus')
window.geometry('400x300')
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
tk.Label(window, text='中 英 对 照 语 料 库', font=('黑体', 24), fg='BlueViolet').place(x=40, y=60)
tk.Label(window, text='用户名', font=('黑体', 12)).place(x=100, y=140)
tk.Label(window, text='密  码', font=('黑体', 12)).place(x=100, y=175)
tk.Label(window, text='验证码', font=('黑体', 12)).place(x=100, y=210)

# 获取文本框输入内容
var_user_name = tk.StringVar()
var_user_pwd = tk.StringVar()
var_code = tk.StringVar()

# 创建文本框
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=160, y=140)
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd)
entry_user_pwd.place(x=160, y=175)
entry_code = tk.Entry(window, textvariable=var_code, width=10)
entry_code.place(x=160, y=210)

txt = tk.StringVar()
code = creat_authcode()
txt.set('验证码')
def click():
    txt.set(code)
    return 0
codestr = tk.Button(window, textvariable=txt, command=click, fg='SeaGreen', bg='#F8F8FF')
codestr.place(x=240, y=205)

# 创建注册和登录按钮
btn_login = tk.Button(window, text='登 录', font=('黑体', 12))
btn_login.place(x=130, y=250)
btn_sign_up = tk.Button(window, text='注 册', font=('黑体', 12))
btn_sign_up.place(x=220, y=250)

login = window.mainloop()





