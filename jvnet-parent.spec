%{?scl:%scl_package jvnet-parent}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}jvnet-parent
Version:        4
Release:        8.1%{?dist}
Summary:        Java.net parent POM file

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://www.java.net
Source0:        http://repo1.maven.org/maven2/net/java/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  %{?scl_prefix}jpackage-utils
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-enforcer-plugin

%description
Java.net parent POM file used by most Java.net subprojects such as
Glassfish

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# we provide correct version of maven, no need to enforce and pull in dependencies
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 4-8.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-4
- Rebuild to regenerate Maven auto-requires

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-3
- Rebuild to regenerate provides

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 gil cattaneo <puntogil@libero.it> - 4-1
- Update to version 4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 3-7
- Build with xmvn

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3-6
- Add LICENSE-2.0.txt to lookaside cache

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3-5
- Install LICENSE file
- Resolves: rhbz#878990

* Tue Jul 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3-4
- Remove enforcer-plugin from pom (not needed)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3-2
- Remove maven from requires to simplify other deps

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3-1
- Update to version 3

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1-1
- Initial version of the package
