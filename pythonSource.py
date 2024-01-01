#be nam khoda
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

class Mokhatab:
    def __init__(self,nam,nam_khanevadegi,shomare_hamrah,shomare_mahal_sokunat,neshani_manzel,code_melli,address_email):
        self.nam = nam
        self.nam_khanevadegi = nam_khanevadegi
        self.shomare_hamrah = shomare_hamrah
        self.shomare_mahal_sokunat = shomare_mahal_sokunat
        self.neshani_manzel = neshani_manzel
        self.code_melli = code_melli
        self.address_email = address_email
    
    def getNam(self) :
        return self.nam
    def getNam_khanevadegi(self) :
        return self.nam_khanevadegi
    def getShomare_hamrah(self) :
        return self.shomare_hamrah
    def getShomare_mahal_sokunat(self) :
        return self.shomare_mahal_sokunat
    def getNeshani_manzel(self) :
        return self.neshani_manzel
    def getCode_melli(self) :
        return self.code_melli
    def getAddress_email(self) :
        return self.address_email
    
    def setNam(self,nam) :
        self.nam = nam
    def setNam_khanevadegi(self , nam_khanevadegi) :
        self.nam_khanevadegi = nam_khanevadegi
    def setShomare_hamrah(self,shomare_hamrah) :
        self.shomare_hamrah = shomare_hamrah
    def setShomare_mahal_sokunat(self,shomare_mahal_sokunat) :
        self.shomare_mahal_sokunat = shomare_mahal_sokunat
    def setNeshani_manzel(self,neshani_manzel) :
        self.neshani_manzel = neshani_manzel
    def setCode_melli(self,code_melli) :
        self.code_melli = code_melli
    def setAddress_email(self,address_email) :
        self.address_email = address_email    

x = Mokhatab("maziar","ghanbari", "09211862118","061111","abadan","18135555","maziar@gh.com")
x2 = Mokhatab("mehdi","delfi", "09166655451","0612222","khoramshahr","18246666","mehdi@delf.com")
x3 = Mokhatab("mostafa","derisavi", "09393455312","0613333","shiraz","18357777","mstf@drsv.com")
x4 = Mokhatab("mohamadjavad","mashali", "091000154527","0614444","mashhad","18468888","mmdjd@mshl.com")
x5 = Mokhatab("jafar","jasemian", "09789655664","0615555","shadegan","18579999","jafar@salmyn.com")
#x.setNam("ali")
fehrest=[x] 
fehrest.append(x2)
fehrest.append(x3)
fehrest.append(x4)
fehrest.append(x5)

ws = Tk()
ws.title('دفترچه تلفن')
ws.geometry('500x500')
#main window

#btn
def afzudanMokhatab():
     
    mokhatabJadid = Toplevel(ws)
    mokhatabJadid.resizable(False,False)
    mokhatabJadid.title("افزودن مخاطب")
 
    mokhatabJadid.geometry('270x300')
    nam_var= StringVar()
    nam_khanevadegi_var = StringVar()
    shomare_hamrah_var = StringVar()
    shomare_mahal_sokunat_var = StringVar()
    neshani_manzel_var = StringVar()
    code_melli_var = StringVar()
    address_email_var = StringVar()


    frame1 = Frame(mokhatabJadid, padx=5, pady=5)
    
    frame2 = Frame(mokhatabJadid, padx=5, pady=5)
    frame2.grid(row=0, column=1)

    Entry(frame2,textvariable = nam_var).pack(padx=5, pady=5)
    Entry(frame2,textvariable = nam_khanevadegi_var).pack(padx=5, pady=5)
    Entry(frame2,textvariable = shomare_hamrah_var).pack(padx=5, pady=5)
    Entry(frame2,textvariable = shomare_mahal_sokunat_var).pack(padx=5, pady=5)
    Entry(frame2,textvariable = neshani_manzel_var).pack(padx=5, pady=5)
    Entry(frame2,textvariable = code_melli_var).pack(padx=5, pady=5)
    Entry(frame2,textvariable = address_email_var).pack(padx=5, pady=5)
    
    frame1.grid(row=0, column=2)

    Label(frame1, text='نام', padx=5, pady=5).pack()
    Label(frame1, text='نام خانوادگی', padx=5, pady=5).pack()
    Label(frame1, text='شماره همراه', padx=5, pady=5).pack()
    Label(frame1, text='شماره محل سکونت', padx=5, pady=5).pack()
    Label(frame1, text='نشانی محل سکونت', padx=5, pady=5).pack()
    Label(frame1, text='کد ملی', padx=5, pady=5).pack()
    Label(frame1, text='آدرس ایمیل', padx=5, pady=5).pack()
    
    def sabt():
        code_melli = code_melli_var.get()
        if(kavoshCodeMeli(code_melli).getCode_melli() == "-1") :
            nam= nam_var.get()
            nam_khanevadegi = nam_khanevadegi_var.get()
            shomare_hamrah = shomare_hamrah_var.get()
            shomare_mahal_sokunat = shomare_mahal_sokunat_var.get()
            neshani_manzel = neshani_manzel_var.get()
            address_email = address_email_var.get()
            if nam != "" and nam_khanevadegi != "" and shomare_hamrah != "" and shomare_mahal_sokunat != "" and neshani_manzel != "" and address_email != "" and code_melli != "" :
                x = Mokhatab(nam,nam_khanevadegi,shomare_hamrah,shomare_mahal_sokunat,neshani_manzel,code_melli,address_email)
                fehrest.append(x)
                mokhatabJadid.destroy()
                messagebox.showinfo("پیام", "مخاطب با موفقیت ثبت")
            else :
                messagebox.showerror("خطا", "هیچ کادر متنی نمی تواند تهی باشد")    
        else :
            messagebox.showerror("خطا", "کد ملی تکراری است")
    Button(mokhatabJadid, text='ثبت', padx=10,command=sabt).grid(row=1, columnspan=5, pady=5)
def kavoshCodeMeli(codeMelli) :
    for i in fehrest :
        if (i.getCode_melli() == codeMelli) :
            return i
    return Mokhatab("","","","","","-1","")
#btn
def kavoshMokhatab() :
    
    kavoshMokhatab = Toplevel(ws)
    kavoshMokhatab.resizable(False,False)
    kavoshMokhatab.title("جست و جوی مخاطب")
    kavosh_var = StringVar()
    kavoshMokhatab.geometry('600x300')

    

    def kavosh_btn() :
        natije = Toplevel(ws)
        natije.resizable(False,False)
        natije.title("نتیجه کاوش")
        natije.geometry('600x300')
        
        #nam,nam_khanevadegi,shomare_hamrah,shomare_mahal_sokunat,neshani_manzel,code_melli,address_email
        tv = ttk.Treeview(natije)
        tv['columns']=('nam', 'nam_khanevadegi', 'shomare_hamrah' , 'shomare_mahal_sokunat','neshani_manzel','code_melli','address_email')
        tv.column('#0', width=0, stretch=NO)
        tv.column('nam', anchor=CENTER, width=80)
        tv.column('nam_khanevadegi', anchor=CENTER, width=80)
        tv.column('shomare_hamrah', anchor=CENTER, width=80)
        tv.column('shomare_mahal_sokunat', anchor=CENTER, width=80)
        tv.column('neshani_manzel', anchor=CENTER, width=80)
        tv.column('code_melli', anchor=CENTER, width=80)
        tv.column('address_email', anchor=CENTER, width=80)
    
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('nam', text='نام', anchor=CENTER)
        tv.heading('nam_khanevadegi', text='نام خانوادگی', anchor=CENTER)
        tv.heading('shomare_hamrah', text='شماره همراه', anchor=CENTER)
        tv.heading('shomare_mahal_sokunat', text='شماره منزل', anchor=CENTER)
        tv.heading('neshani_manzel', text='نشانی منزل', anchor=CENTER)
        tv.heading('code_melli', text='کد ملی', anchor=CENTER)
        tv.heading('address_email', text='آدرس ایمیل', anchor=CENTER)
    
        kavosh = kavosh_var.get()
        mothatabKavide = kavoshCodeMeli(kavosh)
        nam= "مخاطب یافت نشد"
        nam_khanevadegi = "مخاسب یافت نشد"
        shomare_hamrah = "مخاطب یافت نشد"
        shomare_mahal_sokunat = "مخاطب یافت نشد"
        neshani_manzel = "مخاطب یافت نشد"
        code_melli = "مخاطب یافت نشد"
        address_email = "مخاطب یافت نشد"
        
        if mothatabKavide.getCode_melli() == "-1" :
            pass        
        else :
            nam= mothatabKavide.getNam()
            nam_khanevadegi = mothatabKavide.getNam_khanevadegi()
            shomare_hamrah = mothatabKavide.getShomare_hamrah()
            shomare_mahal_sokunat = mothatabKavide.getShomare_mahal_sokunat()
            neshani_manzel = mothatabKavide.getNeshani_manzel()
            code_melli = mothatabKavide.getCode_melli()
            address_email = mothatabKavide.getAddress_email()
            
        tv.insert(parent='', index=0, iid=0, text='', values=(nam,nam_khanevadegi,shomare_hamrah,shomare_mahal_sokunat,neshani_manzel,code_melli,address_email))
        tv.pack()
        kavoshMokhatab.destroy()
        natije.mainloop()
    Label(kavoshMokhatab, text=' : لطفا کد ملی مخاطب را وارد کرده و سپس بر روی جست و جو کلیک نمایید', padx=5, pady=5).pack(padx=5, pady=5)
    Entry(kavoshMokhatab , textvariable=kavosh_var).pack(padx=5, pady=5)
    Button(kavoshMokhatab, text='جست و جو', padx=10,command=kavosh_btn).pack(padx=5, pady=5)

    
    
    #tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
    
    kavoshMokhatab.mainloop()
#btn
def virayesh() :
    virayeshMokhatab1 = Toplevel(ws)
    virayeshMokhatab1.resizable(False,False)
    virayeshMokhatab1.title("ویرایش مخاطب بر اساس کد ملی")
    virayesh_barasas_codemelli_var = StringVar()
    virayeshMokhatab1.geometry('600x300')

    

    def virayesh_btn_1() :
        virayeshMokhatab2 = Toplevel(ws)
        virayeshMokhatab2.resizable(False,False)
        virayeshMokhatab2.title("ویرایش مخاطب")
        
        virayeshMokhatab2.geometry('270x300')
        nam_var= StringVar()
        nam_khanevadegi_var = StringVar()
        shomare_hamrah_var = StringVar()
        shomare_mahal_sokunat_var = StringVar()
        neshani_manzel_var = StringVar()
        code_melli_var = StringVar()
        address_email_var = StringVar()


        frame1 = Frame(virayeshMokhatab2, padx=5, pady=5)
    
        frame2 = Frame(virayeshMokhatab2, padx=5, pady=5)
        frame2.grid(row=0, column=1)

        Entry(frame2,textvariable = nam_var).pack(padx=5, pady=5)
        Entry(frame2,textvariable = nam_khanevadegi_var).pack(padx=5, pady=5)
        Entry(frame2,textvariable = shomare_hamrah_var).pack(padx=5, pady=5)
        Entry(frame2,textvariable = shomare_mahal_sokunat_var).pack(padx=5, pady=5)
        Entry(frame2,textvariable = neshani_manzel_var).pack(padx=5, pady=5)
        Entry(frame2,textvariable= code_melli_var , state=DISABLED).pack(padx = 5 , pady = 5)
        Entry(frame2,textvariable = address_email_var).pack(padx=5, pady=5)
    
        frame1.grid(row=0, column=2)

        Label(frame1, text='نام', padx=5, pady=5).pack()
        Label(frame1, text='نام خانوادگی', padx=5, pady=5).pack()
        Label(frame1, text='شماره همراه', padx=5, pady=5).pack()
        Label(frame1, text='شماره محل سکونت', padx=5, pady=5).pack()
        Label(frame1, text='نشانی محل سکونت', padx=5, pady=5).pack()
        Label(frame1, text='کد ملی', padx=5, pady=5).pack()
        Label(frame1, text='آدرس ایمیل', padx=5, pady=5).pack()
    
        def virayesh_btn_2():
            nam= nam_var.get()
            nam_khanevadegi = nam_khanevadegi_var.get()
            shomare_hamrah = shomare_hamrah_var.get()
            shomare_mahal_sokunat = shomare_mahal_sokunat_var.get()
            neshani_manzel = neshani_manzel_var.get()
            address_email = address_email_var.get()
            if nam != "" and nam_khanevadegi != "" and shomare_hamrah != "" and shomare_mahal_sokunat != "" and neshani_manzel != "" and address_email != "" :
                for i in fehrest :
                    if (i.getCode_melli() == code_melli_var.get()) :
                        i.setNam(nam)
                        i.setNam_khanevadegi(nam_khanevadegi)
                        i.setShomare_hamrah(shomare_hamrah)
                        i.setShomare_mahal_sokunat(shomare_mahal_sokunat)
                        i.setNeshani_manzel(neshani_manzel)
                        i.setAddress_email(address_email)
                        virayeshMokhatab2.destroy()
                        messagebox.showinfo("پیام","ویرایش مخاطب موفقیت آمیز بود")
            else :
                messagebox.showerror("خطا", "هیچ کادر متنی نمی تواند تهی باشد")    
            
        Button(virayeshMokhatab2, text='ثبت تغییرات', padx=10,command=virayesh_btn_2).grid(row=1, columnspan=5, pady=5)

        codemelliBarayeGashtan = virayesh_barasas_codemelli_var.get()
        mothatabKavide = kavoshCodeMeli(codemelliBarayeGashtan)
        
        if mothatabKavide.getCode_melli() == "-1" :
            virayeshMokhatab1.destroy()
            virayeshMokhatab2.destroy()
            messagebox.showerror("خطا", "هیچ مخاطبی با این کد ملی برای ویرایش یافت نشد")
        else :
            nam= mothatabKavide.getNam()
            nam_khanevadegi = mothatabKavide.getNam_khanevadegi()
            shomare_hamrah = mothatabKavide.getShomare_hamrah()
            shomare_mahal_sokunat = mothatabKavide.getShomare_mahal_sokunat()
            neshani_manzel = mothatabKavide.getNeshani_manzel()
            address_email = mothatabKavide.getAddress_email()
            
            code_melli_var.set(mothatabKavide.getCode_melli())
            nam_var.set(nam)
            nam_khanevadegi_var.set(nam_khanevadegi)
            shomare_hamrah_var.set(shomare_hamrah)
            shomare_mahal_sokunat_var.set(shomare_mahal_sokunat)
            neshani_manzel_var.set(neshani_manzel)
            address_email_var.set(address_email)
            virayeshMokhatab1.destroy()
            virayeshMokhatab2.mainloop()
    Label(virayeshMokhatab1, text=' : لطفا کد ملی مخاطب را وارد کرده و سپس بر روی جست و جوی مخاطب برای ویرایش کلیک نمایید', padx=5, pady=5).pack(padx=5, pady=5)
    Entry(virayeshMokhatab1, textvariable=virayesh_barasas_codemelli_var).pack(padx=5, pady=5)
    Button(virayeshMokhatab1, text='جست و جو مخاطب برای ویرایش', padx=10,command=virayesh_btn_1).pack(padx=5, pady=5)
    
    virayeshMokhatab1.mainloop()
#btn
def hazfBarasasNamKhanevdegi() :
    hazfMokhatab = Toplevel(ws)
    hazfMokhatab.resizable(False,False)
    hazfMokhatab.title("ویرایش مخاطب بر اساس کد ملی")
    namKhanevadegi_var = StringVar()
    hazfMokhatab.geometry('600x300')
    def hazfKardan() :
        ayaHazfShod = False
        namKhanevadegi = namKhanevadegi_var.get()
        for i in fehrest :
            if i.getNam_khanevadegi() == namKhanevadegi :
                fehrest.remove(i)
                ayaHazfShod = True
        if ayaHazfShod :
            messagebox.showinfo("پیام", "مخاطب حذف شد")
            hazfMokhatab.destroy()
        else :
            messagebox.showerror("خطا", "هیچ مخاطبی با این نام خانوادگی برای حذف یافت نشد")
    Label(hazfMokhatab, text=' : لطفا نام خانوادگی مخاطب را وارد کرده و سپس بر روی حذف کردن کلیک نمایید', padx=5, pady=5).pack(padx=5, pady=5)
    Entry(hazfMokhatab, textvariable=namKhanevadegi_var).pack(padx=5, pady=5)
    Button(hazfMokhatab, text='حذف کردن', padx=10,command=hazfKardan).pack(padx=5, pady=5)
    

def gozardan(s,z) :
    gozardan = Toplevel(ws)
    gozardan.resizable(False,False)
    gozardan.title(z)
    gozardan.geometry('600x300')

    frameGozardan = Frame(ws, padx=5, pady=5)
    frameGozardan.place(relx=0.5, rely=0.5, anchor=CENTER)

    tv = ttk.Treeview(gozardan)
    tv['columns']=('nam', 'nam_khanevadegi', 'shomare_hamrah' , 'shomare_mahal_sokunat','neshani_manzel','code_melli','address_email')
    tv.column('shomare_hamrah', anchor=CENTER, width=80)
    tv.column('shomare_mahal_sokunat', anchor=CENTER, width=80)
    tv.column('neshani_manzel', anchor=CENTER, width=80)
    
    tv.heading('shomare_hamrah', text='شماره همراه', anchor=CENTER)
    tv.heading('shomare_mahal_sokunat', text='شماره منزل', anchor=CENTER)
    tv.heading('neshani_manzel', text='نشانی منزل', anchor=CENTER)
    tv.heading('code_melli', text='کد ملی', anchor=CENTER)
    if s == 0 :
        tv['columns']=('nam', 'nam_khanevadegi', 'address_email')
        tv.column('#0', width=0, stretch=NO)
        tv.column('nam', anchor=CENTER, width=80)
        tv.column('nam_khanevadegi', anchor=CENTER, width=80)
        tv.column('address_email', anchor=CENTER, width=80)
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('nam', text='نام', anchor=CENTER)
        tv.heading('nam_khanevadegi', text='نام خانوادگی', anchor=CENTER)
        tv.heading('address_email', text='آدرس ایمیل', anchor=CENTER)        
        ii = 0
        for i in fehrest :
            tv.insert(parent='', index=ii, iid=ii, text='', values=(i.getNam(),i.getNam_khanevadegi(),i.getAddress_email()))
            ii += 1
        tv.pack()
    
        frameGozardan.mainloop()
    elif s == 1 :
        tv['columns']=('nam', 'nam_khanevadegi', 'neshani_manzel')
        tv.column('#0', width=0, stretch=NO)
        tv.column('nam', anchor=CENTER, width=80)
        tv.column('nam_khanevadegi', anchor=CENTER, width=80)
        tv.column('neshani_manzel', anchor=CENTER, width=80)
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('nam', text='نام', anchor=CENTER)
        tv.heading('nam_khanevadegi', text='نام خانوادگی', anchor=CENTER)
        tv.heading('neshani_manzel', text='نشانی منزل', anchor=CENTER)
        ii = 0
        for i in fehrest :
            tv.insert(parent='', index=ii, iid=ii, text='', values=(i.getNam(),i.getNam_khanevadegi(),i.getNeshani_manzel()))
            ii += 1
        tv.pack()
    
        frameGozardan.mainloop()
    elif s == 2 :
        tv['columns']=('nam', 'nam_khanevadegi', 'shomare_hamrah')
        tv.column('#0', width=0, stretch=NO)
        tv.column('nam', anchor=CENTER, width=80)
        tv.column('nam_khanevadegi', anchor=CENTER, width=80)
        tv.column('shomare_hamrah', anchor=CENTER, width=80)
        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('nam', text='نام', anchor=CENTER)
        tv.heading('nam_khanevadegi', text='نام خانوادگی', anchor=CENTER)
        tv.heading('shomare_hamrah', text='شماره همراه', anchor=CENTER)
        ii = 0
        for i in fehrest :
            tv.insert(parent='', index=ii, iid=ii, text='', values=(i.getNam(),i.getNam_khanevadegi(),i.getShomare_hamrah()))
            ii += 1
        tv.pack()
    
        frameGozardan.mainloop()
    
    
#btn
def gozaresh_emailha() :
    gozardan(0,"گزارش رایانامه های مخاطبان")
def gozaresh_neshaniHayeManzeHa() :
    gozardan(1,"گزارش نشانی های منزل های مخاطبان")
def gozaresh_shomareHa() :
    gozardan(2,"گزارش شماره های مخاطبان")
frameMain = Frame(ws, padx=5, pady=5)
frameMain.place(relx=0.5, rely=0.5, anchor=CENTER)
ws.resizable(False,False)
Button(frameMain, text='افزودن مخاطب', padx=10,command=afzudanMokhatab).pack(padx=5, pady=5)
Button(frameMain, text='جست و جوی مخاطب', padx=10,command=kavoshMokhatab).pack(padx=5, pady=5)
Button(frameMain, text='حذف بر اساس نام خانوادگی', padx=10,command=hazfBarasasNamKhanevdegi).pack(padx=5, pady=5)
Button(frameMain, text='ویرایش', padx=10,command=virayesh).pack(padx=5, pady=5)
Button(frameMain, text='گزارش رایانامه مخاطبان', padx=10,command=gozaresh_emailha).pack(padx=5, pady=5)
Button(frameMain, text='گزارش نشانی مخاطبان', padx=10,command=gozaresh_neshaniHayeManzeHa).pack(padx=5, pady=5)
Button(frameMain, text='گزارش شماره مخاطبان', padx=10,command=gozaresh_shomareHa).pack(padx=5, pady=5)

Label(frameMain, text='مازیار قنبری رشته علوم کامپیوتر درس برنامه\nسازی پیشرفته\nشماره دانشجویی : 995193047', padx=5, pady=5).pack()

ws.mainloop()

