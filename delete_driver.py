from db import db_session
from models import Drivers

driver = Drivers.query.first()