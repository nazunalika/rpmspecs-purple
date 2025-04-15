%global purplename discord

%global commit ddc118bdb46f02d865ae56b470cf3176520df59b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250414

Name:          purple-%{purplename}
Version:       0
Release:       40.%{date}git%{shortcommit}%{?dist}.nalika

License:       GPL-3.0-or-later
Summary:       Discord plugin for libpurple
URL:           https://github.com/EionRobb/%{name}
Source0:       %{url}/archive/%{commit}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libqrencode)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)

BuildRequires: ImageMagick
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: make

%package       -n pidgin-%{purplename}
Summary:       Adds pixmaps, icons and smileys for Discord protocol
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
Requires:      pidgin

%description
Adds support for Discord to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{purplename}
Adds pixmaps, icons and smileys for Discord protocol implemented by
purple-discord.

%prep
%autosetup -n %{name}-%{commit}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_libdir}/purple-2/lib%{purplename}.so

%files -n pidgin-%{purplename}
%{_datadir}/pixmaps/pidgin/protocols/*/%{purplename}.png

%changelog
* Mon Apr 14 2025 Louis Abel <tucklesepk@gmail.com> - 0-40.20250414git.nalika
- Rebuild on latest commit

* Mon Jul 29 2024 Louis Abel <tucklesepk@gmail.com> - 0-39.20240729git.nalika
- Rebuild on latest commit

* Wed Apr 24 2024 Louis Abel <tucklesepk@gmail.com> - 0-38.20240424git.nalika
- Rebuild for Fedora based on original spec

