Name:           oologinctl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Inspects user sessions, seats, and systemd-logind properties.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oologinctl
Source0:        oologinctl-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oologinctl is a sovereign, capability-bounded SESSION MANAGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oologinctl
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oologinctl-uninstall

%files
/usr/bin/oologinctl
/usr/bin/oologinctl-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
