import os

__all__ = ['BASE_DIR', 'LOG_PATH', 'REPORT_PATH',
           'TEST_CASE_PATH', 'BASE_URL', 'TEST_DATA_PATH']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# [log]
LOG_PATH = os.path.join(BASE_DIR + '/outputs/log')

# [image]
IMG_PATH = os.path.join(BASE_DIR + '/outputs/image/')

# [report]
REPORT_PATH = os.path.join(BASE_DIR + '/outputs/report/')

# [test_case]
TEST_CASE_PATH = os.path.join(BASE_DIR + '/scripts')

# [base_url]
BASE_URL = 'http://localhost/zentaopms/www/user-login.html'

# [test_data]
TEST_DATA_PATH = os.path.join(BASE_DIR + '/data/')