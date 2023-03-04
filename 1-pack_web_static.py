#!/usr/bin/python3
"""
Fabric script that generates  a tar archive from the contents
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generate a tar archives
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
