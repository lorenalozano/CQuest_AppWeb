"""Run this script once to update lesson theory content in the existing database.
Usage: docker exec cquest_backend python update_theories.py
"""
import sys
sys.path.insert(0, "/app")

from database import SessionLocal
from services.seed import update_lesson_theories

db = SessionLocal()
try:
    update_lesson_theories(db)
    print("✓ All lesson theories updated successfully.")
finally:
    db.close()
