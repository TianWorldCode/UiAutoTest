import pytest
from utils.load_data_utils import detail_yaml
import config
import allure


@allure.feature('添加用户模块')
@pytest.mark.usefixtures('setup_class')
class TestAddUser:
    @pytest.mark.parametrize('data', detail_yaml(config.TEST_DATA_PATH + 'add_user_data/add_user_data.yaml'))
    def test_add_user_success(self, data, setup_class):
        with allure.step('1、输入用户名：{}, 2、输入密码：{}, 3、重复输入密码：{}, '
                         '4、选择职位：{}, 5、输入名字：{}, 6、输入权限密码：{}'.format(data['username'], data['password'],
                                                                    data['recur_password'], data['position'],
                                                                    data['name'], data['root_password'])):
            setup_class.add_user(data['username'],
                                 data['password'],
                                 data['recur_password'],
                                 data['position'],
                                 data['name'],
                                 data['root_password'])
