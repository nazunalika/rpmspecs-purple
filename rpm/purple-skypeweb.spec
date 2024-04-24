%global purplename skypeweb

Name:          purple-%{purplename}
Version:       1.7
Release:       8%{?dist}.nalika
Summary:       Adds support for Skype to Pidgin

License:       GPL-3.0-or-later
URL:           https://github.com/EionRobb/skype4pidgin
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: gcc
BuildRequires: make

Provides:      skype4pidgin = %{version}-%{release}
Obsoletes:     skype4pidgin < %{version}-%{release}

%description
Adds support for Skype to Pidgin, Adium, Finch and other libpurple 
based messengers.

%package       -n pidgin-%{purplename}
Summary:       Adds pixmaps, icons and smileys for Skype protocol
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
Requires:      pidgin

%description -n pidgin-%{purplename}
Adds pixmaps, icons and smileys for Skype protocol implemented by libskypeweb.

%prep
%autosetup -n skype4pidgin-%{version}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," %{purplename}/README.md

%build
%set_build_flags
%make_build -C %{purplename}

%install
%make_install -C %{purplename}

%files
%doc %{purplename}/README.md
%license %{purplename}/gpl3.txt
%{_libdir}/purple-2/lib%{purplename}.so

%files -n pidgin-%{purplename}
%{_datadir}/pixmaps/pidgin/protocols/*/skype*.png
%{_datadir}/pixmaps/pidgin/emotes/skype

%changelog
* Wed Apr 24 2024 Louis Abel <tucklesepk@gmail.com> - 1.7-8.nalika
- Rebuild for Fedora
