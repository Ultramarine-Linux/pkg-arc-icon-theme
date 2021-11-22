Name:		arc-icon-theme
Version:	20161122
Release:	2%{?dist}
Summary:	Arc Icon Theme

License:	GPLv3
URL:		https://github.com/horst3180/arc-icon-theme
Source0:	https://github.com/horst3180/%{name}/archive/%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  make
Requires:	hicolor-icon-theme

%description
The Arc Icon Theme

%prep
%autosetup
autoreconf -fi

%build
%configure
make

%install
%makeinstall

for f in 128 128@2x 16 16@2x 22 22@2x 24 24@2x 32 32@2x 48 48@2x 64 64@2x 96 96@2x; do
	ln -s ../../mimetypes/$f/x-office-calendar.png %{buildroot}/%{_datadir}/icons/Arc/apps/$f/preferences-calendar-and-tasks.png
done
ln -s ../../mimetypes/symbolic/x-office-calendar.svg %{buildroot}/%{_datadir}/icons/Arc/apps/symbolic/preferences-calendar-and-tasks.svg

%files
%doc COPYING CREDITS
%{_datadir}/icons/Arc

%changelog
* Fri Nov 29 2019 Thomas Batten <stenstorpmc@gmail.com> - 20161122-2
- Link icon preferences-calendar-and-tasks to x-office-calendar

* Mon Oct 28 2019 Thomas Batten <stenstorpmc@gmail.com> - 20161122-1
- Initial commit
