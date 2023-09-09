from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
 
options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/sana9/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
sleep(10)
driver.get('https://web.whatsapp.com/')
numbers= ["" ,""] # put your numbers 
wait=WebDriverWait(driver,100)

for number in numbers: 
    search=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))
    search.send_keys(number , Keys.ENTER)

#message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    mes="hii"
#message = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    sleep(6)
    message_box=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
    message_box.send_keys(mes ,Keys.ENTER)
    sleep(10)








