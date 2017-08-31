# Upstream xbmc hardcodes a Git hash for OSes that bundle xbmc-pvr-addons. Let's
# try using the same hash that upstream uses for the current Kodi version
# available in RPMFusion. It can be found in the Kodi source tree like so:
#   grep ^VERSION tools/depends/target/xbmc-pvr-addons/Makefile
%global commit a0a437eac14c9532ea0c6d38f8f222a612aea147
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20150125
%global snapshot_release %{commit_date}git%{short_commit}
# %%global tag 14.0-Helix

%global alt_name xbmc-pvr-addons

# Minimum supported version of Kodi
%global kodi_version 14.0

Name:           kodi-pvr-addons
Version:        14.0
Release:        0.4.%{snapshot_release}%{?dist}
# Release:        1%%{?dist}
Summary:        Kodi PVR add-ons

Group:          Applications/Multimedia
# Entire package is GPLv3 (see COPYING). All the PVR addons are GPLv2+. Portions
# of lib/libhts are LGPLv2+. lib/dvblinkremote is MIT
License:        GPLv3 and GPLv2+ and LGPLv2+ and MIT
URL:            https://github.com/opdenkamp/xbmc-pvr-addons/
Source0:        https://github.com/opdenkamp/%{alt_name}/archive/%{short_commit}/%{alt_name}-%{short_commit}.tar.gz
# Source0:        https://github.com/opdenkamp/%%{name}/archive/%%{tag}/%%{name}-%%{tag}.tar.gz
# Use system cppmyth library
Patch0:         %{name}-14.0-use_external_cppmyth.patch
# Use system jsoncpp library
Patch1:         %{name}-14.0-use_external_jsoncpp.patch
# Use system rapidxml library
Patch2:         %{name}-14.0-use_external_rapidxml.patch
# Use system tinyxml library
Patch3:         %{name}-14.0-use_external_tinyxml.patch
# Use system tinyxml2 library
Patch4:         %{name}-14.0-use_external_tinyxml2.patch
# Use system Kodi headers
Patch5:         %{name}-14.0-use_external_xbmc.patch

BuildRequires:  cppmyth-devel
BuildRequires:  cryptopp-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  mariadb-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  rapidxml-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  zlib-devel

%description
%{summary}.


%package        common
Summary:        Files common to Kodi PVR addons
Group:          Applications/Multimedia
Provides:       xbmc-pvr-addons-common = %{version}-%{release}
Obsoletes:      xbmc-pvr-addons-common < 14.0
Requires:       kodi >= %{kodi_version}
BuildArch:      noarch

%description    common
This package contains files common to Kodi PVR addons.


%package -n     kodi-pvr-argustv
Summary:        Kodi frontend for the ARGUS TV PVR
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-argustv = %{version}-%{release}
Obsoletes:      xbmc-pvr-argustv < 14.0

%description -n kodi-pvr-argustv
ARGUS TV PVR frontend for Kodi. Supports streaming of Live TV & recordings,
listening to radio channels, EPG and schedules.


%package -n     kodi-pvr-demo
Summary:        Demo PVR Client for Kodi
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-demo = %{version}-%{release}
Obsoletes:      xbmc-pvr-demo < 14.0

%description -n kodi-pvr-demo
%{summary}.


%package -n     kodi-pvr-dvblink
Summary:        Kodi PVR Plugin for DVBLink
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-dvblink = %{version}-%{release}
Obsoletes:      xbmc-pvr-dvblink < 14.0

%description -n kodi-pvr-dvblink
PVR Plugin for DVBLink from DvbLogic.com for Kodi; supporting streaming of Live
TV & recordings, EPG, timers.


%package -n     kodi-pvr-dvbviewer
Summary:        Kodi's frontend for DVBViewer
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-dvbviewer = %{version}-%{release}
Obsoletes:      xbmc-pvr-dvbviewer < 14.0

%description -n kodi-pvr-dvbviewer
DVBViewer Recording Service frontend; supporting streaming of LiveTV, timers,
recordings & EPG.


%package -n     kodi-pvr-filmon
Summary:        Filmon PVR client for Kodi
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}

%description -n kodi-pvr-filmon
Filmon frontend. Supports live TV, recordings, EPG. Requires a Filmon
subscription.

Before enabling:
  (a) in Filmon set channels as favourite to see them in Kodi
  (b) enter your username and password in this addon's settings.
Note: recordings can take several minutes to appear after timer is completed.


%package -n     kodi-pvr-hts
Summary:        Kodi's frontend for Tvheadend
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       bundled(sha1-niedermayer)
Provides:       xbmc-pvr-hts = %{version}-%{release}
Obsoletes:      xbmc-pvr-hts < 14.0

%description -n kodi-pvr-hts
Tvheadend frontend; supporting streaming of Live TV & recordings, EPG, timers.


%package -n     kodi-pvr-iptvsimple
Summary:        Kodi PVR addon for IPTV support
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-iptvsimple = %{version}-%{release}
Obsoletes:      xbmc-pvr-iptvsimple < 14.0

%description -n kodi-pvr-iptvsimple
IPTV Simple PVR Client support m3u playlists, streaming of Live TV for
multicast/unicast sources, listening to radio channels and EPG.


%package -n     kodi-pvr-mediaportal-tvserver
Summary:        Kodi frontend for the MediaPortal TV Server (ffmpeg + tsreader version)
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-mediaportal-tvserver = %{version}-%{release}
Obsoletes:      xbmc-pvr-mediaportal-tvserver < 14.0

%description -n kodi-pvr-mediaportal-tvserver
MediaPortal TV Server frontend for Kodi. Supports streaming of Live TV &
recordings, listening to radio channels, EPG and timers. This addon combines the
former ffmpeg and tsreader addons.


%package -n     kodi-pvr-mythtv
Summary:        Kodi frontend for MythTV
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
# mythtv-cmyth addon replaced by mythtv addon since XBMC/Kodi 14.0
Provides:       xbmc-pvr-mythtv-cmyth = %{version}-%{release}
Obsoletes:      xbmc-pvr-mythtv-cmyth < 14.0

%description -n kodi-pvr-mythtv
MythTV frontend (up to MythTV 0.28). Supports streaming of Live TV & recordings,
listening to radio channels, EPG and timers.


%package -n     kodi-pvr-nextpvr
Summary:        Kodi frontend for the NextPVR
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       bundled(md5-plumb)
Provides:       xbmc-pvr-nextpvr = %{version}-%{release}
Obsoletes:      xbmc-pvr-nextpvr < 14.0

%description -n kodi-pvr-nextpvr
NextPVR frontend for Kodi. Supports streaming of Live TV & recordings, listening
to radio channels and EPG.


%package -n     kodi-pvr-njoy
Summary:        Njoy N7 PVR Client for Kodi
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-njoy = %{version}-%{release}
Obsoletes:      xbmc-pvr-njoy < 14.0

%description -n kodi-pvr-njoy
%{summary}.


%package -n     kodi-pvr-vdr-vnsi
Summary:        PVR client to connect VDR to Kodi over the VNSI interface
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-vdr-vnsi = %{version}-%{release}
Obsoletes:      xbmc-pvr-vdr-vnsi < 14.0

%description -n kodi-pvr-vdr-vnsi
VDR frontend for Kodi; supporting streaming of Live TV & recordings, EPG, timers
over the VNSI plugin.

NOTE: this package requires the VNSI plugin (package vdr-vnsiserver on Fedora)
to be installed on the VDR backend.


%package -n     kodi-pvr-vuplus
Summary:        Kodi's frontend for VU+/Enigma2 based settop boxes
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-vuplus = %{version}-%{release}
Obsoletes:      xbmc-pvr-vuplus < 14.0

%description -n kodi-pvr-vuplus
VU+ frontend; supporting streaming of Live TV & recordings, EPG, timers.


%package -n     kodi-pvr-wmc
Summary:        Windows Media Center client for Kodi
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Provides:       xbmc-pvr-wmc = %{version}-%{release}
Obsoletes:      xbmc-pvr-wmc < 14.0

%description -n kodi-pvr-wmc
A Kodi client to interface to Windows Media Center's record and EPG service.


%prep
%setup -q -n %{alt_name}-%{commit}
# %%setup -q -n %%{alt_name}-%%{tag}
%patch0 -p0 -b .use_external_cppmyth
%patch1 -p0 -b .use_external_jsoncpp
%patch2 -p0 -b .use_external_rapidxml
%patch3 -p0 -b .use_external_tinyxml
%patch4 -p0 -b .use_external_tinyxml2
%patch5 -p0 -b .use_external_xbmc

# Delete bundled libraries jsoncpp, rapidxml, and tinyxml2
rm -r lib/{cppmyth,jsoncpp,rapidxml,tinyxml2}/
# Delete bundled tinyxml, but keep wrapper files provided by Kodi developers
rm lib/tinyxml/{readme.txt,tiny*}
# Delete bundled Kodi headers
rm -r xbmc/{*.h,xbmc_stream_utils.hpp,NOTE}

# Fix permissions
chmod 0644 addons/pvr.demo/addon/{genre-numbers.txt,README.md}


%build
[ -f configure ] || ./bootstrap
%configure \
  --enable-addons-with-dependencies \
  --libdir=%{_libdir}/kodi/addons/ \
  --datadir=%{_datadir}/kodi/addons/
make %{?_smp_mflags}


%install
%make_install

# Fix permissions at installation (see
# https://github.com/opdenkamp/xbmc-pvr-addons/pull/303)
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;


%files common
# TODO: add ChangeLog and NEWS if non-empty
%doc AUTHORS COPYING README


%files -n kodi-pvr-argustv
%doc addons/pvr.argustv/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.argustv/
%{_datadir}/kodi/addons/pvr.argustv/


%files -n kodi-pvr-demo
%doc addons/pvr.demo/addon/{genre-numbers.txt,README.md}
%{_libdir}/kodi/addons/pvr.demo/
%{_datadir}/kodi/addons/pvr.demo/


%files -n kodi-pvr-dvblink
%doc addons/pvr.dvblink/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.dvblink/
%{_datadir}/kodi/addons/pvr.dvblink/


%files -n kodi-pvr-dvbviewer
%doc addons/pvr.dvbviewer/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.dvbviewer/
%{_datadir}/kodi/addons/pvr.dvbviewer/


%files -n kodi-pvr-filmon
%doc addons/pvr.filmon/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.filmon/
%{_datadir}/kodi/addons/pvr.filmon/


%files -n kodi-pvr-hts
%doc addons/pvr.hts/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.hts/
%{_datadir}/kodi/addons/pvr.hts/


%files -n kodi-pvr-iptvsimple
%doc addons/pvr.iptvsimple/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.iptvsimple/
%{_datadir}/kodi/addons/pvr.iptvsimple/


%files -n kodi-pvr-mediaportal-tvserver
%doc addons/pvr.mediaportal.tvserver/{addon/changelog.txt,addon/LICENSE.txt,src/README}
%{_libdir}/kodi/addons/pvr.mediaportal.tvserver/
%{_datadir}/kodi/addons/pvr.mediaportal.tvserver/


%files -n kodi-pvr-mythtv
%doc addons/pvr.mythtv/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.mythtv/
%{_datadir}/kodi/addons/pvr.mythtv/


%files -n kodi-pvr-nextpvr
%doc addons/pvr.nextpvr/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.nextpvr/
%{_datadir}/kodi/addons/pvr.nextpvr/


%files -n kodi-pvr-njoy
%{_libdir}/kodi/addons/pvr.njoy/
%{_datadir}/kodi/addons/pvr.njoy/


%files -n kodi-pvr-vdr-vnsi
%{_libdir}/kodi/addons/pvr.vdr.vnsi/
%{_datadir}/kodi/addons/pvr.vdr.vnsi/


%files -n kodi-pvr-vuplus
%doc addons/pvr.vuplus/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.vuplus/
%{_datadir}/kodi/addons/pvr.vuplus/


%files -n kodi-pvr-wmc
%doc addons/pvr.wmc/addon/changelog.txt
%{_libdir}/kodi/addons/pvr.wmc/
%{_datadir}/kodi/addons/pvr.wmc/


%changelog
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 14.0-0.4.20150125gita0a437e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 14.0-0.3.20150125gita0a437e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 31 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.0-0.2.20150125gita0a437e
- Sync with Kodi 14.1
- Fix Obsoletes for kodi-pvr-mediaportal-tvserver (RFBZ #3528)

* Mon Dec 29 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 14.0-0.1.20140716git9f63d1b
- Sync with Kodi 14.0
- Rename to kodi-pvr-addons

* Wed Aug 06 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.0-2.20140716gitbe12a8d
- Sync with XBMC 13.2 beta3
- Use bundled (and heavily patched!) version of dvblinkremote library
- Use system tinyxml2 library to build dvblinkremote instead of bundled one


* Tue May 13 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.0-1
- Update to 13.0
- Drop empty M3U file provided by the iptvsimple addon
- Add upstream report links for each packaging issue in comments
- Add common subpackage for common license/documentation files
- Add missing license GPLv3
- Drop vdr-vnsiserver subpackage (now a separate project, packaged in Fedora)

* Fri May 09 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.0-0.4.Gotham_rc1
- Fix build on Fedora 21 (thanks to Ken Dreyer)
- Fix license tag
- Spec cleanup
- Add Provides for bundled implementations of MD5 and SHA1 (copylibs)

* Fri May 02 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.0-0.3.Gotham_rc1
- Sync with XBMC Gotham_rc1

* Mon Mar 24 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.0-0.2.20140314git1d9e336
- Sync with XBMC Gotham_beta2
- Drop embedded dvblinkremote and tinyxml2 libraries
- Add new dvblink and wmc subpackages

* Tue Feb 11 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 13.0-0.1.20130907git18597fd
- Initial RPM release
