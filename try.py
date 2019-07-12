import sqlite3
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# def Gettables(db):
#     try:
#         # conn=sqlite3.connect('test.db')
#         # c=conn.cursor()
#         c.execute("select name from sqlite_master where type='table' order by name")
#         print(c.fetchall())
#     except sqlite3.Error as e:
#         print(e)
def Creatlist(newlistname):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('select table from test')
    res=c.fetchall()
    for line in res:
        if line==newlistname:
            conn.close()
            return False
    c.execute('''create table if not exists {} 
           (State INT PRIMARY KEY     NOT NULL,
           nametodo           TEXT    NOT NULL,
           time               TEXT    NOT NULL,);'''.format(newlistname))
    conn.commit()
    conn.close()
    return True
def delete():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('select table from test')
    res = c.fetchall()
    f=0
    for line in res:
        if line == newlistname:
            f=1
    if f==0:
        conn.close()
        return False
    c.execute("drop table ToDoList")
    #c.execute("DELETE from ToDoList where ID=2;")
    conn.commit()
    conn.close()
    return True
def ListAll():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("SELECT State, nametodo, time  from ToDoList")
    conn.commit()
    conn.close()
    return cursor
def SaveData(listname,ToDoname):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    sql='''insert into listname (State, nametodo, time) values (?,?,?)'''
    para = (ToDoname[0],ToDoname[1],ToDoname[2])
    c.execute(sql,para)
    #c.execute('insert into listname values(%s)'%ToDoname)
    conn.commit()
    conn.close()
def TakeOutData(listname,todoname):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor=c.execute("select State, nametodo, time  from ToDoList where name=todoname")
    conn.commit()
    conn.close()
    return cursor
def ChangeStateDo(listname,todoname):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("UPDATE listname set State = 1 where nametodo=todoname")
    conn.commit()
    conn.close()
def ChangeStateUndo():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("UPDATE listname set State = 0 where nametodo=todoname")
    conn.commit()
    conn.close()
bol=CreatList(newlistname)
bol=Delete(newlistname)
Listall=ListAll()
SaveData(listname,ToDoname)
ToDoname=TakeOutData(listname,todoname)
ChangeStateDo(listname,todoname)
ChangeStateUndo(listname,todoname)