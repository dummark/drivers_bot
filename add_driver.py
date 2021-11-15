from db import db_session
from models import Drivers

driver = Drivers(name=,pass_number=,pass_series=,place_issue=,date_issue=,date_arrive=)
db_session.add(driver)
db_session.commit()