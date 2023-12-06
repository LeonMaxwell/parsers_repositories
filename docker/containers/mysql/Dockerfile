FROM mysql:5.7

ADD my.cnf /etc/mysql/conf.d/my.cnf

CMD ["mysqld", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_general_ci", "--skip-character-set-client-handshake"]
EXPOSE 3306