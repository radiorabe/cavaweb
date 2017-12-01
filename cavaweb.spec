Name:		cavaweb
Version:	master
Release:	1%{?dist}
Summary:	C.A.V.A. Web

Group:		Application/Utility
License:	APLG-v3
URL:		https://github.com/radiorabe/cavaweb
Source0:	https://github.com/radiorabe/cavaweb/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:	gotty-bin
Requires:	cava

BuildArch:	noarch

%description
C.A.V.A. Web SystemD configuration that exposes C.A.V.A. to the web using gotty.

%prep
%setup -q


%build


%install
install -d %{buildroot}/%{_unitdir}
install cavaweb.service %{buildroot}/%{_unitdir}/cavaweb.service
install -d %{buildroot}/%{_sharedstatedir}/%{name}/.config/cava/ 
install cava.config.example %{buildroot}/%{_sharedstatedir}/%{name}/.config/cava/config.example


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -G %{name} -d /var/lib/cavaweb/ -m \
    -c "C.A.V.A Web" %{name}
exit 0


%post
%systemd_post cavaweb.service


%preun
%systemd_preun cavaweb.service


%postun
%systemd_postun cavaweb.service


%files
%doc README.md
%attr(550, -, -) %{_unitdir}/cavaweb.service
%attr(-, root, cavaweb) %{_sharedstatedir}/%{name}/.config/cava/config.example
