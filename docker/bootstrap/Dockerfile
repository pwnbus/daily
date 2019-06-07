FROM daily/base

COPY bin/setup /app/bin/setup

CMD ["./wait-for-port.sh", "mysql:3306", "python", "/app/bin/setup"]
