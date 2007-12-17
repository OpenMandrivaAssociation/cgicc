%define	name	cgicc
%define version 3.2.3
%define release %mkrel 3

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d


Summary:	Cgicc is an ANSI C++ class lib that simplifies the creation of CGI apps
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/C
URL:		http://www.gnu.org/software/cgicc
Source:		ftp://ftp.gnu.org/gnu/cgicc/%{name}-%{version}.tar.bz2

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
Summary:        Cgicc is an ANSI C++ class lib that simplifies the creation of CGI apps
Group:          Development/C

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
Summary:        Cgicc is an ANSI C++ class lib that simplifies the creation of CGI apps
Group:          Development/C
Requires:	%libname = %version
Provides: 	libcgicc-devel

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

%configure

%build

%install

%makeinstall

rm -rf $RPM_BUILD_ROOT/%_prefix/doc/
rm -rf $RPM_BUILD_ROOT/%_docdir/%name-%version/example/.libs

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
#%doc AUTHORS COPYING ChangeLog NEWS README example
%doc doc/html/* 
%_bindir/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%_includedir/%name

