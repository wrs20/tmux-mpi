import sys
import socket
import subprocess
import os
import errno
import pty
import shutil


def get_ssh_fingerprints(work_dir):
    hostname = socket.gethostname()
    fingerprint_file = os.path.join(work_dir, "fingerprint")
    try:
        fh = os.open(fingerprint_file, os.O_CREAT | os.O_EXCL)
        os.close(fh)
        with open(fingerprint_file, "bw+") as fh:
            stdout = subprocess.check_output(("ssh-keyscan", hostname), stderr=subprocess.DEVNULL)
            fh.write(stdout)
    except FileExistsError:
        return


def setup_work_dirs(work_dir):
    try:
        os.makedirs(work_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise RuntimeError("Error creating work directory.")

    work_dir_host = os.path.join(work_dir, socket.gethostname())
    try:
        os.makedirs(work_dir_host)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise RuntimeError("Error creating work directory.")

    return work_dir_host


def fork(work_dir_host):

    pid = os.fork()
    if pid == 0:
        # child
        cmd = ["dtach", "-N", dtach_socket] + sys.argv[1:]
        os.execv(shutil.which("dtach"), cmd)

    else:
        # parent
        print(os.getpid(), pid)


if __name__ == "__main__":

    work_dir = os.path.join(os.getcwd(), "tmux_mpi_remote")
    work_dir_host = setup_work_dirs(work_dir)
    get_ssh_fingerprints(work_dir_host)

    pid = os.getpid()
    print(pid)
    print(sys.argv)

    dtach_socket = os.path.join(work_dir_host, "dtach.socket.{}".format(pid))
    print(dtach_socket)
    fork(dtach_socket)
