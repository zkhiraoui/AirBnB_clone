from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a City instance"""
        super().__init__(*args, **kwargs)
        if not 'state_id' in kwargs:
            self.state_id = State.save(State())
