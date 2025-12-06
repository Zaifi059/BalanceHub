# User Management Scripts

This directory contains several scripts for managing users in the Accounts Management System.

## Available Scripts

### 1. `quick_superuser.py` - Quick Super User Creation
**Purpose**: Creates a super user with default credentials for quick setup.

**Usage**:
```bash
python quick_superuser.py
```

**Default Credentials**:
- Username: `digizone`
- Password: `digizone@00001`
- Email: `digizone@example.com`

**Features**:
- Creates a system-wide admin user
- No business association (can manage all businesses)
- Perfect for development and testing
- ⚠️ **Important**: Change the password after first login!

### 2. `create_superuser.py` - Interactive Super User Creation
**Purpose**: Creates a super user with custom credentials and optional business setup.

**Usage**:
```bash
python create_superuser.py
```

**Features**:
- Interactive setup process
- Custom username, email, and password
- Option to create a default business
- Secure password generation option
- System-wide or business-specific admin

### 3. `user_management.py` - Comprehensive User Management
**Purpose**: Full-featured user management system with multiple operations.

**Usage**:
```bash
python user_management.py
```

**Features**:
- List all users and businesses
- Create super users
- Create business admins
- Create regular users
- Toggle user status (activate/deactivate)
- Change user passwords
- Interactive menu system

## User Roles

### Super User (System Admin)
- **Role**: `admin`
- **Access**: System-wide (all businesses)
- **Business ID**: `None`
- **Permissions**: Full system access

### Business Admin
- **Role**: `admin`
- **Access**: Specific business only
- **Business ID**: Assigned business ID
- **Permissions**: Full access to assigned business

### Manager
- **Role**: `manager`
- **Access**: Specific business only
- **Business ID**: Assigned business ID
- **Permissions**: Limited administrative access

### Regular User
- **Role**: `user`
- **Access**: Specific business only
- **Business ID**: Assigned business ID
- **Permissions**: Basic user access

## Quick Start

1. **For Development/Testing**:
   ```bash
   python quick_superuser.py
   ```
   Then login with:
   - Username: `digizone`
   - Password: `digizone@00001`

2. **For Production Setup**:
   ```bash
   python create_superuser.py
   ```
   Follow the interactive prompts to create a secure super user.

3. **For Ongoing User Management**:
   ```bash
   python user_management.py
   ```
   Use the interactive menu to manage users.

## Security Notes

- Always change default passwords after first login
- Use strong passwords (minimum 6 characters)
- Regularly review user access and permissions
- Deactivate unused accounts
- Use the comprehensive user management script for production environments

## Troubleshooting

### Common Issues

1. **"No businesses found"**
   - Create a business first using the web interface
   - Or use the super user to create businesses

2. **"Username already exists"**
   - Choose a different username
   - Or use the user management script to modify existing users

3. **"Email already exists"**
   - Choose a different email address
   - Or use the user management script to modify existing users

### Database Issues

If you encounter database errors:
1. Ensure the Flask app is properly configured
2. Check that the database exists and is accessible
3. Verify all required dependencies are installed

## Accessing the System

After creating users, you can access the system at:
- **URL**: http://localhost:5000
- **Login Page**: http://localhost:5000/auth/login

## Support

For issues or questions:
1. Check the application logs
2. Verify database connectivity
3. Ensure all dependencies are installed
4. Check user permissions and roles
