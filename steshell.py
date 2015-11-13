import subprocess

#   Example:
#
#   import steshell as ss
#
#   # get command output (stdout and stderr) as list of strings
#   out, err = ss.sh('ls -l *.txt')
#   out, err = ss.bash('ls -l *.txt')
#
#   # print output (stdout and stderr) during execution
#   ss.ish('grep -rin asd /')
#   ss.ibash('grep -rin asd /')


# cmd: sh command string
def sh(cmd, logger = None):
    sh_cmd = []
    sh_cmd.append('sh')
    sh_cmd.append('-c')
    sh_cmd.append(cmd)
    return cmda(sh_cmd, logger)

# cmd: sh command string
def ish(cmd, logger = None):
    sh_cmd = []
    sh_cmd.append('sh')
    sh_cmd.append('-c')
    sh_cmd.append(cmd)
    return icmda(sh_cmd, logger)

# cmd: bash command string
def bash(cmd, logger = None):
    sh_cmd = []
    sh_cmd.append('bash')
    sh_cmd.append('-c')
    sh_cmd.append(cmd)
    return cmda(sh_cmd, logger)

# cmd: bash command string
def ibash(cmd, logger = None):
    sh_cmd = []
    sh_cmd.append('bash')
    sh_cmd.append('-c')
    sh_cmd.append(cmd)
    return icmda(sh_cmd, logger)



######################### utilities #########################

# cmd_a: array of commands
# return stdout and stderr as list of lines
def cmda(cmd_a, logger = None):
    if logger != None:
        logger.getChild('steshell.icmda').info(cmd_a)

    process = subprocess.Popen(cmd_a, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = process.communicate()
    shout = ret[0].decode()
    sherr = ret[1].decode()

    if logger != None:
        logger.getChild('steshell.cmda').info("out: " + shout)
        logger.getChild('steshell.cmda').info("out: " + sherr)

    return shout.splitlines(), sherr.splitlines()

# cmd_a: array of commands
# interactive cmd (print output -stdout and stderr- during execution)
def icmda(cmd_a, logger = None):
    if logger != None:
        logger.getChild('steshell.cmda').info(cmd_a)

    process = subprocess.Popen(cmd_a, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout:
        print(line.decode(), end='')

    return

