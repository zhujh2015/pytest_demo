import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_lagou_search():
    #执行用例之前的操作
    def setup_method(self,method):
        self.driver=webdriver.Chrome()
        self.vars={}

    # 执行用例之后的操作
    def teardown_method(self,method):
        self.driver.quit()

    #弹出框div 显示
    def wait_div_block(self):
        displaystr=self.driver.find_element(By.ID, "colorbox").get_attribute("style")
        print(displaystr)
        return displaystr.__contains__('display: block')

    #用例结构
    def test_search_1(self):
        #打开页面，设置窗口大小
        self.driver.get("https://www.lagou.com/")
        self.driver.set_window_size(1546,922)

        #WebDriverWait(self.driver, 10).until(method=self.wait_div_block(),message='')
        # 强制等待
        # 定位到弹窗，点击叉号
        time.sleep(2)
        self.driver.find_element(By.ID, "cboxClose").click()
        # 根据弹框页面获取跟北京相匹配的文本框

        time.sleep(2)
        #输入搜索信息
        search_input_el=self.driver.find_element(By.ID,"search_input")
        search_input_el.send_keys("字节跳动")
        search_button_el=self.driver.find_element(By.ID,"search_button")
        search_button_el.click()

        search_text_el=self.driver.find_element(By.CSS_SELECTOR,".cl-right-top__1cCMk div")
        print(search_text_el.text)
        assert search_text_el.text == "“我们的使命：激发创造，丰富生活。”"

