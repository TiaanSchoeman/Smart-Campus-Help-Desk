#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cp "$ROOT/deploy/nginx/blue.conf" "$ROOT/deploy/nginx/active.conf"
docker exec campus-production nginx -s reload
echo "Rolled back. Production now points to BLUE (v1.0)"
