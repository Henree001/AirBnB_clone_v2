#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Fabric script that generates a .tgx archive"""
    n = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(n))
    except Exception:
        return None
    return 'versions/web_static_{}.tgz'.format(n)
