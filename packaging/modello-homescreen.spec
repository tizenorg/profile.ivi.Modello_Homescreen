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
Requires:   wrt-installer
Requires:   wrt-plugins-ivi
Requires:   wrt-plugins-tizen-bt

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%build

make wgtPkg

%install
    %make_install
    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{_libdir}/systemd/user/weston.target.wants/
    install -m 755 systemd/modello_launcher.sh %{buildroot}%{_bindir}
    install -m 0644 systemd/Modello_Homescreen-launchpad-ready.path %{buildroot}%{_libdir}/systemd/user
    install -m 0644 systemd/Modello_Homescreen.service %{buildroot}%{_libdir}/systemd/user
    ln -sf systemd/Modello_Homescreen-launchpad-ready.path %{buildroot}%{_libdir}/systemd/user/weston.target.wants/

%post
    wrt-installer -i /opt/usr/apps/.preinstallWidgets/html5UIHomescreen.wgt
    cp -r /opt/usr/apps/_common/js/services /opt/usr/apps/html5POC05/res/wgt/js/
    cp -r /opt/usr/apps/_common/css/* /opt/usr/apps/html5POC05/res/wgt/css/

%postun
    wrt-installer -un html5POC05.Homescreen

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/html5UIHomescreen.wgt
%{_libdir}/systemd/user/Modello_Homescreen.service
%{_libdir}/systemd/user/Modello_Homescreen-launchpad-ready.path
%{_bindir}/modello_launcher.sh
%{_libdir}/systemd/user/weston.target.wants
