"""
Migration script: seeds exercises into the existing database.
Run inside the backend container:
  docker exec cquest_backend python migrate_exercises.py
"""
from database import SessionLocal, engine
from models import Base
from services.seed import seed_exercises

Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    seed_exercises(db)
    print("Migration complete.")
finally:
    db.close()
