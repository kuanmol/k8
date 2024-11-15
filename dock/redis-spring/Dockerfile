# Use the latest OpenJDK image
FROM openjdk:latest

# Set working directory
WORKDIR /app

# Copy the JAR file from the target directory to the container
COPY target/redis-0.0.1-SNAPSHOT.jar app.jar

# Expose the application port
EXPOSE 8080

# Run the Spring Boot application
ENTRYPOINT ["java", "-jar", "app.jar"]
