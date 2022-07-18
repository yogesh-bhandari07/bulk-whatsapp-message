from database import Base, engine
from models import Numbers,Message
print('Connecting.....')
Base.metadata.create_all(engine)