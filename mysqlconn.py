import pymysql
import numpy as np

'''
# 打开数据库连接
#db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     port=3306,
                     db='corpus',
                     charset='utf8')
# 创建游标对象
 cursor = db.cursor()

# 提取数据，执行SQL语句
# cursor.execute('select count(*) from manager')
# m_num = cursor.fetchone()
# m_nums = cursor.fetchall()

# 关闭数据库
db.close()
'''


# 用户信息
class UserInfo(object):
    def __init__(self):
        super().__init__()
        self.user_data_dic = {}

    # 从数据库获取用户信息并为数据添加信息
    def u_data(self):
        # 连接数据库调用user表
        db = pymysql.connect(host='localhost',
                             user='root',
                             passwd='123456',
                             port=3306,
                             db='corpus',
                             charset='utf8')
        cursor = db.cursor()
        cursor.execute('select * from user')
        users_data = cursor.fetchall()
        db.close()

        u_data_list = list(map(list, users_data))  # 元组转列表
        user_data_init = np.array(u_data_list)  # 列表成行显示
        # print(user_data_init)  # 初始数据
        # 添加数据名称
        users_data_dic_list = []
        for i in user_data_init:
            self.user_data_dic = {'User_Id': i[0],
                                  'Manager_Id': i[1],
                                  'u_name': i[2],
                                  'u_password': i[3],
                                  'u_Email': i[4],
                                  'u_phone': i[5],
                                  'u_memo': i[6],
                                }
            users_data_dic_list.append(self.user_data_dic)
        user_data = np.array(users_data_dic_list)
        # print(user_data)  # 添加键后的数据
        return user_data

    def get_uname(self):
        uname_list = []
        user_data = self.u_data()
        for user in user_data:
            user_name = user['u_name']
            uname_list.append(user_name)
        return uname_list

    def get_upwd(self):
        upwd_list = []
        user_data = self.u_data()
        for i in user_data:
            upwd_list.append(i['u_password'])
        return upwd_list

    def get_uid(self):
        uid_ls = []
        user_data = self.u_data()
        for i in user_data:
            uid_ls.append(i['User_Id'])
        return uid_ls


# 管理员信息
class ManagerInfo(object):
    def __init__(self):
        super().__init__()
        self.managers_date_dic = {}

    # 获取管理员信息
    def m_data(self):
        # 连接数据库调用manager表
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             port=3306,
                             db='corpus',
                             charset='utf8')
        cursor = db.cursor()
        cursor.execute('select * from manager')
        managers_date = cursor.fetchall()
        db.close()

        mgr_data_list = []
        for i in managers_date:
            self.managers_data_dic = {'Manager_Id': i[0],
                                      'M_name': i[1],
                                      'M_password': i[2],
                                      'M_Email': i[3],
                                      'M_phone': i[4],
                                      'M_type': i[5],
                                      'M_memo': i[6]}
            mgr_data_list.append(self.managers_data_dic)
        mgr_list = np.array(mgr_data_list)
        return mgr_list

    def get_mname(self):
        m_name_list = []
        m_list = self.m_data()
        for i in m_list:
            m_name_list.append(i['M_name'])
        return m_name_list

    def get_mpwd(self):
        m_pwd_list = []
        m_list = self.m_data()
        for i in m_list:
            m_pwd_list.append(i['M_password'])
        return m_pwd_list

    def get_mtype(self):
        m_type_list = []
        m_list = self.m_data()
        for i in m_list:
            m_type_list.append(i['M_type'])
        return m_type_list


def registered_insert(data):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         port=3306,
                         db='corpus',
                         charset='utf8')
    cursor = db.cursor()
    # sql语句中，用%s做占位符，参数用一个元组
    sql = 'insert into user values(%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, data)
    # 提交
    db.commit()
    db.close()


# 获取数据
# 用户信息
u_list = UserInfo().u_data()
u_name = UserInfo().get_uname()
u_password = UserInfo().get_upwd()
# 管理员信息
m_list = ManagerInfo().m_data()
m_name = ManagerInfo().get_mname()
m_pwd = ManagerInfo().get_mpwd()
m_type = ManagerInfo().get_mtype()


# 输出测试
if __name__ == '__main__':
    print('---------------------------------------------------------------------')
    # 用户信息
    u_list = UserInfo().u_data()
    u_name = UserInfo().get_uname()
    u_password = UserInfo().get_upwd()
    u_id = UserInfo().get_uid()
    print('用户信息')
    print(u_list)
    print(u_name)
    print(u_password)
    print(u_id)
    print('---------------------------------------------------------------------')
    # 管理员信息
    m_list = ManagerInfo().m_data()
    m_name = ManagerInfo().get_mname()
    m_pwd = ManagerInfo().get_mpwd()
    m_type = ManagerInfo().get_mtype()
    print('管理员信息')
    print(m_list)
    print(m_name)
    print(m_pwd)
    print(m_type)
    print('---------------------------------------------------------------------')
