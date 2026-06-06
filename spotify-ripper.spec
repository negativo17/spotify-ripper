Name:           spotify-ripper
Version:        3.0.3
Release:        1%{?dist}
Summary:        Command-line ripper for Spotify
License:        MIT
URL:            https://github.com/scaronni/%{name}
BuildArch:      noarch

Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

Requires:       lame
Recommends:     fdkaac
Recommends:     ffmpeg
Recommends:     flac
Recommends:     opus-tools
Recommends:     sox

%description
A Spotify ripper that uses Librespot in the backend. Requires a Premium account
for usage.Ripping music from Spotify violates Terms and Conditions of Use:
https://www.spotify.com/legal

%prep
%autosetup -p1
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spotify_ripper

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
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
