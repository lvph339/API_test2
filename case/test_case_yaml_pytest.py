import ddt
from utils.getwt import get_token
import requests
import threading
from utils.Logger import Log
from utils.envUtils import envUtils
from utils.OperationalData import data_splicing
from utils.OperationalData import get_exp_datas
from utils.OperationalData import dependent_data

log = Log()
l_params = {}
@ddt.ddt
class Test_test():

    @classmethod
    def setUpClass(cls):
        log.info('接口测试开始了')

    @classmethod
    def tearDownClass(cls):
        log.info('接口测试结束了')

    @ddt.file_data('/Users/lph/Documents/API_test/data/case1.yaml')
    def test_02(self, **kwargs):
        threading.currentThread().name
        #判断运行环境
        DOMAIN = envUtils(kwargs['huanjing'])
        #获取登录token
        zhipin_cookie, zp_token_date = get_token()
        #拼接入参
        testdata = data_splicing(kwargs['public_key'], kwargs['private_key'])
        log.info('测试用例名称是：' + kwargs['casename'])
        log.info('测试接口是：' + DOMAIN + kwargs['url'])
        log.info('测试参数是：' + str(testdata))
        log.info('wt2是：' + str(zhipin_cookie))
        #发出请求
        response_date = requests.request(url=DOMAIN + kwargs['url'], cookies=zhipin_cookie,headers=zp_token_date, params=testdata, method=kwargs['method'])
        response = response_date.json()
        log.info('测试返回结果++++++++' + str(response))
        ##获取期望
        report_date_list, value_list = get_exp_datas(kwargs['qiwang'],response_date)
        for a in range(len(report_date_list)):
            log.info('断言：预期结果：' + str(value_list[a]) + '  实际结果：' + report_date_list[a])
            assert report_date_list[a] == str(value_list[a])
        l_params = dependent_data(kwargs['get_key'], response_date, l_params={})
        log.info('l_params参数是:'+str(l_params))
