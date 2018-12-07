


import json
import hashlib
import re
import logging.config
import logging_conf


# 加载日志配置
logging.config.dictConfig(logging_conf.LOGGING_DIC)
# 获取日志生成器
logger = logging.getLogger("mylog")


def login():
    while True:
        name = input("请输入姓名(输入q退出):")
        # 如果为q就退出
        if name == "q":
            break
        password = input("请输入密码:")

        #得到用户名 去json中查询数据
        with open("users.json","rt",encoding="UTF-8") as f:
            users = json.load(f)
            # 如果用户名不存在与json字典中 则表示用户名不存在
            if name not in users:
                print("用户名不存在")
                #记录错误日志
                logger.error("用户名不存在!")
                break
            # 存在则取出用户信息
            usr = users[name]

            #先将用户输入的密码进行加密
            m = hashlib.md5(password.encode("utf-8"))
            hash_password = m.hexdigest()

            # 判断json中的密码与用户输入的密码是否相同
            if usr["password"] == hash_password:
                print("登录成功!")
                #记录日志
                logger.info("登录成功!")
                return
            else:
                print("密码错误!")
                #记录错误日志
                logger.error("%s 密码错误" % name)

def register():
    while True:
        name = input("请输入姓名(输入q退出):")
        # 如果为q就退出
        if name == "q":
            break
        password = input("请输入密码:")


        #正则验证 用户名长度必须大于三 且必须为数字字母下划线组合,不能以数字或下划线开头
        res = re.match("[a-zA-Z]\w{2,}",name)
        if not res:
            print("用户名长度必须大于三 且必须为数字字母下划线组合,不能以数字开头")
            print("请重新输入!")
            logger.error("用户名不符合规范!")
            continue


        # 得到用户名 去json中查询数据
        with open("users.json", "rt", encoding="UTF-8") as f:
            users = json.load(f)
            # 如果用户名已经存在与json字典中 则表示用户名重复
            if name in users:
                print("用户名已经存在")
                # 记录错误日志
                logger.error("用户名已存在!")
                break

            # 不存在则取出存入新用户的数据到字典中
            #先对对密码进行加密
            m = hashlib.md5(password.encode("utf-8"))
            hash_password = m.hexdigest()

            # 将用户名与加密后的密码存储到字典中
            users[name] = {"name":name,"password":hash_password}

            #将字典序列化到文件中
            with open("users.json", "wt", encoding="UTF-8") as f1:
                json.dump(users,f1)
                print("注册成功")
                #记录日志
                logger.info("%s 注册成功!" % name)
                return



