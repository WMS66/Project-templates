FROM maven:3.9.6-amazoncorretto-21-debian as build

COPY src /app/src
COPY pom.xml /app

WORKDIR /app
RUN mvn clean install

FROM amazoncorretto:21

ENV DB_URL=jdbc:postgresql://URL_AQUI/postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=SUA_SENHA_AQUI
ENV AWS_REGION=us-east-1
ENV AWS_BUCKET_NAME=eventostec-imagens

COPY --from=build /app/target/api-0.0.1-SNAPSHOT.jar /app/app.jar

WORKDIR /app

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]
