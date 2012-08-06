%define	shortname	bashets
Summary:	Bashets is a widget library that displays data from scripts
Name:		awesome-plugin-%{shortname}
Version:	0.6.3
Release:	0.1
License:	GPL v3
Group:		X11/Window Managers/Tools
Source0:	http://gitorious.org/bashets/bashets/blobs/raw/master/bashets.lua
# Source0-md5:	fead95b357bc800773c6a506c126ba72
URL:		http://awesome.naquadah.org/wiki/Bashets
Requires:	awesome >= 3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bashets is a user widget library powered by shell scripts. Bashets is
glue code which empowers you to fetch data somewhere, and put it
somewhere. It is a distinct approach from Obvious or Vicious, which
try to implement and package predefined widgets themselves.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/bashets
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/awesome/lib/bashets.lua

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/bashets
%{_datadir}/awesome/lib/bashets.lua
