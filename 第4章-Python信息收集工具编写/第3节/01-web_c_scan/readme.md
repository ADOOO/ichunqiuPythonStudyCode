tips:

	1、对c段内所的的地址进行扫描

		a.引入nmap模块
		b.在外部，使用nmap、zmap进行快速的扫描，将结果保存，再放入程序，进行扫描识别


nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 -oX nmap.xml

-sn 不进行端口扫描，只进行ping检测
-PE 通过ICMP echo来判定主机是否存活
--min-hostgroup 1024 最小分组设置1024个IP地址
--min-parallelism 1024 将探针的数量设置最小为1024