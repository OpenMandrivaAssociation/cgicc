%define	name	cgicc
%define version 3.2.8
%define release %mkrel 1

%define major 5
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary:	ANSI C++ class lib that simplifies the creation of CGI apps
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv3+
Group:		Development/C
URL:		http://www.gnu.org/software/cgicc
Source:		ftp://ftp.gnu.org/gnu/cgicc/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GNU Cgicc is an ANSI C++ compliant class library that greatly
simplifies the creation of CGI applications for the World Wide
Web. Cgicc performs the following functions:

 - Parses both GET and POST form data transparently. 
 - Provides string, integer, floating-point and single- and
   multiple-choice retrieval methods for form data.
 - Provides methods for saving and restoring CGI environments to aid
   in application debugging.
 - Provides full on-the-fly HTML generation capabilities, with support
   for cookies and file inclusion.
 - Supports HTTP file upload. 

%package -n %libname
Summary:        ANSI C++ class lib that simplifies the creation of CGI apps
Group:          Development/C
Obsoletes:	%mklibname cgicc 1

%description -n %libname
GNU Cgicc is an ANSI C++ compliant class library that greatly
simplifies the creation of CGI applications for the World Wide
Web. Cgicc performs the following functions:

 - Parses both GET and POST form data transparently.
 - Provides string, integer, floating-point and single- and
   multiple-choice retrieval methods for form data.
 - Provides methods for saving and restoring CGI environments to aid
   in application debugging.
 - Provides full on-the-fly HTML generation capabilities, with support
   for cookies and file inclusion.
 - Supports HTTP file upload.

%package -n %libnamedev
Summary:        ANSI C++ class lib that simplifies the creation of CGI apps
Group:          Development/C
Requires:	%libname = %version
Provides: 	libcgicc-devel
Obsoletes:	%mklibname -d cgicc 1

%description -n %libnamedev
GNU Cgicc is an ANSI C++ compliant class library that greatly
simplifies the creation of CGI applications for the World Wide
Web. Cgicc performs the following functions:

 - Parses both GET and POST form data transparently.
 - Provides string, integer, floating-point and single- and
   multiple-choice retrieval methods for form data.
 - Provides methods for saving and restoring CGI environments to aid
   in application debugging.
 - Provides full on-the-fly HTML generation capabilities, with support
   for cookies and file inclusion.
 - Supports HTTP file upload.

%prep
%setup -q

# fix doc files perms
chmod 644 doc/html/* \
	AUTHORS COPYING* ChangeLog NEWS README


%build
autoreconf -f -i
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

rm -rf %{buildroot}/%_prefix/doc/
rm -rf %{buildroot}/%_docdir/%name-%version/example/.libs

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS README
%doc doc/html/* 
%_bindir/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
