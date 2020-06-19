import unittest
from selenium import webdriver
from ddt import ddt,data,unpack
import time
from shujuqudong_ddt.Excel_00 import Excel_data

Path = "C:\\Users\\Administrator\\PycharmProjects\\shujuqudong_ddt\\123.xlsx"
excel= Excel_data(Path, sheetname="Sheet2")
@ddt
class OA_login_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.0.126:801")
        self.driver.implicitly_wait(5)

    # 正用例，正常登录
    def test_login_01(self):
        self.driver.find_element_by_css_selector("#tbx_UserName").clear()
        self.driver.find_element_by_css_selector("#tbx_UserName").send_keys("adm")
        self.driver.find_element_by_css_selector("#tbx_Password").clear()
        self.driver.find_element_by_css_selector("#tbx_Password").send_keys("adm")
        self.driver.find_element_by_css_selector("#ibtLogin").click()
        self.driver.implicitly_wait(5)
        a = self.driver.find_element_by_css_selector(".collapse").text
        self.assertEqual(a, "电子邮件", msg="登陆失败")

    # 反用列，用户名正确，密码为空，密码为空格，密码错误
    @data(*excel.post_data())
    @unpack
    def test_login_02(self, data1, data2):
        self.driver.find_element_by_css_selector("#tbx_UserName").clear()
        self.driver.find_element_by_css_selector("#tbx_UserName").send_keys(data1)
        self.driver.find_element_by_css_selector("#tbx_Password").clear()
        self.driver.find_element_by_css_selector("#tbx_Password").send_keys(data2)
        self.driver.find_element_by_css_selector("#ibtLogin").click()
        time.sleep(3)
        a = self.driver.switch_to.alert.text
        self.assertEqual(a, "失败：用户账号或密码错误！")
        self.driver.switch_to.alert.accept()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

