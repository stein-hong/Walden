import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import os


# driver=webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
# driver.get("https://www.baidu.com/")
#打开浏览器
# chromedriver='D:\python\webdriver\chromedriver.exe'
# os.environ["webdriver.chrome.driver"]=chromedriver
# driver=webdriver.Chrome(chromedriver)
# driver.get('https://www.baidu.com/')
#打开浏览器
driver=webdriver.Firefox()
# # headers={}
# # head["User-Agent"]='"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"'
driver.get("https://www.baidu.com/")

#登录
# login=driver.find_element_by_name("tj_login")
login=driver.find_element_by_xpath("//div[@id='u1']/a[1]")
print(login.text)
print(login.get_attribute('href'))
login.click()

#用户名，密码
name=driver.find_element_by_id("TANGRAM__PSP_11__userName")
name.clear
name.send_keys(u"斯坦洪")
pwd=driver.find_element_by_id("TANGRAM__PSP_11__password")
pwd.clear
pwd.send_keys("4285xde")

#暂停输入验证码
time.sleep(5)
pwd.send_keys(Keys.RETURN)
driver.close()



# 登录QQ
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get('http://www.zentao.net/ ')
#
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_class_name('qq').click()
# driver.switch_to.frame('ptlogin_iframe')                             # 通过frame方式定位
# driver.find_element_by_css_selector('#switcher_plogin').click()
# driver.find_element_by_id('u').send_keys('3247959119')
# driver.find_element_by_id('p').send_keys('9aaaylhxde')
# driver.find_element_by_id('login_button').click()
# time.sleep(10)
#
# driver.quit()