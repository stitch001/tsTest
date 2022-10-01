# 导入 webdriver
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

# 继承 unittest.TeseCase 类
class AutoTest1(unittest.TestCase):

    # 每个case测试之前执行
    def setUp(self) -> None:
        print("--- case setup ---")

    # case 结束后执行
    def tearDown(self) -> None:
        print("--- case teardown ---")

    # 一个case
    def test_open(self):
        service = Service(executable_path=r"D:\lib\Documents\Programming\tsTest\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        driver.get("http://localhost:5500/")
        submit_button = driver.find_element(by=By.ID, value="bt1")
        submit_button.click()
        data_p = driver.find_element(By.ID, "datap")
        self.assertEqual(data_p.text, "windows,linux,MacOS")
        driver.quit()
    
    # Negative 的case
    @unittest.expectedFailure
    def test_ok(self):
        self.assertEqual("abc","bcd")
