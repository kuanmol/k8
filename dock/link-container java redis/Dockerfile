# Build stage
FROM maven:latest as build

WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Run stage
FROM openjdk:latest
WORKDIR /app

# Copy the correct JAR from the build stage
COPY --from=build /app/target/redis-0.0.1-SNAPSHOT.jar /app/your-app.jar

ENTRYPOINT ["java", "-jar", "/app/your-app.jar"]
