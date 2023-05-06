import pytest

from core.loginPO import LoginPage
from core.adminPO import AdminPage
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


@pytest.mark.parametrize(
    "username, role, msg",
    read_csv("newAdmin.csv"),
)
def test_new_admin(user_driver, username, role, msg):
    user_driver.get(AdminPage.url)
    page = AdminPage(user_driver)
    page.new_admin(username, role)
    assert msg == page.get_msg(msg)
