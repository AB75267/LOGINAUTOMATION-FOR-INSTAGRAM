from time import sleep
from selenium import webdriver 
from py import USERNAME,PASSWORD   
driver=webdriver.Chrome ()
driver.get("https://www.instagram.com/")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(USERNAME)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(PASSWORD)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()



