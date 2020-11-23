import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tkr
import tkinter as tk
import time
from pprint import pprint

class GuiHandler:
    @staticmethod
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

    def OnMouseWheel(self,event):
        self.listData1.yview("scroll",event.delta,"units")
        self.listData2.yview("scroll",event.delta,"units")
        self.listData3.yview("scroll",event.delta,"units")
        self.listData4.yview("scroll",event.delta,"units")
        self.listData5.yview("scroll",event.delta,"units")
        self.listData6.yview("scroll",event.delta,"units")
        self.listData7.yview("scroll",event.delta,"units")
        return "break"

    def OnVsb(self,*args):
        self.listData1.yview(*args)
        self.listData2.yview(*args)
        self.listData3.yview(*args)
        self.listData4.yview(*args)
        self.listData5.yview(*args)
        self.listData6.yview(*args)
        self.listData7.yview(*args)

    def Check(self):
        strData1, strData2, strData3, strData4, strData5, strData6, strData7 = [], [], [], [], [], [], []
        con = sqlite3.connect("db.db") 
        cur = con.cursor()
        try :
            cur.execute("SELECT A.OrderID, A.OrderDate, B.ProductID, C.ProductName, B.Quantity, B.UnitPrice, B.Quantity * B.UnitPrice AS Amount FROM Orders A INNER JOIN OrderDetails B ON A.OrderID = B.OrderID  INNER JOIN Products C ON B.ProductID = C.ProductID INNER JOIN Customers D ON A.CustomerID=D.CustomerID WHERE 1 = 1 AND B.Quantity * B.UnitPrice >= 1000 AND B.ProductID % 10 != 0 AND D.CompanyName=(?) ORDER BY A.OrderDate DESC, B.ProductID ASC",(selcom,))
        except :
            messagebox.showerror('오류', '거래처를 먼저 고른 후에 조회를 눌러주세요. 처음화면으로 돌아갑니다.')

        while (True) :
            row = cur.fetchone()
            if row == None :
                break;
            strData1.append(row[0]); strData2.append(row[1])
            strData3.append(row[2]); strData4.append(row[3])
            strData5.append(row[4]); strData6.append(row[5])
            strData7.append(row[6]);

        self.listData1.delete(0, self.listData1.size() - 1); self.listData2.delete(0, self.listData2.size() - 1)
        self.listData3.delete(0, self.listData3.size() - 1); self.listData4.delete(0, self.listData4.size() - 1)
        self.listData5.delete(0, self.listData5.size() - 1); self.listData6.delete(0, self.listData6.size() - 1)
        self.listData7.delete(0, self.listData7.size() - 1);

        for item1,item2,item3,item4,item5,item6,item7 in zip(strData1,strData2,strData3,strData4,strData5,strData6,strData7):
            self.listData1.insert(END, item1);
            self.listData2.insert(END, item2);
            self.listData3.insert(END, item3);
            self.listData4.insert(END, item4);
            self.listData5.insert(END, item5);
            self.listData6.insert(END, item6);
            self.listData7.insert(END, item7);
            
        con.close()

        self.CompanyNumber()

    def CompanyNumber(self):
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(A.OrderID) FROM Orders A INNER JOIN OrderDetails B ON A.OrderID = B.OrderID  INNER JOIN Products C ON B.ProductID = C.ProductID INNER JOIN Customers D ON A.CustomerID=D.CustomerID WHERE 1 = 1 AND B.Quantity * B.UnitPrice >= 1000 AND B.ProductID % 10 != 0 AND D.CompanyName=(?) ORDER BY A.OrderDate DESC, B.ProductID ASC",(selcom,)) 
        numorder = cur.fetchone()
        testlist = list(numorder)
        num = testlist[0]
        self.label7.config(text=num)
        con.close()

    def AddLayout(self):
        global edt1, edt2, edt3, edt4, edt5, edt6, edt7, edt8,edt9
        top = Toplevel()
        top.title("항목 추가하기")
        top.geometry("270x300")

        edt1= Entry(top)
        edt1.insert(END,'거래처 코드')
        edt1.pack()
        edt2= Entry(top)
        edt2.insert(END,'거래처명')
        edt2.pack()
        edt3= Entry(top)
        edt3.insert(END,'주문번호')
        edt3.pack()
        edt4= Entry(top)
        edt4.insert(END,'주문일자')
        edt4.pack()
        edt5= Entry(top)
        edt5.insert(END,'품목코드')
        edt5.pack()
        edt6= Entry(top)
        edt6.insert(END,'품목명')
        edt6.pack()
        edt7= Entry(top)
        edt7.insert(END,'수량')
        edt7.pack()
        edt8= Entry(top)
        edt8.insert(END,'단가')
        edt8.pack()
        edt9= Entry(top)
        edt9.insert(END,'금액')
        edt9.pack()

        AddButton = Button(top,bg='#B7F0B1',fg='black',text="추가",command=GuiHandler.combine_funcs(self.Add,top.destroy))
        AddButton.pack(padx = 10, pady = 10, ipadx=10,ipady=5)

    def Add(self):
        data1 = edt1.get()
        data2 = edt2.get()
        data3 = edt3.get()
        data4 = edt4.get()
        data5 = edt5.get()
        data6 = edt6.get()
        data7 = edt7.get()
        data8 = edt8.get()
        data9 = edt9.get()

        con = sqlite3.connect("db.db") 
        cur = con.cursor()
        # try :
        cur.execute("INSERT INTO Orders (OrderID,OrderDate,CustomerID) VALUES(?,?,?)",(data3,data4,data1))
        print(con.commit())
        cur.execute("INSERT INTO OrderDetails (OrderID,ProductID,Quantity,UnitPrice) VALUES(?,?,?,?)",(data3,data5,data7,data8))
        print(con.commit())
        cur.execute("INSERT INTO Products (ProductID,ProductName,UnitPrice) VALUES(?,?,?)",(data5,data6,data8))
        print(con.commit())
        cur.execute("INSERT INTO Customers (CustomerID,CompanyName) VALUES(?,?)",(data1,data2))
        print(con.commit())
        messagebox.showinfo("추가","DB에 성공적으로 추가되었습니다.")
        # except :
            # messagebox.showerror('오류', '데이터 추가 오류가 발생함')

        con.close()
        self.Check()

    def getCompany(self):

        global selcom
        try :
            index = CompanyList.curselection()[0]
            selcom = CompanyList.get(index)
        except :
            messagebox.showerror('오류', '거래처를 선택하지 않으셨습니다. 처음화면으로 돌아갑니다.')

    def CompanyCheck(self):
        global CompanyList
        top = Toplevel()
        top.title("거래처 리스트")
        top.geometry("400x360")
        companydata = []
        companydata.append("거래처명");
        companydata.append("----------------------------------");
        CompanyList = Listbox(top,bg='orange',fg='black',selectmode=SINGLE)
        CompanyList.pack()
        NoticeLabel=Label(top,bg='#F0F0F0',fg='black',text="원하는 거래처를 클릭 후 선택 버튼을 누른 뒤 조회를 누르세요.")
        NoticeLabel.pack()
        SendCompanyButton = Button(top,bg='#B7F0B1',fg='black',text="선택",command=self.getCompany)
        SendCompanyButton.pack(padx = 10, pady = 10, ipadx=5,ipady=5)
        CheckProductButton = Button(top,bg='#B7F0B1',fg='black',text="조회",command=self.Check)
        CheckProductButton.pack(padx = 10, pady = 10, ipadx=5,ipady=5)
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        try :
            cur.execute("SELECT DISTINCT A.CompanyName FROM Customers A INNER JOIN Orders B ON A.CustomerID = B.CustomerID INNER JOIN OrderDetails C ON B.OrderID = C.OrderID WHERE 1 = 1 AND C.Quantity * C.UnitPrice >= 1000 AND C.ProductID % 10 != 0")
        except :
            messagebox.showerror('오류', '데이터 입력 오류가 발생함')
        
        while (True) :
            row = cur.fetchone()
            if row == None :
                break;
            companydata.append(row[0]);

        for company in companydata:
            CompanyList.insert(END, company);

        con.close()

    def ClickaboutMenu(self) :
        messagebox.showinfo("개발자정보","개발자 이름 : 임정묵 \n 학번 : 2015040033 \n 메일주소 : mook6688@naver.com \n 학과 : 컴퓨터공학과 \n 전화번호 : 010-7254-0005 ")

    def ExitProgram(self) :
        top = Toplevel()
        top.title("프로그램 종료")
        top.geometry("100x150")
        NoticeLabel=Label(top,bg='#F0F0F0',fg='black',text="정말 종료하시겠습니까?")
        NoticeLabel.pack()
        ExitButton = Button(top,bg='#B7F0B1',fg='black',text="예",command=window.destroy)
        ExitButton.pack(padx = 10, pady = 10, ipadx=5,ipady=5)
        CancelButton = Button(top,bg='#B7F0B1',fg='black',text="아니오",command=top.destroy)
        CancelButton.pack(padx = 10, pady = 10, ipadx=5,ipady=5)

    def alterLayout(self):
        global entry_list1, entry_list2, entry_list3, entry_list4, entry_list5, entry_list6, entry_list7, entry_list8
        global entry_list_for_sql1, entry_list_for_sql2, entry_list_for_sql3, entry_list_for_sql4, entry_list_for_sql5, entry_list_for_sql6, entry_list_for_sql7, entry_list_for_sql8
        top = Toplevel()
        top.title("항목 수정하기")
        top.geometry("270x230")
        curselection = self.checkList()
        entry_list1= Entry(top)
        entry_list1.insert(END,self.listData1.get(curselection))
        entry_list1.pack()
        entry_list2= Entry(top)
        entry_list2.insert(END,self.listData2.get(curselection))
        entry_list2.pack()
        entry_list3= Entry(top)
        entry_list3.insert(END,self.listData3.get(curselection))
        entry_list3.pack()
        entry_list4= Entry(top)
        entry_list4.insert(END,self.listData4.get(curselection))
        entry_list4.pack()
        entry_list5= Entry(top)
        entry_list5.insert(END,self.listData5.get(curselection))
        entry_list5.pack()
        entry_list6= Entry(top)
        entry_list6.insert(END,self.listData6.get(curselection))
        entry_list6.pack()
        entry_list7= Entry(top)
        entry_list7.insert(END,self.listData7.get(curselection))
        entry_list7.pack()

        entry_list_for_sql1= self.listData1.get(curselection)
        entry_list_for_sql2= self.listData2.get(curselection)
        entry_list_for_sql3= self.listData3.get(curselection)
        entry_list_for_sql4= self.listData4.get(curselection)
        entry_list_for_sql5= self.listData5.get(curselection)
        entry_list_for_sql6= self.listData6.get(curselection)
        entry_list_for_sql7= self.listData7.get(curselection)

        # AddButton = Button(top,bg='#B7F0B1',fg='black',text="수정",command=lambda: alter(entry_list1,entry_list2,entry_list3,entry_list4,entry_list5,entry_list6,entry_list7))
        AddButton = Button(top,bg='#B7F0B1',fg='black',text="수정",command=GuiHandler.combine_funcs(lambda: self.alter(entry_list1,entry_list2,entry_list3,entry_list4,entry_list5,entry_list6,entry_list7),top.destroy))
        AddButton.pack(padx = 10, pady = 10, ipadx=5,ipady=5)

    def alter(self,a1,a2,a3,a4,a5,a6,a7):
        tmp_alter_data1 = a1.get()
        tmp_alter_data2 = a2.get()
        tmp_alter_data3 = a3.get()
        tmp_alter_data4 = a4.get()
        tmp_alter_data5 = a5.get()
        tmp_alter_data6 = a6.get()
        tmp_alter_data7 = a7.get()
        # use selcom in SQL
        con = sqlite3.connect("db.db")
        # update
        cur = con.cursor()
        # try :
        cur.execute("UPDATE Orders SET OrderID=?, OrderDate=?  WHERE OrderID=? AND OrderDate=?",(tmp_alter_data1,tmp_alter_data2,entry_list_for_sql1,entry_list_for_sql2))
        print(con.commit())
        cur.execute("UPDATE OrderDetails SET OrderID=?, ProductID=?, Quantity=?,UnitPrice=? WHERE OrderID=? AND ProductID=? AND Quantity=? AND UnitPrice=?",(tmp_alter_data1,tmp_alter_data3,tmp_alter_data5,tmp_alter_data6,entry_list_for_sql1,entry_list_for_sql3,entry_list_for_sql5,entry_list_for_sql6))
        print(con.commit())
        cur.execute("UPDATE Products SET ProductID=?, ProductName=?, UnitPrice=? WHERE UnitPrice=? AND ProductID=? AND ProductName=?",(tmp_alter_data3, tmp_alter_data4,tmp_alter_data6,entry_list_for_sql6,entry_list_for_sql3,entry_list_for_sql4))
        print(con.commit())
        # except :
            # messagebox.showerror('오류', '데이터 수정 오류가 발생함')

        con.close()
        self.Check()
        
    def checkList(self):
        curselect_list=[]
        curselect_index=None
        curselect_list.append(self.listData1.curselection())
        curselect_list.append(self.listData2.curselection())
        curselect_list.append(self.listData3.curselection())
        curselect_list.append(self.listData4.curselection())
        curselect_list.append(self.listData5.curselection())
        curselect_list.append(self.listData6.curselection())
        curselect_list.append(self.listData7.curselection())
        for i in curselect_list:
            if i!=():
                curselect_index=i
                break
        if curselect_index==None:
            print("Plz select list")
            return None
        else:
            # print(curselect_index)
            return curselect_index

    def remove(self):
        curselection = self.checkList()
        # sql용 변수선언
        tmp_remove_data1 = self.listData1.get(curselection)
        tmp_remove_data2 = self.listData2.get(curselection)
        tmp_remove_data3 = self.listData3.get(curselection)
        tmp_remove_data4 = self.listData4.get(curselection)
        tmp_remove_data5 = self.listData5.get(curselection)
        tmp_remove_data6 = self.listData6.get(curselection)
        tmp_remove_data7 = self.listData7.get(curselection)
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        try :
            cur.execute("DELETE FROM Orders WHERE OrderID=? AND OrderDate=?",(tmp_remove_data1,tmp_remove_data2))
            print(con.commit())
            cur.execute("DELETE FROM Products WHERE UnitPrice=? AND ProductID=? AND ProductName=?",(tmp_remove_data3, tmp_remove_data4, tmp_remove_data6))
            print(con.commit())
            cur.execute("DELETE FROM OrderDetails WHERE OrderID=? AND ProductID=? AND Quantity=? AND UnitPrice=?",(tmp_remove_data1, tmp_remove_data3, tmp_remove_data5, tmp_remove_data6))
            print(con.commit())
        except :
            messagebox.showerror('오류', '데이터 삭제 오류가 발생함')

        con.close()
        self.Check()
        
    def __init__(self, master):
        self.master = master
        master.title("거래처 및 주문 현황")
        master.geometry("1300x600")

        mainMenu = Menu(master)
        master.config(menu=mainMenu)
        fileMenu = Menu(mainMenu)
        mainMenu.add_cascade(label ="파일", menu=fileMenu)
        fileMenu.add_command(label ="조회", command=self.Check)
        fileMenu.add_separator()
        fileMenu.add_command(label ="추가", command=self.AddLayout)
        fileMenu.add_separator()
        fileMenu.add_command(label ="수정")
        fileMenu.add_separator()
        fileMenu.add_command(label ="삭제")
        fileMenu.add_separator()
        fileMenu.add_command(label ="종료",command=self.ExitProgram)
        aboutMenu = Menu(mainMenu)
        mainMenu.add_cascade(label ="About", menu=aboutMenu)
        aboutMenu.add_command(label ="개발자 정보", command=self.ClickaboutMenu)

        buttonFrame = Frame(master)
        btnCheck = Button(buttonFrame, text ="조회", bg='#ABF200',fg='black', command=self.Check)
        btnAdd = Button(buttonFrame, text ="추가", bg='#ABF200',fg='black', command=self.AddLayout)
        btnAlter = Button(buttonFrame, text ="수정", bg='#ABF200',fg='black', command=self.alterLayout)
        btnDelete = Button(buttonFrame, text ="삭제", bg='#ABF200',fg='black',command=self.remove)
        btnExit = Button(buttonFrame, text ="종료", bg='#ABF200',fg='black',command=self.ExitProgram)
        buttonFrame.pack(side=RIGHT)
        btnCheck.pack(side = TOP, padx = 10, pady = 10, ipadx=30,ipady=20)
        btnAdd.pack(side = TOP, padx = 10, pady = 10, ipadx=30,ipady=20)
        btnAlter.pack(side = TOP, padx = 10, pady = 10, ipadx=30,ipady=20)
        btnDelete.pack(side = TOP, padx = 10, pady = 10, ipadx=30,ipady=20)
        btnExit.pack(side = TOP, padx = 10, pady = 10, ipadx=30,ipady=20)

        customerFrame = Frame(master)
        customerFrame.pack(side = TOP, fill=BOTH)
        label1 = Label(customerFrame, font=("bold",13), bg = 'black', fg = 'white',text = '거래처 현황')
        label1.pack(fill=BOTH)
        btnCompanyCheck = Button(customerFrame,text="거래처 리스트 확인 및 선택한 거래처 주문현황 조회",bg="orange",fg="black",command=self.CompanyCheck)
        btnCompanyCheck.pack(side = TOP, padx = 5, pady = 10, ipadx=700,ipady=5)

        customernumFrame = Frame(master)
        customernumFrame.pack(side=TOP, fill=BOTH)
        label2 = Label(customerFrame, font=("bold",13), bg = '#F0F0F0', fg = 'black',text = '조회건수 :')
        label2.pack(side=LEFT)
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(DISTINCT A.CustomerID)as 조회건수 FROM Customers A INNER JOIN Orders B ON A.CustomerID = B.CustomerID INNER JOIN OrderDetails C ON B.OrderID = C.OrderID WHERE 1 = 1 AND C.Quantity * C.UnitPrice >= 1000 AND C.ProductID % 10 != 0")
        numcompany = cur.fetchone()
        label3 = Label(customerFrame, font=("bold",13), bg = '#F0F0F0', fg = 'black',text = numcompany)
        label3.pack(side=LEFT)
        con.close()

        OrderFrame = Frame(master)
        OrderFrame.pack(side=TOP, fill=BOTH)
        label4 = Label(OrderFrame, font=("bold",13), bg = 'black', fg = 'white',text = '주문현황')
        label4.pack(fill=BOTH)
        label5 = Label(OrderFrame, font=("bold",13), bg = '#4C4C4C', fg = 'white',text = '주문번호                        주문일자                      품목코드                      품목명                        수량                          단가                            금액         ')
        label5.pack(fill=BOTH)

        ListFrame = Frame(master)
        ListFrame.pack(side=TOP, fill=BOTH)
        scrollbar = tk.Scrollbar(ListFrame,orient=VERTICAL,command=self.OnVsb)
        scrollbar.pack(side="right",fill="y")
        self.listData1 = Listbox(ListFrame, bg = 'orange', height='20', yscrollcommand = scrollbar.set)
        self.listData2 = Listbox(ListFrame, bg = 'orange', height='20', yscrollcommand = scrollbar.set)
        self.listData3 = Listbox(ListFrame, bg = 'orange', height='20', yscrollcommand = scrollbar.set)
        self.listData4 = Listbox(ListFrame, bg = 'orange', height='20',yscrollcommand = scrollbar.set)
        self.listData5 = Listbox(ListFrame, bg = 'orange', height='20',yscrollcommand = scrollbar.set)
        self.listData6 = Listbox(ListFrame, bg = 'orange', height='20', yscrollcommand = scrollbar.set)
        self.listData7 = Listbox(ListFrame, bg = 'orange', height='20', yscrollcommand = scrollbar.set)

        self.listData1.bind("<MouseWheel>", self.OnMouseWheel)
        self.listData2.bind("<MouseWheel>", self.OnMouseWheel)
        self.listData3.bind("<MouseWheel>", self.OnMouseWheel)
        self.listData4.bind("<MouseWheel>", self.OnMouseWheel)
        self.listData5.bind("<MouseWheel>", self.OnMouseWheel)
        self.listData6.bind("<MouseWheel>", self.OnMouseWheel)
        self.listData7.bind("<MouseWheel>", self.OnMouseWheel)

        self.listData1.pack(side = LEFT, fill = BOTH, expand = True)
        self.listData2.pack(side = LEFT, fill = BOTH, expand = True)
        self.listData3.pack(side = LEFT, fill = BOTH, expand = True)
        self.listData4.pack(side = LEFT, fill = BOTH, expand = True)
        self.listData5.pack(side = LEFT, fill = BOTH, expand = True)
        self.listData6.pack(side = LEFT, fill = BOTH, expand = True)
        self.listData7.pack(side = LEFT, fill = BOTH, expand = True)

        OrdernumFrame = Frame(master)
        OrdernumFrame.pack(side=TOP, fill=BOTH)
        label6 = Label(OrdernumFrame, font=("bold",13), bg = '#F0F0F0', fg = 'black',text = '조회건수 :')
        label6.pack(side=LEFT)
        self.label7 = Label(OrdernumFrame, font=("bold",13), bg = '#F0F0F0', fg = 'black',text = "")
        self.label7.pack(side=LEFT)

        DateinfoFrame = Frame(master)
        DateinfoFrame.pack(side=TOP, fill=BOTH)
        label8 = Label(DateinfoFrame, font=("bold",13), bg = '#F0F0F0', fg = 'black',text = '현재일시 :')
        label8.pack(side=LEFT)
        now = time.localtime()  
        s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        label9 = Label(DateinfoFrame, font=("bold",13), bg = '#F0F0F0', fg = 'black',text=s)
        label9.pack(side=LEFT)

window = Tk()
my_gui = GuiHandler(window)
window.mainloop()

# if __name__ == '__main__':
#     pass
#     