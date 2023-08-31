from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import Label
import visium_sep
#from done import scRNA_sep
import tkinter.messagebox
import sys


# 打开指定的图片文件，缩放至指定尺寸
def get_image(filename, width, height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

def txt_read(files):
    txt_dict = {}
    fopen = open(files)
    for line in fopen.readlines():
        line = str(line).replace("\n","")
        txt_dict[line.split(' ',1)[0]] = line.split(' ',1)[1]
        #split（）函数用法，逗号前面是以什么来分割，后面是分割成n+1个部分，且以数组形式从0开始
    fopen.close()
    return txt_dict

#txt_dict = txt_read('explain.txt')


class visium_App():

    def __init__(self,master):

        self.root = master
        self.root.title("visium Task Progress")
        self.root.geometry("800x600")

        # 创建画布，设置要显示的图片，把画布添加至应用程序窗口
        canvas_root = tkinter.Canvas(self.root, width=800, height=600)
        im_root = get_image('窗口图片.jpg', 800, 600)
        canvas_root.create_image(400, 300, image=im_root)
        canvas_root.pack()

        # 初始化任务进度条
        self.progress = tk.DoubleVar()
        self.progress.set(0.0)

        # 创建label
        self.label = tk.Label(self.root, text="")
        self.label.place(x=30,y=10)

        #global current_path
        #current_path = os.getcwd()

        # 创建按钮并添加点击事件
        self.button_select = tk.Button(self.root, text="Select Folder", command=self.select_folder, fg = "Gold", bg = "#006400") #选择文件夹按钮
        #self.button_select.pack(padx=10, pady=10)
        self.button_select.place(x=30,y=40)

        global adata

        self.button1 = tk.Button(self.root, text="1.Spatial clustering graph", command=self.do_task1,width=25)
        self.button1.place(x=50,y=120)
        self.button2 = tk.Button(self.root, text="2.UMI statistics graph", command=self.do_task2,width=25)
        self.button2.place(x=50,y=190)
        self.button3 = tk.Button(self.root, text="3.nFeature statistics graph", command=self.do_task3,width=25)
        self.button3.place(x=50,y=260)
        self.button4 = tk.Button(self.root, text="4.Heatmap of marker expression", command=self.do_task4,width=30)
        self.button4.place(x=50, y=330)
        self.button5 = tk.Button(self.root, text="5.Clustering of one genes", command=self.do_task5,width=25)
        self.button5.place(x=320, y=120)
        self.button6 = tk.Button(self.root, text="6.Clustering of one genes\nBlack background highlights", command=self.do_task6,width=25)
        self.button6.place(x=320, y=190)
        self.button7 = tk.Button(self.root, text="7.Single cluster graph", command=self.do_task7,width=25)
        self.button7.place(x=320, y=275)


        self.show_select = tk.Button(self.root, text="Slide show result pictures", command=self.display_images, fg = "OrangeRed", bg = "Wheat")  # 幻灯片放映
        #self.show_select.pack(side = 'bottom')
        self.show_select.place(x=620, y=550)

        self.init()

        # 创建进度条并放置在窗口中
        #self.progressbar = Progressbar(self.root, orient="horizontal", length=200, mode="determinate", variable=self.progress)
        #self.progressbar.pack(pady=20)
        #self.progressbar.place(x=300,y=290)

        self.tip = tk.Label(self.root,
                            text="← Please select the data folder before pressing the data processing buttons.",
                            font=('Helvetica', 10, 'bold'))
        self.tip.place(x=120,y=45)

        self.tip_ENpath = tk.Label(self.root,
                            text="[Full English path]",font=('Helvetica', 8, 'italic'))
        self.tip_ENpath.place(x=230, y=23)

        self.message = tk.Label(self.root,
                            text="Please follow the instructions.\nMake sure that the path you choose\nhas the following files:\n    barcodes.tsv.gz\n    barcodes_pos.tsv.gz\n    matrix.mtx.gz\n    features.tsv.gz\n    he_new.png",anchor=SE,justify='left')
        self.message.place(x=540, y=100)

        self.back_main = tk.Button(self.root, text='back',font=('Helvetica', 15, 'bold'),  command=self.back)
        self.back_main.place(x=20, y=550)

        # 创建label
        self.label = tk.Label(self.root, text="")
        #self.label.pack(padx=10, pady=10)
        self.label.place(x=30,y=10)

        global current_path
        current_path = os.getcwd()

        # 创建按钮并添加点击事件
        self.button_select = tk.Button(self.root, text="Select Folder", command=self.select_folder, fg = "Gold", bg = "#006400") #选择文件夹按钮
        #self.button_select.pack(padx=10, pady=10)
        self.button_select.place(x=30,y=40)

        self.min_cells_message = tk.Label(self.root, text="read min cells:", anchor=NW, justify='right')
        self.min_cells_message.place(x=550, y=315)
        self.min_features_message = tk.Label(self.root, text="read min features:", anchor=NW, justify='right')
        self.min_features_message.place(x=550, y=360)

        self.min_cells = tk.Text(self.root, height=1.5, width=8)
        self.min_cells.place(x=680, y=310)
        self.min_features = tk.Text(self.root, height=1.5, width=8)
        self.min_features.place(x=680, y=360)

        self.dims_message = tk.Label(self.root, text="dims:", anchor=NW, justify='right')
        self.dims_message.place(x=550, y=415)
        self.resolution_message = tk.Label(self.root, text="resolution:", anchor=NW, justify='right')
        self.resolution_message.place(x=550, y=460)

        self.dims = tk.Text(self.root, height=1.5, width=8)
        self.dims.place(x=680, y=410)
        self.resolution = tk.Text(self.root, height=1.5, width=8)
        self.resolution.place(x=680, y=460)

        self.point_size_message = tk.Label(self.root, text="point_size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=510)

        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=510)

        self.root.mainloop()

    def init(self):
        self.button1.configure(state=DISABLED)
        self.button2.configure(state=DISABLED)
        self.button3.configure(state=DISABLED)
        self.button4.configure(state=DISABLED)
        self.button5.configure(state=DISABLED)
        self.button6.configure(state=DISABLED)
        self.button7.configure(state=DISABLED)
        self.show_select.configure(state=DISABLED)

    def enable(self):
        self.button1.configure(state=NORMAL)
        self.button2.configure(state=NORMAL)
        self.button3.configure(state=NORMAL)
        self.button4.configure(state=NORMAL)
        self.button5.configure(state=NORMAL)
        self.button6.configure(state=NORMAL)
        self.button7.configure(state=NORMAL)
        self.show_select.configure(state=NORMAL)

    def do_task1(self):
        global adata
        self.button1.configure(text="busy...", state=DISABLED)

        if self.min_cells.get("1.0", "end") != '\n' :
            min_cells = self.min_cells.get("1.0", "end")
        else:
            min_cells = '10'

        if self.min_features .get("1.0", "end") != '\n' :
            min_features = self.min_features .get("1.0", "end")
        else:
            min_features = '100'

        if self.dims.get("1.0", "end") != '\n' :
            dims = self.dims.get("1.0", "end")
        else:
            dims = '30'

        if self.resolution.get("1.0", "end") != '\n' :
            resolution = self.resolution.get("1.0", "end")
        else:
            resolution = '0.5'

        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '3'

        adata = visium_sep.tran_1(folder_path,min_cells,min_features,dims,resolution,point_size)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button1.configure(text="1.The spatial clustering graph\n完成/重启", fg='DarkCyan', state=NORMAL)

        self.message.update()
        self.resolution.destroy()
        self.resolution_message.destroy()
        self.min_cells.destroy()
        self.min_cells_message.destroy()
        self.min_features.destroy()
        self.min_features_message.destroy()
        self.dims.destroy()
        self.dims_message.destroy()
        self.point_size.destroy()
        self.point_size_message.destroy()

        self.point_size_message = tk.Label(self.root, text="point size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=365)
        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=360)

    def do_task2(self):
        global adata
        self.button2.configure(text="busy...", state=DISABLED)

        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '3'

        adata = visium_sep.tran_2(folder_path,point_size)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button2.configure(text="2.The UMI statistics graph\n完成/重启", fg='DarkCyan', state=NORMAL)

        self.point_size.destroy()
        self.point_size_message.destroy()

        self.point_size_message = tk.Label(self.root, text="point size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=365)
        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=360)

    def do_task3(self):
        global adata
        self.button3.configure(text="busy...", state=DISABLED)

        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '2'
        adata = visium_sep.tran_3(folder_path,point_size)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button3.configure(text="3.The nFeature statistics graph\n完成/重启", fg='DarkCyan', state=NORMAL)

        self.point_size.destroy()
        self.point_size_message.destroy()

        self.point_size_message = tk.Label(self.root, text="point size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=365)
        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=360)


    def do_task4(self):
        global adata
        self.button4.configure(text="busy...", state=DISABLED)
        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '2'
        adata = visium_sep.tran_4(folder_path,point_size)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button4.configure(text="4.Heat map of marker gene expression\n完成/重启", fg='DarkCyan', state=NORMAL)

        self.point_size.destroy()
        self.point_size_message.destroy()

        self.point_size_message = tk.Label(self.root, text="point size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=315)
        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=310)

        self.top_gene_message = tk.Label(self.root, text="top gene num:", anchor=NW, justify='right')
        self.top_gene_message.place(x=550, y=360)
        self.top_gene = tk.Text(self.root, height=1.5, width=8)
        self.top_gene.place(x=680, y=360)

        self.min_pct_message = tk.Label(self.root, text="min pct:", anchor=NW, justify='right')
        self.min_pct_message.place(x=550, y=415)
        self.min_pct = tk.Text(self.root, height=1.5, width=8)
        self.min_pct.place(x=680, y=410)

        self.logfc_threshold_message = tk.Label(self.root, text="logfc threshold:", anchor=NW, justify='right')
        self.logfc_threshold_message.place(x=550, y=460)
        self.logfc_threshold = tk.Text(self.root, height=1.5, width=8)
        self.logfc_threshold.place(x=680, y=460)

    def do_task5(self):
        global adata
        self.button5.configure(text="busy...", state=DISABLED)
        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '2'

        if self.top_gene .get("1.0", "end") != '\n' :
            top_gene = self.top_gene.get("1.0", "end")
        else:
            top_gene = '1'

        if self.min_pct.get("1.0", "end") != '\n' :
            min_pct = self.min_pct.get("1.0", "end")
        else:
            min_pct = '0.25'

        if self.logfc_threshold.get("1.0", "end") != '\n' :
            logfc_threshold = self.logfc_threshold.get("1.0", "end")
        else:
            logfc_threshold = '0.25'
        adata = visium_sep.tran_5(folder_path,point_size,top_gene,min_pct,logfc_threshold)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button5.configure(text="5.Cluster map of one or some genes\n完成/重启", fg='DarkCyan', state=NORMAL)

        self.point_size_message.destroy()
        self.point_size.destroy()
        self.top_gene_message.destroy()
        self.top_gene.destroy()
        self.min_pct_message.destroy()
        self.min_pct.destroy()
        self.logfc_threshold_message.destroy()
        self.logfc_threshold.destroy()

        self.point_size_message = tk.Label(self.root, text="point size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=365)
        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=360)

        self.gene_list_message = tk.Label(self.root, text="gene_list (divide with spaces):", anchor=NW, justify='right')
        self.gene_list_message.place(x=550, y=415)
        self.gene_list = tk.Text(self.root, height=3, width=20)
        self.gene_list.place(x=680, y=410)

    def do_task6(self):
        global adata
        self.button6.configure(text="busy...", state=DISABLED)

        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '2.6'

        if self.gene_list.get("1.0", "end") != '\n' :
            gene_list = self.gene_list.get("1.0", "end").strip()
            gene_list = "'"+gene_list.replace(" ", "','")+"'"
        else:
            gene_list = 'Solyc07g007755.2'

        adata = visium_sep.tran_6(folder_path,point_size,gene_list)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button6.configure(text="6.Cluster map of one or some genes\n完成/重启", fg='DarkCyan', state=NORMAL)

        self.point_size_message.destroy()
        self.point_size.destroy()
        self.gene_list_message.destroy()
        self.gene_list.destroy()

        self.point_size_message = tk.Label(self.root, text="point size:", anchor=NW, justify='right')
        self.point_size_message.place(x=550, y=365)
        self.point_size = tk.Text(self.root, height=1.5, width=8)
        self.point_size.place(x=680, y=360)


    def do_task7(self):
        global adata
        self.button7.configure(text="busy...", state=DISABLED)
        if self.point_size.get("1.0", "end") != '\n' :
            point_size = self.point_size.get("1.0", "end")
        else:
            point_size = '2'
        adata = visium_sep.tran_7(folder_path,point_size)
        self.root.update()
        tkinter.messagebox.showinfo('System Prompt', 'Task completed.')
        self.button7.configure(text="7.Single cluster graph\n完成/重启", fg='DarkCyan', state=NORMAL)


    def select_folder(self):
        global folder_path
        folder_path = filedialog.askdirectory()
        self.label.config(text="Selected Folder: " + folder_path)
        self.tip.config(text="← data folder selected")
        #self.tip = tk.Label(self.root, text="← data folder selected")
        #self.tip.place(x=130, y=45)
        self.tip.update()
        self.enable()

        f = open('visium_tip.txt')
        visium_tip = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
        f.close()  # 关
        visium_tip = ''.join(visium_tip)

        self.message.config(text=visium_tip,justify='left',wraplength = 250)
        self.message.update()
        self.tip_ENpath.config(text="")
        self.tip_ENpath.update()


    def display_images(self):
        self.top = Toplevel()
        self.top.title('幻灯片展示')
        self.top.geometry("800x600")
        # 创建画布，设置要显示的图片，把画布添加至应用程序窗口
        canvas_top = tkinter.Canvas(self.top, width=800, height=600)
        im_top = get_image(current_path+'/窗口图片.jpg', 800, 600)
        canvas_top.create_image(400, 300, image=im_top)
        canvas_top.pack()
        images = []

        print(folder_path)

        #upDir=os.path.abspath(os.path.join(os.path.dirname(folder_path), os.path.pardir))
        upDir=os.path.abspath (os.path.join (folder_path, "../"))
        print(upDir)
        folder_path_figures = os.listdir(upDir)
        for i in range(len(folder_path_figures)):
            folder_path_figures_add_num=upDir+'/'+folder_path_figures[i]
            for filename in os.listdir(folder_path_figures_add_num):
                if filename.endswith(('.jpg', '.png', '.jpeg')) and filename != 'he_new.png':
                    image = Image.open(os.path.join(folder_path_figures_add_num, filename))
                    image = image.resize((400, 400))
                    images.append(ImageTk.PhotoImage(image))

        if images:
            index = 0

            def show_image():
                nonlocal index

                if index >= len(images):
                    #self.top.label.config(text="已经读取完毕")
                    #label(self.top, text="已经读取完毕")
                    widget = Label(self.top, text="已经读取完毕")
                    widget.config(bg='black', fg='yellow')

                    return
                #im_show = Label(self.top)
                #im_show.config(image=images[index])

                label_img = Label(self.top, image=images[index])
                label_img.configure(image=images[index])
                label_img.place(x=10, y=10)
                #label = tk.Label(self.top, image=images[index])
                #label.pack()

                widget = Label(self.top, text="This is the {} th picture.".format(index + 1),font=('Arial', 15))
                widget.config(bg='black', fg='yellow')
                widget.place(x=500, y=100)

                #explain = Label(self.top, text=txt_dict[str(index)], height=15, width=35,wraplength=300,font=('Arial', 12), justify='left')
                #explain.config(fg="#006400")
                #explain.place(x=450, y=150)



                #explain.update()


                index += 1

                self.top.after(4000, show_image)





            show_image()

        self.top.mainloop()


    def back(self):
        self.root.destroy()
        self.root = tk.Tk()
        from main_show import basedesk  #防止互相调用进入死循环
        basedesk(self.root)



