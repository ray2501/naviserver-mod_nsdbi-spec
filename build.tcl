#!/usr/bin/tclsh

set arch "x86_64"
set base "naviserver-mod_nsdbi-0.4"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsdbi.spec]
exec >@stdout 2>@stderr {*}$buildit

