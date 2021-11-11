from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# pass in a service object driver & initialize webdriver
s = Service("C:\\Users\\User\\PycharmProjects\\SeleniumDemo\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# open the link
driver.get("http://tutorialsninja.com/demo/")

# maximize the window
driver.maximize_window()

# click the phone
# phone = driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[6]/a')
phone = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
phone.click()

# go to laptop & notebook
laptops_1 = driver.find_element(By.XPATH, "//a[text()='Laptops & Notebooks']")
action = ActionChains(driver)
action.move_to_element(laptops_1).perform()
time.sleep(2)

# click show all laptop & notebook
laptops_2 = driver.find_element(By.XPATH, "//a[text()='Show All Laptops & Notebooks']")
laptops_2.click()
time.sleep(1)

# click on HP laptop
HP = driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
HP.click()

# view laptop image
image = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul[1]/li[1]/a')
image.click()
time.sleep(5)

# screenshot the image
driver.save_screenshot('HP.png')

# close the image
close = driver.find_element(By.CLASS_NAME, 'mfp-close')
close.click()

# scroll
btn_cart = driver.find_element(By.ID, 'button-cart')
btn_cart.location_once_scrolled_into_view
time.sleep(1)

# calendar
calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar = driver.find_element(By.CLASS_NAME, 'next')
month_year = driver.find_element(By.CLASS_NAME, 'picker-switch')

# year:2022 month:december
while month_year.text != 'December 2022':
    next_click_calendar.click()
time.sleep(2)

# day 31
calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
calendar_date.click()
time.sleep(2)

# add to cart button
btn_cart.click()
time.sleep(2)

# click checkout
btn_checkout = driver.find_element(By.CSS_SELECTOR, '#top-links > ul > li:nth-child(5) > a')
btn_checkout.click()
time.sleep(2)

## STEP 1 : Checkout Options
# click on guest account
guest = driver.find_element(By.XPATH, '//input[@value="guest"]')
guest.click()

# click continue 1
continue_1 = driver.find_element(By.ID, 'button-account')
continue_1.click()
time.sleep(1)

## STEP 2 : Billing Details
# scrolling
step_2 = driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

# first name
first_name = driver.find_element(By.ID, 'input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_first_name')
time.sleep(1)

# last_name
last_name = driver.find_element(By.ID, 'input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test_last_name')
time.sleep(1)

# email
email = driver.find_element(By.ID, 'input-payment-email')
email.click()
time.sleep(1)
email.send_keys('test@test.com')
time.sleep(1)

# telephone
telephone=driver.find_element(By.ID, 'input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)

# address
address=driver.find_element(By.ID, 'input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)

# city
city=driver.find_element(By.ID, 'input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Frankfurt')
time.sleep(1)

# postcode
postcode=driver.find_element(By.ID, 'input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)

# country
country = driver.find_element(By.ID, 'input-payment-country')
country.click()
dropdown_1 = Select(country)
time.sleep(1)
dropdown_1.select_by_index(87)
time.sleep(1)

# region
region=driver.find_element(By.ID, 'input-payment-zone')
region.click()
dropdown_2 = Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Hessen')
time.sleep(1)

# click continue 2
continue_2 = driver.find_element(By.ID, 'button-guest')
continue_2.click()
time.sleep(1)

## STEP 3 : Payment Method
#click continue 3
continue_3 = driver.find_element(By.ID, 'button-shipping-method')
continue_3.click()
time.sleep(1)

## STEP 5 : Payment Method
#accept terms & conditions
t_e = driver.find_element(By.NAME, 'agree')
t_e.click()
time.sleep(1)

#click continue 4
continue_4=driver.find_element(By.ID, 'button-payment-method')
continue_4.click()
time.sleep(3)

## STEP 6 : Confirm Order
#final price
final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)
time.sleep(2)

#click on the confirmation button
confirmation_button = driver.find_element(By.ID, 'button-confirm')
confirmation_button.click()
time.sleep(2)

#success text
success_text = driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

driver.close()