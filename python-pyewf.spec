# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcaes_ver		20220529
%define		libcdata_ver		20230108
%define		libcdatetime_ver	20141018
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfdatetime_ver	20180910
%define		libfguid_ver		20120426
%define		libfvalue_ver		20200711
%define		libhmac_ver		20200104
%define		libodraw_ver		20120630
%define		libsmdev_ver		20140406
%define		libsmraw_ver		20120630
%define		libuna_ver		20230702
Summary:	Python 2 bindings for libewf library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libewf
Name:		python-pyewf
Version:	20231119
Release:	2
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/libyal/libewf/releases
Source0:	https://github.com/libyal/libewf/releases/download/%{version}/libewf-experimental-%{version}.tar.gz
# Source0-md5:	9a8a2dc9fa7023e3c7144dcf3cdb256f
URL:		https://github.com/libyal/libewf/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcaes-devel >= %{libcaes_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcdatetime-devel >= %{libcdatetime_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfdatetime-devel >= %{libfdatetime_ver}
BuildRequires:	libfguid-devel >= %{libfguid_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libhmac-devel >= %{libhmac_ver}
BuildRequires:	libodraw-devel >= %{libodraw_ver}
BuildRequires:	libsmdev-devel >= %{libsmdev_ver}
BuildRequires:	libsmraw-devel >= %{libsmraw_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel >= 2.20
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	zlib-devel >= 1.2.5
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libewf >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libewf library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libewf.

%prep
%setup -q -n libewf-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python2 \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keep only python2 module
%{__rm} $RPM_BUILD_ROOT%{_bindir}/ewf*
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libewf*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libewf.*
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libewf.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[13]

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyewf.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{py_sitedir}/pyewf.so
