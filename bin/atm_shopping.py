#程序运行窗口
import os,sys,json
# 创建主程序目录
Base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 导入到配置文件
sys.path.append(Base_dir)

# 导入主程序模块
from core import main

if __name__ == '__main__':
    main.run("atm")