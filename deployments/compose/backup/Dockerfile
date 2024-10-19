FROM postgres:15-alpine

# Install dcron and postgresql-client
RUN apk update && apk upgrade && apk add --no-cache dcron postgresql-client

# Add the backup script to the container
COPY deployments/compose/backup/backup.sh /start-backup
RUN chmod +x /start-backup

# Add crontab
RUN echo "* * * * * /start-backup" > /etc/crontabs/root

# Start cron and PostgreSQL server together
CMD crond -f && tail -f /dev/null