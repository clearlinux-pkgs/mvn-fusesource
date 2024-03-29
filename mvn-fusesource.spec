#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-fusesource
Version  : 1.17.1
Release  : 3
URL      : https://github.com/fusesource/jansi/archive/jansi-project-1.17.1.tar.gz
Source0  : https://github.com/fusesource/jansi/archive/jansi-project-1.17.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi-project/1.12/jansi-project-1.12.pom
Source2  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.12/jansi-1.12.jar
Source3  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.12/jansi-1.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-fusesource-data = %{version}-%{release}

%description
# [![Jansi][logo]][Jansi]
[logo]: http://fusesource.github.io/jansi/images/project-logo.png "Jansi"

%package data
Summary: data components for the mvn-fusesource package.
Group: Data

%description data
data components for the mvn-fusesource package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.12
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.12/jansi-project-1.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.12
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.12/jansi-1.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.12
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.12/jansi-1.12.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.12/jansi-project-1.12.pom
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.12/jansi-1.12.jar
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.12/jansi-1.12.pom
