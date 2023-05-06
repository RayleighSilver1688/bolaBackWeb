import time

from webdriver_helper.pom import *


class LoginPage(BasePage):
    url = "http://16.163.103.237:81/login"
    ipt_username = LazyElement(By.XPATH, '//*[@id="username-login"]')
    ipt_password = LazyElement(By.XPATH, '//*[@id="-password-login"]')
    btn_submit = LazyElement(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/div['
                                       '3]/div/button')
    username_tips = LazyElement(By.XPATH, '//*[@id="standard-weight-helper-text-username-login"]', check_on_init=False)
    password_tips = LazyElement(By.XPATH, '//*[@id="standard-weight-helper-text-password-login"]', check_on_init=False)
    error_msg = LazyElement(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]', check_on_init=False)
    suc_msg = LazyElement(By.XPATH, '//*[@id="root"]/div/main/div[2]/div[2]/div/div/nav/ol/li[3]/h6',
                          check_on_init=False)  # 动态元素，初始化不检查是否存在
    btn_avatar = LazyElement(By.XPATH, '//*[@id="root"]/div/header/div/div[2]/button', check_on_init=False)
    btn_Logout = LazyElement(By.XPATH, '//*[@id="root"]/div/header/div/div[2]/div/div/div/div/div/div/div/div['
                                       '4]/button', check_on_init=False)

    def get_msg(self, msg):
        if msg == 'Dashboard':
            return self.wait.until(lambda _: self.suc_msg.text)
        if msg == 'Username is required':
            return self.wait.until(lambda _: self.username_tips.text)
        if msg == 'Password is required':
            return self.wait.until(lambda _: self.password_tips.text)
        if msg == 'User does not exist':
            return self.wait.until(lambda _: self.error_msg.text)
        if msg == 'Wrong password':
            return self.wait.until(lambda _: self.error_msg.text)

    def login(self, username, password):
        self.send_keys(self.ipt_username, username)
        self.send_keys(self.ipt_password, password)
        self.click(self.btn_submit)


class AdminPage(BasePage):
    url = "http://16.163.103.237:81/login"
    ipt_username = LazyElement(By.XPATH, '//*[@id="username-login"]')
    ipt_password = LazyElement(By.XPATH, '//*[@id="-password-login"]')
    btn_submit = LazyElement(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/form/div/div['
                                       '3]/div/button')
    suc_msg = LazyElement(By.XPATH, '//*[@id="root"]/div/main/div[2]/div[2]/div/div/nav/ol/li[3]/h6',
                          check_on_init=False)  # 动态元素，初始化不检查是否存在

    def get_msg(self):
        return self.wait.until(lambda _: self.suc_msg.text)

    def login(self, username, password):
        self.send_keys(self.ipt_username, username)
        self.send_keys(self.ipt_password, password)
        self.click(self.btn_submit)


