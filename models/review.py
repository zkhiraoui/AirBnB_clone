from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance"""
        super().__init__(*args, **kwargs)
        if not 'place_id' in kwargs:
            self.place_id = Place.save(Place())
        if not 'user_id' in kwargs:
            self.user_id = User.save(User())

