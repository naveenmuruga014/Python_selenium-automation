from selenium import webdriver
from Locators import *
from utils import *
import time


#login into demo application
def logging_into_application():
     driver=open_page()
     driver.find_element(*LoginpageLocators.UsernameLocator).send_keys("standard_user")
     driver.find_element(*LoginpageLocators.passwordLocator).send_keys("secret_sauce")
     driver.find_element(*LoginpageLocators.LoginBtnLocator).click()
     logintitle=driver.title
     if logintitle=="Swag Labs":
        print("Login functionality working as Expected")
     else:
         print("Login functionality working as not Expected")
     return driver

logging_into_application()


#Add the products to cart
def Add_to_cart():
     driver=logging_into_application()
     driver.find_element(*addToCart.BackpackLocator).click()
     driver.find_element(*addToCart.TshirtLocator).click()
     driver.find_element(*addToCart.CheckoutLocator).click()
     CartTitle=driver.find_element(*addToCart.CartTitleLocator).text
     if CartTitle=='Your Cart':
         AddcartItems=driver.find_elements(*addToCart.InventoryItems)
         Items=len(AddcartItems)
         time.sleep(5)
         if Items==2:  #we added two products , so we are expecting only products are avialble in cart section
             # We need to make sure that the two products available under the cart section are the same as the ones we added to the carts.
             CartItems=[]
             for item in AddcartItems:
                 CartItems.append(str(item.text))
             if CartItems[0]=='Sauce Labs Backpack':
                 print("Bacpack is sucessfully added to the cart")
             else:
                 print("Bacpack is not added to the cart")
             if CartItems[1]=="Sauce Labs Bolt T-Shirt":
                 print("Tshirt is sucessfully added to the cart")
             else:
                 print("Tshirt is not added to the cart")
         else:
             print("products are not available under the cart")
     else:
         print("cart section is not opened properly")
         

Add_to_cart()
     
