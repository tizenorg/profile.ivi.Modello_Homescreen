PROJECT = html5UIHomescreen

VERSION := 0.0.1
PACKAGE = $(PROJECT)-$(VERSION)

INSTALL_FILES = $(PROJECT).wgt
INSTALL_DIR = ${DESTDIR}/opt/usr/apps/.preinstallWidgets

wgtPkg:
	zip -r $(PROJECT).wgt config.xml css icon.png index.html js

install:
	@echo "Installing Homescreen, stand by..."
	mkdir -p $(INSTALL_DIR)/
	mkdir -p ${DESTDIR}/usr/bin
	mkdir -p ${DESTDIR}/usr/lib/systemd/user
	mkdir -p ${DESTDIR}/etc/xdg/weston/
	mkdir -p ${DESTDIR}/usr/lib/systemd/user/weston.target.wants/
	mkdir -p ${DESTDIR}/boot/loader/entries/
	cp $(PROJECT).wgt $(INSTALL_DIR)/
	install -m 755 systemd/modello_launcher.sh ${DESTDIR}/usr/bin
	install -m 0644 systemd/Modello_Homescreen-launchpad-ready.path ${DESTDIR}/usr/lib/systemd/user
	install -m 0644 systemd/Modello_Homescreen.service ${DESTDIR}/usr/lib/systemd/user
	ln -sf systemd/Modello_Homescreen-launchpad-ready.path ${DESTDIR}/usr/lib/systemd/user/weston.target.wants/
	install -m 0644 systemd/weston.ini.new ${DESTDIR}/etc/xdg/weston/
	install -m 0644 systemd/vmlinuz-3.13.3-3.2-x86-ivi.conf.new ${DESTDIR}/boot/loader/entries/

dist:
	tar czf ../$(PACKAGE).tar.bz2 .
