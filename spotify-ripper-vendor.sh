#!/bin/sh
# Generate the vendored crates bundle for the version in the SPEC file.
set -e

PKGDIR=$(pwd)
SPEC=spotify-ripper.spec
VERSION=$(rpmspec -q --srpm --qf '%{version}' $SPEC)

TMP=$(mktemp -d)
trap 'rm -fr "$TMP"' EXIT

spectool -g $SPEC
tar -xzf spotify-ripper-$VERSION.tar.gz -C "$TMP"

cd "$TMP/spotify-ripper-$VERSION"
cargo vendor --locked --versioned-dirs ../vendor > /dev/null
cd ..
tar -cJf "$PKGDIR/spotify-ripper-$VERSION-vendor.tar.xz" vendor
