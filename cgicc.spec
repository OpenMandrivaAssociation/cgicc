%define major 3
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	ANSI C++ class lib that simplifies the creation of CGI apps
Name:		cgicc
Version:	3.2.12
Release:	1
License:	LGPLv3+
Group:		Development/C
URL:		http://www.gnu.org/software/cgicc
Source:		ftp://ftp.gnu.org:21/gnu/cgicc/%{name}-%{version}.tar.gz
BuildRequires:	doxygen

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

%package -n %{libname}
Summary:        ANSI C++ class lib that simplifies the creation of CGI apps
Group:          Development/C
Obsoletes:	%mklibname cgicc 1

%description -n %{libname}
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

%package -n %{libnamedev}
Summary:        ANSI C++ class lib that simplifies the creation of CGI apps
Group:          Development/C
Requires:	%{libname} = %{version}
Provides: 	libcgicc-devel
Obsoletes:	%mklibname -d cgicc 1

%description -n %{libnamedev}
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
chmod 644 AUTHORS COPYING* ChangeLog NEWS README

%build
autoreconf -f -i
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}/%{_prefix}/doc/
rm -rf %{buildroot}/%{_docdir}/%{name}-%{version}/example/.libs

%files 
%doc AUTHORS COPYING* ChangeLog NEWS README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
