# Base image with Java 17
FROM openjdk:17-jdk-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Spring Boot JAR file into the container
COPY target/health-0.0.1-SNAPSHOT.jar app.jar

# Expose the application port
EXPOSE 8080

# Default command to run the Spring Boot application
CMD ["java", "-jar", "app.jar"]
