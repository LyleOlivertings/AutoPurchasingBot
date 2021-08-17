import time 
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


browser = webdriver.Chrome("C:\chromedriver.exe")


browser.get("https://www.sportscene.co.za/pdp/jordan-men-s-ma2-white-sneaker/_/A-060601ACKL8")

emailAd = "Oliverlyle29@gmail.com"
First = "Lyle"


buyButton = False

while not buyButton:
    
    try:

        AddToCartBtn = addButton = browser.find_element_by_class_name("penis")

        print("Sneaker isn't availalbe yet")

        time.sleep(1)
        browser.refresh

    except:
       

        
        ShoeSize = Shoebutton = browser.find_element_by_xpath('/html/body/div[5]/section/div[6]/div[2]/div/div[1]/div[2]/div[6]')
        Shoebutton.click()

        time.sleep(1)
        browser.refresh
      
        AddToCartBtn = addButton = browser.find_element_by_xpath("/html/body/div[5]/section/div[6]/div[2]/div/div[1]/div[2]/div[16]/div[1]")
        AddToCartBtn.click()

        time.sleep(1)
        browser.refresh

        print("halfway there")


        element =WebDriverWait(browser, 1).until
        browser.get("https://www.sportscene.co.za/basket/basket.jsp")

        time.sleep(1)
        browser.refresh


        SecureCO = SecureCObtn = browser.find_element_by_xpath("/html/body/div[5]/section/div[3]/div/div[1]/div[2]/div[3]/button")
        SecureCO.click()

        
        
        browser.refresh

        WithoutLogin = WithoutLoginBtn = browser.find_element_by_xpath("/html/body/div[5]/section/div[2]/div/div/div[1]/div[2]/div[6]/div/div[1]/div")
        WithoutLogin.click()
        
        browser.refresh

        deliver = DeliverBtn = browser.find_element_by_xpath("/html/body/div[5]/section/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/fieldset/div/div[1]")
        deliver.click()
        
        time.sleep(1)
        browser.refresh

        Entermanually = EntermanuallyBtn = browser.find_element_by_xpath("/html/body/div[5]/section/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/section/fieldset/div[4]/a")
        Entermanually.click()

        time.sleep(1)
        browser.refresh

        emailAdBtn = EmailAddressBtn = browser.find_element_by_id("shipping-address__email")
        time.sleep(1)
        browser.refresh
        
        FirstNameAdBtn = FirstAddressBtn = browser.find_element_by_id("shipping-address__firstname")
        time.sleep(1)
        browser.refresh
        
        SurnameAdBtn = SurnameAddressBtn = browser.find_element_by_id("shipping-address__lastname")
        time.sleep(1)
        browser.refresh

        CellAdBtn = CellAddressBtn = browser.find_element_by_id("shipping-address__number")
        time.sleep(1)
        browser.refresh

        StreetAd1 = Str1AddressBtn = browser.find_element_by_id("shipping-address__straddress1")
        time.sleep(1)
        browser.refresh

        Suburb = SubsBtn = browser.find_element_by_id("shipping-address__suburb")
        time.sleep(1)
        browser.refresh

        City = Citybn = browser.find_element_by_id("shipping-address__city-town")
        time.sleep(1)
        browser.refresh

        PostlCode = PstlCod = browser.find_element_by_id("shipping-address__postal-code")

        RegionSelc = Rgselc = browser.find_element_by_name("shipping-address_region")

        emailAdBtn.send_keys(emailAd)
        FirstNameAdBtn.send_keys("Lyle")
        SurnameAdBtn.send_keys("Oliver")
        CellAdBtn.send_keys("652845981")
        StreetAd1.send_keys("54 selbourne street")
        City.send_keys("Cape Town")
        Suburb.send_keys("Kraaifontein")
        PostlCode.send_keys("7570")
        RegionSelc.click()
        time.sleep(1)

        WestrnCp = WestercpBtn = browser.find_element_by_xpath("/html/body/div[5]/section/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/section/div/div/fieldset[5]/div[2]/div/div/select/option[10]")

        WestrnCp.click()
        
        RegionSelc.click()
        time.sleep(1)

        Sumbtn = Submited = browser.find_element_by_xpath("/html/body/div[5]/section/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/section/div/fieldset[6]/div/button")
        Sumbtn.click()

        time.sleep(5)
        

        nextBTN = NextNext = browser.find_element_by_xpath("/html/body/div[5]/section/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div/div/fieldset/div/button")

        time.sleep(1)

        nextBTN.click()

    

    

        

        





        

