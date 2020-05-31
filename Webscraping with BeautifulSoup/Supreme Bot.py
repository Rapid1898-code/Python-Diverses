import os
from selenium import webdriver
import time

keys = {"product_url": "https://www.supremenewyork.com/shop/jackets/qxgy36ias",
        "name": "John",
        "email": "testmail@gmx.com",
        "address": "Forest Hill Drive 3",
        "zip": "1230",
        "phone_number": "08503020484",
        "card_number": "841181111212",
        "card_cvv": 333
        }

def order(k):
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
    driver.get(k["product_url"])
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath ('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="cnb"]').send_keys(k["card_number"])
    driver.find_element_by_xpath('//*[@id="vval"]').send_keys(k["card_cvv"])
    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[4]').click()
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

if __name__ == "__main__":
    order(keys)
