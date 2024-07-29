%global purplename    purple-plugin-pack
%global purpleplugver pp_2_8_0

Name:           purple-plugin_pack
Version:        2.8.0
Release:        8%{?dist}.nalika

License:        GPL-2.0-or-later
Summary:        A set of plugins for libpurple, pidgin, and finch
URL:            https://keep.imfreedom.org/pidgin/%{purplename}
Source0:        https://keep.imfreedom.org/pidgin/purple-plugin-pack/archive/%{purpleplugver}.tar.gz
Source1:        %{purplename}.metainfo.xml

BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(pidgin)
BuildRequires:  pkgconfig(purple)

BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  ninja-build

Provides:       %{purplename} = %{version}-%{release}

%description
This package contains a number of plugins for use with the purple IM/IRC
library.

%package pidgin
Summary:        A set of plugins for pidgin
Provides:       %{purplename}-pidgin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pidgin%{?_isa}

Provides:       %{name}-pidgin-xmms = %{version}-%{release}
Obsoletes:      %{name}-pidgin-xmms < %{version}-%{release}

%description pidgin
This package contains a number of plugins for use with the pidgin client.

%prep
%autosetup -n %{purplename}-%{purpleplugver}

%build
%meson \
    -Dwerror=false \
    -Dpurple-version=2 \
    -Dtypes=default \
    -Dnls=true
%meson_build

%install
%meson_install
%find_lang plugin_pack
install -Dm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{purplename}.metainfo.xml

%files -f plugin_pack.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_metainfodir}/%{purplename}.metainfo.xml
%{_libdir}/purple-2/*.so

%files pidgin
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/pidgin/*.so

%changelog
* Wed Apr 24 2024 Louis Abel <tucklesepk@gmail.com> - 2.8.0-8.nalika
- Start maintaining for Fedora, based on original spec
