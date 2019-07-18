import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CONF_DIR = os.path.join(BASE_DIR, 'conf')

DATA_DIR = os.path.join(BASE_DIR, 'data')

LOG_DIR = os.path.join(BASE_DIR, 'logs')

REPORT_DIR = os.path.join(BASE_DIR, 'reports')

CASE_DIR = os.path.join(BASE_DIR, 'testcases')

OK_DIR = os.path.join(BASE_DIR, 'ok')

SS_DIR = os.path.join(BASE_DIR, 'ss')

files = 'banji.xls'
files_path = os.path.join(DATA_DIR, files)
print(DATA_DIR)
print(files_path)

print('=============================')
files1 = 'ss\\banji\\banji.xls'
files_path1 = os.path.join(DATA_DIR, files1)
print(DATA_DIR)
print(files_path1)
