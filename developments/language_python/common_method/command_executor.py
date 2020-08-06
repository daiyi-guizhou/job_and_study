import subprocess
import logging.config
import os
def get_logger(name=None, save_dir="log"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    conf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             "config", "logging.conf")
    logging.config.fileConfig(conf_path)
    return logging.getLogger(name)
logger = get_logger()

def exec_cmd(cmd, throw=True):
    logger.info("Prepare to execute cmd, cmd=[%s]" % cmd)
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    stdout = stdout.strip("\n")
    stderr = stderr.strip("\n")
    if p.returncode:
        if throw:
            raise ExecCmdException(cmd, p.returncode, stdout, stderr)
    return p.returncode, stdout, stderr

class ExecCmdException(Exception):
    def __init__(self, cmd, status, stdout, stderr):
        self.cmd = cmd
        self.status = status
        self.stdout = stdout
        self.stderr = stderr
    def __str__(self):
        return "execute cmd failed, cmd=[%s], status=[%s], stdout=[%s], stderr=[%s]" % (
            self.cmd, self.status, self.stdout, self.stderr)