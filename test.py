from selenium import webdriver   #导入selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()   #打开浏览器

driver.get("https://www.feishu.cn/")  #输入飞书官网网址
time.sleep(2)

driver.find_element(By.XPATH,value="/html/body/div[2]/div[2]/div/div/div").click()  #关闭广告弹窗
time.sleep(2)

driver.find_element(By.XPATH,value="//*[@id='app']/div/div[2]/div/div/div/div/a[3]").click()  #进入登录页
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="switch-login-mode-box").click()  #选择账号登录
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="mobile-input-phone").send_keys("18320842163")  #输入账号
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="ud__checkbox").click()  #勾选协议
time.sleep(2)


driver.find_element(By.XPATH,value="/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/button").click()   #点击下一步
time.sleep(10)

driver.find_element(By.XPATH,value="/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/button").click()  #点击密码登录
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,value='div.ud__input-password-input-wrap > input').send_keys("qwer123789") #输入密码
time.sleep(2)

driver.find_element(By.XPATH,value="//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div[3]/div").click()  #点击下一步
time.sleep(2)

driver.find_element(By.XPATH,value="//*[@id='root']/div/div[2]/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div/div[1]/div[2]/div/div[3]/span").click()  #选择企业
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="universe-icon _pp-product-icon").click() #输入更多选项
time.sleep(2)

driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div/div/div[1]/ul/li[1]").click()  #点击消息
time.sleep(2)

driver.find_element(By.XPATH,value="/html/body/div[3]/div[2]/div[1]/section/div/section/section/section[5]").click()  #点击消息
time.sleep(2)

driver.find_element(By.XPATH,value="/html/body/div[3]/div[2]/div[1]/section/div/section/section/section[5]").click()  #点击通讯录
time.sleep(2)

driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/div[1]/section/div/main/div/div/div[2]/div[2]/div/div/div/div/div[2]/div").click()  #点击联系人
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="usercard__ctas").click() #点击发消息
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="lark-editor-container").send_keys("qwer123789") #输入消息内容
time.sleep(2)

driver.find_element(By.CLASS_NAME,value="lark-editor-container").send_keys(Keys.ENTER)   #回车发送
time.sleep(2)


driver.quit()   #退出浏览器






