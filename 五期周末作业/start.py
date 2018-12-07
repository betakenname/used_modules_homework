import os,sys
sys.path.append(os.path.dirname(__file__))


import core
if __name__ == '__main__':
    #功能字典
    funcs = {"1":core.login,"2":core.register}

    while True:
        print("""
        1.登录
        2.注册
        """)
        res =  input("请选择功能(q退出):")
        if res == "q": # 输入q则退出
            print("再见!")
            break
        if res in funcs:
            funcs[res]()
        else:
            print("输入错误 请重试!")





