# Use openjdk image as the base image
FROM openjdk:17-jdk-slim

# Set the working directory inside the container
WORKDIR /usr/app

# Copy the JAR file from your local machine to the container
COPY target/proxy-0.0.1-SNAPSHOT.jar /usr/app/proxy-0.0.1-SNAPSHOT.jar

# Expose port 8080 (default Spring Boot port)
EXPOSE 8080

# Run the Spring Boot application
ENTRYPOINT ["java", "-jar", "/usr/app/proxy-0.0.1-SNAPSHOT.jar"]
