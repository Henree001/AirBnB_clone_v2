#!/usr/bin/python3
"""A module for web application deployment with Fabric."""

from fabric.api import run, env, put, local
import os
from datetime import datetime

env.hosts = ['100.26.151.162', '54.86.155.217']


def do_pack():
    """Fabric script that generates a .tgx archive"""
    n = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(n))
    except Exception:
        return None
    return 'versions/web_static_{}'.format(n)


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if os.path.exists(archive_path) is False:
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace('.tgz', "")
    folder_path = '/data/web_static/releases/{}/'.format(folder_name)
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}".format(folder_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, folder_path))
        run('sudo rm -rf /tmp/{}'.format(file_name))
        run('sudo mv -f {}web_static/* {}'.format(folder_path, folder_path))
        run("sudo rm -rf {}web_static".format(folder_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {} /data/web_static/current'.format(folder_path))
    except Exception:
        return False
    return True


def deploy():
    """creates and distributes an archive to your web servers"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
