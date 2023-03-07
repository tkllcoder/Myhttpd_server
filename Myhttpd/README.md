### 运行注意

我的项目运行环境：Linux-CentOS7, gcc, perl-cgi.

（1）需要本机安装perl，同时安装perl-cgi，sudo yum install perl-CGI.

（2）需要修改htdocs文件夹下的.cgi代码首行路径为本机perl所在路径。在Linux终端可用指令which perl查看本机perl的路径。

（3）index.html必须没有执行权限，否则看不到内容，并且会产生Program received signal SIGPIPE, Broken pipe，因为程序中如果有可执行权限会当cgi脚本处理。所以假如html有执行权限先把它去除了，chmod 600 index.html ，此外，color.cgi必须要有执行权限。

详细说明请访问：https://blog.csdn.net/TL_mood/article/details/129375233

