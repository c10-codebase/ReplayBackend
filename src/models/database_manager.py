from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config.config import settings
from models import Base
from sqlalchemy.orm import Session


class DatabaseManager:
    __instance = None
    def __init__(self) -> None:
        if DatabaseManager.__instance is not None:
            raise Exception("this class is singleton!")
        else:
            DatabaseManager.__instance = self
            
        self.db_user = "postgres"
        self.db_pass = "adhi1998"
        self.db_host = "127.0.0.1"
        self.db_port = 5432
        self.database = "replayback"
        
        self.engine = self.__get_engine()
        
        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine)
        
    @staticmethod
    def get_instance():
        if DatabaseManager.__instance is None:
            DatabaseManager()
        return DatabaseManager.__instance
        
    def __get_db_string(self):
        db_string = f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.database}"
        return db_string
        
    def __get_engine(self):
        connection_string = self.__get_db_string()
        engine = create_engine(connection_string,echo=False)
        return engine 
    
    def get_session(self) -> scoped_session:
        session = scoped_session(self.session_factory)
        return session()
    
    def save_entity(self,session,entity):
        session.add(entity)
        self.safe_commit(session)
        return entity
    
    
    def save_all_entities(self,session, entity_list):
        session.add_all(entity_list)
        return self.safe_commit(session)
    
    def safe_commit(self, session):
        try:
            session.commit()
        except Exception:
            session.rollback()
            session.flush()
            raise
        
    def get_session_factory(self):
        return self.session_factory
    
   