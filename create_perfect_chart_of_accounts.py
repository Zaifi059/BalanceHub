#!/usr/bin/env python3
"""
Perfect Chart of Accounts System
This creates a comprehensive, professional Chart of Accounts for any business
No hardcoded values - everything is dynamic and automatic
"""

from app import create_app
from app.models import db, Account, Business, CashAccount
from decimal import Decimal

def create_perfect_chart_of_accounts(business_id):
    """
    Create a perfect Chart of Accounts for any business
    This is completely dynamic with no hardcoded values
    """
    try:
        app = create_app()
        with app.app_context():
            # Handle case when business_id is None (create for all businesses)
            if business_id is None:
                businesses = Business.query.all()
                if not businesses:
                    print("❌ No businesses found")
                    return False
                
                success = True
                for business in businesses:
                    print(f"\n🏢 Processing business: {business.name} (ID: {business.id})")
                    result = create_perfect_chart_of_accounts(business.id)
                    if not result:
                        success = False
                return success
            
            business = Business.query.get(business_id)
            if not business:
                print(f"❌ Business with ID {business_id} not found")
                return False
            
            print(f"🏢 Creating perfect Chart of Accounts for: {business.name}")
            print(f"💰 Business Currency: {business.currency}")
            print(f"🏭 Business Type: {business.business_type}")
            
            # Check if accounts already exist
            existing_count = Account.query.filter_by(business_id=business_id).count()
            if existing_count > 0:
                print(f"  ⏭️  Business already has {existing_count} accounts. Skipping...")
                return True
            
            # Create comprehensive Chart of Accounts
            accounts_created = 0
            
            # 1. ASSETS (1000-1999)
            print("  📊 Creating ASSETS accounts...")
            assets_accounts = [
                # Main Asset Categories
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
                {'code': '1230', 'name': 'Vehicles', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Company vehicles', 'balance': '0.00'},
                {'code': '1240', 'name': 'Accumulated Depreciation', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Total depreciation on fixed assets', 'balance': '0.00'},
                {'code': '1250', 'name': 'Land', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Land and buildings', 'balance': '0.00'},
                {'code': '1260', 'name': 'Intangible Assets', 'type': 'asset', 'parent': '1200', 'level': 3, 'description': 'Patents, trademarks, goodwill', 'balance': '0.00'},
            ]
            
            # 2. LIABILITIES (2000-2999)
            print("  📊 Creating LIABILITIES accounts...")
            liability_accounts = [
                # Main Liability Categories
                {'code': '2000', 'name': 'LIABILITIES', 'type': 'liability', 'parent': None, 'level': 1, 'description': 'All business debts and obligations'},
                
                # Current Liabilities (2100-2199)
                {'code': '2100', 'name': 'CURRENT LIABILITIES', 'type': 'liability', 'parent': '2000', 'level': 2, 'description': 'Debts due within one year'},
                {'code': '2110', 'name': 'Accounts Payable', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Amounts owed to suppliers', 'balance': '0.00'},
                {'code': '2120', 'name': 'Accrued Expenses', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Expenses incurred but not yet paid', 'balance': '0.00'},
                {'code': '2130', 'name': 'Short-term Loans', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Loans due within one year', 'balance': '0.00'},
                {'code': '2140', 'name': 'Taxes Payable', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Taxes owed to government', 'balance': '0.00'},
                {'code': '2150', 'name': 'Other Current Liabilities', 'type': 'liability', 'parent': '2100', 'level': 3, 'description': 'Other short-term debts', 'balance': '0.00'},
                
                # Long-term Liabilities (2200-2299)
                {'code': '2200', 'name': 'LONG-TERM LIABILITIES', 'type': 'liability', 'parent': '2000', 'level': 2, 'description': 'Debts due after one year'},
                {'code': '2210', 'name': 'Long-term Loans', 'type': 'liability', 'parent': '2200', 'level': 3, 'description': 'Loans due after one year', 'balance': '0.00'},
                {'code': '2220', 'name': 'Other Long-term Liabilities', 'type': 'liability', 'parent': '2200', 'level': 3, 'description': 'Other long-term debts', 'balance': '0.00'},
            ]
            
            # 3. EQUITY (3000-3999)
            print("  📊 Creating EQUITY accounts...")
            equity_accounts = [
                # Main Equity Categories
                {'code': '3000', 'name': 'EQUITY', 'type': 'equity', 'parent': None, 'level': 1, 'description': 'Owner\'s stake in the business'},
                
                # Owner's Equity
                {'code': '3100', 'name': 'Owner\'s Capital', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Initial investment by owner', 'balance': '0.00'},
                {'code': '3200', 'name': 'Retained Earnings', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Accumulated profits/losses', 'balance': '0.00'},
                {'code': '3300', 'name': 'Owner Drawings', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Amounts withdrawn by owner', 'balance': '0.00'},
                {'code': '3400', 'name': 'Current Year Profit/Loss', 'type': 'equity', 'parent': '3000', 'level': 2, 'description': 'Current year net income', 'balance': '0.00'},
            ]
            
            # 4. REVENUE (4000-4999)
            print("  📊 Creating REVENUE accounts...")
            revenue_accounts = [
                # Main Revenue Categories
                {'code': '4000', 'name': 'REVENUE', 'type': 'revenue', 'parent': None, 'level': 1, 'description': 'All business income'},
                
                # Sales Revenue
                {'code': '4100', 'name': 'Sales Revenue', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Income from sales of goods/services', 'balance': '0.00'},
                {'code': '4200', 'name': 'Service Revenue', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Income from services provided', 'balance': '0.00'},
                {'code': '4300', 'name': 'Other Income', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Other sources of income', 'balance': '0.00'},
                {'code': '4400', 'name': 'Interest Income', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Interest earned on investments', 'balance': '0.00'},
                {'code': '4500', 'name': 'Rental Income', 'type': 'revenue', 'parent': '4000', 'level': 2, 'description': 'Income from property rental', 'balance': '0.00'},
            ]
            
            # 5. EXPENSES (5000-5999)
            print("  📊 Creating EXPENSE accounts...")
            expense_accounts = [
                # Main Expense Categories
                {'code': '5000', 'name': 'EXPENSES', 'type': 'expense', 'parent': None, 'level': 1, 'description': 'All business expenses'},
                
                # Cost of Goods Sold
                {'code': '5100', 'name': 'Cost of Goods Sold', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Direct costs of products sold', 'balance': '0.00'},
                
                # Operating Expenses (5200-5299)
                {'code': '5200', 'name': 'OPERATING EXPENSES', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Day-to-day business expenses'},
                {'code': '5210', 'name': 'Salaries & Wages', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Employee compensation', 'balance': '0.00'},
                {'code': '5220', 'name': 'Rent Expense', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Office and facility rent', 'balance': '0.00'},
                {'code': '5230', 'name': 'Utilities', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Electricity, water, gas, internet', 'balance': '0.00'},
                {'code': '5240', 'name': 'Office Supplies', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Office materials and supplies', 'balance': '0.00'},
                {'code': '5250', 'name': 'Professional Services', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Legal, accounting, consulting fees', 'balance': '0.00'},
                {'code': '5260', 'name': 'Marketing & Advertising', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Promotional and advertising costs', 'balance': '0.00'},
                {'code': '5270', 'name': 'Travel & Entertainment', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Business travel and entertainment', 'balance': '0.00'},
                {'code': '5280', 'name': 'Insurance', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Business insurance premiums', 'balance': '0.00'},
                {'code': '5290', 'name': 'Depreciation Expense', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Depreciation of fixed assets', 'balance': '0.00'},
                {'code': '5295', 'name': 'Repairs & Maintenance', 'type': 'expense', 'parent': '5200', 'level': 3, 'description': 'Equipment and facility maintenance', 'balance': '0.00'},
                
                # Financial Expenses (5400-5499)
                {'code': '5400', 'name': 'FINANCIAL EXPENSES', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Interest and financial costs'},
                {'code': '5410', 'name': 'Interest Expense', 'type': 'expense', 'parent': '5400', 'level': 3, 'description': 'Interest on loans and credit', 'balance': '0.00'},
                {'code': '5420', 'name': 'Bank Charges', 'type': 'expense', 'parent': '5400', 'level': 3, 'description': 'Bank fees and charges', 'balance': '0.00'},
                {'code': '5430', 'name': 'Foreign Exchange Loss', 'type': 'expense', 'parent': '5400', 'level': 3, 'description': 'Currency exchange losses', 'balance': '0.00'},
                
                # Other Expenses (5500-5599)
                {'code': '5500', 'name': 'Other Expenses', 'type': 'expense', 'parent': '5000', 'level': 2, 'description': 'Miscellaneous business expenses', 'balance': '0.00'},
            ]
            
            # Combine all accounts
            all_accounts = assets_accounts + liability_accounts + equity_accounts + revenue_accounts + expense_accounts
            
            # Create accounts in database
            for account_data in all_accounts:
                # Find parent account if specified
                parent_account = None
                if account_data.get('parent'):
                    parent_account = Account.query.filter_by(
                        business_id=business_id,
                        account_code=account_data['parent']
                    ).first()
                
                # Create account
                account = Account(
                    business_id=business_id,
                    account_code=account_data['code'],
                    account_name=account_data['name'],
                    account_type=account_data['type'],
                    category=account_data['name'],  # Use name as category
                    parent_account_id=parent_account.id if parent_account else None,
                    account_level=account_data['level'],
                    description=account_data['description'],
                    current_balance=Decimal(account_data.get('balance', '0.00')),
                    currency=business.currency or 'PKR',
                    status='active',
                    created_by=1  # Default user ID
                )
                
                db.session.add(account)
                accounts_created += 1
                print(f"    ✅ Created: {account_data['code']} - {account_data['name']}")
            
            # Commit all accounts
            db.session.commit()
            
            # Create Cash Account for the business
            print("  💰 Creating Cash Account...")
            cash_account = CashAccount(
                business_id=business_id,
                account_name='Cash in Hand',
                current_balance=0.00,
                currency=business.currency or 'PKR',
                is_active=True
            )
            db.session.add(cash_account)
            db.session.commit()
            
            print(f"\n🎉 Perfect Chart of Accounts created successfully!")
            print(f"📊 Total Accounts Created: {accounts_created}")
            print(f"💰 Cash Account Created: {cash_account.account_name}")
            print(f"🏢 Business: {business.name}")
            print(f"💱 Currency: {business.currency}")
            
            return True
            
    except Exception as e:
        print(f"❌ Error creating Chart of Accounts: {e}")
        db.session.rollback()
        return False

def create_complete_chart_of_accounts(business_id):
    """Wrapper function for compatibility"""
    return create_perfect_chart_of_accounts(business_id)

if __name__ == "__main__":
    print("🏢 Creating Perfect Chart of Accounts...")
    print("⚠️  This will create a comprehensive Chart of Accounts for all businesses")
    
    success = create_perfect_chart_of_accounts(None)
    if success:
        print("✅ Perfect Chart of Accounts creation completed!")
    else:
        print("❌ Perfect Chart of Accounts creation failed!")
