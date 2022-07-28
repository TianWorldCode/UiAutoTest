import time

import pytest
import config
import allure
from utils.load_data_utils import detail_yaml



@pytest.mark.usefixtures('setup_class')
@pytest.mark.usefixtures('refresh_page')
@allure.feature('登录模块')
class TestLogin:

    @pytest.mark.parametrize('data', detail_yaml(config.TEST_DATA_PATH + '/login_data/login_data.yaml'))
    def test_login(self, setup_class, data):
        with allure.step('1、输入用户名：{}, 2、输入密码：{}, 3、点击登录'.format(data['username'], data['password'])):
            setup_class[1].login(data['username'], data['password'])
            setup_class[1].alert_is_present()
            setup_class[1].save_screenshot('登录模块')




        # setup_class[1].enter_add_user()
        # setup_class[2].add_user('test100', 'tian159.', 'tian159.', '测试', '测试100', 'tian159.')
