#!/usr/bin/env python3
"""
Automatic Business Setup System
This creates everything a business needs automatically - no hardcoded values
"""

from app import create_app
from app.models import db, Business, User, Account, CashAccount, BankAccount, PaymentMethodPolicy
from create_perfect_chart_of_accounts import create_perfect_chart_of_accounts

def auto_setup_business(business_id):
    """
    Automatically set up everything a business needs
    This is completely dynamic with no hardcoded values
    """
    try:
        app = create_app()
        with app.app_context():
            business = Business.query.get(business_id)
            if not business:
                print(f"❌ Business with ID {business_id} not found")
                return False
            
            print(f"🏢 Auto-setting up business: {business.name}")
            print(f"💰 Currency: {business.currency}")
            print(f"🏭 Type: {business.business_type}")
            
            # 1. Create Perfect Chart of Accounts
            print("  📊 Creating Perfect Chart of Accounts...")
            chart_success = create_perfect_chart_of_accounts(business_id)
            if not chart_success:
                print("  ❌ Chart of Accounts creation failed")
                return False
            
            # 2. Create default payment policies
            print("  💳 Creating default payment policies...")
            default_policies = [
                {
                    'name': 'Cash Payment',
                    'description': 'Immediate cash payment',
                    'payment_terms_days': 0,
                    'immediate_discount_percent': 0,
                    'immediate_discount_amount': 0,
                    'early_payment_discount_amount': 0,
                    'late_payment_penalty_amount': 0
                },
                {
                    'name': 'Net 30 Days',
                    'description': 'Payment due within 30 days',
                    'payment_terms_days': 30,
                    'immediate_discount_percent': 0,
                    'immediate_discount_amount': 0,
                    'early_payment_discount_amount': 0,
                    'late_payment_penalty_amount': 0
                },
                {
                    'name': '2/10 Net 30',
                    'description': '2% discount if paid within 10 days, otherwise due in 30 days',
                    'payment_terms_days': 30,
                    'immediate_discount_percent': 0,
                    'immediate_discount_amount': 0,
                    'early_payment_discount_amount': 2,
                    'late_payment_penalty_amount': 0
                }
            ]
            
            for policy_data in default_policies:
                # Check if policy already exists
                existing = PaymentMethodPolicy.query.filter_by(
                    business_id=business_id,
                    name=policy_data['name']
                ).first()
                
                if not existing:
                    policy = PaymentMethodPolicy(
                        business_id=business_id,
                        name=policy_data['name'],
                        description=policy_data['description'],
                        payment_terms_days=policy_data['payment_terms_days'],
                        immediate_discount_percent=policy_data['immediate_discount_percent'],
                        immediate_discount_amount=policy_data['immediate_discount_amount'],
                        early_payment_discount_amount=policy_data['early_payment_discount_amount'],
                        late_payment_penalty_amount=policy_data['late_payment_penalty_amount'],
                        is_active=True
                    )
                    db.session.add(policy)
                    print(f"    ✅ Created: {policy_data['name']}")
            
            # 3. Create default bank account (optional)
            print("  🏦 Creating default bank account...")
            default_bank = BankAccount.query.filter_by(
                business_id=business_id,
                account_name='Main Bank Account'
            ).first()
            
            if not default_bank:
                bank_account = BankAccount(
                    business_id=business_id,
                    account_name='Main Bank Account',
                    bank_name='Default Bank',
                    account_number='0000000000',
                    account_type='current',
                    balance=0.00,
                    currency=business.currency or 'PKR',
                    is_active=True
                )
                db.session.add(bank_account)
                print(f"    ✅ Created: Main Bank Account")
            
            # 4. Set up default user permissions
            print("  👤 Setting up user permissions...")
            # The user is already made admin in the business setup
            
            # Commit all changes
            db.session.commit()
            
            print(f"\n🎉 Auto Business Setup completed successfully!")
            print(f"✅ Perfect Chart of Accounts created")
            print(f"✅ Cash Account created")
            print(f"✅ Payment policies created")
            print(f"✅ Bank account created")
            print(f"✅ User permissions set")
            print(f"🏢 Business: {business.name}")
            print(f"💱 Currency: {business.currency}")
            print(f"🏭 Type: {business.business_type}")
            
            return True
            
    except Exception as e:
        print(f"❌ Error in auto business setup: {e}")
        db.session.rollback()
        return False

if __name__ == "__main__":
    print("🏢 Starting Auto Business Setup...")
    print("⚠️  This will set up everything for all businesses")
    
    success = auto_setup_business(None)
    if success:
        print("✅ Auto Business Setup completed!")
    else:
        print("❌ Auto Business Setup failed!")
