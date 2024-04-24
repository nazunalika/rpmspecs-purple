%global purplename googlechat

%global commit ddc118bdb46f02d865ae56b470cf3176520df59b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20240424

Name:          purple-%{purplename}
Version:       0
Release:       100.%{date}git%{shortcommit}%{?dist}.nalika

License:       GPL-3.0-or-later
Summary:       Google Chat plugin for libpurple
URL:           https://github.com/EionRobb/%{name}
Source0:       %{url}/archive/%{commit}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: make

Provides:      purple-hangouts = %{version}-%{release}
Obsoletes:     purple-hangouts < 0-80.20210629git55b9f01

%package       -n pidgin-%{purplename}
Summary:       Adds pixmaps, icons and smileys for Google Chat protocol
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
Requires:      pidgin
Provides:      pidgin-hangouts = %{version}-%{release}
Obsoletes:     pidgin-hangouts < 0-80.20210629git55b9f01

%description
Adds support for Google Chat to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{purplename}
Adds pixmaps, icons and smileys for Google Chat protocol implemented by
purple-googlechat.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{purplename}.so

%files
%{_libdir}/purple-2/lib%{purplename}.so
%license LICENSE
%doc README.md

%files -n pidgin-%{purplename}
%{_datadir}/pixmaps/pidgin/protocols/*/%{purplename}.png

%changelog
* Wed Apr 24 2024 Louis Abel <tucklesepk@gmail.com> - 0-100.20240424git.nalika
- Rebuild for Fedora
