#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """A method"""
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(datetime.now()
                                               .strftime("%Y%m%d%H%M%S"))
    filename = local("tar -cvzf {} web_static".format(name))
    if filename.failed:
        return None
    return name
