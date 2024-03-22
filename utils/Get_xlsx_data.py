import xlrd,os
from utils.Logger import Log

path = os.path.dirname(os.path.dirname(__file__))


def get_xlsx():
    try:
        file = xlrd.open_workbook(path + '/casedata/case1.xlsx')
        rslut = file.sheets()[0]
        nrows = rslut.nrows
        listid = []
        listkey = []#期望从当前接口返回值中获取的字段
        listconeent = []#没有接口依赖的参数
        listurl = []
        listfangshi = []
        listqiwang = []
        listname = []
        listquanju = []#有接口依赖的参数
        listphonenumber = []
        listenv = []
        for i in range(1, nrows):
            listid.append(rslut.cell(i, 0).value)
            listkey.append(rslut.cell(i, 2).value)
            listconeent.append(rslut.cell(i, 3).value)
            listurl.append(rslut.cell(i, 5).value)
            listname.append(rslut.cell(i, 1).value)
            listfangshi.append((rslut.cell(i, 6).value))
            listqiwang.append((rslut.cell(i, 7).value))
            listquanju.append((rslut.cell(i, 4).value))
            listphonenumber.append((rslut.cell(i, 8).value))
            listenv.append((rslut.cell(i, 9).value))
        return listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname , listquanju, listphonenumber, listenv
    except Exception as e:
        print(e)
        Log.info('打开测试用例失败，原因是:%s' % e)
        return


def ddt_data():
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname , listquanju, listphonenumber, listenv = get_xlsx()
    ddt_data_detil = []
    for i in range(len(listid)):
        ddt_data_detil.append((listurl[i], listfangshi[i], listconeent[i], listqiwang[i], listname[i], listkey[i], listquanju[i], listphonenumber[i], listenv[i]))
    return ddt_data_detil
