# pysteutils
python utilities

* steshell.py
  * execute shell command in python scripts
  * example:
  ```
    from pysteutils.steshell import SteShell
    ss = SteShell()
    
    # get command output (stdout and stderr) as list of strings
    out, err = ss.sh('ls -l *.txt')
    out, err = ss.bash('ls -l *.txt')
    
    # print output (stdout and stderr) during execution
    ss.ish('grep -rin asd /')
    ss.ibash('grep -rin asd /')
```
* stelogger.py
  * create simple application logger (on file)
