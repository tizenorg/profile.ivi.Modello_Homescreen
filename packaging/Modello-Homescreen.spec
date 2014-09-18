Name:       Modello-Homescreen
Summary:    A proof of concept pure html5 UI
Version:    0.0.2
Release:    0
Group:      Automotive/Modello
License:    Apache-2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
Source1001: Modello-Homescreen.manifest

BuildRequires: zip
BuildRequires: pkgconfig(libtzplatform-config)
Requires:      Modello-Common

BuildArchitectures: noarch

%description
A proof of concept pure html5 UI files

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
#empty

%install
    mkdir -p %{buildroot}%{TZ_SYS_APP_PREINSTALL}
    mkdir -p %{buildroot}%{_datadir}/Modello/Common/icons
    zip -r %{buildroot}%{TZ_SYS_APP_PREINSTALL}/%{name}.wgt config.xml manifest.json css Homescreen_icon.png index.html js
    install -m 0644 Homescreen_icon.png %{buildroot}%{_datadir}/Modello/Common/icons

    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{_unitdir_user}/weston.target.wants/
    install -m 755 systemd/modello_launcher.sh %{buildroot}%{_bindir}
    install -m 0644 systemd/Modello_Homescreen-launchpad-ready.path %{buildroot}%{_unitdir_user}
    install -m 0644 systemd/Modello_Homescreen.service %{buildroot}%{_unitdir_user}
    ln -sf ../Modello_Homescreen-launchpad-ready.path %{buildroot}%{_unitdir_user}/weston.target.wants/

%files
%defattr(-,root,root,-)
%{TZ_SYS_APP_PREINSTALL}/%{name}.wgt
%{_datadir}/Modello/Common/icons/Homescreen_icon.png
%{_unitdir_user}/Modello_Homescreen.service
%{_unitdir_user}/Modello_Homescreen-launchpad-ready.path
%{_bindir}/modello_launcher.sh
%{_unitdir_user}/weston.target.wants
