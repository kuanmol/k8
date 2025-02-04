FROM postgres:15

ENV POSTGRES_USER=app_user
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_DB=app_db

COPY init.sql /docker-entrypoint-initdb.d/
