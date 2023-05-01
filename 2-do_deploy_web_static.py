#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import local, env, put, run
import os
env.hosts = ['100.26.151.162', '54.86.155.217']


def do_deploy(archive_path):
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
        run('sudo ln -s {} /data/web_static/current'.format(folder_path))
    except Exception:
        return False
    return True
