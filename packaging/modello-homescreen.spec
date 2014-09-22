Name:       Modello_Homescreen
Summary:    A proof of concept pure html5 UI
Version:    0.0.2
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  zip
Requires:   Modello_Common
BuildRequires: pkgconfig(libtzplatform-config)

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%install
    mkdir -p %{buildroot}%{TZ_SYS_APP_PREINSTALL}
    mkdir -p %{buildroot}%{_datadir}/Modello/Common/icons
    zip -r %{buildroot}%{TZ_SYS_APP_PREINSTALL}/%{name}.wgt config.xml manifest.json css Homescreen_icon.png index.html js
    install -m 0644 Homescreen_icon.png %{buildroot}%{_datadir}/Modello/Common/icons

    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{_libdir}/systemd/user/weston.target.wants/
    install -m 755 systemd/modello_launcher.sh %{buildroot}%{_bindir}
    install -m 0644 systemd/Modello_Homescreen-launchpad-ready.path %{buildroot}%{_libdir}/systemd/user
    install -m 0644 systemd/Modello_Homescreen.service %{buildroot}%{_libdir}/systemd/user
    ln -sf ../Modello_Homescreen-launchpad-ready.path %{buildroot}%{_libdir}/systemd/user/weston.target.wants/

%files
%defattr(-,root,root,-)
%{TZ_SYS_APP_PREINSTALL}/Modello_Homescreen.wgt
%{_datadir}/Modello/Common/icons/Homescreen_icon.png
%{_libdir}/systemd/user/Modello_Homescreen.service
%{_libdir}/systemd/user/Modello_Homescreen-launchpad-ready.path
%{_bindir}/modello_launcher.sh
%{_libdir}/systemd/user/weston.target.wants
