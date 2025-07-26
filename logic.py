import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database # имя базы данных
        
    def create_tables(self):
        con = sqlite3.connect("portfolio.db") # соединение с базой данных, если бд нет, то файл создастся
        with con:
            cur = con.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS Projects (
                user_id INTEGER PRIMARY KEY,
                project_name VARCHAR,
                description TEXT,
                url TEXT,
                status TEXT,
                FOREIGN KEY (project_name) REFERENCES Status(project_name)
            )""")

            cur.execute("""CREATE TABLE IF NOT EXISTS Status (
                project_name VARCHAR PRIMARY KEY,
                status_name TEXT
            )""")

            cur.execute("""CREATE TABLE IF NOT EXISTS Project_skills ( 
                project_name VARCHAR, 
                skill_name VARCHAR, 
                FOREIGN KEY (project_name) REFERENCES Projects(project_name), 
                FOREIGN KEY (skill_name) REFERENCES Skills(skill_name), 
                PRIMARY KEY (project_name, skill_name) 
            )""")

            cur.execute("""CREATE TABLE IF NOT EXISTS Skills(
                skills_name VARCHAR)""")
            con.commit()

            
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()