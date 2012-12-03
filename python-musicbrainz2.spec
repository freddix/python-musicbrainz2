Summary:	Python module for MusicBrainz 2nd generation
Name:		python-musicbrainz2
Version:	0.7.4
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/python-musicbrainz2/%{name}-%{version}.tar.gz
# Source0-md5:	40ac802d832deca737cce57235cb23a5
URL:		http://musicbrainz.org/doc/PythonMusicBrainz2
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-musicbrainz2 is a client library written in python, which
provides easy object oriented access to the MusicBrainz Database using
the XMLWebService. It has been written from scratch and uses
a different model than PythonMusicbrainz, the first generation Python
bindings.

%prep
%setup -q

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT

%{__python} ./setup.py install	\
	--optimize=2		\
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt COPYING.txt README.txt
%attr(755,root,root) %{_bindir}/mb-submit-disc
%{py_sitescriptdir}/musicbrainz2

