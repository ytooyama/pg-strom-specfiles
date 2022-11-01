Name: mysql2arrow
Version: 3.4
Release: b1%{?dist}
Summary: MySQL query results to Apache Arrow conversion tool
Group: Applications/Databases
License: PostgreSQL
URL: https://github.com/heterodb/pg-strom
Source0: pg-strom-master.zip
BuildRequires: mysql-devel
Requires: mysql-libs
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mysql2arrow is a command line tool to dump MySQL query results
as Apache Arrow file.
This package is built from master (commit:cf0a106) of the Git repo.

%prep
%setup -q -n pg-strom-master

%build
%{__make} -C arrow-tools DESTDIR=%{buildroot} PREFIX=/usr mysql2arrow

%install
rm -rf %{buildroot}
%{__make} -C arrow-tools DESTDIR=%{buildroot} PREFIX=/usr install-mysql2arrow

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/mysql2arrow

%changelog
* Tue Nov 1 2022 Tooyama Youhei <ytooyama@users.noreply.github.com> - 3.4b1
- test relase

* Sun Nov 28 2021 KaiGai Kohei <kaigai@heterodb.com> - 3.2-2
- Rebuild for CUDA11.5 Update 1; contains compiler optimization bugfix
- Various bug fixes

* Sun Nov 14 2021 KaiGai Kohei <kaigai@heterodb.com> - 3.3-1
- Support of heterodb-extra API version 20211018
- Allows multiple optimal GPUs
- GpuPreAgg: fix optimizer error if ORDER BY is used together.
- Various bug fixes

* Tue Oct  5 2021 KaiGai Kohei <kaigai@heterodb.com> - 3.2-1
- GpuPreAgg: reduction logic reworked (local+global hybrid hash)
- GpuPreAgg: add hyper-log-log cardinarity estimation with hll_count(X)
- Add information views for CUDA programs/shared memory chunks
- Add truncate handler for PG14
- Various bug fixes

* Sat Aug 21 2021 KaiGai Kohei <kaigai@heterodb.com> - 3.1-1
- Arrow_Fdw supports min/max statistics as like BRIN index
- GpuCache: BEFORE TRUNCATE trigger is not needed on PG13
- GpuCache: add corruption state if failed on redo-log-apply
- Now PG-Strom can be built standalong (w/o heterodb-extra)
- various bug fixes

* Wed Jun 30 2021 KaiGai Kohei <kaigai@heterodb.com> - 3.0-2
- Built for CUDA11.4

* Tue Jun 29 2021 KaiGai Kohei <kaigai@heterodb.com> - 3.0-1
- several PostGIS functions are added for GPU execution
- GiST-index support was added for GpuJoin
- GpuCache was added for small data workloads
- experimental support of NVIDIA GPUDirect Storage
- support of custom GPU types/functions with 3rd party modules
- pg2arrow/arrow_fdw support wider Arrow files than PG limit
- pcap2arrow was added to capture network packets as Arrow files
- experimental support of 8bit-integer type (int1)
- add support of Ampere GPUs (A100) and CUDA11.3
- add support of PostgreSQL 13.x, drop support of PostgreSQL 10.x
- add support of ScaleFlux CSD drives as source of GPUDirect SQL
- error reports in GPU kernels were more human readable
- ...and miscellaneous improvement and fix various bugs

* Tue Mar 24 2020 KaiGai Kohei <kaigai@heterodb.com> - 2.3-1
- GpuJoin supports parallel execution on inner hash/heap table.
- Partition-wise GpuJoin was refactored for better query plan.
- Arrow_Fdw now supports INSERT/TRUNCATE commands.
- mysql2arrow was added, for collaboration with MySQL database.
- CuPy_Strom enables to share data frame between DB and Python.
- PL/CUDA was deprecated, CuPy + CuPy_Strom can do same jobs.
- Gstore_Fdw was deprecated, Arrow_Fdw is successor

* Wed Dec 25 2019 KaiGai Kohei <kaigai@heterodb.com> - 2.2-2
- support of RHEL8/CentOS8
- pg2arrow supports the latest Arrow 0.15 format; upcoming 1.0
- add support of ANALYZE on arrow_fdw
- PostgreSQL v9.6 is dropped from the supported list.

* Thu Sep  5 2019 KaiGai Kohei <kaigai@heterodb.com> - 2.2-1
- fixes of various bugs
- support of Apache Arrow columnar store (Arrow_Fdw)
- pg2arrow utility command is added
- support of JSONB data type
- pre-built GPU binary for quick code compilation/optimization
- support of nvme_strom v2; enables to handle cached disk pages
- asymmetric partition-wise JOIN support

* Wed Feb 20 2019 KaiGai Kohei <kaigai@heterodb.com> - 2.1-1
- hotfixes for various bugs
- Device Numeric is now based on 128bit
- Various groundwork to support Apache Arrow in the next version

* Thu Dec 27 2018 KaiGai Kohei <kaigai@heterodb.com> - 2.0-181227
- hotfixes for various bugs
- Add PostgreSQL 11 support
- columnar cache was removed
- Gstore_Fdw can be used for source relation of SELECT, with GpuSort
- add partitioning and multi-GPUs support
- PL/CUDA design revised

* Thu Jul 12 2018 KaiGai Kohei <kaigai@heterodb.com> - 2.0-180712
- hotfixes for various bugs
- add BRIN index support

* Thu Jun  7 2018 KaiGai Kohei <kaigai@heterodb.com> - 2.0-180607
- hotfixes for various bugs
- add partition-wise GpuJoin/GpuPreAgg (experimental)

* Tue May 15 2018 KaiGai Kohei <kaigai@heterodb.com> - 2.0-180515
- hotfixes for various bugs

* Mon Apr 30 2018 KaiGai Kohei <kaigai@heterodb.com> - 2.0-180430
- hotfixes for reported bugs
- CUDA C code builder is re-designed as background worker, instead of
  the worker thread of GpuContext.

* Tue Apr 17 2018 KaiGai Kohei <kaigai@heterodb.com> - 2.0-1
- PG-Strom v2.0 release

* Sat Jan 20 2018 KaiGai Kohei <kaigai@heterodb.com> - 1.9-180120
- initial RPM specfile
