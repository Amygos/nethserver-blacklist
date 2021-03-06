Summary: NethServer blacklist
Name: nethserver-blacklist
Version: 1.0.6
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
# Build Source1 by executing prep-sources
Source1: %{name}-ui.tar.gz

BuildArch: noarch

Requires: git
Requires: nethserver-firewall-base

BuildRequires: nethserver-devtools

%description
Blacklist module for NethServer.


%prep
%setup -q

%build
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
tar xf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} --file /etc/sudoers.d/50_nsapi_nethserver_blacklist 'attr(0440,root,root)' > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist


%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
/usr/libexec/nethserver/api/%{name}/

%changelog
* Mon Jun 15 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1
- Firewall: Prevent object deletion if used in Threat Shield whitelist - Bug NethServer/dev#6196

* Fri May 29 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.5-1
- Threat Shield: weird analysis page layout after update - Bug NethServer/dev#6188

* Fri May 22 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1
- UI enhancements on Threat Shield - NethServer/dev#6171

* Tue Apr 28 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1
- Threat Shield: cannot sort by category status - NethServer/dev#6140

* Thu Apr 09 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Threat shield: check IP address by clicking on recent logs entries - NethServer/dev#6123

* Wed Apr 01 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Blacklist: systemd logs ignoring a conf - Bug NethServer/dev#6104

* Tue Mar 24 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Blacklist support (threat shield) - NethServer/dev#6072

