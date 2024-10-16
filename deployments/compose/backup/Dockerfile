FROM postgres:15-alpine

# Cron o'rnatish
RUN apt-get update && apt-get install -y cron

# Backup skriptni konteynerga qo'shish
COPY deployments/compose/backup/backup.sh /usr/local/bin/backup.sh
RUN chmod +x /usr/local/bin/backup.sh

# Crontab qo'shish
RUN echo "* * * * * /usr/local/bin/backup.sh" > /etc/cron.d/db-backup
RUN crontab /etc/cron.d/db-backup

# Cron va PostgreSQL serverni birgalikda ishga tushirish
CMD cron && tail -f /dev/null
