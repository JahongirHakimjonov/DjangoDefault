FROM nginx:1.21-alpine

# Remove the default NGINX configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom NGINX configuration file
COPY ./compose/nginx/nginx.conf /etc/nginx/conf.d/default.conf