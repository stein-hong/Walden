import datetime
import re
import os
import shutil
from PIL import Image
import pytesseract


from appium import webdriver
import time
import os
import datetime
import re
import shutil
from PIL import Image

# name=datetime.datetime.now()
# strname=str(name)
# print(strname)
# pattern=re.compile('(.*)\..*')
# res=re.findall(pattern,strname)[0]
# savepath='D:\\python\\Test\\Appium\\'+str(res.replace(':',' '))
# os.makedirs(savepath)
# print(res.replace(':',' '))

# image=Image.open('D:\\python\\Test\\Appium\\2022-02-11 20 55\\2022-02-11 20 55.png')
# size=image.size
# kuangdong=image.crop((302,2150,355,2215))
# kuangdong.save('D:\\python\\Test\\Appium\\2022-02-11 20 55\\kuangdong.png')
# print(size)



# print(pytesseract.image_to_string(Image.open("D:\\python\\Test\\Appium\\2022-02-11 21 28\\kuangdong.png"),lang="eng",config="-psm 7"))
# if __name__ == '__main__':
#     text = pytesseract.image_to_string(Image.open("D:\\python\\Test\\Appium\\2022-02-12 13 31\\huangjin1.PNG"),lang="eng")
#     print(text)

# #二值化
# image=Image.open('D:\\python\\Test\\Appium\\1.jpg')
# w,h=image.size
# for x in range(w):
#     for y in range(h):
#         pixel=image.getpixel((x,y))
#
#         # r=pixel[0],g=pixel[1],b=pixel[2]
#         print(pixel)
        # if pixel[0]>100 or pixel[1]>100 or pixel[2]>100:
        #     image.putpixel((x,y),(0,0,0))
        # else:
        #     image.putpixel((x, y), (255, 255, 255))
# image.save('D:\\python\\Test\\Appium\\2022-02-12 13 31\\huangjin1.PNG')


#统计图片内偏红点个数
# image=Image.open('D:\\python\\Test\\Appium\\image\\0find2.png')
# w,h=image.size
# # print(w,h)
# i=0
# for x in range(w):
#     for y in range(h):
#         pixel=image.getpixel((x,y))
#         # print(pixel)
#         if pixel[2]>220:
#             i=i+1
# print(i)

#恢复输入法
# os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')


# 得到黄巾个数为0的截图
# desired_caps = {
#     'platformName': 'Android', # 被测手机是安卓
#     'platformVersion': '11', # 手机安卓版本
#     'deviceName': 'desperado', # 设备名，安卓手机可以随意填写
#     'appPackage': 'com.tencent.tmgp.sgqyz', # 启动APP Package名称
#     'appActivity': 'com.tencent.gcloud.msdk.core.policy.MSDKPolicyActivity', # 启动Activity名称
#     'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
#     'resetKeyboard': True, # 执行完程序恢复原来输入法
#     'noReset': True,       # 不要重置App
#     'newCommandTimeout': 6000,
#     'automationName' : 'UiAutomator2'
#   }
# # 连接Appium Server，初始化自动化环境
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# # 最初登录界面，设置缺省等待时间
# time.sleep(10)
# # 取消登录页面提醒
# driver.tap([(710, 2740)], 360)
# # 登录
# driver.tap([(715, 2750)], 340)
# time.sleep(6)
# # 取消开始推送
# driver.tap([(906, 492),(910, 485)], 210)
# time.sleep(0.5)
# driver.tap([(910, 485)], 350)
# time.sleep(0.3)
# driver.tap([(890, 480)], 310)
# time.sleep(0.32)
# driver.tap([(220,2820)],220)
# time.sleep(2)
# #搜索野怪
# driver.tap([(100,2280)],110)
# #拖动显示野怪
# driver.swipe(1050,2130,110,2132,560)
# time.sleep(1)
# driver.tap([(1200, 1970)], 180)      #点击选择南蛮部落
# time.sleep(1)
# driver.tap([(890,1980)],225)
# driver.get_screenshot_as_file('D:\\python\\Test\\Appium'+'\\'+'3.png')
# image=Image.open('D:\\python\\Test\\Appium'+'\\'+'3.png')
# huangjin=image.crop((934,2155,984,2215))        #黄巾
# huangjin.save('D:\\python\\Test\\Appium'+'\\'+'5.png')


# shutil.rmtree('D:\\python\\Test\\Appium\\test')