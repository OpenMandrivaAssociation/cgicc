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


%changelog
* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 3.2.8-1mdv2010.0
+ Revision: 384506
- update to new version 3.2.8
- fix doc files perms
- use autoreconf
- remove Makefile.in workaround (no more needed)
- clean spec file

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 3.2.5-2mdv2008.1
+ Revision: 170782
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 3.2.5-1mdv2008.1
+ Revision: 164440
- BR doxygen
- New version 3.2.5
- License should be LGPLv3+

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.2.3-3mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cgicc


* Wed Aug 02 2006 Lenny Cartier <lenny@mandriva.com> 3.2.3-3mdv2007.0
- rebuild

* Thu Oct 27 2005 Lenny Cartier <lenny@mandriva.com> 3.2.3-2mdk
- rebuild for dependencies

* Wed May 25 2005 Nicolas L�cureuil <neoclust@mandriva.org> 3.2.3-1mdk
- New release 3.2.3

* Fri Jun 18 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-4mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-3mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-2mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Thu Jun 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.1.5-1mdk
- update to 3.1.5

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-1mdk
- updated to 3.1.4
- use install-info

* Wed Aug 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.1.3-2mdk
- more macros
- bm

* Thu Jul 06 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 3.0-1mdk
- mandrake-ize package
- update version
- macro-ize package
- don't use RPM_OPT_FLAGS as we need -fexceptions and not -fno-exeptions

* Wed May 26 1999 Ryan Weaver <ryanw@infohwy.com>
  [cgicc-3.0-1]
- Initial RPM build.
- Reworked to use the C++ standard template library. 
  In most places, the STL class string is used where bare char* was
  used before. The obsolete classes implementing linked lists are
  gone, replaced by the STL classes vector and iterator. 
- Include files are now installed in the package include directory 
  cgicc/ under the include/ directory, instead of in the
  include/ directory itself.
- Documentation changed to info format, and expanded.
- The test/ directory was renamed to demo/.
- The demo programs are no longer installed.
- The demo programs now contain internal stylesheet information, instead 
  of linking to an external stylesheet.
- Released as part of the GNU project under the GPL.
