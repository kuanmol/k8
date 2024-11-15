# Use the latest OpenJDK image
FROM openjdk:17-oracle

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file into the container
COPY target/order-service-0.0.1-SNAPSHOT.jar order-service.jar

# Expose the port for the Order Service
EXPOSE 8080

# Run the JAR file
ENTRYPOINT ["java", "-jar", "order-service.jar"]
