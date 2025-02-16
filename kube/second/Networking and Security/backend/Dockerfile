# Use an official Node.js image
FROM node:alpine
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "app.js"]
