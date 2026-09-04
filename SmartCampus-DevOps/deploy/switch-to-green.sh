#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cp "$ROOT/deploy/nginx/green.conf" "$ROOT/deploy/nginx/active.conf"
docker exec campus-production nginx -s reload
echo "Production now points to GREEN (v2.0)"
