import sqlite3 as sql 


class DatabaseHandler:
    def __init__(self, dbName = "appData.db"):
        self.dbName = dbName 

    def connect(self):
        return sql.connect(self.dbName)
    
    def createTables(self):
        with self.connect() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS users (
                         userID INTEGER PRIMARY KEY AUTOINCREMENT,
                         username TEXT UNIQUE NOT NULL,
                         password TEXT NOT NULL);""")
            
    def createUser(self, username, password):
        try:
            with self.connect() as conn:
                conn.execute("INSERT INTO users (username, password) VALUES(?,?)", (username, password))
                conn.commit()
            return True
        except: 
            return False
        
    def loginUser(self, username, password):
        try:
            with self.connect() as conn:
                res = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password ))
                user = res.fetchone()
                
                print(user)
            return True
        except: 
            return False 
