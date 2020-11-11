import shelve
from time import sleep

import pytest
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

    @pytest.mark.skip
    def test_cookie(self):
        # cookies = self.driver.get_cookies()#获取当前打开页面的cookie
        # print(cookies) #拿出来的cookie信息如下
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Z-7Ct1hJy-Ob3x42M7D1Fi9p1hxdNtkeTuGwUSuV9t3gyAf1_-PsDj3KUzLOCtkFJr8CK34MfKS-KMuNXyM_qvxH_RzKXAwix7ehibrNBx_TIO1FuuBheWDW2hs_djDZtzW73_G_eRPRdo9JZe9oEZlvI7qL8A--0E73hVOD58jZEhep5QG-4UaMA6FaIQ0qfXdtGLmO8rhzpOxygM1RbjEBniBdc0SEA4UV3Ly8HRG0HVqKIX4rP668I5cMoOlXJeClMxD9FieGNSxusBMgkg'},
            {'domain': '.qq.com', 'expiry': 1605067177, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': True, 'value': '1604935201'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853545025459'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853545025459'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1605153565, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2064751088.1605067118'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1605090367, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5r6qngk'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'AgqwnI89AWpfH6Yyo6UDLTqvt0UmcGduVon6NdJiFhgYwC70QstPdGPkrB95QFid'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636192714, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636471201, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
             'value': '1604656716,1604933283,1604935192,1604935201'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607659169, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325056182431'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '6971992064'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a447797'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'dzb8dZ83HB'},
            {'domain': '.qq.com', 'expiry': 1668139165, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1744996768.1604656722'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '6f9ed2b2c9a2929d944d78622c74e5e8d3edbafa8370915387ac88433d8b44ec'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '19396440841191353'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '3964613435'}]

        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')  # 打开一个未提前登录的页面
        for cookie in cookies:  # 由于add_cookie接受的是字典类型的参数，我们把cookie从列表中遍历出来
            self.driver.add_cookie(cookie)  # 把列表遍历出来的cookie添加到页面中去
        # # 验证页面添加cookie后是否可以正常登录
        # 第一种方法
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # # 第二种方法直接刷新该页面
        # # self.driver.refresh()
        sleep(3)

    # @pytest.mark.skip
    def test_shelve(self):  # web自动化第二节课 23：42
        # cookies =[{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'Z-7Ct1hJy-Ob3x42M7D1Fi9p1hxdNtkeTuGwUSuV9t3gyAf1_-PsDj3KUzLOCtkFJr8CK34MfKS-KMuNXyM_qvxH_RzKXAwix7ehibrNBx_TIO1FuuBheWDW2hs_djDZtzW73_G_eRPRdo9JZe9oEZlvI7qL8A--0E73hVOD58jZEhep5QG-4UaMA6FaIQ0qfXdtGLmO8rhzpOxygM1RbjEBniBdc0SEA4UV3Ly8HRG0HVqKIX4rP668I5cMoOlXJeClMxD9FieGNSxusBMgkg'}, {'domain': '.qq.com', 'expiry': 1605067177, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1604935201'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853545025459'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853545025459'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1605153565, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2064751088.1605067118'}, {'domain': 'work.weixin.qq.com', 'expiry': 1605090367, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5r6qngk'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'AgqwnI89AWpfH6Yyo6UDLTqvt0UmcGduVon6NdJiFhgYwC70QstPdGPkrB95QFid'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636192714, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636471201, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1604656716,1604933283,1604935192,1604935201'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607659169, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325056182431'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '6971992064'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a447797'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'dzb8dZ83HB'}, {'domain': '.qq.com', 'expiry': 1668139165, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1744996768.1604656722'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '6f9ed2b2c9a2929d944d78622c74e5e8d3edbafa8370915387ac88433d8b44ec'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '19396440841191353'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '3964613435'}]
        # # shelve python内置模块，专门用来对数据进行持久存储的库，相当于小型的数据库
        # # 可以通过key,value 来把数据保存到shelve中
        # db = shelve.open('cookies')
        # db['cookie'] = cookies #已经存到小型数据库中就可以注释掉了
        # db.close()

        db = shelve.open('cookies')
        cookies = db['cookie']  # 拿到存好的库中的cookie
        db.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')  # 打开一个未提前登录的页面
        for cookie in cookies:  # 由于add_cookie接受的是字典类型的参数，我们把cookie从列表中遍历出来
            self.driver.add_cookie(cookie)  # 把列表遍历出来的cookie添加到页面中去
        # # 验证页面添加cookie后是否可以正常登录
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        sleep(3)
        # 找到导入联系人按钮
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[1]').click()
        # 找到上传按钮
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/a/input').send_keys(
            '/Users/duningning/Downloads/通讯录批量导入模板.xlsx')
        filename = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]').text  # 找到上传后文件的名字
        assert '通讯录批量导入模板.xlsx' == filename  # 断言
