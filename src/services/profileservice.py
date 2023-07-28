

from models.profile import Profile
#from models.database_manager import get_session_factory SessionLocal
from models.database_manager import DatabaseManager


class ProfileServices:
    
    def __init__(self) -> None:
        self.db_manager = DatabaseManager()
        # self.database_manager: DatabaseManager = DatabaseManager.get_instance()
        # pass
    
    def register_user(self, username: str, email: str, phone: int, password: str):
        with self.db_manager.get_session() as db:
            user = db.query(Profile).filter(Profile.email == email).first()
            if user:
                return "email already register"
            else:
                user_phone = db.query(Profile).filter(Profile.phone == phone).first()
                if user_phone:
                    return "phone number already register"
                else:
                    user_data_save = Profile(username=username, email=email,password=password,phone=phone)
                    try:
                        db.add(user_data_save)
                        db.commit()
                        db.refresh(user_data_save)
                        return "register successfully"
                    except:
                        return "register unsuccessfully"
        

    def login_user(self, email: str, password: str):
        with self.db_manager.get_session() as db:
            user = db.query(Profile).filter(Profile.email == email).first()
            pass_check = user.validate_password(password)
            if pass_check == True:
                data = {
                        "id":str(user.profileid),
                        "email":user.email,
                        "name":user.username
                    }
                return data
            else:
                return None
    
    def get_user_data(self, token_data):
        with self.db_manager.get_session() as db:
            user = db.query(Profile).filter(Profile.profileid == token_data['id']).first()
            print(user)
            if user:
                data = {
                        "id":str(user.profileid),
                        "email":user.email,
                        "name":user.username,
                        "phone":user.phone,
                        "height":user.height,
                        "weight":user.weight,
                        "DOB":user.DOB,
                        "sex":user.sex,
                        "photo":user.photo,
                        "points":user.points,
                        "created_at":user.created_at,
                    }
                return data
            else:
                return None
    
    def user_data_update(self, token_data, user_data:str):
        with self.db_manager.get_session() as db:
            user = db.query(Profile).filter(Profile.profileid == token_data['id']).first()
            if user:
                for key, value in user_data.items():
                    setattr(user, key, value)
                db.commit()
                db.refresh(user)
                return "update successful"
            else:
                return None
    
   
   