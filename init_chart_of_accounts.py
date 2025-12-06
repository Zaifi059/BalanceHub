#!/usr/bin/env python3
"""
Chart of Accounts Initialization Script
This script creates a comprehensive chart of accounts for new businesses
Run this script after creating a new business to set up proper accounting structure
"""

from app import create_app
from app.models import db, Account, Business
from decimal import Decimal

def init_chart_of_accounts(business_id=None):
    """
    Initialize Chart of Accounts for a business
    If business_id is None, creates accounts for all businesses
    """
    try:
        app = create_app()
        with app.app_context():
            # Get businesses to process
            if business_id:
                businesses = Business.query.filter_by(id=business_id).all()
            else:
                businesses = Business.query.all()
            
            if not businesses:
                print("No businesses found.")
                return False
            
            for business in businesses:
                print(f"Initializing Chart of Accounts for: {business.name}")
                
                # Check if accounts already exist
                existing_count = Account.query.filter_by(business_id=business.id).count()
                if existing_count > 0:
                    print(f"  ⏭️  Business already has {existing_count} accounts. Skipping...")
                    continue
                
                # Define comprehensive chart of accounts
                accounts_data = [
                    # ASSETS (1000-1999)
                    {'code': '1000', 'name': 'ASSETS', 'type': 'asset', 'parent': None, 'level': 1, 'description': 'All business assets'},
                    
                    # Current Assets (1100-1199)
                    {'code': '1100', 'name': 'CURRENT ASSETS', 'type': 'asset', 'parent': '1000', 'level': 2, 'description': 'Assets convertible to cash within one year'},
                    {'code': '1110', 'name': 'Cash & Bank', 'type': 'asset', 'parent': '1100', 'level': 3, 'description': 'Cash in hand and bank accounts', 'balance': '0.00'},
                    {'code': '1120', 'name': 'Accounts Receivable', 'type': 'asset', 'parent': '1100', 'level': 3, 'description': 'Amounts owed by customers', 'balance': '0.00'},
                    {'code': '1130', 'name': 'Inventory', 'type': 'asset', 'parent': '1100', 'level': 3, 'description': 'Stock of goods for sale', 'balance': '0.00'},
                    {'code': '1140', 'name': 'Prepaid Expenses', 'type': 'asset', 'parent': '1100', 'level': 3, 'description': 'Expenses paid in advance', 'balance': '0.00'},
                    {'code': '1150', 'name': 'Other Current Assets', 'type': 'asset', 'parent': '1100', 'level': 3, 'description': 'Other short-term assets', 'balance': '0.00'},
                    
                    # Fixed Assets (1200-1299)
                    {'code': '1200', 'name': 'FIXED ASSETS', 'type': 'asset', 'parent': '1000', 'level': 2, 'description': 'Long-term assets'},
                    {'code': '1210', 'name': 'Equipment', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Business equipment and machinery', 'balance': '0.00'},
                    {'code': '1220', 'name': 'Furniture & Fixtures', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Office furniture and fixtures', 'balance': '0.00'},
                    {'code': '1230', 'name': 'Vehicles', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Business vehicles', 'balance': '0.00'},
                    {'code': '1240', 'name': 'Accumulated Depreciation', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Total depreciation on fixed assets', 'balance': '0.00'},
                    
                    # LIABILITIES (2000-2999)
                    {'code': '2000', 'name': 'LIABILITIES', 'type': 'liability', 'parent': None, 'level': 1, 'description': 'All business liabilities'},
                    
                    # Current Liabilities (2100-2199)
                    {'code': '2100', 'name': 'CURRENT LIABILITIES', 'type': 'liability', 'parent': '2000', 'level': 2, 'description': 'Liabilities due within one year'},
                    {'code': '2110', 'name': 'Accounts Payable', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Amounts owed to suppliers', 'balance': '0.00'},
                    {'code': '2120', 'name': 'Accrued Expenses', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Expenses incurred but not yet paid', 'balance': '0.00'},
                    {'code': '2130', 'name': 'Short-term Loans', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Loans due within one year', 'balance': '0.00'},
                    {'code': '2140', 'name': 'Taxes Payable', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Taxes owed to government', 'balance': '0.00'},
                    {'code': '2150', 'name': 'Other Current Liabilities', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Other short-term liabilities', 'balance': '0.00'},
                    
                    # Long-term Liabilities (2200-2299)
                    {'code': '2200', 'name': 'LONG-TERM LIABILITIES', 'type': 'liability', 'parent': '2000', 'level': 2, 'description': 'Liabilities due after one year'},
                    {'code': '2210', 'name': 'Long-term Loans', 'type': 'liability', 'parent': '2200', 'level': 3, 'description': 'Loans due after one year', 'balance': '0.00'},
                    {'code': '2220', 'name': 'Other Long-term Liabilities', 'type': 'liability', 'parent': '2200', 'level': 3, 'description': 'Other long-term liabilities', 'balance': '0.00'},
                    
                    # EQUITY (3000-3999)
                    {'code': '3000', 'name': 'EQUITY', 'type': 'equity', 'parent': None, 'level': 1, 'description': 'Owner\'s equity in the business'},
                    {'code': '3100', 'name': 'Owner\'s Capital', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Initial investment by owner', 'balance': '0.00'},
                    {'code': '3200', 'name': 'Retained Earnings', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Accumulated profits retained in business', 'balance': '0.00'},
                    {'code': '3300', 'name': 'Owner Drawings', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Amounts withdrawn by owner', 'balance': '0.00'},
                    {'code': '3400', 'name': 'Current Year Profit/Loss', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Current year profit or loss', 'balance': '0.00'},
                    
                    # REVENUE (4000-4999)
                    {'code': '4000', 'name': 'REVENUE', 'type': 'revenue', 'parent': None, 'level': 1, 'description': 'All business income'},
                    {'code': '4100', 'name': 'Sales Revenue', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Revenue from sales of goods', 'balance': '0.00'},
                    {'code': '4200', 'name': 'Service Revenue', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Revenue from services provided', 'balance': '0.00'},
                    {'code': '4300', 'name': 'Other Income', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Miscellaneous income', 'balance': '0.00'},
                    {'code': '4400', 'name': 'Interest Income', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Interest earned on investments', 'balance': '0.00'},
                    
                    # EXPENSES (5000-5999)
                    {'code': '5000', 'name': 'EXPENSES', 'type': 'expense', 'parent': None, 'level': 1, 'description': 'All business expenses'},
                    
                    # Cost of Goods Sold
                    {'code': '5100', 'name': 'Cost of Goods Sold', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Direct costs of goods sold', 'balance': '0.00'},
                    
                    # Operating Expenses (5200-5299)
                    {'code': '5200', 'name': 'OPERATING EXPENSES', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Day-to-day business expenses'},
                    {'code': '5210', 'name': 'Salaries & Wages', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Employee salaries and wages', 'balance': '0.00'},
                    {'code': '5220', 'name': 'Rent Expense', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Office and warehouse rent', 'balance': '0.00'},
                    {'code': '5230', 'name': 'Utilities', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Electricity, water, gas, internet', 'balance': '0.00'},
                    {'code': '5240', 'name': 'Office Supplies', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Office supplies and stationery', 'balance': '0.00'},
                    {'code': '5250', 'name': 'Professional Services', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Legal, accounting, consulting fees', 'balance': '0.00'},
                    {'code': '5260', 'name': 'Marketing & Advertising', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Marketing and advertising expenses', 'balance': '0.00'},
                    {'code': '5270', 'name': 'Travel & Entertainment', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Business travel and entertainment', 'balance': '0.00'},
                    {'code': '5280', 'name': 'Insurance', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Business insurance premiums', 'balance': '0.00'},
                    {'code': '5290', 'name': 'Depreciation Expense', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Depreciation on fixed assets', 'balance': '0.00'},
                    {'code': '5295', 'name': 'Repairs & Maintenance', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Equipment and facility maintenance', 'balance': '0.00'},
                    
                    # Financial Expenses (5400-5499)
                    {'code': '5400', 'name': 'FINANCIAL EXPENSES', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Financial and interest expenses'},
                    {'code': '5410', 'name': 'Interest Expense', 'type': 'expense', 'parent': '5400', 'level': 3, 'description': 'Interest on loans and credit', 'balance': '0.00'},
                    {'code': '5420', 'name': 'Bank Charges', 'type': 'expense', 'parent': '5400', 'level': 3, 'description': 'Bank fees and charges', 'balance': '0.00'},
                    {'code': '5430', 'name': 'Foreign Exchange Loss', 'type': 'expense', 'parent': '5400', 'level': 3, 'description': 'Foreign exchange losses', 'balance': '0.00'},
                    
                    # Other Expenses
                    {'code': '5500', 'name': 'Other Expenses', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Miscellaneous business expenses', 'balance': '0.00'},
                ]
                
                # Create account ID mapping for parent relationships
                account_id_map = {}
                
                # Create accounts in order (parents first)
                for account_data in accounts_data:
                    # Find parent account ID
                    parent_id = None
                    if account_data['parent']:
                        parent_id = account_id_map.get(account_data['parent'])
                        if not parent_id:
                            # Try to find parent in existing accounts
                            parent_account = Account.query.filter_by(
                                business_id=business.id,
                                account_code=account_data['parent']
                            ).first()
                            if parent_account:
                                parent_id = parent_account.id
                                account_id_map[account_data['parent']] = parent_id
                    
                    # Create new account
                    new_account = Account(
                        business_id=business.id,
                        account_code=account_data['code'],
                        account_name=account_data['name'],
                        account_type=account_data['type'],
                        category=account_data['name'],
                        parent_account_id=parent_id,
                        account_level=account_data['level'],
                        created_by=1,  # Assuming user ID 1 exists
                        description=account_data['description'],
                        is_system_account=True  # Mark as system account
                    )
                    
                    # Set balance if specified
                    if 'balance' in account_data:
                        new_account.current_balance = Decimal(account_data['balance'])
                    
                    db.session.add(new_account)
                    db.session.flush()  # Get the ID
                    account_id_map[account_data['code']] = new_account.id
                    
                    print(f"  ✅ Created: {account_data['code']} - {account_data['name']}")
                
                # Commit all changes
                db.session.commit()
                print(f"✅ Chart of Accounts initialized for {business.name}")
            
            print("✅ Chart of Accounts initialization completed!")
            return True
            
    except Exception as e:
        print(f"❌ Error initializing Chart of Accounts: {e}")
        db.session.rollback()
        return False

if __name__ == "__main__":
    print("Initializing Chart of Accounts...")
    success = init_chart_of_accounts()
    if success:
        print("✅ Chart of Accounts initialization completed successfully!")
    else:
        print("❌ Chart of Accounts initialization failed!")
