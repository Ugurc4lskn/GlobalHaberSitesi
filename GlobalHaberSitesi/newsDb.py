import sqlite3
from sendMsgToTg import send_to_telegram

class DataBase():
    def __init__(self) -> None:
        super().__init__()
        self.createDataBase()
        
    
    def createDataBase(self):
        self.__db = sqlite3.connect("haber.sqlite", check_same_thread=False)
        
        with self.__db:

            self.__cursor =  self.__db.cursor()

            self.__cursor.execute('''CREATE TABLE IF NOT EXISTS newsDb
                (content_id INTEGER PRIMARY KEY,
                    title NOT NULL,
                    content NOT NULL,
                    TrTitle NOT NULL,
                    TrContent NOT NULL,
                    url NOT NULL,
                    domainName NOT NULL,
                    dateTime NOT NULL,
                    imageUrl NOT NULL
                    )'''
                )
            

    def appendData(self, title:str, content: str, TrTitle:str, TrContent:str, url:str, domain_name:str, datatime:str, image_url:str):
        if self.fetchallData(link=url):
            self.__cursor.executemany('INSERT INTO newsDb(title, content, TrTitle, TrContent, url, domainName, dateTime, imageUrl) VALUES (?,?,?,?,?,?,?,?)', [(title, content, TrTitle, TrContent, url, domain_name,datatime,image_url)])
            print(f"{title} Adında Haber Veritabanına kayıt edildi.")
            result = f"📰 Haber Botu 📰\n\n```{TrTitle}```\n\n{TrContent[0:200]} ..."
            send_to_telegram(message=result, image=image_url)
            self.__db.commit()
            
        else:
            print(f"{title} Adında haber veritabanında bulundu...")
            
            
            

    def fetchallData(self, link:str):
        data = self.__cursor.execute("SELECT * From newsDb WHERE url = ?", (str(link),))
        if data.fetchone():
            return False
        else:
            return True


    def getTotalContent(self):
        data = self.__cursor.execute("SELECT * From newsDb").fetchall()
        return data[::-1]

    def fetchTitle(self, title:str):
        __data = self.__cursor.execute("SELECT * From newsDb WHERE TrTitle = ?", (str(title),)).fetchone()
        if __data != 0:
            return __data


    def queryIdNumber(self, Id:int):
        __IdNumber = self.__cursor.execute("SELECT * From newsDb WHERE content_id = ?", (int(Id),)).fetchone()
        if __IdNumber != None:
            return (__IdNumber)
        
        else:
            return False
