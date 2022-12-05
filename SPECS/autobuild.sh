#!/bin/bash

#rpmbuild -ba pg_strom-PG12.spec --noclean
#rpmbuild -ba pg_strom-PG13.spec --noclean
#rpmbuild -ba pg_strom-PG14.spec --noclean
rpmbuild -ba pg_strom-PG15.spec --noclean

rpmbuild -ba pg2arrow.spec --noclean
rpmbuild -ba mysql2arrow.spec --noclean

# Build the pcap2arrow-rpm, Need Enable the codeready-builder, remi and ntop repos.
# See the article: https://packages.ntop.org/centos/
#rpmbuild -ba pcap2arrow.spec --noclean

zip -r pgstrom-arch.zip RPMS SOURCES SPECS SRPMS
