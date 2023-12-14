from src.dao import BaseDAO
from users.models import UserModel, RefreshSessionModel
from users.schemas import UserCreateDB, UserUpdateDB, RefreshSessionCreate, RefreshSessionUpdate


class UserDAO(BaseDAO[UserModel, UserCreateDB, UserUpdateDB]):
    model = UserModel


class RefreshSessionDAO(BaseDAO[RefreshSessionModel, RefreshSessionCreate, RefreshSessionUpdate]):
    model = RefreshSessionModel
