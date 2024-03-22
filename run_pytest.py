# -*- coding:utf-8 -*-
import os
import pytest
from utils.PublicUtils import send_mail
from utils.PublicUtils import zip_file



if __name__ == '__main__':
    pytest.main(['-s','-v','./workplace/test_case_yaml_pytest.py','-n=4','--clean-alluredir', '--alluredir=./allure/allure-results'])  # -n=x,x代表启动进程数
    os.system('allure generate ./allure/allure-results -o ./allure/allure-report/ --clean')
    zip_file('./allure')
    send_mail('XXXXXXX','./allure.zip')
