import time

from selenium.webdriver.common.action_chains import ActionChains    #引入鼠标键盘库
from selenium import webdriver

driver=webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
driver.set_window_size(2000,2000)
driver.get("https://www.baidu.com")


# ActionChains(driver)           #构造ActionChains对象
# context_click()                #单击鼠标右键
# double.click()                 #双击左键
# drag_and_drop(source,target)   #拖曳到某个元素后松开
# drag_and_drop_by_offset(source,xoffset,yoffset)  #拖曳到某个坐标后松开
# key_down(value,element=None)   #按下键盘某个键
# key_up(value,element=None)     #松开某个键
# move_by_offset(xoffset,yoffset)#鼠标从当前位置移动到某个坐标
# move_to_element(to_element)    #鼠标移动到某个元素

above=driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(above).perform()
time.sleep(5)
driver.quit()