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
rm -rf %{buildroot}
%make_install

%post
    wrt-installer -i /opt/usr/apps/.preinstallWidgets/html5UIHomescreen.wgt
    cp -r /opt/usr/apps/_common/js/services /opt/usr/apps/html5POC05/res/wgt/js/
    cp -r /opt/usr/apps/_common/css/* /opt/usr/apps/html5POC05/res/wgt/css/

    if [ ! -f /etc/xdg/weston/weston.ini.orig ] ; then \
	mv /etc/xdg/weston/weston.ini /etc/xdg/weston/weston.ini.orig; \
    fi;

    if [ ! -f /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf.orig ] ; then \
	mv /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf.orig; \
    fi;

    cp /etc/xdg/weston/weston.ini.new /etc/xdg/weston/weston.ini
    cp /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf.new /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf

%postun
    wrt-installer -un html5POC05.Homescreen
    rm /etc/xdg/weston/weston.ini
    mv /etc/xdg/weston/weston.ini.orig /etc/xdg/weston/weston.ini
    rm /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf
    mv /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf.orig /boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/html5UIHomescreen.wgt
/usr/lib/systemd/user/Modello_Homescreen.service
/usr/lib/systemd/user/Modello_Homescreen-launchpad-ready.path
/usr/bin/modello_launcher.sh
/etc/xdg/weston/weston.ini.new
/boot/loader/entries/vmlinuz-3.13.3-3.2-x86-ivi.conf.new
/usr/lib/systemd/user/weston.target.wants
