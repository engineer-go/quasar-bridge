FROM golang:1.27.3 AS build

WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -trimpath -ldflags="-s -w" -o /out/quasar-bridge ./cmd/quasar-bridge

FROM debian:bookworm-slim

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates curl tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --uid 1000 --user-group --no-create-home quasar

WORKDIR /app
COPY --from=build /out/quasar-bridge /usr/local/bin/quasar-bridge
USER 1000:1000
ENTRYPOINT ["/usr/local/bin/quasar-bridge"]
CMD ["-config", "/app/config.json"]
