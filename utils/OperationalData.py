from utils.Logger import Log
import re

log = Log()
#所有全局变量全部存储在这里

#请求前字段拼接（把有接口传递的数据进行拼接）
def data_splicing(public_key, private_key, l_params):
    testdata = public_key
    if private_key is not None:
        log.info('有依赖参数需要拼接')
        quanju = private_key
        for key, value in quanju.items():
            if key is not None and value is not None:
                quanju.update({key: l_params[value]})
                log.info('依赖参数更新value')
        if testdata is not None:
            testdata.update(quanju)
            log.info('依赖参数拼接数据作为入参')
        else:
            testdata = quanju
            log.info('入参全部为依赖参数')

    return testdata

def get_exp_datas(qiwang,response_date):
    report_date_list = []
    value_list = []
    if qiwang is None:
        log.info('期望填写错误')
    else:
        report = qiwang
        for key, value in report.items():
            report_date = ''
            try:
                pattern = r'"{}":\s*"([^"]+)"'.format(re.escape(key))
                report_dates = re.findall(pattern, response_date.text)
                report_date = report_dates[0]
            except BaseException as e:
                print(e)
            if value is None:
                value = 'null'
            report_date_list.append(report_date)
            value_list.append(value)
    return report_date_list, value_list

def dependent_data(get_key, response_date, l_params):
    print(type(l_params))
    if get_key is not None:
        for key in get_key:
            try:
                pattern = r'"{}":\s*"([^"]+)"'.format(re.escape(key))
                param = re.findall(pattern, response_date.text)[0]
                l_params[key] = param
            except BaseException as e:
                print(e)
    return l_params
