Name:  proton-bridge
Version: 3.21.2
Release: 2%{dist}
Summary: Proton Mail Bridge application

License: GPL-3
URL: https://github.com/ProtonMail/proton-bridge
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz
Source10: ./proton-bridge

BuildRequires: golang
BuildRequires: gcc
BuildRequires: make
BuildRequires: libsecret-devel

Requires: gnutls
Requires: libffi
Requires: glib2
Requires: pcre2
Requires: libunistring
Requires: libsecret
Requires: libtasn1
Requires: libidn2
Requires: p11-kit
Requires: libblkid
Requires: libmount
Requires: zlib-ng-compat

Recommends: gnome-keyring

%description
Proton Mail Bridge for e-mail clients.

%prep
%autosetup


%build
%make_build build-nogui build-launcher


%install
%{__mkdir_p} %{buildroot}%{_libexecdir}/%{name}
%{__install} -s -m 0755 -t %{buildroot}%{_libexecdir}/%{name}/ bridge
%{__install} -m 0755 -D %{SOURCE10} %{buildroot}%{_bindir}/%{name}

%check


%files
%{_bindir}/proton-bridge
%{_libexecdir}/%{name}/bridge
%license LICENSE
%doc Changelog.md


%changelog
* Sun Nov 09 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 3.21.2-2
- Modify package dependencies

* Sun Nov 09 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 3.21.2-1
- Initial packaging for proton-bridge
