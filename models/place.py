from models.base_model import BaseModel
from models.city import City
from models.user import User

class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes a Place instance"""
        super().__init__(*args, **kwargs)
        if not 'city_id' in kwargs:
            self.city_id = City.save(City())
        if not 'user_id' in kwargs:
            self.user_id = User.save(User())


