from webdriver_helper.pom import *


class AdminPage(BasePage):
    url = "http://16.163.103.237:81/authorization/admin"
    btn_authorization = LazyElement(By.XPATH, '//*[@id="root"]/div/nav/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/ul/div[1]/div[2]/h6')
    btn_adminList = LazyElement(By.XPATH,
                                    '//*[@id="root"]/div/nav/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/ul/div[2]/div/div/ul/a[1]/div/h6')
    btn_newAccount = LazyElement(By.XPATH, '//*[@id="root"]/div/main/div[2]/div[3]/div[2]/div[1]/div[3]/button[2]')
    ipt_username = LazyElement(By.XPATH, '//*[@id="username"]', check_on_init=False)
    btn_role = LazyElement(By.XPATH, '//*[@id="role"]', check_on_init=False)
    btn_role_admin = LazyElement(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[1]', check_on_init=False)
    btn_role_streamer = LazyElement(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[2]', check_on_init=False)
    btn_role_streamerAss = LazyElement(By.XPATH, '//*[@id="menu-role_id"]/div[3]/ul/li[3]', check_on_init=False)
    ipt_remark = LazyElement(By.XPATH, '//*[@id="remark"]', check_on_init=False)
    btn_inactive = LazyElement(By.XPATH, '//*[@id="status"]/label[2]/span[1]/input', check_on_init=False)
    btn_active = LazyElement(By.XPATH, '//*[@id="status"]/label[2]/span[1]/input', check_on_init=False)
    btn_cancel = LazyElement(By.XPATH, '//*[@id="status"]/label[2]/span[1]/input', check_on_init=False)
    btn_confirm = LazyElement(By.XPATH, '/html/body/div[2]/div[3]/div/form/div/div[2]/button[2]', check_on_init=False)
    suc_msg = LazyElement(By.XPATH, '/div/div/div[2]', check_on_init=False)
    err_msg = LazyElement(By.XPATH, '//*[@id="username-helper-text"]', check_on_init=False)
    dup_msg = LazyElement(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]', check_on_init=False)

    def get_msg(self, msg):
        if msg == 'Only letters and numbers allowed':
            return self.wait.until(lambda _: self.err_msg.text)
        if msg == 'Admin username duplicated':
            return self.wait.until(lambda _: self.dup_msg.text)
        if msg == 'Add account successfully.':
            return self.wait.until(lambda _: self.suc_msg.text)

    def new_admin(self, username, role):
        self.click(self.btn_newAccount)
        self.send_keys(self.ipt_username, username)
        self.click(self.btn_role)
        if role == 'admin':
            self.click(self.btn_role_admin)
        if role == 'streamer':
            self.click(self.btn_role_streamer)
        if role == 'streamerAss':
            self.click(self.btn_role_streamerAss)
        self.send_keys(self.ipt_remark, 'pytest')
        self.click(self.btn_confirm)
