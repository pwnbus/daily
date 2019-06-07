FROM daily/base

USER root

# Install curl for docker health check
RUN \
  apt-get update && \
  apt-get install -y curl && \
  rm -rf /var/lib/apt/lists/*

USER daily

COPY bin/web /app/bin/web

CMD ["./wait-for-container.sh", "bootstrap", "/app/bin/web"]

EXPOSE 5000
