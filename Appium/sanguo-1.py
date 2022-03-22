from appium import webdriver
import time
import os
import datetime
import re
import shutil
from PIL import Image




def main():
  lockon()
    #打开游戏
  desired_caps = {
    'platformName': 'Android', # 被测手机是安卓
    'platformVersion': '11', # 手机安卓版本
    'deviceName': 'desperado', # 设备名，安卓手机可以随意填写
    'appPackage': 'com.tencent.tmgp.sgqyz', # 启动APP Package名称
    'appActivity': 'com.tencent.gcloud.msdk.core.policy.MSDKPolicyActivity', # 启动Activity名称
    'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
    'resetKeyboard': True, # 执行完程序恢复原来输入法
    'noReset': True,       # 不要重置App
    'newCommandTimeout': 6000,
    'automationName' : 'UiAutomator2'
  }
  # 连接Appium Server，初始化自动化环境
  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
  kaishi(driver)                      #坊市任务
  convert(driver)                     #切换到外城
  savepath,wholepath=getscreen(driver)                 #野怪截图
  kuangnum, huangnum, nanmannum=yeguai(savepath,wholepath)
  fail=0                                                             #拉取南蛮失败次数
  bijiao(kuangnum, huangnum, nanmannum,driver,savepath,wholepath,fail)         #刷野
  # findnum=0                                                                      #换寨子找矿次数
  # findnum=findkuang(driver, findnum, savepath)

  shutil.rmtree('D:\\python\\Test\\Appium\\image')    #删除图片文件夹
  os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')   #恢复输入法
  # driver.quit()


def lockon():
    os.system('adb shell input keyevent 26')
    time.sleep(1)
    os.system('adb shell input swipe 700 2000 690 1000')    # 显示
    time.sleep(0.2)
    os.system('adb shell input tap 340 1700')
    os.system('adb shell input tap 710 1450')
    os.system('adb shell input tap 717 1919')
    os.system('adb shell input tap 720 1700')
    os.system('adb shell input tap 343 1921')
    os.system('adb shell input tap 348 1450')

def bijiao(kuangnum, huangnum, nanmannum,driver,savepath,wholepath,fail):                        #比较黄巾南蛮矿洞数
     print(nanmannum,huangnum)
     if kuangnum>=0 or huangnum>=0 or nanmannum>=0:
         shuaye(kuangnum, huangnum, nanmannum,driver,savepath,wholepath,fail)
     else:
         pass

def shuaye(kuangnum, huangnum, nanmannum,driver,savepath,wholepath,fail):                                  #刷野                                                                                            #拉取南蛮助阵失败次数
    while huangnum<10 and nanmannum<10:
        dahuangjin(driver, huangnum)                #打黄巾
        fail=dananman(driver, nanmannum,savepath,fail)        #打南蛮
        print(fail)

        time.sleep(10)                 #循环打野
        savepath, wholepath = getscreen(driver)
        kuangnum, huangnum, nanmannum = yeguai(savepath, wholepath)
        if fail>=2:
            nanmannum=11                                                                  #拉取助阵失败次数过多，放弃打南蛮
            bijiao(kuangnum,huangnum,nanmannum,driver,savepath,wholepath,fail)
        else:
            bijiao(kuangnum, huangnum, nanmannum, driver, savepath, wholepath,fail)

    while huangnum<10 and nanmannum>10:
        dahuangjin(driver, huangnum)
        time.sleep(10)  # 循环
        savepath, wholepath = getscreen(driver)
        kuangnum, huangnum, nanmannum = yeguai(savepath, wholepath)
        bijiao(kuangnum, huangnum, nanmannum,driver,savepath,wholepath,fail)

    while huangnum>10 and nanmannum<10:
        fail=dananman(driver, nanmannum,savepath,fail)
        print(fail)
        time.sleep(10)  # 循环
        savepath, wholepath = getscreen(driver)
        kuangnum, huangnum, nanmannum = yeguai(savepath, wholepath)
        if fail>=2:
            nanmannum=11                                                                  #拉取助阵失败次数过多，放弃打南蛮
            bijiao(kuangnum,huangnum,nanmannum,driver,savepath,wholepath,fail)
        else:
            bijiao(kuangnum, huangnum, nanmannum, driver, savepath, wholepath,fail)

    while huangnum>10 and nanmannum>10:
        break



def kaishi(driver):                #开始游戏页面及执行坊市

  # 最初登录界面，设置缺省等待时间
  time.sleep(12)
  # 取消登录页面提醒
  driver.tap([(710, 2740)], 360)
  # 登录
  driver.tap([(715, 2750)], 340)
  time.sleep(6)
  # 取消开始推送
  driver.tap([(906, 492),(910, 485)], 210)
  time.sleep(0.5)
  driver.tap([(910, 485)], 350)
  time.sleep(0.3)
  driver.tap([(890, 480)], 310)
  time.sleep(0.32)
  #执行坊市
  driver.tap([(1313,2870)],220)
  time.sleep(0.5)
  driver.tap([(1100, 1486)], 240)
  time.sleep(0.5)
  driver.tap([(1074, 2860)], 200)
  time.sleep(0.5)
  driver.tap([(1084, 2850)], 200)
  time.sleep(0.5)
  driver.tap([(83, 250)], 220)
  time.sleep(0.5)
  driver.tap([(89, 260)], 210)
  time.sleep(0.5)

def convert(driver):               #切换内外城
  #切换到外城
  driver.tap([(220,2820)],220)
  time.sleep(2)
  # #搜索野怪
  # driver.tap([(100,2280)],110)
  # #拖动显示野怪
  # driver.swipe(1050,2130,110,2132,560)

def getscreen(driver):
  # 截图识别野怪数量
  # 搜索野怪
  driver.tap([(100,2280)],110)
  #拖动显示野怪
  driver.swipe(1050,2130,110,2132,560)
  name=datetime.datetime.now()    #正则提取时间为图片命名
  strname=str(name)
  pattern=re.compile('(.*)\..*')
  res=re.findall(pattern,strname)[0]
  ress=res.replace(':',' ')

  savepath='D:\\python\\Test\\Appium\\image\\'+str(ress)   #建立路径保存整幅图片
  picname='\\'+str(ress)+'.png'
  wholepath=savepath+picname
  os.makedirs(savepath)
  driver.get_screenshot_as_file(wholepath)
  driver.tap([(1360, 1770)], 130)
  time.sleep(0.1)
  return (savepath,wholepath)

#像素识别野怪及矿洞是否有剩余
def yeguai(savepath,wholepath):
  image = Image.open(wholepath)
  kuangdong = image.crop((302, 2150, 355, 2215))  # 矿洞
  kuangdong.save(savepath+'\\kuangdong.png')

  huangjin=image.crop((934,2155,984,2215))        #黄巾
  huangjin.save(savepath+'\\huangjin.png')

  nanman=image.crop((1250,2150,1300,2215))       #南蛮
  nanman.save(savepath+'\\nanman.png')

  kuangimage = Image.open(savepath+'\\kuangdong.png')              #统计矿洞数像素偏红数量
  w1, h1 = kuangimage.size
  kuangnum = 0
  for x in range(w1):
    for y in range(h1):
      pixel1 = kuangimage.getpixel((x, y))
      if pixel1[0] > 180:
        kuangnum = kuangnum + 1

  huangimage=Image.open(savepath+'\\huangjin.png')                  #统计黄巾数
  w2, h2 = huangimage.size
  huangnum = 0
  # huang0=0                               #个数为0却显示绿色
  for x in range(w2):
    for y in range(h2):
      pixel2 = huangimage.getpixel((x, y))
      if pixel2[0] > 180:
        huangnum = huangnum + 1
      # if pixel2[0]>130:
      #   huang0=huang0+1
  # if huang0 ==45:
  #     huangnum=11                  #绿色0时将红色像素数置为大于10
  # else:
  #     pass


  nanmanimage = Image.open(savepath+'\\nanman.png')  # 统计南蛮数
  w3, h3 = nanmanimage.size
  nanmannum = 0
  for x in range(w3):
    for y in range(h3):
      pixel3 = nanmanimage.getpixel((x, y))
      if pixel3[0] > 180:
       nanmannum = nanmannum + 1
  return (kuangnum,huangnum,nanmannum)


def dahuangjin(driver,huangnum):          #打黄巾
    # 搜索野怪
    driver.tap([(100, 2280)], 110)
    # 拖动显示野怪
    driver.swipe(1050, 2130, 110, 2132, 560)
    driver.tap([(890,1980)],225)            #选择黄巾框
    time.sleep(0.2)
    driver.tap([(452,2864)],190)
    time.sleep(0.6)
    driver.tap([(1134,1091)],120)
    time.sleep(1.8)
    driver.tap([(700,2195)], 230)   #前往歼敌
    # driver.swipe(700, 2190, 790, 2200, 160)     #前往歼敌
    time.sleep(1.5)
    driver.tap([(1317,1024)], 220)
    time.sleep(1)
    driver.tap([(1034,1157)], 210)
    time.sleep(1)
    driver.tap([(1014,2850)], 226)
    time.sleep(1)

def dananman(driver,nanmannum,savepath,fail):     #打南蛮
    # 搜索野怪
    driver.tap([(100, 2280)], 110)
    # 拖动显示野怪
    driver.swipe(1050, 2130, 110, 2132, 400)
    time.sleep(0.1)
    driver.tap([(1200, 1970)], 180)      #点击选择南蛮部落
    time.sleep(1)
    driver.tap([(880, 2867)], 190)
    time.sleep(1)
    driver.tap([(1000, 1909)], 190)           #南蛮刷新点提醒
    time.sleep(1)
    driver.tap([(711, 2065)], 190)             #发起集结
    time.sleep(0.5)
    driver.tap([(1014, 1919)], 230)         #盟友已经发起集结提醒
    time.sleep(0.5)
    driver.tap([(1150, 2232),(1155,2228)], 220)      #选择集结点
    time.sleep(1)
    driver.tap([(1174, 708)], 150)    #选择集结地
    time.sleep(1)
    driver.swipe(1064, 1975, 455, 1985, 200)      #集结数量
    time.sleep(0.5)
    driver.tap([(711, 2368)], 190)      #前往编队
    time.sleep(1)
    driver.tap([(1007, 2840)], 190)     #出征
    time.sleep(1)
    driver.tap([(500, 1500)], 190)      #邀请助阵
    time.sleep(0.5)

    #判断是否有助阵队伍
    driver.get_screenshot_as_file(savepath+'\\'+'zhuzhen.png')
    image=Image.open(savepath+'\\'+'zhuzhen.png')
    zhuzhengduiwu=image.crop((1050,1160,1333,1204))
    zhuzhengduiwu.save(savepath+'\\zhuzhenduiwu.png')
    zhuz = Image.open(savepath+'\\zhuzhenduiwu.png')
    w, h = zhuz.size
    zhu = 0
    for x in range(w):
        for y in range(h):
            pixel = zhuz.getpixel((x, y))
            if pixel[0] > 180:
                zhu = zhu + 1
    if zhu>100:                                   #有助阵队伍
        driver.tap([(1194, 1220)], 150)
        time.sleep(1)
        driver.tap([(90, 240)], 150)
        time.sleep(0.5)
        driver.tap([(95, 241)], 160)       #返回到主地图
        time.sleep(0.5)
    else:                                  #解散集结
        fail=fail+1                        #拉取失败次数
        # print(fail)
        driver.tap([(95, 245)], 150)
        time.sleep(0.5)
        driver.tap([(1300, 1000)], 140)    #解散
        time.sleep(0.5)
        driver.tap([(1014, 1909)], 160)
        time.sleep(0.2)
    return fail

def findkuang(driver,findnum,savepath):          #找矿
    # 搜索
    driver.tap([(100, 2280)], 110)
    # 拖动显示矿洞
    driver.swipe(1050, 2130, 110, 2132, 400)
    time.sleep(0.2)
    driver.tap([(260, 1985)], 110)
    time.sleep(0.1)
    driver.tap([(1167, 2677)], 110)
    time.sleep(0.3)
    driver.swipe(450, 2400, 450, 1300, 400)       #上拖显示找矿寨子
    time.sleep(0.2)

    kuangzhailist = [(1184, 2558), (1190, 2280), (1207, 1982), (1190, 1700), (1200, 1400), (1200, 1100),(1200, 811)]  # 寨子坐标
    driver.tap([kuangzhailist[findnum]],100)
    time.sleep(0.2)
    driver.tap([(425, 2854)], 110)
    time.sleep(0.5)
    kuangimage(driver,savepath,findnum)                                #找矿截图识别及是否前往挖矿


def kuangimage(driver,savepath,findnum):
    # k=0
    # while k<4:
    #     if k>0:                                               #第一次不用拖动
            driver.swipe(1230,2190,1217,1252,1.5)                                            #滚动找矿
            time.sleep(3)


            driver.swipe(1230, 2190, 1217, 1252, 1.5)  # 滚动找矿
            time.sleep(3)
            driver.swipe(1230,2190,1217,1252,1.5)                                            #滚动找矿
            time.sleep(3)
            driver.swipe(1230,2190,1217,1252,1.5)                                            #滚动找矿
            time.sleep(3)
    #     driver.get_screenshot_as_file(savepath + '\\' + str(findnum) + str(k) + 'kuang.png')
    #     kuang = Image.open(savepath + '\\' +str(findnum)+ 'kuang.png')
    #     find1 = kuang.crop((515, 1024, 710, 1140))
    #     find1.save(savepath + '\\'+str(findnum)+str(k)+'find1.png')
    #
    #     find2=kuang.crop((525,1353,711,1456))
    #     find2.save(savepath + '\\' + str(findnum)+str(k) + 'find2.png')
    #
    #     find3=kuang.crop((518,1663,711,1766))
    #     find3.save(savepath + '\\' + str(findnum)+str(k) + 'find3.png')
    #
    #     find4=kuang.crop((518,1965,748,2079))
    #     find4.save(savepath + '\\' + str(findnum) +str(k)+ 'find4.png')
    #
    #     kuangaxis=[(1127,1101),(1134,1407),(1134,1723),(1124,2032)]         #找矿'前往'坐标
    #
    #     i=0
    #     for item in ['find1','find2','find3','find4']:
    #         kuangshu=0
    #         image = Image.open(savepath + '\\' + str(findnum)+str(k) +item+'.png')
    #         w, h = image.size
    #         for x in range(w):
    #             for y in range(h):
    #                 pixel=image.getpixel((x,y))
    #                 if pixel[2] > 220:
    #                     kuangshu = kuangshu + 1
    #         if kuangshu>10:                                  #空矿
    #            driver.tap([kuangaxis[i]])
    #            time.sleep(2)                                 #前往
    #            driver.tap([(918,1882)],150)
    #            time.sleep(1.5)
    #            driver.tap([(1014,2847)],130)      #出征
    #            time.sleep(1)
    #            driver.tap([(400,1900)],140)     #盟友前往提醒,取消挖矿
    #            time.sleep(1)
    #            driver.tap([(1120,256)],120)     #误触野怪取消
    #            KUANG=True
    #            break
    #
    #         else:
    #             i=i+1
    #             continue
    #     if KUANG==True:
    #         break
    #     else:
    #         k=k+1
    #         continue
    # if KUANG!=True:            #一个寨子没找到矿
    #     driver.tap([(1254,675)],120)    #退出矿洞显示界面
    #     time.sleep(0.3)
    #     driver.tap([(1120, 256)], 120)   #返回原始外城界面
    # else:
    #     findnum=findnum+1
    #     return findnum
    #



if __name__ == '__main__':
    main()

# driver.quit()



