#!/usr/bin/env bash
set -euo pipefail

REPO="moon-rize-official/open-agent-os"
WIKI_URL="git@github.com:${REPO}.wiki.git"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Publishing wiki source from $ROOT/wiki"
git clone "$WIKI_URL" "$TMP/wiki"

find "$TMP/wiki" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -R "$ROOT/wiki/." "$TMP/wiki/"

cd "$TMP/wiki"
git add .
if git diff --cached --quiet; then
  echo "Wiki already up to date."
  exit 0
fi

git commit -m "docs: sync Open Agent OS wiki"
git push origin master 2>/dev/null || git push origin main

echo "Wiki published."
