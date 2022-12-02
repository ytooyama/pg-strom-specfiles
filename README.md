# PG-Strom-specfiles

## 使い方

[PG-Strom](https://github.com/heterodb/pg-strom) のrpmパッケージ作るためのspecファイルを置いています。
公式からソースのzipファイルをダウンロードしてそれぞれ配置して、rpmbuildコマンドを実行してsrpmやrpmパッケージを作ってください。RHEL 8.6で確認済み。

specファイルは必要に応じて編集してください。

```bash
# dnf install rpmdevtools
# rpmdev-setuptree
# tree ~/rpmbuild/
/root/rpmbuild/
|-- BUILD
|-- RPMS
|-- SOURCES
|-- SPECS
`-- SRPMS
... (Copy and Edit the files)
# tree SPECS SOURCES
SPECS
`-- pg_strom-PG13.spec
SOURCES
|-- pg-strom-3.4.zip
`-- systemd-pg_strom.conf

# rpmbuild -ba pg_strom-PG13.spec 
...
# tree SRPMS/ RPMS/
SRPMS/
`-- pg_strom-PG13-3.4-b1.el8.src.rpm
RPMS/
`-- x86_64
    |-- pg_strom-PG13-3.4-b1.el8.x86_64.rpm
    |-- pg_strom-PG13-debuginfo-3.4-b1.el8.x86_64.rpm
    `-- pg_strom-PG13-debugsource-3.4-b1.el8.x86_64.rpm

1 directory, 4 files

# dnf install ./pg_strom-PG13-3.4-b1.el8.x86_64.rpm 
```
