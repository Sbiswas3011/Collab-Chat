import psycopg2
import psycopg2.extras

DB_HOST = "localhost"
DB_NAME = "snehangsubiswas"
DB_USER = ""
DB_PASS = ""

def GetAccounts():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    data = {}
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM Chat_Accounts;")
            data = cur.fetchall()
    conn.close()

    return data

def VerifyAccount(username,password):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    data = {}
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM Chat_Accounts WHERE username = %s AND password = %s;",(username,password))
            data = cur.fetchall()
    conn.close()

    if len(data) == 0:
        return False
    else:
        return True

def SetAccount(name,password,email,phno):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO Chat_Accounts (username,password,email,phno) VALUES (%s,%s,%s,%s);",(name,password,email,phno))
    conn.close()

    return True

