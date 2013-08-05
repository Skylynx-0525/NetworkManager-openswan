%define nm_version        1:0.9.2

%define realversion 0.9.8.0

Summary:   NetworkManager VPN plug-in for openswan
Name:      NetworkManager-openswan
Version:   0.9.8.0
Release:   1%{?dist}
License:   GPLv2+
Group:     System Environment/Base
URL:       http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/0.9/
Source0:   http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/0.9/%{name}-%{realversion}.tar.xz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gtk3-devel
BuildRequires: dbus-devel
BuildRequires: NetworkManager-devel       >= %{nm_version}
BuildRequires: NetworkManager-glib-devel  >= %{nm_version}
%if 0%{?fedora} > 16 || 0%{?rhel} >= 7
BuildRequires: libgnome-keyring-devel
%else
BuildRequires: gnome-keyring-devel
%endif
BuildRequires: intltool gettext

Requires: NetworkManager   >= %{nm_version}
Requires: gnome-keyring

%description
This package contains software for integrating the openswan VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -q  -n NetworkManager-openswan-%{realversion}

%build
%configure --disable-static --enable-more-warnings=yes
make %{?_smp_mflags}

%install

make install DESTDIR=$RPM_BUILD_ROOT

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root,-)
%config /etc/NetworkManager/VPN/nm-openswan-service.name
%config /etc/dbus-1/system.d/nm-openswan-service.conf

%doc AUTHORS ChangeLog COPYING
%{_libdir}/NetworkManager/lib*.so*
%{_libexecdir}/nm-openswan-auth-dialog
%{_sysconfdir}/dbus-1/system.d/nm-openswan-service.conf
%{_sysconfdir}/NetworkManager/VPN/nm-openswan-service.name
%{_libexecdir}/nm-openswan-service
%{_libexecdir}/nm-openswan-service-helper
%{_datadir}/gnome-vpn-properties/openswan/nm-openswan-dialog.ui
%dir %{_datadir}/gnome-vpn-properties/openswan

%changelog
* Mon Aug 5 2013 Avesh Agarwal <avagarwa@redhat.com> - 0.9.8.0-1
- Rebase to latest upstream version 0.9.8.0
- Fixed several issues with the packaging

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.995-5.git20120302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Avesh Agarwal <avagarwa@redhat.com> - 0.9.3.995-4
Resolves: #845599, #865883

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.995-3.git20120302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Avesh Agarwal <avagarwa@redhat.com> - 0.9.3.995-2
- Ported changes from rhel to fedora

* Fri Mar  2 2012 Dan Williams <dcbw@redhat.com> - 0.9.3.995-1
- Update to 0.9.3.995 (0.9.4-beta1)
- ui: add support for external UI mode, eg GNOME Shell

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.0-2
- Rebuild for new libpng

* Fri Aug 26 2011 Dan Williams <dcbw@redhat.com> - 0.9.0-1
- Update to 0.9.0
- ui: translation fixes

* Thu Jul 21 2011 Dan Williams <dcbw@redhat.com> - 0.8.999-2.git20110721
- Update to git snapshot
- Fixes for secrets handling and saving

* Tue May 03 2011 Dan Williams <dcbw@redhat.com> - 0.8.999-1
- Update to 0.8.999 (0.9-rc2)
- Port to GTK 3.0 and GtkBuilder
- Fix some issues with secrets storage

* Sun Mar 27 2011 Christopher Aillon <caillon@redhat.com> - 0.8.0-9.20100411git
- Rebuild against NetworkManager 0.9

* Wed Feb 16 2011 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-8.20100411git
- fixes for compile time errors

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7.20100411git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 7 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-6.20100411git
- Modified import and export interfaces to import_from_file and export_to_file, respectively,
  due to changes in NMVpnPluginUiInterface struct in NM (bz 631159). 

* Mon Jul 26 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-5.20100411git
Resolves: #616910
- Support for reading phase1 and phase2 algorithms through GUI

* Tue Jul 13 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-4.20100411git
- Modified fix for the bz 607352
- Fix to read connection configuration from stdin
- Fix to read Xauth user password from stdin
- Fix to delete the secret file as soon as read by Openswan

* Thu Jul 8 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-3.20100411git
- Modified the patch so that it does not pass user password to 
  "ipsec whack" command.   

* Thu Jul 8 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-2.20100411git
- Modified to initiate VPN connections with openswan whack interface
- Fixed the issue of world readable conf and secret files 
- Cleaned conf and secret files after VPN connection is stopped
- Fixed the issue of storing sensitive information like user 
  password in a file (rhbz# 607352)
- Changed PLUTO_SERVERBANNER to PLUTO_PEER_BANNER due
  to the same change in Openswan
- Modifed GUI to remove unused configuration boxes

* Tue Jun 15 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-1.20100411git
- Initial build
