from sqlalchemy_utils import create_database
class CreateDatabase:
    def __init__(self, database_name):
        self.database_name = f"postgresql://postgres:123@localhost/{database_name}"
        create_database(self.database_name)