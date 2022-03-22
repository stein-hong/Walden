import uiautomator2
import time

driver=uiautomator2.connect_usb('416ed9b3')
driver.screen_on()
driver.swipe_points([(700,2000),(690,1000)],0.6)
time.sleep(0.5)
driver.click(340,1700)
driver.click(710,1450)
driver.click(717,1919)
driver.click(720,1700)
driver.click(343,1921)
driver.click(345,1450)
time.sleep(0.2)
