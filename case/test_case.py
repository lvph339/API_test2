import json
import unittest
import ddt,re
from utils.getwt import get_token
import requests
from utils.Get_xlsx_data import ddt_data
from utils.Logger import Log

ddt_data_detil = ddt_data()
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

    @ddt.data(*ddt_data_detil)
    @ddt.unpack
    def test_02(self, url, method, testdata, report, casename, listkeys, quanju, phonenumber, env):
        if str(env) == 'qa':
            DOMAIN = 'XXXXXX'
        elif str(env) == '预发':
            DOMAIN = 'XXXXXXXX'
        else:
            DOMAIN = 'XXXXXXXX'
        cookie = get_token(DOMAIN, int(phonenumber))
        if testdata != '':
            testdata = json.loads(testdata)
        if quanju != '':
            quanju = json.loads(quanju)
            for key, value in quanju.items():
                if key != '' and value != '':
                    quanju.update({key: l_params[value]})
            if testdata != '':
                testdata.update(quanju)
            else:
                testdata = quanju
        log.info('测试用例名称是：' + casename)
        log.info('测试接口是：' + DOMAIN + url)
        log.info('测试参数是：' + str(testdata))
        response_date = requests.request(url=DOMAIN + url, cookies=cookie, params=testdata, method=method)
        response = response_date.json()
        log.info('测试返回结果++++++++' + str(response))
        ##取期望
        if report == '':
            log.info('期望填写错误')
        else:
            report = json.loads(report)
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
        if listkeys != '' and re == {}:
            listkeys = list(eval(listkeys))
            for key in listkeys:
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
