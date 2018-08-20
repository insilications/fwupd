#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fwupd
Version  : 1.1.0
Release  : 16
URL      : https://github.com/hughsie/fwupd/archive/1.1.0.tar.gz
Source0  : https://github.com/hughsie/fwupd/archive/1.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1
Requires: fwupd-bin
Requires: fwupd-config
Requires: fwupd-autostart
Requires: fwupd-lib
Requires: fwupd-data
Requires: fwupd-license
Requires: fwupd-locales
Requires: fwupd-man
BuildRequires : Pillow
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : clear-font
BuildRequires : font-bitstream-type1
BuildRequires : fontconfig
BuildRequires : gcab
BuildRequires : glibc-bin
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : help2man
BuildRequires : libgpg-error-dev
BuildRequires : libsmbios-dev
BuildRequires : libxslt
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(colorhug)
BuildRequires : pkgconfig(efivar)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(gusb)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(udev)
BuildRequires : popt-dev
BuildRequires : pycairo
BuildRequires : pygobject
BuildRequires : pygobject-dev
BuildRequires : python3-dev
BuildRequires : vala
Patch1: 0001-Fixups-for-Clear-Linux-stateless-settings.patch

%description
This project aims to make updating firmware on Linux automatic, safe and
reliable. Additional information is available at the website: https://fwupd.org

%package autostart
Summary: autostart components for the fwupd package.
Group: Default

%description autostart
autostart components for the fwupd package.


%package bin
Summary: bin components for the fwupd package.
Group: Binaries
Requires: fwupd-data
Requires: fwupd-config
Requires: fwupd-license
Requires: fwupd-man

%description bin
bin components for the fwupd package.


%package config
Summary: config components for the fwupd package.
Group: Default

%description config
config components for the fwupd package.


%package data
Summary: data components for the fwupd package.
Group: Data

%description data
data components for the fwupd package.


%package dev
Summary: dev components for the fwupd package.
Group: Development
Requires: fwupd-lib
Requires: fwupd-bin
Requires: fwupd-data
Provides: fwupd-devel

%description dev
dev components for the fwupd package.


%package doc
Summary: doc components for the fwupd package.
Group: Documentation
Requires: fwupd-man

%description doc
doc components for the fwupd package.


%package lib
Summary: lib components for the fwupd package.
Group: Libraries
Requires: fwupd-data
Requires: fwupd-license

%description lib
lib components for the fwupd package.


%package license
Summary: license components for the fwupd package.
Group: Default

%description license
license components for the fwupd package.


%package locales
Summary: locales components for the fwupd package.
Group: Default

%description locales
locales components for the fwupd package.


%package man
Summary: man components for the fwupd package.
Group: Default

%description man
man components for the fwupd package.


%prep
%setup -q -n fwupd-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534191679
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dgtkdoc=false --sysconfdir=/usr/share/fwupd/  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/fwupd
cp COPYING %{buildroot}/usr/share/doc/fwupd/COPYING
cp contrib/debian/copyright %{buildroot}/usr/share/doc/fwupd/contrib_debian_copyright
cp data/tests/thunderbolt/COPYING %{buildroot}/usr/share/doc/fwupd/data_tests_thunderbolt_COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang fwupd
## install_append content
install -D -m 0644 %{buildroot}/usr/share/fwupd/dbus-1/system.d/org.freedesktop.fwupd.conf %{buildroot}/usr/share/dbus-1/system.d/org.freedesktop.fwupd.conf
rm -fr %{buildroot}/usr/share/fwupd/dbus-1
rm %{buildroot}/usr/lib/systemd/system/system-update.target.wants/fwupd-offline-update.service
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../fwupd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/fwupd.service
## install_append end

%files
%defattr(-,root,root,-)
%exclude /var/lib/fwupd/builder/README.md

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/fwupd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/dfu-tool
/usr/bin/fwupdmgr
/usr/libexec/fwupd/efi/fwupdx64.efi
/usr/libexec/fwupd/fwupd
/usr/libexec/fwupd/fwupdate
/usr/libexec/fwupd/fwupdtool

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/fwupd.service
/usr/lib/systemd/system/fwupd-offline-update.service
/usr/lib/systemd/system/fwupd.service
/usr/lib/udev/rules.d/90-fwupd-devices.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Fwupd-2.0.typelib
/usr/share/bash-completion/completions/fwupdmgr
/usr/share/bash-completion/completions/fwupdtool
/usr/share/dbus-1/interfaces/org.freedesktop.fwupd.xml
/usr/share/dbus-1/system-services/org.freedesktop.fwupd.service
/usr/share/dbus-1/system.d/org.freedesktop.fwupd.conf
/usr/share/fwupd/firmware-packager
/usr/share/fwupd/fwupd/daemon.conf
/usr/share/fwupd/fwupd/remotes.d/fwupd.conf
/usr/share/fwupd/fwupd/remotes.d/lvfs-testing.conf
/usr/share/fwupd/fwupd/remotes.d/lvfs.conf
/usr/share/fwupd/fwupd/remotes.d/vendor.conf
/usr/share/fwupd/fwupd/uefi.conf
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
/usr/share/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Foundation-Metadata
/usr/share/fwupd/pki/fwupd-metadata/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd-metadata/LVFS-CA.pem
/usr/share/fwupd/pki/fwupd/GPG-KEY-Hughski-Limited
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Foundation-Firmware
/usr/share/fwupd/pki/fwupd/GPG-KEY-Linux-Vendor-Firmware-Service
/usr/share/fwupd/pki/fwupd/LVFS-CA.pem
/usr/share/fwupd/quirks.d/altos.quirk
/usr/share/fwupd/quirks.d/colorhug.quirk
/usr/share/fwupd/quirks.d/csr-aiaiai.quirk
/usr/share/fwupd/quirks.d/dell.quirk
/usr/share/fwupd/quirks.d/dfu.quirk
/usr/share/fwupd/quirks.d/ebitdo.quirk
/usr/share/fwupd/quirks.d/nitrokey.quirk
/usr/share/fwupd/quirks.d/steelseries.quirk
/usr/share/fwupd/quirks.d/wacomhid.quirk
/usr/share/fwupd/remotes.d/fwupd/metadata.xml
/usr/share/fwupd/remotes.d/vendor/firmware/README.md
/usr/share/gir-1.0/*.gir
/usr/share/installed-tests/fwupd/fakedevice123.cab
/usr/share/installed-tests/fwupd/fakedevice124.cab
/usr/share/installed-tests/fwupd/firmware-example.xml.gz
/usr/share/installed-tests/fwupd/firmware-example.xml.gz.asc
/usr/share/installed-tests/fwupd/fwupdmgr.sh
/usr/share/installed-tests/fwupd/fwupdmgr.test
/usr/share/installed-tests/fwupd/hardware.py
/usr/share/locale/ca/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/ca/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/cs/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/en/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/fi/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/fur/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/hr/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/hu/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/id/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/it/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/ko/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/pl/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/pt_BR/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/ru/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/sr/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/sv/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/uk/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/zh_CN/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-1024-768.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-1920-1080.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-3840-2160.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-5120-2880.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-5688-3200.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-640-480.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-7680-4320.bmp.gz
/usr/share/locale/zh_TW/LC_IMAGES/fwupd-800-600.bmp.gz
/usr/share/metainfo/org.freedesktop.fwupd.metainfo.xml
/usr/share/polkit-1/actions/org.freedesktop.fwupd.policy
/usr/share/polkit-1/rules.d/org.freedesktop.fwupd.rules
/usr/share/vala/vapi/fwupd.deps
/usr/share/vala/vapi/fwupd.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/fwupd-1/fwupd.h
/usr/include/fwupd-1/libfwupd/fwupd-client.h
/usr/include/fwupd-1/libfwupd/fwupd-common.h
/usr/include/fwupd-1/libfwupd/fwupd-deprecated.h
/usr/include/fwupd-1/libfwupd/fwupd-device.h
/usr/include/fwupd-1/libfwupd/fwupd-enums.h
/usr/include/fwupd-1/libfwupd/fwupd-error.h
/usr/include/fwupd-1/libfwupd/fwupd-release.h
/usr/include/fwupd-1/libfwupd/fwupd-remote.h
/usr/include/fwupd-1/libfwupd/fwupd-version.h
/usr/lib64/libfwupd.so
/usr/lib64/pkgconfig/fwupd.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/fwupd/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/fwupd-plugins-3/libfu_plugin_altos.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_amt.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_colorhug.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_csr.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dell.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dell_esrt.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_dfu.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_ebitdo.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_nitrokey.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_redfish.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_steelseries.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_synapticsmst.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_thunderbolt.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_thunderbolt_power.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_udev.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_uefi.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_unifying.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_upower.so
/usr/lib64/fwupd-plugins-3/libfu_plugin_wacomhid.so
/usr/lib64/libfwupd.so.2
/usr/lib64/libfwupd.so.2.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/fwupd/COPYING
/usr/share/doc/fwupd/data_tests_thunderbolt_COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/dfu-tool.1
/usr/share/man/man1/fwupdmgr.1

%files locales -f fwupd.lang
%defattr(-,root,root,-)

