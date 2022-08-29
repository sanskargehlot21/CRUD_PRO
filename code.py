import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='',
                                     database='pythontest')
        query = 'create table if not exists py(userId int(5) ,userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    #Insert
    def insert_user(self, userid, username, phone):
        query = "insert into py(userId,userName,phone) values({},'{}','{}')".format(
            userid, username, phone)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("USER SAVED TO DATABASE")

        # Fech All
    def fetch_all(self):
            query = "select * from py"
            cur = self.con.cursor()
            cur.execute(query)
            for row in cur:
                print("User Id : ", row[0])
                print("User Name :", row[1])
                print("User Phone : ", row[2])
                print()
                print()
    def delete_user(self,userId):
        query="delete from py where userId={}".format(userId)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("!!DELETED SUCCESSFULLY!!")
    def update_user(self,userId,Newname,Newphone):
        query= "update py set userName='{}',phone='{}' where userId={}".format(Newname,Newphone,userId)
        cur1= self.con.cursor()
        cur1.execute(query)
        self.con.commit()
        print("!!UPDATED SUCCESSDULLY!!")