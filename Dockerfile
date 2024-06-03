# Use the official Nginx image from Docker Hub
FROM nginx:latest

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/

# Copy your website files to the Nginx document root
COPY html/* /usr/share/nginx/html/

# Copy SSL certificates
COPY ssl/* /etc/nginx/ssl/

# Expose ports 80 and 443
EXPOSE 80
EXPOSE 443

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]