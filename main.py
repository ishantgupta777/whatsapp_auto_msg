from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

input('Scan your QR code and then press Enter to continue')

group_title = 'Fuck off'

msg = 'This is a test message, ignore this and dont reply. It is just to test a script.'

driver.find_element_by_xpath("//span[@class = '_1wjpf _3NFp9 _3FXB1' and @title = '" + group_title +"']").click()

time.sleep(2);

# group_mem_str = driver.find_element_by_css_selector('.O90ur._3FXB1').text

# group_mem_list = group_mem_str.split(',')

# for member in group_mem_list:
#     user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(member))
#     user.click()


# !make sure you open all contacts in group details before using this script



driver.find_element_by_xpath("//div[@class = '_3XrHh']/span[@class = '_1wjpf _3NFp9 _3FXB1' and @title = '" + group_title +"']").click()

time.sleep(2);

try:
    if driver.find_element_by_css_selector('._3Wg5_').size['width'] != 0:
        driver.find_element_by_css_selector('._3Wg5_').click()
except :
    print('Group has less members')

time.sleep(4)

members = driver.find_elements_by_css_selector('._2EXPL._3xj48 ._1wjpf._3NFp9._3FXB1')

group_mem_list = []

for member in members:
    group_mem_list.append(member.text)

print(group_mem_list)
group_mem_list.pop(0)


for member in group_mem_list:
    try:
        driver.find_element_by_css_selector('._3F6QL._3xlwb ._2S1VP').send_keys(member)
        time.sleep(1)
        user = driver.find_element_by_xpath('//span[@title = "' + member + '" ]')
        user.click()
        driver.find_element_by_css_selector('._3F6QL._2WovP ._2S1VP').send_keys(msg)
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
        driver.find_element_by_css_selector('._3F6QL._3xlwb ._2S1VP').clear()
    except:
        driver.find_element_by_css_selector('._3F6QL._3xlwb ._2S1VP').clear()
        continue
    

driver.quit()