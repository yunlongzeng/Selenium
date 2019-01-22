from appium import webdriver

desired_caps = desired_caps = {
  'platformName': 'Android',
  'platformVersion': '6.0.1',
  'deviceName': 'dbcbc435',
  'automationName': 'UiAutomator2',
  'noReset': True,
  'appPackage': 'org.cnodejs.android.md',
  'appActivity': '.ui.activity.LaunchActivity',
  'unicodeKeyboard': True, #此两行是为了解决字符输入不正确的问题
  'resetKeyboard': True    #运行完成后重置软键盘的状态
#   'app': PATH('/path/to/app')  #安装apk到手机
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) 
driver.find_element_by_class_name('android.widget.ImageButton').click()
driver.find_element_by_id('org.cnodejs.android.md:id/btn_nav_good').click()






