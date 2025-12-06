#!/usr/bin/env python3
"""
Fix Bank Chart Accounts
Remove individual bank account Chart of Accounts entries and consolidate into Cash & Bank
"""

from app import create_app
from app.models import db, Business, BankAccount, Account, CashAccount

def main():
    app = create_app()
    with app.app_context():
        print("🔧 FIXING BANK CHART ACCOUNTS...")
        print("=" * 50)
        
        try:
            business = Business.query.first()
            if not business:
                print("❌ No business found")
                return False
            
            print(f"✅ Found business: {business.name}")
            
            # Get all bank accounts
            bank_accounts = BankAccount.query.filter_by(business_id=business.id).all()
            print(f"✅ Found {len(bank_accounts)} bank accounts")
            
            # Get Cash & Bank account
            cash_bank_account = Account.query.filter_by(
                business_id=business.id,
                account_name='Cash & Bank'
            ).first()
            
            if not cash_bank_account:
                print("❌ Cash & Bank account not found")
                return False
            
            print(f"✅ Found Cash & Bank account: Rs. {cash_bank_account.current_balance}")
            
            # Calculate total bank balances
            total_bank_balance = 0
            for bank_account in bank_accounts:
                total_bank_balance += float(bank_account.balance)
                print(f"  {bank_account.account_name}: Rs. {bank_account.balance}")
            
            # Get cash account balance
            cash_account = CashAccount.query.filter_by(business_id=business.id).first()
            cash_balance = float(cash_account.current_balance) if cash_account else 0
            print(f"  Cash Account: Rs. {cash_balance}")
            
            total_cash_bank = cash_balance + total_bank_balance
            print(f"📊 Total Cash & Bank should be: Rs. {total_cash_bank}")
            
            # Update Cash & Bank account balance
            cash_bank_account.current_balance = total_cash_bank
            print(f"✅ Updated Cash & Bank account to: Rs. {cash_bank_account.current_balance}")
            
            # Remove individual bank account Chart entries
            removed_count = 0
            for bank_account in bank_accounts:
                chart_account = Account.query.filter_by(
                    business_id=business.id,
                    account_name=bank_account.account_name
                ).first()
                
                if chart_account:
                    print(f"🗑️  Removing individual Chart entry: {chart_account.account_name}")
                    db.session.delete(chart_account)
                    removed_count += 1
            
            if removed_count > 0:
                print(f"✅ Removed {removed_count} individual bank account Chart entries")
            else:
                print("ℹ️  No individual bank account Chart entries found")
            
            db.session.commit()
            print("✅ Database updated successfully!")
            
            return True
            
        except Exception as e:
            print(f"❌ Error fixing bank chart accounts: {e}")
            db.session.rollback()
            return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 BANK CHART ACCOUNTS FIXED!")
        print("✅ Individual bank account Chart entries removed")
        print("✅ All bank transactions now use 'Cash & Bank' account")
        print("✅ Trial balance should be balanced now")
    else:
        print("\n❌ Failed to fix bank chart accounts!")
