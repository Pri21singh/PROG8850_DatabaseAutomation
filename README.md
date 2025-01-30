# PROG8850_DatabaseAutomation
environment with Python and MySQL
# Database Setup and Backup System

## Overview
1. **deploy_changes_scripts.py**: Creates a 'Students' table in MySQL.
2. **backup_scripts.py**: Backs up the database using mysqldump.

## Requirements
- Python 3.x
- `pymysql` library (install via `pip install pymysql`)
- MySQL server and `mysqldump` utility installed.

## Usage
1. **Create Table**:
   bash
   python scripts/deploy_changes_scripts.py
2. **Backup MySQLDump**
   python scripts/creates the backup with current timestamp
