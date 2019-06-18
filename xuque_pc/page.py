from configparser import *
from tkinter import ttk
from tkinter.filedialog import *


class main_page(object):
    def __init__(self, master=None):
        self.root = master
        self.cfg = StringVar()
        self.page_designer()

    def page_designer(self):
        self.main_page = Frame(self.root, width=60, height=40)
        self.main_page.pack()
        # Entry(self.main_page,textvariable=self.cfg,width=35).grid(row=0,column=0,columnspan=2,sticky=W,padx=8,pady=6)
        Entry(self.main_page, textvariable=self.cfg, width=35).grid(row=0, column=0, columnspan=2, padx=8,
                                                                    pady=6)
        Button(self.main_page, text="选择文件", width=15, height=1, command=self.select_file).grid(row=0, column=2)
        Button(self.main_page, text="查询当前配置信息", width=52, height=1, command=self.showinfo).grid(row=1, column=0,
                                                                                                columnspan=3, pady=6)
        Label(self.main_page, text='选择你需要的配置').grid(row=2, column=0, sticky=W)
        self.cmb = ttk.Combobox(self.main_page)
        self.cmb.grid(row=2, column=1, padx=5, sticky=W)
        self.cmb['value'] = (
            '配置1', '配置2', '配置3', '配置4', '配置5', '配置6', '配置7', '配置8', '配置9', '配置10', '配置11', '配置12', '配置13', '配置14',
            '配置15')
        self.cmb.set(self.cmb['value'][0])
        Button(self.main_page, text='确认切换', width=13, height=1, command=self.switch_and_show).grid(row=2, column=2,
                                                                                                   padx=10, pady=20,
                                                                                                   sticky=W)
        self.txt = Text(self.main_page, width=54, height=33, background='#ffffff', borderwidth=3).grid(row=3, column=0,
                                                                                                       columnspan=3,
                                                                                                       padx=5, pady=6,
                                                                                                       sticky=W)
        # self.txt.grid(row=3,column=0,columnspan=3,padx=5,pady=6,sticky=W)

    def config_cfg(self, str=None):
        cfg_dict = {}
        cfg_dict['配置1'] = '192.168.0.1'
        cfg_dict['配置2'] = '192.168.0.2'
        cfg_dict['配置3'] = '192.168.0.3'
        cfg_dict['配置4'] = '192.168.0.4'
        cfg_dict['配置5'] = '192.168.0.5'
        cfg_dict['配置6'] = '192.168.0.6'
        cfg_dict['配置7'] = '192.168.0.7'
        cfg_dict['配置8'] = '192.168.0.8'
        cfg_dict['配置9'] = '192.168.0.9'
        cfg_dict['配置10'] = '192.168.0.10'
        cfg_dict['配置11'] = '192.168.0.11'
        cfg_dict['配置12'] = '192.168.0.12'
        cfg_dict['配置13'] = '192.168.0.13'
        cfg_dict['配置14'] = '192.168.0.14'
        cfg_dict['配置15'] = '192.168.0.15'
        return cfg_dict[str]

    def select_file(self):
        file = askopenfilename()
        self.cfg.set(file)

    def showinfo(self):
        self.txt.delete(0.0, END)
        cfg_path = os.path.abspath(self.cfg.get())
        cfg_file = open(cfg_path, 'r', encoding='gbk')
        self.txt.insert(END, '您当前的配置信息如下:\n======================================================\n')
        for line in cfg_file.readlines():
            if not line.__contains__(';'):
                self.txt.insert(END, line)
        cfg_file.close()

    def switch_and_show(self):
        self.txt.delete(0.0, END)
        key = self.cmb.get()
        ip_value = self.config_cfg(key)
        cfg_path = os.path.abspath(self.cfg.get())
        cfg_init = ConfigParser()
        cfg_init.read(cfg_path, encoding='gbk')
        cfg_init.set(section='game', option='ip', value=ip_value)
        to_write = open(cfg_path, 'w')
        cfg_init.write(to_write)
        to_write.close()
        cfg_read = open(cfg_path, 'r', encoding='gbk')
        self.txt.insert(END, '配置修改成功，最新配置信息如下:\n===============================================\n')
        for line in cfg_read.readlines():
            if not line.__contains__(';'):
                print(line)
                self.txt.insert(END, line)
        cfg_read.close()
