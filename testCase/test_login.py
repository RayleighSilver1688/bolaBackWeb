import pytest

from core.loginPO import LoginPage, AdminPage, AdminPage
from core.data import read_csv


@pytest.mark.parametrize(
    "username, password, msg",
    read_csv("loginPage.csv"),
)
def test_login(driver, username, password, msg):
    driver.get(LoginPage.url)
    page = LoginPage(driver)
    page.login(username, password)
    assert msg == page.get_msg(msg)


def test_new_admin(user_driver):
    user_driver.get(AdminPage.url)
    page = AdminPage(user_driver)
    # page = page.new_address()
    # page.sbmint(
    # "username", "phone", "省市区", alias=""
    # )
    # assert pasge_msg == "操作成功"
