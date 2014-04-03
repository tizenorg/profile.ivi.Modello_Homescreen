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
	cp $(PROJECT).wgt $(INSTALL_DIR)/

dist:
	tar czf ../$(PACKAGE).tar.bz2 .
