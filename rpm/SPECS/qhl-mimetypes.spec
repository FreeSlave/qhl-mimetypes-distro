Name:           qhl-mimetypes
Version:        1.0
Release:        1%{?dist}
Summary:        Collection of mime-type definitions for various Quake and Half-Life file formats
BuildArch:      noarch

License:        CC-BY
URL:            https://github.com/FreeSlave/qhl-mimetypes
Source0:        https://github.com/FreeSlave/qhl-mimetypes/archive/%{name}-%{version}.tar.gz

BuildRequires:  shared-mime-info

%description
qhl-mimetypes provides MIME-type definitions
for Quake and Half-Life related
file formats.

%prep
%setup -q

%post
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install

%files
%{_datadir}/mime/packages/quake-hl.xml
%{_datadir}/mime/packages/jack-mapeditor.xml

%changelog
* Wed Jan 15 2020 Roman Chistokhodov 1.0-1
- Initial release
