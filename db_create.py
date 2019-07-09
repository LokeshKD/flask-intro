from app import db
from models import BlogPost

# Create the databse and the tables
db.create_all()

# Insert
db.session.add(BlogPost("Good", "I am Good"))
db.session.add(BlogPost("Well", "I am Well"))

# Commit
db.session.commit()
