#!/usr/bin/python3
""" Fabric script that distribute an archive to your web servers"""

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os import path
env.hosts = ['54.157.32.137', '52.55.249.213']


def do_pack():
        """ Generate a tar archives """
        date_recent = datetime.now().strftime("%Y%m%d%H%M%S")
        path_ruth = "versions/web_static_{}.tgz".format(date_recent)
        try:
                local("mkdir -p versions")
                local("tar -czvf {} web_static".format(path_ruth))
                return path_ruth
        except:
                return None


def do_deploy(archive_path):
        try:
                if not os.path.exists(archive_path):
                        return False
                put(archive_path, "/tmp/")
                fileComp = archive_path.split("/")[1].split(".")[0]
                path = "/data/web_static/releases/{}".format(fileComp)
                tgzFile = fileComp + '.tgz'
                print(fileComp)
                print(path)
                print(tgzFile)
                
                run("mkdir -p {}".format(path))
                run("tar -xvzf /tmp/{}.tgz -C {}".format(fileComp, path))
                run("sudo rm /tmp/{}.tgz".format(fileComp))
                run("sudo rm /data/web_static/current")
                run("sudo ln -sf /data/web_static/releases/{}\
                /data/web_static/current".format(fileComp))
                run("sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(fileComp, fileComp))
                run("rm -rf /data/web_static/releases/{}/web_static".format(fileComp))
                return True
        except:
                return False
