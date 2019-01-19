from app import ma
from models import User

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
