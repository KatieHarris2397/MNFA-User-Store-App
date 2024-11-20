# Serve the Angular app using nginx
FROM nginx:alpine

# Copy the build output to the nginx HTML directory
COPY ./dist/mnfa-user-store-app/browser /usr/share/nginx/html

# Copy the nginx configuration template file
COPY default.conf.template /etc/nginx/conf.d/default.conf.template

# Copy in entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose port 80
EXPOSE 80

# Substitute the environment variables in the nginx configuration template and start nginx
CMD ["/entrypoint.sh"]
