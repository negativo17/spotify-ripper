Name:           spotify-ripper
Version:        2.16
Release:        1%{?dist}
Summary:        Command-line ripper for Spotify
License:        MIT
URL:            https://github.com/scaronni/%{name}
BuildArch:      noarch

Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

# For tests
#BuildRequires:  python3-colorama
#BuildRequires:  python3-mutagen
#BuildRequires:  python3-requests
#BuildRequires:  python3-schedule

Requires:       lame

Suggests:       fdkaac
Suggests:       ffmpeg
Suggests:       flac
Suggests:       opus-tools
Suggests:       sox
Suggests:       vorbis-tools

%description
A fork of spotify-ripper that still uses spotipy for a small set of functions,
but progressively moves to Spotify's WebAPI for most functions (e.g. playlist
functions), including the automated handling of tokens given the fact that most
WebAPI functions now require an authorization token. This fork also adds a few
options and formating capabilities.

%prep
%autosetup -p1

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

#%check
#%{__python3} setup.py test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
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
