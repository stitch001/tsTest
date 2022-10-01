# 导入 webdriver
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path=r"D:\lib\Documents\Programming\tsTest\msedgedriver.exe")
driver = webdriver.Edge(service=service)

import unittest

class AutoTest1(unittest.TestCase):
    def test_open(self):
        driver.get("http://localhost:5500/")
        submit_button = driver.find_element(by=By.ID, value="bt1")
        submit_button.click()
        data_p = driver.find_element(By.ID, "datap")
        self.assertEqual(data_p.text, "windows,linux,MacOS")
        driver.quit()
        return 
    
    @unittest.expectedFailure
    def test_ok(self):
        self.assertEqual("abc","bcd")

if __name__ == "__main__":
    unittest.main()