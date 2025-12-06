#!/usr/bin/env python3
"""
User Management Script for Accounts Management System

This script provides comprehensive user management functionality including:
- Creating super users
- Creating business admins
- Creating regular users
- Listing users
- Managing user roles
- Activating/deactivating users

Usage:
    python user_management.py
"""

import os
import sys
import getpass
from datetime import datetime

# Add the app directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models import User, Business, db
from app.extensions import db as db_instance

class UserManager:
    def __init__(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.app_context.pop()
    
    def list_users(self):
        """List all users in the system"""
        users = User.query.all()
        
        if not users:
            print("No users found in the system.")
            return
        
        print("\n" + "=" * 80)
        print("SYSTEM USERS")
        print("=" * 80)
        print(f"{'ID':<5} {'Username':<15} {'Email':<25} {'Role':<10} {'Business':<20} {'Status':<10}")
        print("-" * 80)
        
        for user in users:
            business_name = user.business.name if user.business else "System-wide"
            status = "Active" if user.is_active else "Inactive"
            print(f"{user.id:<5} {user.username:<15} {user.email:<25} {user.role:<10} {business_name:<20} {status:<10}")
        
        print("=" * 80)
    
    def list_businesses(self):
        """List all businesses in the system"""
        businesses = Business.query.all()
        
        if not businesses:
            print("No businesses found in the system.")
            return
        
        print("\n" + "=" * 60)
        print("SYSTEM BUSINESSES")
        print("=" * 60)
        print(f"{'ID':<5} {'Name':<25} {'Type':<20} {'Status':<10}")
        print("-" * 60)
        
        for business in businesses:
            status = "Active" if business.is_active else "Inactive"
            print(f"{business.id:<5} {business.name:<25} {business.business_type:<20} {status:<10}")
        
        print("=" * 60)
    
    def create_superuser(self):
        """Create a super user with system-wide access"""
        print("\n" + "=" * 50)
        print("CREATE SUPER USER")
        print("=" * 50)
        
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return False
        
        if User.query.filter_by(username=username).first():
            print("Username already exists!")
            return False
        
        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty!")
            return False
        
        if User.query.filter_by(email=email).first():
            print("Email already exists!")
            return False
        
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        
        password = getpass.getpass("Enter password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long!")
            return False
        
        try:
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
            
            print(f"\nSuper user '{username}' created successfully!")
            print(f"Email: {email}")
            print(f"Role: System Administrator")
            return True
            
        except Exception as e:
            print(f"Error creating super user: {str(e)}")
            db_instance.session.rollback()
            return False
    
    def create_business_admin(self):
        """Create a business admin user"""
        print("\n" + "=" * 50)
        print("CREATE BUSINESS ADMIN")
        print("=" * 50)
        
        # List businesses
        businesses = Business.query.all()
        if not businesses:
            print("No businesses found. Please create a business first.")
            return False
        
        print("Available businesses:")
        for i, business in enumerate(businesses, 1):
            print(f"{i}. {business.name} ({business.business_type})")
        
        try:
            choice = int(input("\nSelect business (number): ")) - 1
            if choice < 0 or choice >= len(businesses):
                print("Invalid selection!")
                return False
            selected_business = businesses[choice]
        except ValueError:
            print("Invalid input!")
            return False
        
        print(f"\nSelected business: {selected_business.name}")
        
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return False
        
        if User.query.filter_by(username=username).first():
            print("Username already exists!")
            return False
        
        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty!")
            return False
        
        if User.query.filter_by(email=email).first():
            print("Email already exists!")
            return False
        
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        
        password = getpass.getpass("Enter password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long!")
            return False
        
        try:
            admin_user = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role='admin',
                business_id=selected_business.id,
                is_active=True
            )
            admin_user.set_password(password)
            
            db_instance.session.add(admin_user)
            db_instance.session.commit()
            
            print(f"\nBusiness admin '{username}' created successfully!")
            print(f"Email: {email}")
            print(f"Business: {selected_business.name}")
            print(f"Role: Business Administrator")
            return True
            
        except Exception as e:
            print(f"Error creating business admin: {str(e)}")
            db_instance.session.rollback()
            return False
    
    def create_regular_user(self):
        """Create a regular user"""
        print("\n" + "=" * 50)
        print("CREATE REGULAR USER")
        print("=" * 50)
        
        # List businesses
        businesses = Business.query.all()
        if not businesses:
            print("No businesses found. Please create a business first.")
            return False
        
        print("Available businesses:")
        for i, business in enumerate(businesses, 1):
            print(f"{i}. {business.name} ({business.business_type})")
        
        try:
            choice = int(input("\nSelect business (number): ")) - 1
            if choice < 0 or choice >= len(businesses):
                print("Invalid selection!")
                return False
            selected_business = businesses[choice]
        except ValueError:
            print("Invalid input!")
            return False
        
        print(f"\nSelected business: {selected_business.name}")
        
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return False
        
        if User.query.filter_by(username=username).first():
            print("Username already exists!")
            return False
        
        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty!")
            return False
        
        if User.query.filter_by(email=email).first():
            print("Email already exists!")
            return False
        
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        
        # Role selection
        print("\nAvailable roles:")
        print("1. user (Regular user)")
        print("2. manager (Manager)")
        print("3. admin (Business admin)")
        
        role_choice = input("Select role (1-3): ").strip()
        role_map = {"1": "user", "2": "manager", "3": "admin"}
        role = role_map.get(role_choice, "user")
        
        password = getpass.getpass("Enter password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long!")
            return False
        
        try:
            user = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role=role,
                business_id=selected_business.id,
                is_active=True
            )
            user.set_password(password)
            
            db_instance.session.add(user)
            db_instance.session.commit()
            
            print(f"\nUser '{username}' created successfully!")
            print(f"Email: {email}")
            print(f"Business: {selected_business.name}")
            print(f"Role: {role.title()}")
            return True
            
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            db_instance.session.rollback()
            return False
    
    def toggle_user_status(self):
        """Activate or deactivate a user"""
        print("\n" + "=" * 50)
        print("TOGGLE USER STATUS")
        print("=" * 50)
        
        users = User.query.all()
        if not users:
            print("No users found.")
            return False
        
        print("Available users:")
        for i, user in enumerate(users, 1):
            status = "Active" if user.is_active else "Inactive"
            print(f"{i}. {user.username} ({user.email}) - {status}")
        
        try:
            choice = int(input("\nSelect user (number): ")) - 1
            if choice < 0 or choice >= len(users):
                print("Invalid selection!")
                return False
            selected_user = users[choice]
        except ValueError:
            print("Invalid input!")
            return False
        
        try:
            selected_user.is_active = not selected_user.is_active
            db_instance.session.commit()
            
            status = "activated" if selected_user.is_active else "deactivated"
            print(f"\nUser '{selected_user.username}' has been {status}!")
            return True
            
        except Exception as e:
            print(f"Error updating user status: {str(e)}")
            db_instance.session.rollback()
            return False
    
    def change_user_password(self):
        """Change a user's password"""
        print("\n" + "=" * 50)
        print("CHANGE USER PASSWORD")
        print("=" * 50)
        
        users = User.query.all()
        if not users:
            print("No users found.")
            return False
        
        print("Available users:")
        for i, user in enumerate(users, 1):
            print(f"{i}. {user.username} ({user.email})")
        
        try:
            choice = int(input("\nSelect user (number): ")) - 1
            if choice < 0 or choice >= len(users):
                print("Invalid selection!")
                return False
            selected_user = users[choice]
        except ValueError:
            print("Invalid input!")
            return False
        
        new_password = getpass.getpass("Enter new password: ")
        if len(new_password) < 6:
            print("Password must be at least 6 characters long!")
            return False
        
        try:
            selected_user.set_password(new_password)
            db_instance.session.commit()
            
            print(f"\nPassword for user '{selected_user.username}' has been changed!")
            return True
            
        except Exception as e:
            print(f"Error changing password: {str(e)}")
            db_instance.session.rollback()
            return False

def main():
    """Main function"""
    print("Accounts Management System - User Management")
    print("=" * 50)
    
    with UserManager() as um:
        while True:
            print("\nChoose an option:")
            print("1. List all users")
            print("2. List all businesses")
            print("3. Create super user")
            print("4. Create business admin")
            print("5. Create regular user")
            print("6. Toggle user status (activate/deactivate)")
            print("7. Change user password")
            print("8. Exit")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                um.list_users()
            elif choice == "2":
                um.list_businesses()
            elif choice == "3":
                um.create_superuser()
            elif choice == "4":
                um.create_business_admin()
            elif choice == "5":
                um.create_regular_user()
            elif choice == "6":
                um.toggle_user_status()
            elif choice == "7":
                um.change_user_password()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1)
