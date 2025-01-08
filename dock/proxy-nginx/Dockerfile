FROM openjdk:17-jdk-slim

WORKDIR /usr/app

COPY target/proxy-0.0.1-SNAPSHOT.jar /usr/app/proxy-0.0.1-SNAPSHOT.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/usr/app/proxy-0.0.1-SNAPSHOT.jar"]
