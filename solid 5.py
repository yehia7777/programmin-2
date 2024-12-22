from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving '{data}' to MySQL database.")


class MongoDBDatabase(Database):
    def save(self, data):
        print(f"Saving '{data}' to MongoDB database.")


class DataManager:
    def __init__(self, database: Database):
        self.database = database

    def save_data(self, data):
        self.database.save(data)


# استخدام الكلاسات
mysql_db = MySQLDatabase()
mongo_db = MongoDBDatabase()

data_manager = DataManager(mysql_db)
data_manager.save_data("User Data")

data_manager = DataManager(mongo_db)
data_manager.save_data("User Data")
