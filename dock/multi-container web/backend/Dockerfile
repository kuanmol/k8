# Use a Java base image
FROM openjdk:17-jdk-slim

# Install Maven
RUN apt-get update && apt-get install -y maven

# Set the working directory
WORKDIR /app

# Copy the Maven build file
COPY pom.xml .

# Copy the source code
COPY src /app/src

# Build the Spring Boot app
RUN mvn clean package -DskipTests

# Expose the port Spring Boot will run on
EXPOSE 8080

# Run the Spring Boot app
CMD ["java", "-jar", "target/demo-0.0.1-SNAPSHOT.jar"]
