#!/usr/bin/env python3
"""
Update Admin Credentials Script

This script updates the existing admin user credentials to the new ones specified.
"""

import os
import sys
from datetime import datetime

# Add the app directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models import User, db
from app.extensions import db as db_instance

def update_admin_credentials():
    """Update admin user credentials"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("UPDATE ADMIN CREDENTIALS")
        print("=" * 60)
        print()
        
        # New credentials
        new_username = "digizone"
        new_email = "digizone@example.com"
        new_password = "digizone@00001"
        new_first_name = "Digi"
        new_last_name = "Zone"
        
        try:
            # Find existing admin user
            admin_user = User.query.filter_by(username="admin").first()
            
            if admin_user:
                print(f"Found existing admin user: {admin_user.username}")
                
                # Update credentials
                admin_user.username = new_username
                admin_user.email = new_email
                admin_user.first_name = new_first_name
                admin_user.last_name = new_last_name
                admin_user.set_password(new_password)
                
                db_instance.session.commit()
                
                print("Admin credentials updated successfully!")
                print(f"New Username: {new_username}")
                print(f"New Email: {new_email}")
                print(f"New Password: {new_password}")
                print(f"Name: {new_first_name} {new_last_name}")
                
            else:
                print("No existing admin user found!")
                print("Creating new super user with specified credentials...")
                
                # Create new super user
                superuser = User(
                    username=new_username,
                    email=new_email,
                    first_name=new_first_name,
                    last_name=new_last_name,
                    role='admin',
                    business_id=None,  # System-wide access
                    is_active=True
                )
                superuser.set_password(new_password)
                
                db_instance.session.add(superuser)
                db_instance.session.commit()
                
                print("New super user created successfully!")
                print(f"Username: {new_username}")
                print(f"Email: {new_email}")
                print(f"Password: {new_password}")
                print(f"Name: {new_first_name} {new_last_name}")
            
            print("\n" + "=" * 60)
            print("LOGIN CREDENTIALS")
            print("=" * 60)
            print(f"Username: {new_username}")
            print(f"Password: {new_password}")
            print(f"Email: {new_email}")
            print("\nYou can now login to the system with these credentials!")
            print("=" * 60)
            
            return True
            
        except Exception as e:
            print(f"Error updating admin credentials: {str(e)}")
            db_instance.session.rollback()
            return False

if __name__ == "__main__":
    try:
        update_admin_credentials()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
