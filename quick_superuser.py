#!/usr/bin/env python3
"""
Quick Super User Creation Script

This script creates a super user with default credentials for quick setup.
Use this for development/testing purposes.

Usage:
    python quick_superuser.py
"""

import os
import sys
from datetime import datetime

# Add the app directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models import User, Business, db
from app.extensions import db as db_instance

def create_quick_superuser():
    """Create a super user with default credentials"""
    app = create_app()
    
    with app.app_context():
        print("Creating quick super user...")
        
        # Default credentials
        username = "digizone"
        email = "digizone@example.com"
        password = "digizone@00001"
        first_name = "Digi"
        last_name = "Zone"
        
        # Check if super user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"⚠️  Super user '{username}' already exists!")
            print("You can login with:")
            print(f"Username: {username}")
            print(f"Password: {password}")
            return True
        
        try:
            # Create super user
            superuser = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role='admin',
                business_id=None,  # System-wide access
                is_active=True
            )
            superuser.set_password(password)
            
            db_instance.session.add(superuser)
            db_instance.session.commit()
            
            print("✅ Quick super user created successfully!")
            print("\nLogin credentials:")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"Email: {email}")
            print("\n⚠️  IMPORTANT: Change the password after first login!")
            print("You can access the system at: http://localhost:5000")
            
            return True
            
        except Exception as e:
            print(f"❌ Error creating super user: {str(e)}")
            db_instance.session.rollback()
            return False

if __name__ == "__main__":
    try:
        create_quick_superuser()
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
