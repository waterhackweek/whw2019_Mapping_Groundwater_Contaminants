from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine(
    'postgresql://tethys_super:zpwt49x3@tethys.byu.edu:5435/waterHackWeek')
# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
print(Base.classes)

# session = Session(engine)

# # rudimentary relationships are produced
# session.add(Address(email_address="foo@bar.com", user=User(name="foo")))
# session.commit()

# # collection-based relationships are by default named
# # "<classname>_collection"
# print (u1.address_collection)
