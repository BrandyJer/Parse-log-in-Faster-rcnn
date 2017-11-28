在parse_log.sh中两行代码：

grep '] Solving ' $1 > aux3.txt
# grep 'Testing net' $1 >> aux3.txt
grep 'Train net' $1 >> aux3.txt
这两行代码都是搜索含有字符串的行然后写入aux3.txt。因为我的日志中没有] Solving，并且我的是训练日志，也没有Testing net，所以在没有添加] Solving的时候去运行脚本就报了：无法paste，rm aux4.txt的错误。实际上是因为没有任何东西写进aux3.txt，

aux3.txt是空的，所以运行$DIR/extract_seconds.py aux3.txt aux4.txt就不会生成aux4.txt。当然也就没办法paste，rm。修改的方法可以把Testing net改成Train net，这样可以在日志文件中找到行写入aux3.txt。或者在日志中添加] Solving让能有东西写进

aux3.txt。其实两种改法都可以，反正这个脚本之后要删除这些临时文件，然后再取生成.train的东西，这样改只是为了让程序不报错，能正常运行

===========================================================================================================
注释掉： 24——38行========>test net loss

修改29行为31行

增加32行（参考注释掉的30行修改）
==========================================================================================================
修改41行为 ] Solver
同时修改extract_seconds.py中38行 Solving=====>Solver
