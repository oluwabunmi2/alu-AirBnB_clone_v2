#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os import path
from io import StringIO
env.hosts = ['54.157.32.137', '52.55.249.213']


def do_pack():
    """
    function to pack in .tgz
    """
    local("mkdir -p versions")
    now = datetime.today()
    try:
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                         now.day, now.hour,
                                                         now.minute,
                                                         now.second)
        local("tar -cvzf versions/{} web_static".format(file_name))
        return (file_name)
    except:
        return (None)


def do_deploy(archive_path):
    """
    logic to deploy into ssh servers
    """
    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        directory_path = archive_path.split(".")[0]
        directory_path = directory_path.split("/")[-1]
        archive_path = archive_path.split("/")[-1]
        sudo("mkdir -p /data/web_static/releases/{}/".format(directory_path))
        full_path = "/data/web_static/releases/{}".format(directory_path)
        sudo("tar -xvzf /tmp/{} -C {}".format(archive_path, full_path))
        sudo("rm -rf /tmp/{}".format(archive_path))
        sudo("mv -f {}/web_static/* {}".format(full_path, full_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf {} /data/web_static/current".format(full_path))
        return(True)
    except:
        return(False)


def deploy():
    """
    automatizate creation and deploy
    """
    file_name = do_pack()
    if (not file_name):
        return False
    worked = do_deploy("versions/{}".format(file_name))
    return worked


def do_clean(number=0):
    """
    Cleans old versions from folder
    """
    fh = StringIO()
    my_names = []
    number = int(number)
    if (number == 0):
        number = 1
    revl = "ls -ltr versions | rev | cut -d ' ' -f1 | rev"
    value = local(revl, capture=True)
    for line in value.splitlines():
        my_names.append(line)
    my_names.pop(0)
    for i in range(len(my_names) - number):
        local("rm -rf versions/{}".format(my_names[i]))
    # For remote server
    code = "ls -ltr /data/web_static/releases | rev | cut -d ' ' -f1 | rev"
    fk_value = sudo(code, stdout=fh)
    fh.seek(0)
    my_fk_names = []
    for line in fh.readlines():
        data = line.split()[-1]
        if data.startswith("web_static"):
            my_fk_names.append(data)
    for i in range(len(my_fk_names) - number):
        sudo("rm -rf /data/web_static/releases/{}".format(my_fk_names[i]))
