#!/usr/bin/env python3
"""
Manual Database Clear
Run this script to clear the database
"""

from app import create_app
from app.models import db, Business, User, Account, CashAccount, BankAccount, PaymentMethodPolicy
from app.models import Product, Customer, Supplier, Invoice, InvoiceItem, Purchase, PurchaseItem
from app.models import SalesOrder, SalesOrderItem, Expense, JournalEntry, JournalEntryLine, Batch
from app.models import PaymentMade, PaymentReceived

def main():
    app = create_app()
    with app.app_context():
        print("🗑️  CLEARING DATABASE...")
        print("=" * 50)
        
        try:
            # Clear all data in correct order
            print("Clearing journal entries...")
            JournalEntryLine.query.delete()
            JournalEntry.query.delete()
            
            print("Clearing payments...")
            PaymentMade.query.delete()
            PaymentReceived.query.delete()
            
            print("Clearing invoices...")
            InvoiceItem.query.delete()
            Invoice.query.delete()
            
            print("Clearing sales orders...")
            SalesOrderItem.query.delete()
            SalesOrder.query.delete()
            
            print("Clearing purchases...")
            PurchaseItem.query.delete()
            Purchase.query.delete()
            
            print("Clearing batches...")
            Batch.query.delete()
            
            print("Clearing products...")
            Product.query.delete()
            
            print("Clearing customers and suppliers...")
            Customer.query.delete()
            Supplier.query.delete()
            
            print("Clearing expenses...")
            Expense.query.delete()
            
            print("Clearing bank accounts...")
            BankAccount.query.delete()
            
            print("Clearing payment policies...")
            PaymentMethodPolicy.query.delete()
            
            print("Clearing cash accounts...")
            CashAccount.query.delete()
            
            print("Clearing chart of accounts...")
            Account.query.delete()
            
            print("Clearing users...")
            User.query.delete()
            
            print("Clearing business...")
            Business.query.delete()
            
            # Commit all changes
            db.session.commit()
            
            print("\n✅ DATABASE CLEARED SUCCESSFULLY!")
            print("🗑️  All business data has been removed")
            print("🏗️  Database structure preserved")
            print("🔄 Ready for fresh business setup")
            
        except Exception as e:
            print(f"❌ Error clearing database: {e}")
            db.session.rollback()
            return False
        
        return True

if __name__ == "__main__":
    print("🗑️  Starting Database Clear...")
    print("⚠️  This will remove ALL business data!")
    
    success = main()
    if success:
        print("✅ Database cleared successfully!")
        print("🎉 Ready for new business setup!")
    else:
        print("❌ Database clear failed!")
