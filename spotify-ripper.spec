%bcond check 1

# librespot is pinned to a git snapshot in Cargo.toml
%global librespot_commit e023adbbf017ae1fc10d01531dbe50c409786f2d

# cargo install ignores Cargo.lock otherwise, and git sources can't be resolved against vendored sources
%global __cargo_common_opts %{__cargo_common_opts} --locked

Name:           spotify-ripper
Version:        4.1.1
Release:        1%{?dist}
Summary:        Command-line ripper for Spotify
License:        MIT AND Apache-2.0 AND BSD-3-Clause AND Unicode-3.0 AND Zlib AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (LGPL-3.0-or-later OR MPL-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR BSD-3-Clause) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
# Detailed breakdown, from %%cargo_license_summary; LICENSE.dependencies in the
# package contains the full per-crate listing:
# (MIT OR Apache-2.0) AND Unicode-3.0
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# LGPL-3.0-or-later OR MPL-2.0
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR LGPL-2.1-or-later
# MIT OR BSD-3-Clause
# MIT OR Zlib OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/scaronni/%{name}

Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Generated with spotify-ripper-vendor.sh
Source1:        %{name}-%{version}-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  pkgconfig(openssl)

Requires:       /usr/bin/ffmpeg
Requires:       lame
Recommends:     fdkaac
Recommends:     flac
Recommends:     opus-tools
Recommends:     sox

%description
A Spotify ripper that uses librespot in the backend. Requires a Premium account
for usage. Ripping music from Spotify violates Terms and Conditions of Use:
https://www.spotify.com/legal

%prep
%autosetup -p1 -a1
%cargo_prep -v vendor
cat >> .cargo/config.toml << EOF
[source."git+https://github.com/librespot-org/librespot?rev=%{librespot_commit}"]
git = "https://github.com/librespot-org/librespot"
rev = "%{librespot_commit}"
replace-with = "vendored-sources"
EOF

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Oct 09 2026 Simone Caronni <negativo17@gmail.com> - 4.1.1-1
- Update to 4.1.1.

* Thu Oct 08 2026 Simone Caronni <negativo17@gmail.com> - 4.1.0-1
- Update to 4.1.0.

* Thu Oct 08 2026 Simone Caronni <negativo17@gmail.com> - 4.0.0-1
- Update to 4.0.0, rewritten in Rust.

* Wed Jun 10 2026 Simone Caronni <negativo17@gmail.com> - 3.2.0-1
- Update to 3.2.0.

* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 3.0.3-1
- Update to rewritten 3.0.3 using librespot-python!

* Sun Oct 24 2021 Simone Caronni <negativo17@gmail.com> - 2.18-1
- Update to 2.18.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 2.17-2
- Add BR: python3-setuptools to fix build on Fedora 35+.

* Tue Mar 16 2021 Simone Caronni <negativo17@gmail.com> - 2.17-1
- Update to 2.17.

* Sun Nov 08 2020 Simone Caronni <negativo17@gmail.com> - 2.16-1
- Update to 2.16.

* Fri Nov 06 2020 Simone Caronni <negativo17@gmail.com> - 2.15-1
- Update to 2.15.

* Wed Jul 08 2020 Simone Caronni <negativo17@gmail.com> - 2.14-1
- Update to 2.14.
- Use automatic Python depencency generator.

* Tue Jul 07 2020 Simone Caronni <negativo17@gmail.com> - 2.13-1
- Update to 2.13.

* Sat Jun 13 2020 Simone Caronni <negativo17@gmail.com> - 2.12-1
- First build.
