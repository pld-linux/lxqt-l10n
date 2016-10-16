#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-l10n
Name:		lxqt-l10n
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	6abf67c48449da9817618bf5cc2221bd
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	lxqt-common >= 0.11.0
BuildRequires:	xz-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-l10n.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/compton-conf/translations
%dir %{_datadir}/libfm-qt/translations
%dir %{_datadir}/lximage-qt/translations
%dir %{_datadir}/obconf-qt/translations
%dir %{_datadir}/pcmanfm-qt/translations
%dir %{_datadir}/qterminal/translations

%dir %{_datadir}/lxqt/translations/liblxqt
%dir %{_datadir}/lxqt/translations/lxqt-about
%dir %{_datadir}/lxqt/translations/lxqt-admin-time
%dir %{_datadir}/lxqt/translations/lxqt-admin-user
%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
%dir %{_datadir}/lxqt/translations/lxqt-config-brightness
%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
%dir %{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts
%dir %{_datadir}/lxqt/translations/lxqt-config-input
%dir %{_datadir}/lxqt/translations/lxqt-config-locale
%dir %{_datadir}/lxqt/translations/lxqt-config-monitor
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-config-session
%dir %{_datadir}/lxqt/translations/lxqt-config
%dir %{_datadir}/lxqt/translations/lxqt-leave
%dir %{_datadir}/lxqt/translations/lxqt-notificationd
%dir %{_datadir}/lxqt/translations/lxqt-openssh-askpass
%dir %{_datadir}/lxqt/translations/lxqt-panel
%dir %{_datadir}/lxqt/translations/lxqt-panel/clock
%dir %{_datadir}/lxqt/translations/lxqt-panel/cpuload
%dir %{_datadir}/lxqt/translations/lxqt-panel/desktopswitch
%dir %{_datadir}/lxqt/translations/lxqt-panel/directorymenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/dom
%dir %{_datadir}/lxqt/translations/lxqt-panel/kbindicator
%dir %{_datadir}/lxqt/translations/lxqt-panel/mainmenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/mount
%dir %{_datadir}/lxqt/translations/lxqt-panel/networkmonitor
%dir %{_datadir}/lxqt/translations/lxqt-panel/quicklaunch
%dir %{_datadir}/lxqt/translations/lxqt-panel/sensors
%dir %{_datadir}/lxqt/translations/lxqt-panel/showdesktop
%dir %{_datadir}/lxqt/translations/lxqt-panel/spacer
%dir %{_datadir}/lxqt/translations/lxqt-panel/sysstat
%dir %{_datadir}/lxqt/translations/lxqt-panel/taskbar
%dir %{_datadir}/lxqt/translations/lxqt-panel/volume
%dir %{_datadir}/lxqt/translations/lxqt-panel/worldclock
%dir %{_datadir}/lxqt/translations/lxqt-policykit-agent
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-runner
%dir %{_datadir}/lxqt/translations/lxqt-session
%dir %{_datadir}/lxqt/translations/lxqt-sudo


#%%dir %{_datadir}/lxqt/translations/%{name}
