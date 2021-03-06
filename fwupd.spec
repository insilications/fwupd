#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : fwupd
Version  : 1.8.0
Release  : 601
URL      : file:///aot/build/clearlinux/packages/fwupd/fwupd-v1.8.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/fwupd/fwupd-v1.8.0.tar.gz
Summary  : A simple daemon to allow session software to update firmware
Group    : Development/Tools
License  : GPL-2.0
Requires: glib
Requires: gsettings-desktop-schemas
Requires: udisks2
BuildRequires : clear-font
BuildRequires : expat
BuildRequires : expat-dev
BuildRequires : fontconfig
BuildRequires : gcab
BuildRequires : glibc-bin
BuildRequires : gmp
BuildRequires : gmp-dev
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
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
BuildRequires : pypi(pillow)
BuildRequires : python3-dev
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-pki-files-are-moved-under-datadir.patch

%description
This project aims to make updating firmware on Linux automatic, safe and
reliable. Additional information is available at the website: https://fwupd.org

%prep
%setup -q -n fwupd
cd %{_builddir}/fwupd
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651316753
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wno-inline"
export ASMFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wno-inline"
export CXXFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wno-inline"
export FCFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wno-inline"
export FFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wno-inline"
export LDFLAGS="-DNDEBUG -Ofast -mno-vzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -pthread -Wl,--build-id=sha1 -ftrivial-auto-var-init=zero -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --sysconfdir=/usr/share --prefix=/usr --buildtype=plain -Ddefault_library=both -Ddocs=none \
-Dplugin_tpm=false  builddir
ninja --verbose %{?_smp_mflags} -C builddir



%install
## install_macro start
DESTDIR=%{buildroot} ninja -C builddir install || :
## install_macro end
## Remove excluded files
rm -f %{buildroot}*/var/lib/fwupd/builder/README.md
## install_append content
rm -fr %{buildroot}/usr/share/fwupd/dbus-1
rm %{buildroot}/usr/lib/systemd/system/system-update.target.wants/fwupd-offline-update.service
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../fwupd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/fwupd.service
mv %{buildroot}/etc/pki %{buildroot}/usr/share/fwupd/pki
mkdir -p %{buildroot}/usr/share/defaults
mv %{buildroot}/etc/fwupd %{buildroot}/usr/share/defaults/fwupd
## install_append end

%files
%defattr(-,root,root,-)
