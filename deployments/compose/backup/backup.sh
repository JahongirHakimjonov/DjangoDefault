#!/bin/bash

# Hozirgi vaqtni olish (backup fayl nomi uchun)
TIMESTAMP=$(date +"%F_%H-%M-%S")

# Backup saqlanadigan katalogni yaratish
BACKUP_DIR="/backups/$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# PostgreSQL'dan backup olish
PGPASSWORD=$POSTGRES_PASSWORD pg_dump -U $POSTGRES_USER -d $POSTGRES_DB -F c > "$BACKUP_DIR/my_database.dump"

# Eski backuplarni 7 kundan keyin o'chirish
find /backups/* -mtime +7 -exec rm -rf {} \;
