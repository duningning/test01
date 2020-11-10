from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWebDemo():
    def setup_method(self):
        options = Options()  # 复用进程，只针对Chrome浏览器有
        options.debugger_address = "127.0.0.1:9222"  # 链接本机debug地址
        self.driver = webdriver.Chrome(options=options)  # 验证test_cookie时把参数去掉
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_weixin(self):  # 测试的时候只点击运行该条即可
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()  # 登陆企业微信后点击联系人
        sleep(3)

    def test_cookie(self):
        # cookies = self.driver.get_cookies()#获取当前打开页面的cookie
        # print(cookies) #拿出来的cookie信息如下
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853545025459'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '8CqLLv0WwoiUqnlmYvVOVF1WxmTuomGVWcRlBmxxeMuIEpwDoFQmiUNI92zTWWfu0CPweLsMNKaMzlw9eEOZ7Y3gl2egE0QB0IsfuDpqpzIHBw7_WFYdBaoeD-6Fr9IKNJQjxtpO749Zmb6DS-pa7ejNhMOdP7ZGo4Fv9qZ9rdOEfjNFQG7gd73eY63RrFle0E7RumXU_sYciRM2lo1lCY0xS3gxgP_w4fRaUadGcQAoRHirN--NI76eO4v5lSRUYNPccZ20FEq-Jf8E14pX1w'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853545025459'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325056182431'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'AgqwnI89AWpfH6Yyo6UDLRgqD0e2Wgg4tTA4E7fjA0-PF_rEbLxqdmqwvx65ySQJ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2561932'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604963838, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8st0e4t'},
            {'domain': '.qq.com', 'expiry': 1605021655, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1932309850.1604932302'},
            {'domain': '.qq.com', 'expiry': 1668007255, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1744996768.1604656722'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636192714, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636471201, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1604656716,1604933283,1604935192,1604935201'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3964613435'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607527286, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604935201'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '19396440841191353'},
            {'domain': '.qq.com', 'expiry': 1604935315, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '6971992064'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '6f9ed2b2c9a2929d944d78622c74e5e8d3edbafa8370915387ac88433d8b44ec'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'dzb8dZ83HB'}]
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')  # 打开一个未提前登录的页面
        for cookie in cookies:  # 由于add_cookie接受的是字典类型的参数，我们把cookie从列表中遍历出来
            self.driver.add_cookie(cookie)  # 把列表遍历出来的cookie添加到页面中去
        # 验证页面添加cookie后是否可以正常登录
        # self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 第二种方法直接刷新该页面
        self.driver.refresh()
        sleep(3)
