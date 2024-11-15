# Use the latest OpenJDK image
FROM openjdk:17-oracle

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file into the container
COPY target/user-service-0.0.1-SNAPSHOT.jar user-service.jar


# Expose the port for the User Service
EXPOSE 8080

# Run the JAR file
ENTRYPOINT ["java", "-jar", "user-service.jar"]
