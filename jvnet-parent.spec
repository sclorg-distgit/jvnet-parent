%global pkg_name jvnet-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        4
Release:        2.11%{?dist}
Summary:        Java.net parent POM file

License:        ASL 2.0
URL:            http://www.java.net
Source0:        http://repo1.maven.org/maven2/net/java/%{pkg_name}/%{version}/%{pkg_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-enforcer-plugin


%description
Java.net parent POM file used by most Java.net subprojects such as
Glassfish

%prep
%setup -c -T
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# we provide correct version of maven, no need to enforce and pull in dependencies
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 4-2.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 4-2.10
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 4-2.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 4-2.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 4-2.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-2.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-2.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-2.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-2.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-2.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-2.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4-2
- Mass rebuild 2013-12-27

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
