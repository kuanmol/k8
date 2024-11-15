# Use the official OpenJDK image with the latest LTS version
FROM openjdk:17-oracle

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file into the container
COPY target/eureka-server-0.0.1-SNAPSHOT.jar eureka-server.jar

# Expose the Eureka server port
EXPOSE 8761

# Run the JAR file
ENTRYPOINT ["java", "-jar", "eureka-server.jar"]
