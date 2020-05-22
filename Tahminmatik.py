from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import os, sys


tablolar=dict()
global butonkapatma
butonkapatma=0
sonuc=0
tiklayis=0
kapaticam=0

#Tablo verilerini saklar
def tablolariekleme(tsayisi,tsayilari):
    tablolar[tsayisi]= tsayilari

#uygulama
class Tahminmatigim(Tk):
    def __init__(self):
        super().__init__()       
        
        self.configure(bg='#181818')
        
        self.title("Tahminmatik")

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        
        
        self.geometry("%dx%d+0+0" % (w, h))
        
#, width=w, height=h 
        self.rame = Frame(master=self)
        self.rame.pack()
        
#master=self.rame,
        self.a=Label(text="Aşağıya tahmin ettiğinizden yüksek bir sayı giriniz.",foreground="#ffde66",background="#181818",font=20)
        self.a.place(x=530,y=0)
        
        self.kullaniciningirdigisayi=Entry( text="",foreground="red",background="green")       
        self.kullaniciningirdigisayi.place(x=540, y=30)

        self.ilkbaslangic=Button(text="O Zaman başlıyalım",command=self.calistir )
        self.ilkbaslangic.place(x=690, y=28,)

        self.hamlesayisi = Label(text="" ,background="#181818",foreground="white",font=20)
        self.hamlesayisi.place(x=550, y=100)
    
        #self.baslama=Button(text=" ",command=self.isleyis)
        #self.baslama.grid(padx=110, pady=3)
      
        #self.etiket2 = Message(master=self.rame,text="50")
        #self.etiket2.place(x=550, y=260)
      
        self.etiket4 = Label(text="",background="#181818",foreground="white",font=20)
        self.etiket4.place(x=475, y=150)
            
            

        self.etiket11 = Message(text="",foreground="#f8f8ff",background="#181818",font=20)
        self.etiket11.place(x=550, y=300)

        self.varbuttonu=Button(text="Var",command=self.varmi)
        self.varbuttonu.place(width=120,x=550, y=190)

        self.yokbutonu=Button(text="Yok",command=self.yokmu)
        self.yokbutonu.place(width=120,x=700, y=190)

        #self.hazir=Button(text="Devam et ",command=self.programdevami)
        #self.hazir.grid(row=13,column=1)
        
        
        #self.cevabi = Message(master=self.rame,text="")
        #self.cevabi.place(x=90, y=75)
     
        self.protocol("WM_DELETE_WINDOW", self.kapatma)
       
       # self.kapatmabutonu=Button(master=self.rame,text="Programdan Çıkış",command=self.kapatma)
       # self.kapatmabutonu.place(x=0,y=745)
        
    def kapatma(self):
        if messagebox.askokcancel("Uyarı", "Uygulama Kapatılsın mı?"):
            self.destroy()
    #Hamle sayınısını bulur
    def calistir(self):
        global n1uzunluk
        global n2uzunluk 
        global n1
        global n2     
        global buyukluk  
           
        veri=self.kullaniciningirdigisayi.get()
        buyukluk=int(veri)  
        if buyukluk<=2000:
                        
            n1=[*range(1,buyukluk+1)]
            n2=[]       
            for i in n1:
                if buyukluk>=2**i:
                    n2.append(i)
            n2uzunluk=len(n2)+1
            n1uzunluk=len(n1)
            
            messagebox.showwarning("Hamle Sayısı" ,("Tuttuğunuz sayı {} hamlede bulunacaktır.".format(n2uzunluk)))
            self.hamlesayisi["text"]="Tuttuğunuz sayı {} hamlede bulunacaktır.".format(n2uzunluk)  
            #self.baslama["text"]="Sadece {} Hamle hadi devam".format(n2uzunluk)
            self.ilkbaslangic["state"]="disabled"
            self.isleyis()
            if buyukluk>=1000:
                self.etiket11.place(x=300,y=280)
        else:
            messagebox.showinfo("Update","Uygulama Beta sürümdedir lütfen  2000 ve daha düşük bir sayı giriniz.")

    def ekranayazdir(self):
        global butonkapatma
        global buyukluk
        global cevap
        global oldumu
        global sonuc
       
        
        cevap=0

       
        keke=tablolar.get(butonkapatma+1)
        oldumu=keke

        
        self.etiket11["text"]=str(oldumu)[1:-1] 

        
    def varmi(self):
        global butonkapatma
        global oldumu
        global sonuc
        global tiklayis
        global kapaticam
        global n2uzunluk
        
        
        sonuc+=oldumu[0]
        butonkapatma+=1
        print(butonkapatma)
        self.ekranayazdir()
        
        
        if n2uzunluk==butonkapatma:
            #self.hazir["state"]="disabled"
            self.varbuttonu["state"]="disabled"
            self.yokbutonu["state"]="disabled"
            #self.cevabi["text"]=sonuc 
            self.etiket11["text"]=" " 
            messagebox.showinfo("Cevap","Tuttuğunuz sayı \n {}".format(sonuc))
        

    def yokmu(self):
        global butonkapatma
        global oldumu
        global sonuc
        global tiklayis
        global kapaticam
        global n2uzunluk
        
         
        butonkapatma+=1
        self.ekranayazdir()
        
        print(butonkapatma)
        if n2uzunluk==butonkapatma:
            #self.hazir["state"]="disabled"
            self.varbuttonu["state"]="disabled"
            self.yokbutonu["state"]="disabled"
            #self.cevabi["text"]=sonuc 
            self.etiket11["text"]=" " 
            messagebox.showinfo("Cevap","Tuttuğunuz sayı \n {}".format(sonuc))
       

    

    def isleyis(self):
        global tablo
        global varmıyokmu
        global tablo
        global tablo2
        varmıyokmu =2
        tablo=[]
        tablo2=[]
        cevap=0
        for j in range(n2uzunluk):
            for i in n1:
                k=bin(i)[2:]
                k=int(k)
                if (k//10**j)%10==1:
                    k=str(k)
                    k=int(k,2)
                    tablo.append(k)

            metina=("tablo:",j+1," ",tablo)            
            tablo2 = tablo.copy()
            tablolariekleme(j+1,tablo2)
            
                    
            self.etiket4["text"]="Tuttuğunuz sayı tabloda var mı?, Tabloda varsa Var butonu yoksa Yok butonuna basınız"
            
            tablo.clear()
        #self.baslama["state"]="disabled"
        self.ekranayazdir()    
             
   










tahminmatigim=Tahminmatigim()

tahminmatigim.mainloop()