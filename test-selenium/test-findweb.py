import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #导入操作键盘快捷键

driver= webdriver.Firefox()            #其他浏览器如谷歌可能需要定义路径
driver.get('http://www.baidu.com')
assert "百度"in driver.title              #断言判断“百度”是否在文章标题中，无则出现断言报错
print(driver.title)
elem=driver.find_element_by_id("kw")   #通过name查找
elem.send_keys(u"数据分析")
elem.send_keys(Keys.RETURN)             #Keys.RETURN为回车键

time.sleep(10)
driver.save_screenshot('baidu1.png')
driver.close()                           #关闭驱动
driver.quit()                       #推出驱动，quit退出，而close只是关闭