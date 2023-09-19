import tkinter as tk
from tkinter import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import os
from selenium.webdriver.common.keys import Keys
#from selenium import org.openqa.selenium.support.ui.Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, 'chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=address)
#initializing root
root = Tk()
root.configure(bg='pale turquoise')
root.title("!به کارگزاری فیروزه آسیا خوش آمدید")
root.geometry("375x440")

userField = '//*[@id="txtusername"]'
passField = '//*[@id="txtpassword"]'
capField = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[1]/div/div/input'
submit = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[4]/div[1]/button'
refreshcap = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[2]/img'

buy1 = '/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[1]/div[1]/div'
bVolume = '//*[@id="send_order_txtCount"]'
bCost = '//*[@id="send_order_txtPrice"]'
bSubmit = '//*[@id="send_order_btnSendOrder"]'

sell1 = '/html/body/app-container/app-content/div/div/div/div[3]/div[2]/div/div/widget/div/div/div/div[2]/send-order/div/div[1]/div[2]/div'
sVolume = '//*[@id="send_order_txtCount"]'
sCost = '//*[@id="send_order_txtPrice"]'
sSubmit = '//*[@id="send_order_btnSendOrder"]'

DBaan = '/html/body/app-container/app-content/div/div/div/div[1]/div[1]/ul[1]/li[2]/span'
DEnter= '//*[@id="txt_search"]'

page1 = '/html/body/div/div[2]/div[2]/div[1]/div/div[1]/multi-login/div/div[2]/ul/li[2]'
pageMain = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/ul/li[1]'

#LOGINS___________________________________________________________________________________________________________
def firstlogin():
    global second
    second = Toplevel()
    second.configure(bg='pale turquoise')
    second.title("باز کردن صفحه ورود")
    refreshcap = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[2]/img'
    second.geometry("500x300") #500 * 250
    l4 = Label(second,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l4.pack()
    l1 = Label(second,  text = ":نام کاربری")
    l1.pack()
    text1 = Text(second , height = 2 , width = 20)
    text1.pack()
    l2 = Label(second, text = ":رمز عبور")
    l2.pack()
    text2 = Text(second , height = 2 , width = 20)
    text2.pack()
    l3 = Label(second ,text = ":کپچا")
    l3.pack()
    text3 = Text(second , height = 2 , width = 20)
    text3.pack()
    driver.switch_to.window("firsttab")
##############################################
    def ret1():
        #capField = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[1]/div/div/input'
        #submit = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[4]/div[1]/button'
        inp1 = text1.get("1.0",'end-1c' )
        inp2 = text2.get("1.0",'end-1c' )
        inp3 = text3.get("1.0",'end-1c' )
        inp3 = int(inp3)
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_name("capcha")
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        second.withdraw()
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    firstSave = Button(second , height = 1 , width = 15 , text = "اعمال تغییرات" , command=lambda: ret1())
    firstSave.pack(pady=10)
    l12 = Label(second,  text = ".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#____________________________________________________________________________________________________
def secondlogin():
    global sixth
    sixth = Toplevel()
    sixth.configure(bg='pale turquoise')
    sixth.title("باز کردن صفحه ورود")
    refreshcap = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[2]/img'
    sixth.geometry("500x300")
    l44 = Label(sixth,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l44.pack()
    l41 = Label(sixth,  text = ":نام کاربری")
    l41.pack()
    text21 = Text(sixth , height = 2 , width = 20)
    text21.pack()
    l29 = Label(sixth, text = ":رمز عبور")
    l29.pack()
    text22 = Text(sixth, height = 2 , width = 20)
    text22.pack()
    l33 = Label(sixth ,text = ":کپچا")
    l33.pack()
    text23 = Text(sixth, height = 2 , width = 20)
    text23.pack()
    driver.switch_to.window("secondtab")
##############################################
    def ret2(): 
        inp1 = text21.get("1.0",'end-1c' )
        inp2 = text22.get("1.0",'end-1c' )
        #inp1 = 'fa20030733'
        #inp2 = 'w7HbJHFW'
        inp3 = text23.get("1.0",'end-1c' )
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_name("capcha")
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        sixth.withdraw()
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    secondSave = Button(sixth , height = 1 , width = 15 , text = "اعمال تغییرات", command=lambda: ret2())
    secondSave.pack(pady=10)
    l12 = Label(sixth,  text = ".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
    
    #driver.find_element_by_xpath( refreshcap ).click()
#_________________________________________________________________________________________________________________________
def thirdlogin():
    global seventh
    seventh = Toplevel()
    seventh.configure(bg='pale turquoise')
    seventh.title("باز کردن صفحه ورود")
    refreshcap = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[2]/img'
    seventh.geometry("500x300")
    l44 = Label(seventh,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l44.pack()
    l41 = Label(seventh,  text = ":نام کاربری")
    l41.pack()
    text21 = Text(seventh , height = 2 , width = 20)
    text21.pack()
    l29 = Label(seventh, text = ":رمز عبور")
    l29.pack()
    text22 = Text(seventh, height = 2 , width = 20)
    text22.pack()
    l33 = Label(seventh ,text = ":کپچا")
    l33.pack()
    text23 = Text(seventh, height = 2 , width = 20)
    text23.pack()
    driver.switch_to.window("thirdtab")
##############################################
    def ret3(): 
        inp1 = text21.get("1.0",'end-1c' )
        inp2 = text22.get("1.0",'end-1c' )
        inp3 = text23.get("1.0",'end-1c' )
        inp3 = int(inp3)
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_name("capcha")
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        seventh.withdraw()
        #three = 1
        #return three
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    thirdSave = Button(seventh , height = 1 , width = 15 , text = "اعمال تغییرات" , command=lambda: ret3())
    thirdSave.pack(pady=10)
    l12 = Label(seventh,  text = ".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#_________________________________________________________________________________________________________________________
def fourthlogin():
    global eighth
    eighth = Toplevel()
    eighth.configure(bg='pale turquoise')
    eighth.title("باز کردن صفحه ورود")
    refreshcap = '/html/body/div/div[2]/div[2]/div[1]/div/multi-login/div/div[2]/div[1]/form/div[2]/div[2]/img'
    eighth.geometry("500x300")
    l44 = Label(eighth,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l44.pack()
    l41 = Label(eighth,  text = ":نام کاربری")
    l41.pack()
    text21 = Text(eighth , height = 2 , width = 20)
    text21.pack()
    l29 = Label(eighth, text = ":رمز عبور")
    l29.pack()
    text22 = Text(eighth, height = 2 , width = 20)
    text22.pack()
    l33 = Label(eighth ,text = ":کپچا")
    l33.pack()
    text23 = Text(eighth, height = 2 , width = 20)
    text23.pack()
    driver.switch_to.window("fourthtab")
##############################################
    def ret4(): 
        inp1 = text21.get("1.0",'end-1c' )
        inp2 = text22.get("1.0",'end-1c' )
        #inp1 = 'fa20030733'
        #inp2 = 'w7HbJHFW'
        inp3 = text23.get("1.0",'end-1c' )
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_name("capcha")
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        eighth.withdraw()
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    fourthSave = Button(eighth , height = 1 , width = 15 , text = "اعمال تغییرات" , command=lambda: ret4())
    fourthSave.pack(pady=10)
    l12 = Label(eighth,  text =".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#buy_________________________________________________________________________________________________________________________
def buy():
    global third
    third = Toplevel()
    third.configure(bg='pale turquoise')
    third.title(":تعداد و قیمت برای خرید")
    third.geometry("400x225")
    l6 = Label(third,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l6.pack()
    l7 = Label(third,  text = ":تعداد مورد نظر برای خرید را وارد کنید")
    l7.pack()
    text7 = Text(third , height = 2 , width = 20)
    text7.pack()
    l8 = Label(third, text = ":قیمت مورد نظر برای خرید را وارد کنید")
    l8.pack()
    text8 = Text(third , height = 2 , width = 20)
    text8.pack()
#####################################################
    def applybuy():
        inp7 = text7.get("1.0", 'end-1c' )
        inp8 = text8.get("1.0", 'end-1c' )
        driver.switch_to.window("firsttab")
        driver.find_element_by_xpath( buy1 ).click()
        driver.find_element_by_xpath(bVolume).send_keys(inp7)
        driver.find_element_by_xpath(bCost).send_keys(inp8)
        driver.find_element_by_xpath(bSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(bVolume).clear()
        driver.find_element_by_xpath(bCost).clear()
        driver.switch_to.window("secondtab")
        driver.find_element_by_xpath( buy1 ).click()
        driver.find_element_by_xpath(bVolume).send_keys(inp7)
        driver.find_element_by_xpath(bCost).send_keys(inp8)
        driver.find_element_by_xpath(bSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(bVolume).clear()
        driver.find_element_by_xpath(bCost).clear()
        driver.switch_to.window("thirdtab")
        driver.find_element_by_xpath( buy1 ).click()
        driver.find_element_by_xpath(bVolume).send_keys(inp7)
        driver.find_element_by_xpath(bCost).send_keys(inp8)
        driver.find_element_by_xpath(bSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(bVolume).clear()
        driver.find_element_by_xpath(bCost).clear()
        driver.switch_to.window("fourthtab")
        driver.find_element_by_xpath( buy1 ).click()
        driver.find_element_by_xpath(bVolume).send_keys(inp7)
        driver.find_element_by_xpath(bCost).send_keys(inp8)
        driver.find_element_by_xpath(bSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(bVolume).clear()
        driver.find_element_by_xpath(bCost).clear()
        inp7 = 0
        inp8 = 0
        third.withdraw()
    appbuy = Button(third,height = 1 , width = 25 , text="اعمال تغییرات", command=applybuy)
    appbuy.pack(pady=10)

def sell():
    #driver.switch_to.window("tab{}".format(m) )
    global fourth
    fourth = Toplevel()
    fourth.configure(bg='pale turquoise')
    fourth.title(":تعداد و قیمت برای فروش")
    fourth.geometry("400x225")
    l9 = Label(fourth,  text = ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l9.pack()
    l10 = Label(fourth,  text =  ":تعداد مورد نظر برای فروش را وارد کنید")
    l10.pack()
    text10 = Text(fourth , height = 2 , width = 20)
    text10.pack()
    l11 = Label(fourth, text = ":قیمت مورد نظر برای فروش را وارد کنید")
    l11.pack()
    text11 = Text(fourth , height = 2 , width = 20)
    text11.pack()
###################################################
    def applysell():
        inp10 = text10.get("1.0", 'end-1c' )
        inp11 = text11.get("1.0", 'end-1c' )
        driver.switch_to.window("firsttab")
        driver.find_element_by_xpath( sell1 ).click()
        driver.find_element_by_xpath(sVolume).send_keys(inp10)
        driver.find_element_by_xpath(sCost).send_keys(inp11)
        driver.find_element_by_xpath(sSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(sVolume).clear()
        driver.find_element_by_xpath(sCost).clear()
        driver.switch_to.window("secondtab")
        driver.find_element_by_xpath( sell1 ).click()
        driver.find_element_by_xpath(sVolume).send_keys(inp10)
        driver.find_element_by_xpath(sCost).send_keys(inp11)
        driver.find_element_by_xpath(sSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(sVolume).clear()
        driver.find_element_by_xpath(sCost).clear()
        driver.switch_to.window("thirdtab")
        driver.find_element_by_xpath( sell1 ).click()
        driver.find_element_by_xpath(sVolume).send_keys(inp10)
        driver.find_element_by_xpath(sCost).send_keys(inp11)
        driver.find_element_by_xpath(sSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(sVolume).clear()
        driver.find_element_by_xpath(sCost).clear()
        driver.switch_to.window("fourthtab")
        driver.find_element_by_xpath( sell1 ).click()
        driver.find_element_by_xpath(sVolume).send_keys(inp10)
        driver.find_element_by_xpath(sCost).send_keys(inp11)
        driver.find_element_by_xpath(sSubmit).click()
        time.sleep(1)
        #clearing
        driver.find_element_by_xpath(sVolume).clear()
        driver.find_element_by_xpath(sCost).clear()
        inp10 = 0 
        inp11 = 0
        fourth.withdraw()

    appsell = Button(fourth,height = 1 , width = 25 , text="اعمال تغییرات", command=applysell)
    appsell.pack(pady=10)       
# Show the window
#def show():
#    second.deiconify()

#DEDIH BAAN info-----------------------------------------------------------------------------------------
def dideban_f():
    global fifth
    fifth = Toplevel()
    fifth.configure(bg='pale turquoise')
    fifth.title("وارد کردن سهم مورد نظر")
    fifth.geometry("400x175")
    l20 = Label(fifth,  text =".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l20.pack()
    l21 = Label(fifth,  text = ":نام سهم را وارد کنید")
    l21.pack()
    text21 = Text(fifth , height = 2 , width = 20)
    text21.pack()
    def ret_di(): 
        inp1 = text21.get("1.0",'end-1c' )
        inpp = str(inp1) + '1'
        driver.switch_to.window("firsttab")
        driver.find_element_by_xpath( DBaan ).click()
        it1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, DEnter)))
        it1.click()
        for element in inpp:
            print(element , end = '')
            it1.send_keys(element)
            time.sleep(0.1)
        time.sleep(0.1)   
        itt = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="list_dropdown"]/div[1]')))
        #time.sleep(0.5)
        itt.click()
        #
        driver.switch_to.window("secondtab")
        driver.find_element_by_xpath( DBaan ).click()
        it1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, DEnter)))
        it1.click()
        for element in inpp:
            print(element , end = '')
            it1.send_keys(element)
            time.sleep(0.1)
        time.sleep(0.1)    
        itt = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="list_dropdown"]/div[1]')))
        #time.sleep(0.5)
        itt.click()
        #
        driver.switch_to.window("thirdtab")
        driver.find_element_by_xpath( DBaan ).click()
        it1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, DEnter)))
        it1.click()
        for element in inpp:
            print(element , end = '')
            it1.send_keys(element)
            time.sleep(0.1)
        time.sleep(0.1)
        itt = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="list_dropdown"]/div[1]')))
        #time.sleep(0.5)
        itt.click()
        #
        driver.switch_to.window("fourthtab")
        driver.find_element_by_xpath( DBaan ).click()
        it1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, DEnter)))
        it1.click()
        for element in inpp:
            print(element , end = '')
            it1.send_keys(element)
            time.sleep(0.1)
        time.sleep(0.1)
        itt1 = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="list_dropdown"]/div[1]')))
        #time.sleep(0.5)
        itt1.click()
        #
        inp1 = 0
        inpp = 0
        #
        fifth.withdraw()

    dide_enter = Button(fifth,height = 1 , width = 20 , text="اعمال تغییرات", command=ret_di)
    dide_enter.pack(pady=10)
#----------------------------------------------------------------------------------------------------------

#root widgets
l14 = Label(root,  text = ":انجام عملیات مد نظر شما")
l14.pack() 
l17 = Label(root,  text = " ")
l17.pack() 
l15 = Label(root,  text = ":ورود به حساب های مختلف")
l15.pack()
loginfirst = Button(root,height = 1 , width = 25 , text="ورود به اولین حساب", command=firstlogin)
loginfirst.pack()
loginsecond = Button(root,height = 1 , width = 25 , text="ورود به دومین حساب", command=secondlogin)
loginsecond.pack()
loginthird = Button(root,height = 1 , width = 25 , text="ورود به سومین حساب", command=thirdlogin)
loginthird.pack()
loginfourth = Button(root,height = 1 , width = 25 , text="ورود به چهارمین حساب", command=fourthlogin)
loginfourth.pack()
l17 = Label(root,  text = " ")
l17.pack()
l16 = Label(root,  text = ":وارد کردن سهم مورد نظر")
l16.pack()
dideban = Button(root,height = 1 , width = 25 , text="وارد کردن سهم مورد نظر", command=dideban_f)
dideban.pack()
l19 = Label(root,  text = " ")
l19.pack()
l18 = Label(root,  text = ":انتخاب عملیات خرید یا فروش")
l18.pack()
buybutton = Button(root,height = 1 , width = 25 , text="خرید", command=buy)
buybutton.pack()
sellbutton = Button(root,height = 1 , width = 25 , text="فروش", command=sell)
sellbutton.pack()
l23 = Label(root,  text = " ")
l23.pack()
l24 = Label(root,  text = "خدانگهدار؟؟؟ :((")
l24.pack()
byebye = Button(root,height = 1 , width = 25 , text="!خدانگهدار", command=root.quit)
byebye.pack()

driver.execute_script("window.open('https://online.firouzehasia.ir/', 'firsttab');")
driver.execute_script("window.open('https://online.firouzehasia.ir/', 'secondtab');")
driver.execute_script("window.open('https://online.firouzehasia.ir/', 'thirdtab');")
driver.execute_script("window.open('https://online.firouzehasia.ir/', 'fourthtab');")

root.mainloop()

        #ddelement= Select(driver.find_element_by_xpath('//*[@id="list_dropdown"]/div[1]'))
        #ddelement.click()
        #ddelement.select_by_value('1')
        #elll = driver.find_element_by_xpath('//*[@id="list_dropdown"]/div[1]')
        #elll.click()
        #menu = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, " (//div[@class='cYrDcjyGO77__container'])[1]")))
        #menu.click()
        #Waiting untill menu items is visible then selecting the second element - Google
        #Select(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list_dropdown"]/div[1]')))).select_by_value('1')
        #driver.find_element_by_xpath('//*[@id="list_dropdown"]/div[1]').send_keys(Keys.RETURN)
        #driver.find_element_by_name('//*[@id="list_dropdown"]/div[1]').click()
        #driver.find_element_by_xpath('//*[@id="list_dropdown"]/div[1]').send_keys(Keys.RETURN)
        #time.sleep(5)
        #it = Select(driver.find_element_by_xpath(it1))
        #time.sleep(1)
        #it.select_by_visible_text(inpp)
        #menu1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="list_dropdown"]')))
        #menu1.click()
        #time.sleep(5)
        #driver.find_element_by_name(inpp).click()
        #time.sleep(5)
        #driver.find_element_by_xpath( DEnter ).send_keys( inpp )
        #time.sleep(5)
        #item1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="list_dropdown"]/div[1]')))
        #select = Select(item1)
        #select.select_by_visible_text(inpp)
        #
        #dropArrow = driver.find_element_by_id('//*[@id="list_dropdown"]') 
        #dropArrow.click() 
        #time.sleep(2) 
        #dropdown1 = driver.find_element_by_xpath('//*[@id="list_dropdown"]/div[1]') 
        #dropdown1.click()
        #driver.find_element_by_xpath('//*[@id="list_dropdown"]/div[1]').send_keys(Keys.RETURN)