import unittest
import ddt,re
from utils.getwt import get_token
import requests
from utils.Logger import Log

log=Log()
l_params = {}
@ddt.ddt
class Test_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('接口测试开始了')

    @classmethod
    def tearDownClass(cls):
        log.info('接口测试结束了')

    @ddt.file_data('/Users/lph/Documents/API_test/data/case1.yaml')
    def test_01(self, **kwargs):
        if str(kwargs['huanjing']) == 'qa':
            DOMAIN = 'XXXXX'
        elif str(kwargs['huanjing']) == '预发':
            DOMAIN = 'XXXXXX'
        else:
            DOMAIN = 'XXXXXXX'
        cookie,  = get_token()
        testdata = kwargs['public_key']
        if kwargs['private_key'] is not None:
            quanju = kwargs['private_key']
            for key, value in quanju.items():
                if key is not None and value is not None:
                    quanju.update({key: l_params[value]})
            if testdata is not None:
                testdata.update(quanju)
            else:
                testdata = quanju
        log.info('测试用例名称是：' + kwargs['casename'])
        log.info('测试接口是：' + DOMAIN + kwargs['url'])
        log.info('测试参数是：' + str(testdata))
        response_date = requests.request(url=DOMAIN + kwargs['url'], cookies=cookie, params=testdata, method=kwargs['method'])
        response = response_date.json()
        log.info('测试返回结果++++++++' + str(response))
        ##取期望
        if kwargs['qiwang'] is None:
            log.info('期望填写错误')
        else:
            report = kwargs['qiwang']
            for key, value in report.items():
                report_date = ''
                try:  ##字符串匹配
                    report_dates = re.findall('\"' + key + '\":\"(.*?)\"', response_date.text)
                    report_date = report_dates[0]
                except BaseException as e:
                    print(e)
                if len(report_dates) == 0:
                    try:  ##数字/布尔值匹配
                        report_dates = re.findall('\"' + key + '\":(.*?),', response_date.text)
                        report_date = report_dates[0]
                    except BaseException as e:
                        print(e)
                if len(report_dates) == 0:
                    try:  ##末尾匹配
                        report_dates = re.findall('\"' + key + '\":(.*?)}', response_date.text)
                        report_date = report_dates[0]
                    except BaseException as e:
                        print(e)
                if value is None:
                    value = 'null'
                log.info('断言：预期结果：' + str(value) + '  实际结果：' + report_date)
                self.assertEquals(report_date, str(value))
        ##取返回值
        if kwargs['get_key'] is not None:
            for key in kwargs['get_key']:
                try:
                    param = re.findall('\"' + key + '\":\"(.*?)\"', response_date.text)[0]
                    l_params.update({key:param})
                except BaseException as e:
                    print(e)
                if param != '':
                    try:  ##数字/布尔值匹配
                        param = re.findall('\"' + key + '\":(.*?),', response_date.text)[0]
                    except BaseException as e:
                        print(e)
                if param != '':
                    try:  ##末尾匹配
                        param = re.findall('\"' + key + '\":(.*?)}', response_date.text)[0]
                    except BaseException as e:
                        print(e)
