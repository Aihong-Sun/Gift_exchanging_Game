import tkinter as tk
from PIL import ImageTk,Image
import random

#初始化窗口
global myWindow
myWindow = tk.Tk()
#设置标题
myWindow.title('Gift Exchanging')
#设置窗口大小
width = 800
height = 500

global I
I=[]
num = list(range(1, 55))
for i in range(27):
    pair1 = random.choice(num)
    num.remove(pair1)
    pair2 = random.choice(num)
    num.remove(pair2)
    pair = (pair1, pair2)
    I.append(pair)


def create():
    myWindow.destroy()      #删除原界面
    global myWindow1
    myWindow1 = tk.Tk()
    # 设置标题
    myWindow1.title('Gift Exchanging_1')
    # 设置窗口大小
    width = 800
    height = 500
    screenwidth = myWindow1.winfo_screenwidth()     #将界面放置在屏幕最中间
    screenheight = myWindow1.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    myWindow1.geometry(alignstr)
    text = tk.StringVar()
    text.set(I[0])
    status = tk.IntVar()
    def pair():                 #动态更新Label中的数字
        I.remove(I[0])
        text.set(I[0])
    #按钮Pair Begin
    b1 = tk.Button(myWindow1, text='Pair Begin', command=pair,bg="green", font=('Helvetica 10 bold'), relief='raised',
                   width=20,
                   height=3)
    #数字Label
    L = tk.Label(myWindow1, textvariable=text, fg='orange', width=50, height=20, font=('黑体', 180))
    b1.pack(side='top')     #按钮的位置
    L.pack()            #Label的位置
    myWindow1.mainloop()


#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=False)

image2=Image.open(r'New_year.JPG')      #插入图片作为背景图片
background_image = ImageTk.PhotoImage(image2)
w = background_image.width()+200
h = background_image.height()

#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
myWindow.geometry('%dx%d+0+0' % (w,h))
background_label = tk.Label(myWindow, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#创建两个按钮
b1=tk.Button(myWindow, text='Quit',bg="yellow",font=('Helvetica 10 bold'), relief='raised', width=20, height=3)
b1.pack(side='bottom',expand='y',)

b2=tk.Button(myWindow, text='Begin ', bg="orange",command=create,relief='raised',font=('Helvetica 10 bold'),width=20, height=3)
b2.pack(side='bottom',expand='y')
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)

#进入消息循环
myWindow.mainloop()