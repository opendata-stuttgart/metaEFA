#!/usr/bin/env bash
set -e

docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d --remove-orphans
docker-compose -f docker-compose.prod.yml restart caddy
docker-compose -f docker-compose.prod.yml run --rm manage collectstatic --noinput
docker-compose -f docker-compose.prod.yml run --rm manage migrate --noinput
