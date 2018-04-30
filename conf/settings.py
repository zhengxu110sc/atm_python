# 配置文件页面.
import os,sys,logging
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)
# 创建数据库路径
data_path={
    "acc":"%s/db/account_table"%Base_dir,
    "shopping_car":"%s/db/shopping_car"%Base_dir,
}
# 设置默认额度
credict_default={'credit': 15000.0}
# 设置日志级别
LOGLEAVE=logging.INFO
