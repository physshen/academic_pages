#!/usr/bin/env bash
# Local preview with the same Hugo version Netlify builds with.
#
# This site uses the December 2020 Wowchemy theme, which only builds on older
# Hugo: 0.128+ removed the `paginate` config key and `site.GoogleAnalytics`,
# and 0.145+ dropped the `_build` front matter key, all of which the theme
# uses. A Homebrew `hugo` is usually far newer, so instead of relying on it,
# this script reads HUGO_VERSION from netlify.toml, downloads that release of
# Hugo extended once (checksum-verified) into ~/.cache/hugo-bin/<version>/,
# and runs it.
#
# Usage: ./view.sh [extra `hugo server` flags]
#   e.g. ./view.sh --port 1314
set -euo pipefail
cd "$(dirname "$0")"

version=$(sed -n 's/^[[:space:]]*HUGO_VERSION[[:space:]]*=[[:space:]]*"\([^"]*\)".*/\1/p' netlify.toml | head -n 1)
if [ -z "$version" ]; then
  echo "view.sh: HUGO_VERSION not found in netlify.toml" >&2
  exit 1
fi

case "$(uname -s)-$(uname -m)" in
  Darwin-*)                   platform="darwin-universal" ;;
  Linux-x86_64)               platform="linux-amd64" ;;
  Linux-aarch64|Linux-arm64)  platform="linux-arm64" ;;
  *)
    echo "view.sh: no Hugo download known for $(uname -s) $(uname -m)" >&2
    exit 1
    ;;
esac

bin_dir="${XDG_CACHE_HOME:-$HOME/.cache}/hugo-bin/$version"
hugo="$bin_dir/hugo"

if [ ! -x "$hugo" ]; then
  file="hugo_extended_${version}_${platform}.tar.gz"
  base="https://github.com/gohugoio/hugo/releases/download/v${version}"
  tmp=$(mktemp -d)
  trap 'rm -rf "$tmp"' EXIT

  echo "Downloading Hugo extended $version ($platform) ..."
  curl -fsSL -o "$tmp/$file" "$base/$file"
  curl -fsSL -o "$tmp/checksums.txt" "$base/hugo_${version}_checksums.txt"

  expected=$(awk -v f="$file" '$2 == f { print $1 }' "$tmp/checksums.txt")
  if command -v shasum >/dev/null 2>&1; then
    actual=$(shasum -a 256 "$tmp/$file" | awk '{ print $1 }')
  else
    actual=$(sha256sum "$tmp/$file" | awk '{ print $1 }')
  fi
  if [ -z "$expected" ] || [ "$expected" != "$actual" ]; then
    echo "view.sh: checksum mismatch for $file, not installing it" >&2
    exit 1
  fi

  mkdir -p "$bin_dir"
  tar -xzf "$tmp/$file" -C "$bin_dir" hugo
  chmod +x "$hugo"
fi

if ! command -v go >/dev/null 2>&1; then
  echo "view.sh: note: Hugo needs Go to download the theme module on first run" \
       "(macOS: brew install go)." >&2
fi

exec "$hugo" server --disableFastRender --printI18nWarnings "$@"
