## 🏢 BALANCEHUB
---

## 🏢 About the Developer

This system is proudly developed by **Digizone Solutions**, a modern technology company focused on building scalable, enterprise-grade software solutions.

### 👨‍💼 Lead Developer  
**Huzaifa Ihsan**  
CEO & Founder — Digizone Solutions  
Architect of the Multi-Business Accounts Management System  
✔ Full-Stack Developer  
✔ System Designer  
✔ Automation Specialist  

🌐 Official Website: https://digizonesolutions.online  
👤 Personal Portfolio: https://huzaifaihsan.me

---

## Features

### 🏢 **Multi-Business Support** ✅
- **Multi-Tenancy**: Support for multiple businesses with complete data isolation
- **Business Switching**: Easy switching between different business contexts
- **Role-Based Access**: Admin, Manager, and User roles with appropriate permissions
- **Business Management**: Create, edit, and manage multiple business profiles
- **Business Setup**: Guided business setup for new users
- **Session Management**: Business context maintained across user sessions

### 🏠 **Dashboard & Overview**
- **Professional Desktop-like Interface**: Modern web application with a professional sidebar similar to QuickBooks
- **Business-Specific Dashboard**: Each business sees only their own data and metrics
- **Real-time Alerts**: Low stock alerts, payment due reminders, and business-specific notifications

### 💰 **Accounts & Finance**
- **General Ledger**: Complete transaction history and account balances
- **Chart of Accounts**: Professional accounting structure with customizable accounts
- **Journal Entries**: Manual journal entry creation and management
- **Bank Reconciliation**: Automated bank statement reconciliation
- **Cash Flow Reports**: Detailed cash flow analysis and forecasting
- **Accounts Payable**: Vendor bill management and payment tracking
- **Accounts Receivable**: Customer invoice and payment management
- **Credit Notes**: Customer credit and refund management
- **Financial Reports**: Balance Sheet, Profit & Loss, Trial Balance

### 🧪 **Inventory & Chemicals**
- **Pesticide Stock Management**: Complete inventory tracking with batch numbers
- **Chemical Usage Logs**: Detailed usage tracking for compliance
- **Warehouse Management**: Multi-location storage unit management
- **Low Stock Alerts**: Automated reorder notifications
- **Purchase Orders**: Supplier order management
- **Batch & Expiry Tracking**: Chemical safety and compliance
- **Safety & Compliance**: MSDS repository and safety reports

### 👥 **Sales & Customers**
- **Customer CRM**: Complete customer database with contact management
- **Quotations & Estimates**: Professional quote generation and tracking
- **Sales Orders**: Order management and fulfillment tracking
- **Invoices**: Professional invoice creation and management
- **Receipts**: Payment receipt management
- **Contracts & Service Agreements**: Long-term contract management
- **Customer Feedback**: Rating and review system
- **Area Management**: Pakistan local and international territory mapping

### 🚚 **Services & Field Operations**
- **Job Scheduling**: Field service appointment management
- **Route Planning**: Optimized technician route optimization
- **Technician Dispatch**: Field staff assignment and tracking
- **Work Orders**: Service job management and tracking
- **Field Reports**: Technician activity and service reports
- **Service History**: Complete customer service history

### 🛡️ **Compliance & Safety**
- **Chemical Usage Reports**: Regulatory compliance reporting
- **Government Reports**: Automated regulatory submission
- **MSDS Repository**: Material Safety Data Sheets management
- **Licensing & Certification**: Permit and license tracking

### 👨‍💼 **Human Resources (HR)**
- **Employee Directory**: Complete staff management
- **Attendance & Timesheets**: Time tracking and management
- **Payroll Management**: Salary calculation and payment processing
- **Roles & Permissions**: User access control and security
- **Performance Reviews**: Employee evaluation and feedback

### 📦 **Procurement & Vendors**
- **Vendor Directory**: Supplier database and management
- **Supplier Contracts**: Contract management and tracking
- **Purchase Requests**: Internal procurement workflow
- **Payment Status**: Vendor payment tracking
- **Area-based Supplier Management**: Local vs. international supplier organization

### 📊 **Reports & Analytics**
- **Financial Reports**: Comprehensive financial analysis
- **Inventory Reports**: Stock analysis and forecasting
- **Sales Reports**: Revenue and customer analysis
- **Service Reports**: Field operation analytics
- **Compliance Reports**: Regulatory compliance analytics

### ⚙️ **Settings & Configuration**
- **Company Profile**: Business information management
- **User Management & Roles**: System access control
- **Tax & GST/VAT Settings**: Pakistan tax compliance
- **Accounting Periods**: Fiscal year management
- **Area Master & Territory Mapping**: Geographic organization
- **Integration Settings**: Third-party system connections
- **Notification Settings**: Alert and communication preferences

### 🆘 **Help & Support**
- **Knowledge Base**: Comprehensive system documentation
- **FAQs**: Common questions and answers
- **Contact Support**: Multiple support channels
- **User Training Guides**: Learning materials and tutorials

- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (can be easily changed to MySQL/PostgreSQL)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Authentication**: Flask-Login with multi-business support
- **Database ORM**: SQLAlchemy with multi-tenancy
- **Multi-Tenancy**: Business-scoped data isolation

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download

```bash
git clone <repository-url>
cd accounts
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
accounts/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── main.py              # Dashboard routes
│   ├── auth.py              # Authentication
│   ├── customers.py         # Customer management
│   ├── suppliers.py         # Supplier management
│   ├── products.py          # Product management
│   ├── invoices.py          # Invoice management
│   ├── purchases.py         # Purchase management
│   ├── expenses.py          # Expense management
│   ├── bank_accounts.py     # Bank account management
│   ├── reports.py           # Report generation
│   ├── accounts.py          # Professional accounting (GL, COA, Journal Entries)
│   ├── inventory.py         # Chemical & inventory management
│   ├── sales.py             # Sales & CRM management
│   ├── services.py          # Field operations & job management
│   ├── compliance.py        # Safety & regulatory compliance
│   ├── hr.py                # Human resources & payroll
│   ├── procurement.py       # Vendor & procurement management
│   ├── settings.py          # System configuration
│   ├── help.py              # Help & support system
│   └── templates/           # HTML templates
│       ├── base.html        # Base template with professional sidebar
│       ├── main/            # Dashboard templates
│       ├── auth/            # Authentication templates
│       ├── customers/       # Customer templates
│       ├── suppliers/       # Supplier templates
│       ├── products/        # Product templates
│       ├── invoices/        # Invoice templates
│       ├── purchases/       # Purchase templates
│       ├── expenses/        # Expense templates
│       ├── bank_accounts/   # Bank account templates
│       ├── reports/         # Report templates
│       ├── accounts/        # Accounting templates
│       ├── inventory/       # Inventory templates
│       ├── sales/           # Sales templates
│       ├── services/        # Services templates
│       ├── compliance/      # Compliance templates
│       ├── hr/              # HR templates
│       ├── procurement/     # Procurement templates
│       ├── settings/        # Settings templates
│       └── help/            # Help templates
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Usage

### First Time Setup

1. Run the application
2. Navigate to `/auth/register` to create your first user account
3. Login with your credentials
4. Start adding customers, suppliers, and products

### Key Features

- **Dashboard**: Overview of business metrics and quick actions
- **Customers**: Manage customer database with contact details
- **Products**: Track inventory levels and pricing
- **Invoices**: Create professional invoices for customers
- **Reports**: Generate financial and business reports

## Customization

### Adding New Modules

1. Create a new blueprint file in the `app/` directory
2. Add routes and business logic
3. Register the blueprint in `app/__init__.py`
4. Create corresponding templates
5. Add navigation items to the sidebar in `base.html`

### Database Changes

1. Modify models in `app/models.py`
2. Delete the existing `accounts.db` file
3. Restart the application to recreate tables

### Styling

The application uses CSS custom properties for easy theming. Modify the `:root` section in `base.html` to change colors and styling.

## Security Features

- User authentication and session management
- Password hashing with Werkzeug
- CSRF protection (built into Flask)
- SQL injection protection via SQLAlchemy ORM

## Production Deployment

For production use:

1. Change `app.config['SECRET_KEY']` to a secure random string
2. Use a production database (MySQL/PostgreSQL)
3. Set `debug=False` in production
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Set up proper HTTPS with SSL certificates
6. Configure environment variables for sensitive data

## Testing Multi-Business Functionality

To test the multi-business functionality, you can run the provided test script:

```bash
python test_multi_business.py
```

This script will:
1. Create test businesses with different configurations
2. Create test users with different roles
3. Test business relationships and data isolation
4. Verify multi-tenancy functionality
5. Clean up test data

## Support

This application is designed specifically for pesticides businesses in Pakistan but can be easily adapted for other business types. The modular architecture makes it simple to add new features or modify existing ones.

## License

This project is open source and available under the MIT License.

