Name:              telepathy-glib
Version:           0.24.1
Release:           12
Summary:           GObject-based library for the Telepathy D-Bus API

License:           LGPLv2+
URL:               http://telepathy.freedesktop.org/
Source0:           http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz

Patch0:            telepathy-glib-0.24.1-glib246.patch
Source10:          expected-gtypes-f30.h
Source11:          expected-gtypes-body-f30.h

BuildRequires:     dbus-devel dbus-glib-devel glib2-devel gobject-introspection-devel
BuildRequires:     gtk-doc libxslt vala-devel vala git python3
Requires:	   glibc dbus-libs dbus-glib glib2

Provides:          %{name}-vala
Obsoletes:         %{name}-vala

%description
The telepathy-glib library is a GObject-based C binding for the
Telepathy D-Bus API.

%package           devel
Summary:           Header files for telepathy-glib
Requires:          %{name} = %{version}-%{release}
Requires:          dbus-devel dbus-glib-devel glib2-devel telepathy-glib
Requires:          pkgconf-pkg-config telepathy-filesystem

%description       devel
Header files for telepathy-glib

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

# Explicitly switch to python3
env LANG=C grep -rl python . | \
	xargs sed -i \
		-e 's|/usr/bin/python$|/usr/bin/python3|'  \
		-e 's|/usr/bin/env[ \t]*python$|/usr/bin/python3|' \
		%{nil}
 
# And tweak timestamps
touch aclocal.m4
find . -name Makefile.in | xargs touch
touch configure
touch config.h.in
 
 
sed -i tests/all-errors-documented.py -e 's|^\(.*\)print\(.*\)|\1print (\2)|'
cp -p %SOURCE10 tests/tools/expected-gtypes.h
cp -p %SOURCE11 tests/tools/expected-gtypes-body.h
 
%build
export PYTHON=python3

%configure --enable-introspection=yes --enable-vala-bindings=yes
%make_build

%install
%make_install
%delete_la

%ldconfig_scriptlets

%check
make check

%files
%defattr(-,root,root)
%doc README AUTHORS
%license COPYING
%{_libdir}/girepository-1.0/*
%{_libdir}/*.so.*
%{_datadir}/vala/vapi/telepathy-glib.*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/telepathy-glib.pc
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/telepathy-1.0/*
%{_datadir}/gir-1.0/*.gir

%files help
%defattr(-,root,root)
%doc NEWS
%{_datadir}/gtk-doc/html/*

%changelog
* Wed Oct 21 2020 jinzhimin <jinzhimin2@huawei.com> - 0.24.1-12
- modify buildrequire to python3

* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.24.1-11
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:modify the location of COPYING

* Sat Aug 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.24.1-10
- Package init
