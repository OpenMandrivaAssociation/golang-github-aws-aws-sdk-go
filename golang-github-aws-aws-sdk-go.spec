# https://github.com/aws/aws-sdk-go
%global goipath         github.com/aws/aws-sdk-go
Version:                1.15.62

%gometa

Name:           golang-github-aws-aws-sdk-go
Release:        1%{?dist}
Summary:        AWS SDK for the Go programming language
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/go-ini/ini)
BuildRequires: golang(github.com/gucumber/gucumber)
BuildRequires: golang(github.com/jmespath/go-jmespath)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/tools/go/loader)
BuildRequires: golang(github.com/go-sql-driver/mysql)
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%install
%goinstall aws/credentials/example.ini glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.62-1
- Update to release 1.15.62

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.4.22-0.10.20170628git50762c1
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-0.9.git50762c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.4.22-0.8.git50762c1
- Upload handcrafted glide.lock and glide.yaml files
- Update to spec 3.0

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.4.22-0.7.20170628git50762c1
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-0.6.git50762c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.4.22-0.5.git50762c1
- Bump to upstream 50762c1efc55dd2a05eac85fc170b0f65aeec28f
  related: #1274280

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-0.4.git6c577e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-0.3.git6c577e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-0.2.git6c577e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.4.22-0.1.git6c577e9
- Bump to upstream 6c577e9e7b08a6d10bad1c9703227cd0403a8dd7
  resolves: #1274280

* Thu Sep 15 2016 Matthias Runge <mrunge@redhat.com> - 1.4.9-1
- update to 1.4.9 (rhbz#1297679)

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- https://fedoraproject.org/wiki/Changes/golang1.7

* Wed Apr 20 2016 jchaloup <jchaloup@redhat.com> - 1.1.3-1
- Bump to v1.1.3
  related: #1269806

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 jchaloup <jchaloup@redhat.com> - 0.9.5-1
- Bump to upstream f096b7d61df3d7d6d97f0e701f92616d1ea5420d
  related: #1269806

* Thu Oct 22 2015 jchaloup <jchaloup@redhat.com> - 0.9.4-1.rc5.1
- Bump to upstream 5c0313fff8cd85670ae4fc996254dd7d66cb4cf7
  related: #1269806

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0.6.1-1
- First package for Fedora
  resolves: #1269806
