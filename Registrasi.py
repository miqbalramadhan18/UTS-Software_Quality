from selenium import webdriver
# menggunakan fungsi By
from selenium.webdriver.common.by import By
# menggunakan fungsi time
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)

# Masuk Ke halaman utama
driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

#Register
time.sleep(2) # Tunggu 2 detik sebelum mencari elemen

#get by id untuk field yang akan di isi
first_name_input = driver.find_element("id","firstname")
last_name_input = driver.find_element("id","lastname")
email_input = driver.find_element("id","email_address")
password_input = driver.find_element("id","password")
cpassword_input = driver.find_element("id","password-confirmation")
create_button = driver.find_element(By.CSS_SELECTOR,"div.primary button.action.submit.primary[title='Create an Account']")

#Isi Field
first_name_input.send_keys("Mochammad Iqbal")
last_name_input.send_keys("Ramadhan")
email_input.send_keys("1214086@std.ulbi.ac.id")
password_input.send_keys("Qobel123iqbal")
cpassword_input.send_keys("Qobel123iqbal")
create_button.click()
