from selenium.webdriver.common.by import By

class LoginpageLocators:
    UsernameLocator=(By.XPATH,"//input[@id='user-name']")
    passwordLocator=(By.XPATH,"//input[@id='password']")
    LoginBtnLocator=(By.XPATH,"//input[@id='login-button']")    

class addToCart:
    BackpackLocator=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    TshirtLocator=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    CheckoutLocator=(By.XPATH,"//span[@class='shopping_cart_badge']")
    CartTitleLocator=(By.XPATH,"//div[@class='header_secondary_container']//span")
    InventoryItems=(By.XPATH,"//div[@class='inventory_item_name']")