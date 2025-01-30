import os
import datetime
from subprocess import call

# Database connection details
db_host = "localhost"
db_user = "root"
db_password = "Software@2025"  # Replace with your MySQL root password
db_name = "my_database"        # Replace with your database name

# Backup directory
backup_dir = "/path/to/backup/folder"  # Replace with your desired backup directory
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Generate a unique filename using the current timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(backup_dir, f"{db_name}_backup_{timestamp}.sql")

# Command to create a backup using mysqldump
backup_command = f"mysqldump -h {db_host} -u {db_user} -p{db_password} {db_name} > {backup_file}"

# Execute the backup command
try:
    call(backup_command, shell=True)
    print(f"Backup successful! File saved as {backup_file}")
except Exception as e:
    print(f"Backup failed: {e}")