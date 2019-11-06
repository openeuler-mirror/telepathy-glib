Name:              telepathy-glib
Version:           0.24.1
Release:           11
Summary:           GObject-based library for the Telepathy D-Bus API

License:           LGPLv2+
URL:               http://telepathy.freedesktop.org/
Source0:           http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz

Patch0:            telepathy-glib-0.24.1-glib246.patch
BuildRequires:     dbus-devel dbus-glib-devel glib2-devel gobject-introspection-devel
BuildRequires:     gtk-doc libxslt python2 vala-devel vala git python2
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

%build
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
* Mon Oct 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.24.1-11
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:modify the location of COPYING

* Sat Aug 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.24.1-10
- Package init
