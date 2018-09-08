from tkinter import *
from message import *
from DESCRIPTION import *
def ACCOUNTNAME(a,x,y,p):
    n="arial",14,"italic"
    accountName=Tk()
    accountName.title("ACCOUNTNAME")
    accountName.geometry("1000x600+0+0")
    Label(accountName,text="Your Total Bill="+str(x*y),font=(n)).grid(row=0,sticky=W)
    Label(accountName,text="You Have Paid only="+str(p),font=(n)).grid(row=1,sticky=W)
    Label(accountName,text="Amount Left="+str(x*y-p),font=(n)).grid(row=2,sticky=W)
    Label(accountName,text="ENTER NAME",font=(n)).grid(row=3,sticky=W)
    ACCOUNT=open("ACCOUNT.txt","r")
    account=list(map(str,ACCOUNT.read().split()))
    ACCOUNT.close()
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    def makeAccount():
        if var1.get()=="":
            message("ALL FIELDS ARE REQUIRED")
        elif var1.get() not in account:
            accountName.destroy()
            item=open("item.txt","w")
            I[a]-=x
            b=""
            for i in I:
                b=b+str(i)+" "
            item.write(b)
            item.close()
            ACCOUNT=open("ACCOUNT.txt","a")
            ACCOUNT.write(var1.get()+" ")
            ACCOUNT.close()
            message("AMOUNT AND DEAL ACCOUNT HAS BEEN TAKEN and A NEW ACCOUNT with name "+var1.get()+" has been created with balance="+str(x*y-p))
            description(p,0,0,x,"A NEW ACCOUNT CREATE WITH NAME "+var1.get()+" has been created with balance="+str(x*y-p)+"\n")
            PRICE=open("BALANCEPRICE.txt","a")
            PRICE.write(str(x*y-p)+" ")
            PRICE.close()
            acc=open("ACCOUNTNAME.py","a")
            acc.write("    def add"+str(len(account)+1)+"():\n        accountName.destroy()\n        description(p,0,0,x,str(x)+' items of '+Q["+str(len(account))+"]+' is bought by '+account["+str(len(account))+"]+' at the rate of '+str(y)+' per item and he paid only '+str(p)+' INR and now total balance left='+str(x*y-p)+new)\n        price=open('BALANCEPRICE.txt','w')\n        PR["+str(len(account))+"]+=(x*y-p)\n        print(PR["+str(len(account))+"])\n        b=''\n        for i in PR:\n            b=b+str(i)+' '\n        price.write(b+var1.get())\n        message('data saved and Now your balance='+str(PR["+str(len(account))+"]))\n        price.close()\n        item=open('item.txt','w')\n        I[a]-=x\n        b=''\n        for i in I:\n            b=b+str(i)+' '\n        item.write(b)\n        item.close()\n    i+=1\n    Button(accountName,text=account[i],command=add"+str(len(account)+1)+",font=(n),width=20).grid(row=i+5,column=0)\n    Button(accountName,text=PR[i],command=add"+str(len(account)+1)+",font=(n),width=20).grid(row=i+5,column=1)\n")
    var1=StringVar()
    e1=Entry(accountName,width=25,textvariable=var1)
    e1.grid(row=3,column=1)
    Button(accountName,text="Make account",command=makeAccount,font=(n)).grid(row=4,column=1)
    i=-1
    new="\n"
    price=open("BALANCEPRICE.txt","r")
    PR=list(map(int,price.read().split()))
    def add1():
        accountName.destroy()
        description(p,0,0,x,str(x)+' items of '+Q[0]+' is bought by '+account[0]+' at the rate of '+str(y)+' per item and he paid only '+str(p)+' INR and now total balance left='+str(x*y-p)+new)
        price=open('BALANCEPRICE.txt','w')
        PR[0]+=(x*y-p)
        print(PR[0])
        b=''
        for i in PR:
            b=b+str(i)+' '
        price.write(b+var1.get())
        message('data saved and Now your balance='+str(PR[0]))
        price.close()
        item=open('item.txt','w')
        I[a]-=x
        b=''
        for i in I:
            b=b+str(i)+' '
        item.write(b)
        item.close()
    i+=1
    Button(accountName,text=account[i],command=add1,font=(n),width=20).grid(row=i+5,column=0)
    Button(accountName,text=PR[i],command=add1,font=(n),width=20).grid(row=i+5,column=1)
    def add2():
        accountName.destroy()
        description(p,0,0,x,str(x)+' items of '+Q[1]+' is bought by '+account[1]+' at the rate of '+str(y)+' per item and he paid only '+str(p)+' INR and now total balance left='+str(x*y-p)+new)
        price=open('BALANCEPRICE.txt','w')
        PR[1]+=(x*y-p)
        print(PR[1])
        b=''
        for i in PR:
            b=b+str(i)+' '
        price.write(b+var1.get())
        message('data saved and Now your balance='+str(PR[1]))
        price.close()
        item=open('item.txt','w')
        I[a]-=x
        b=''
        for i in I:
            b=b+str(i)+' '
        item.write(b)
        item.close()
    i+=1
    Button(accountName,text=account[i],command=add2,font=(n),width=20).grid(row=i+5,column=0)
    Button(accountName,text=PR[i],command=add2,font=(n),width=20).grid(row=i+5,column=1)
    def add3():
        accountName.destroy()
        description(p,0,0,x,str(x)+' items of '+Q[2]+' is bought by '+account[2]+' at the rate of '+str(y)+' per item and he paid only '+str(p)+' INR and now total balance left='+str(x*y-p)+new)
        price=open('BALANCEPRICE.txt','w')
        PR[2]+=(x*y-p)
        print(PR[2])
        b=''
        for i in PR:
            b=b+str(i)+' '
        price.write(b+var1.get())
        message('data saved and Now your balance='+str(PR[2]))
        price.close()
        item=open('item.txt','w')
        I[a]-=x
        b=''
        for i in I:
            b=b+str(i)+' '
        item.write(b)
        item.close()
    i+=1
    Button(accountName,text=account[i],command=add3,font=(n),width=20).grid(row=i+5,column=0)
    Button(accountName,text=PR[i],command=add3,font=(n),width=20).grid(row=i+5,column=1)
    def add4():
        accountName.destroy()
        description(p,0,0,x,str(x)+' items of '+Q[3]+' is bought by '+account[3]+' at the rate of '+str(y)+' per item and he paid only '+str(p)+' INR and now total balance left='+str(x*y-p)+new)
        price=open('BALANCEPRICE.txt','w')
        PR[3]+=(x*y-p)
        print(PR[3])
        b=''
        for i in PR:
            b=b+str(i)+' '
        price.write(b+var1.get())
        message('data saved and Now your balance='+str(PR[3]))
        price.close()
        item=open('item.txt','w')
        I[a]-=x
        b=''
        for i in I:
            b=b+str(i)+' '
        item.write(b)
        item.close()
    i+=1
    Button(accountName,text=account[i],command=add4,font=(n),width=20).grid(row=i+5,column=0)
    Button(accountName,text=PR[i],command=add4,font=(n),width=20).grid(row=i+5,column=1)
