#!/bin/bash

sleep 10

# Get the current timestamp (for backup file name)
TIMESTAMP=$(date +"%F_%H-%M-%S")

# Create the backup directory
BACKUP_DIR="/backups/$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# Set PostgreSQL host and port
PGHOST=db
PGPORT=5432

# Take a backup of the PostgreSQL database
PGPASSWORD=$POSTGRES_PASSWORD pg_dump -h $PGHOST -p $PGPORT -U $POSTGRES_USER -d $POSTGRES_DB -F c > "$BACKUP_DIR/my_database.dump"

# Delete backups older than 7 days
find /backups/* -mtime +7 -exec rm -rf {} \;