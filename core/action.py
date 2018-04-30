#操作页面。
import os,sys
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)

from conf import settings #导入配置页面
# 创建用户验证装饰器
def login_requird(func):
    def