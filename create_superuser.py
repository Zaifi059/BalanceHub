#!/usr/bin/env python3
"""
Super User Creation Script for Accounts Management System

This script creates a super user with admin privileges for the accounts management system.
The super user can manage all businesses and has full system access.

Usage:
    python create_superuser.py

Features:
- Creates a super user with admin role
- Optionally creates a default business
- Sets up initial permissions
- Provides secure password generation
- Interactive setup process
"""

import os
import sys
import getpass
import secrets
import string
from datetime import datetime

# Add the app directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models import User, Business, db
from app.extensions import db as db_instance

def generate_secure_password(length=12):
    """Generate a secure random password"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def create_superuser():
    """Create a super user with admin privileges"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("SUPER USER CREATION SCRIPT")
        print("=" * 60)
        print()
        
        # Check if super user already exists
        existing_superuser = User.query.filter_by(role='admin').first()
        if existing_superuser:
            print(f"WARNING: Super user already exists: {existing_superuser.username}")
            response = input("Do you want to create another super user? (y/N): ").lower()
            if response != 'y':
                print("Operation cancelled.")
                return
        
        print("Creating a new super user...")
        print()
        
        # Get user information
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            print("Username already exists!")
            return
        
        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty!")
            return
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            print("Email already exists!")
            return
        
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        
        # Password options
        print("\nPassword options:")
        print("1. Generate secure password automatically")
        print("2. Enter custom password")
        
        password_choice = input("Choose option (1/2): ").strip()
        
        if password_choice == "1":
            password = generate_secure_password()
            print(f"Generated secure password: {password}")
            print("IMPORTANT: Save this password securely!")
        else:
            password = getpass.getpass("Enter password: ")
            if len(password) < 6:
                print("Password must be at least 6 characters long!")
                return
        
        # Business setup option
        print("\nBusiness setup:")
        print("1. Create super user without business (can manage all businesses)")
        print("2. Create super user with a default business")
        
        business_choice = input("Choose option (1/2): ").strip()
        
        business_id = None
        if business_choice == "2":
            business_name = input("Enter business name: ").strip()
            if business_name:
                business = Business(
                    name=business_name,
                    business_type="System Administration",
                    address="System Generated",
                    phone="",
                    email=email,
                    country="Pakistan",
                    currency="PKR",
                    timezone="Asia/Karachi"
                )
                db_instance.session.add(business)
                db_instance.session.flush()  # Get the ID
                business_id = business.id
                print(f"Created business: {business_name}")
        
        try:
            # Create super user
            superuser = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role='admin',
                business_id=business_id,
                is_active=True
            )
            superuser.set_password(password)
            
            db_instance.session.add(superuser)
            db_instance.session.commit()
            
            print("\n" + "=" * 60)
            print("SUPER USER CREATED SUCCESSFULLY!")
            print("=" * 60)
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"Role: Admin")
            if business_id:
                print(f"Business: {business_name}")
            else:
                print("Business: System-wide access (all businesses)")
            
            if password_choice == "1":
                print(f"Password: {password}")
                print("IMPORTANT: Save this password securely!")
            
            print("\nYou can now login to the system with these credentials.")
            print("=" * 60)
            
        except Exception as e:
            print(f"Error creating super user: {str(e)}")
            db_instance.session.rollback()
            return False
        
        return True

def create_business_admin():
    """Create a business admin user for a specific business"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("BUSINESS ADMIN CREATION SCRIPT")
        print("=" * 60)
        print()
        
        # List existing businesses
        businesses = Business.query.all()
        if not businesses:
            print("No businesses found. Please create a business first.")
            return
        
        print("Available businesses:")
        for i, business in enumerate(businesses, 1):
            print(f"{i}. {business.name} ({business.business_type})")
        
        try:
            choice = int(input("\nSelect business (number): ")) - 1
            if choice < 0 or choice >= len(businesses):
                print("Invalid selection!")
                return
            selected_business = businesses[choice]
        except ValueError:
            print("Invalid input!")
            return
        
        print(f"\nSelected business: {selected_business.name}")
        
        # Get user information
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        
        if User.query.filter_by(username=username).first():
            print("Username already exists!")
            return
        
        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty!")
            return
        
        if User.query.filter_by(email=email).first():
            print("Email already exists!")
            return
        
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        
        # Password
        password = getpass.getpass("Enter password: ")
        if len(password) < 6:
            print("❌ Password must be at least 6 characters long!")
            return
        
        try:
            # Create business admin
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
            
            print("\n" + "=" * 60)
            print("BUSINESS ADMIN CREATED SUCCESSFULLY!")
            print("=" * 60)
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"Role: Business Admin")
            print(f"Business: {selected_business.name}")
            print("\nThe user can now login and manage this business.")
            print("=" * 60)
            
        except Exception as e:
            print(f"Error creating business admin: {str(e)}")
            db_instance.session.rollback()
            return False
        
        return True

def main():
    """Main function to run the script"""
    print("Accounts Management System - User Creation Script")
    print()
    print("Choose an option:")
    print("1. Create Super User (System-wide admin)")
    print("2. Create Business Admin (Business-specific admin)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        create_superuser()
    elif choice == "2":
        create_business_admin()
    elif choice == "3":
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")
        return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1)
