import ddt
from utils.baseapi import Baseapi
import threading
from utils.Logger import Log
from utils.envUtils import envUtils
from utils.OperationalData import OperationalData

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

    @ddt.file_data('/Users/lph/Documents/API_test/casedata/case1.yaml')
    def test_02(self, **kwargs):
        threading.currentThread().name
        log.info('测试用例名称是：' + kwargs['casename'])
        #判断运行环境
        DOMAIN = envUtils(kwargs['huanjing'])
        log.info('测试接口路径是：' + DOMAIN + kwargs['url'])
        #获取登录token
        zhipin_cookie, zp_token_date = Baseapi.get_token()
        log.info('wt2是：' + str(zhipin_cookie))
        #拼接入参
        testdata = OperationalData.data_splicing(kwargs['public_key'], kwargs['private_key'], l_params={})
        log.info('测试参数是：' + str(testdata))
        #发出请求
        response_date = Baseapi.send(url=DOMAIN + kwargs['url'],  method=kwargs['method'], cookies=zhipin_cookie, headers=zp_token_date, data=testdata)
        response = response_date.json()
        log.info('测试返回结果++++++++' + str(response))
        #获取期望
        report_date_list, value_list = OperationalData.get_exp_datas(kwargs['qiwang'], response_date)
        #进行断言
        for a in range(len(report_date_list)):
            log.info('断言：预期结果：' + str(value_list[a]) + '  实际结果：' + report_date_list[a])
            assert report_date_list[a] == str(value_list[a])
        #添加参数依赖字段到l_params
        l_params = OperationalData.dependent_data(kwargs['get_key'], response_date, l_params={})
        log.info('l_params参数是:'+str(l_params))
