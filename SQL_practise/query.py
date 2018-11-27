
import os
import sqlite3


DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'college.db')
sqlite3.connect(DATABASE_PATH)
def connect_db():
    return sqlite3.connect(DATABASE_PATH)



def create_tablesTeachers():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS teachers(
            subject VARCHAR(32),
            name VARCHAR(32),
            section VARCHAR(32)
            )''')

    conn.commit()
    conn.close()



def initializeTeachers():
    conn = connect_db()
    cur = conn.cursor()


    val = [
        ("Computer Graphics" , "Prof Soubhgya","C1"),
        ("Java" , "Prof Karthikeyan" ,"C1"),
        ("Statistics " , "Prof Santanu mandal","C1"),
        ("Data Anylatics", "Prof Hari Kishan" ,"C1"),
        ("ECE" , "Prof Umakanth Nanda" ,"C1"),
        ("Computer Graphics" , "Prof Sibbi" , "C2"),
        ("Java" , "Prof Karthikeyan" , "C2"),
        ("Statistics" , "Prof Sudhakar" , "C2"),
        ("Data Anylatics" , "Prof Vijaya" , "C2"),
        ("ECE", "Prof Umakanth Nanda ", "C2")
    ]

    cur.executemany("""
                    INSERT INTO teachers ('subject' , 'name' , 'section' )
                    VALUES (?, ? , ?)""", val)

    conn.commit()


def fetchContent(query):
    conn = connect_db()
    cur = conn.cursor()
    result = cur.execute(query)
    result = result.fetchall()
    conn.commit()
    return result


def writeContent(query):
    conn= connect_db()
    cur = conn.cursor()
    result = cur.execute(query)
    conn.commit()
    return ("Sucessfuly Added the item")


def deleteContent(query):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(query)
    conn.commit()
    return ("Sucessfuly deleted!")

def updateContent(query):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return ("Sucessfuly Updated !")
