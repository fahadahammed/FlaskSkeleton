#!/usr/bin/python3
# Date: 2020-01-29_15-59-49
# Project: Flask Skeleton
# Description: Flask Project Initiator
# Creator: Fahad Ahammed
# Github: https://github.com/fahadahammed/FlaskSkeleton
# ------------------------------------------------------

import sys
import os
import datetime
import functools
import time
import logging
import argparse
import subprocess
import random


# Helper Functions
def print_and_log(message):
    logging.info(message)
    print(message)


def timeit_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Alternatively, you can use time.process_time()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        timeit_message = 'Time Took: {0:<10}.{1:<8} : {2:<8} Seconds'.format(func.__module__, func.__name__,
                                                                             end - start)
        print_and_log(message=timeit_message)
        return func_return_val

    return wrapper


def progress_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_return_val = func(*args, **kwargs)
        print("✓ {0:<8}".format(func.__name__))
        return func_return_val

    return wrapper


# Variables
ApplicationName = an = "flaskeleton"
version = 1.1
Description = f"""{an} version: {version} contains some interesting changes."""
release_notes = f"""{Description}\n
1. Initiated.\n
"""
my_dt = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))


# Junk Variables
gitignore = """
*.pyc
*.csv
.idea
.idea/*
.idea/workspace.xml
.virtualenvironment
.virtualenvironment/
.virtualenvironment/*
.venv
.venv/
.venv/*
.virtualenvironments
.virtualenvironments/
.virtualenvironments/*
.env
.env/
.env/*
__pycache__
__pycache__/
__pycache__*
.vscode
.vscode/
.vscode/*
logs.log
"""


class flaSkeletonInitiate:
    def __init__(self, projectName, packages, hostName, port):
        self.projectName, self.packages, self.hostName, self.port = projectName, packages, hostName, port

        # Clean Clutter
        self.projectName = projectName.strip().replace(' ', '')

        self.output_directory = self.od = "_Output"
        self.ap = {
            1: "flask",
            2: "passlib",
            3: "mysqlclient",
            4: "Flask_Caching",
            5: "Flask-Limiter",
            6: "gunicorn",
            7: "requests",
            8: "redis",
            9: "setproctitle",
            10: "python-dateutil",
            11: "skpy",
            12: "pika",
            13: "pymongo",
            14: "apscheduler",
            16: "uwsgi"
        }
        self.project_directory = self.pd = self.od + "/" + self.projectName
        self.config_directory = self.cfgd = self.pd + "/" + self.projectName + "/Configuration"
        self.library_directory = self.libd = self.pd + "/" + self.projectName + "/Library"
        self.model_directory = self.modd = self.pd + "/" + self.projectName + "/Model"
        self.views_directory = self.vied = self.pd + "/" + self.projectName + "/Views"
        self.static_directory = self.statd = self.pd + "/" + self.projectName + "/static"
        self.templates_directory = self.temd = self.pd + "/" + self.projectName + "/templates"

    def file_writer(self, file_name, content, mode="writer"):
        if mode == "writer":
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
        if mode == "append":
            with open(file_name, 'a+', encoding='utf-8') as f:
                f.write(content)

        return f"{file_name} is written with content !"

    def select_package_names(self, pack=None):
        if pack:
            packages = [x[1] for x in self.ap.items() if
                        x[1] not in ("mysqlclient", "skpy", "pika", "gunicorn")]
            if pack == "mongo":
                packages = [x[1] for x in self.ap.items() if x[1] not in ("mysqlclient", "skpy")]
            if pack == "mysql":
                packages = [x[1] for x in self.ap.items() if x[1] not in ("mongo", "skpy")]
            if pack == "gunicorn":
                packages = [x[1] for x in self.ap.items() if x[1] not in ("mysqlclient", "skpy", "uwsgi")]
        else:
            packages = [x[1] for x in self.ap.items() if x[1] not in ("mysqlclient", "skpy", "pika", "gunicorn")]

        return packages

    @progress_wrapper
    def create_folder_structure(self):
        folders_to_create = (self.od, self.pd, self.cfgd, self.libd, self.modd, self.vied, self.statd, self.temd)

        # Folder Creation
        def create_folders(folder):
            if not os.path.exists(folder):
                os.makedirs(folder)

        for _f in folders_to_create:
            create_folders(_f)
            if _f not in (self.od, self.pd, self.statd, self.temd):
                os.mknod(_f + "/__init__.py")
        return "True"

    @progress_wrapper
    def create_requirements_file(self):
        for i in self.select_package_names(pack=self.packages):
            self.file_writer(file_name=self.pd + "/requirements.txt", content=i+"\n", mode="append")
        return True

    @progress_wrapper
    def create_gitignore_file(self):
        self.file_writer(file_name=self.pd + "/.gitignore", content=gitignore)
        return True

    @progress_wrapper
    def create_run_files(self):


    def initiate_project_creation(self):
        self.create_folder_structure()
        self.create_requirements_file()
        self.create_gitignore_file()
        self.create_run_files()
        return self.projectName, self.packages, self.hostName, self.port


def execute():
    parser = argparse.ArgumentParser(
        description=Description,
        epilog=f"""{release_notes}"""
    )

    # Global
    parser.add_argument('-v', '-V', '--version', action='version', version='%(prog)s {version}'.format(version=version))

    # Create Subparser
    subparsers = parser.add_subparsers()

    # create the parser for the 'init' command
    parser_init = subparsers.add_parser(name="init")
    parser_init.add_argument('--projectName', nargs=1, help="Name of the project", required=True)
    parser_init.add_argument('--hostName', nargs=1, help="Project Hostname")
    parser_init.add_argument('--port', nargs=1, help="Project Port")
    parser_init.add_argument('--packages', nargs=1, help="What Packages?")
    parser_init.set_defaults(parser="init")

    # Arguments
    args = parser.parse_args()
    try:
        # Check
        if args.parser == "init":
            projectName = str(args.projectName[0])

            if args.hostName:
                hostName = str(args.hostName[0])
            else:
                hostName = "127.0.0.1"

            if args.port:
                port = str(args.port[0])
            else:
                port = int(random.randrange(21000, 21999))

            if args.packages:
                packages = str(args.packages[0])
            else:
                packages = None

            return flaSkeletonInitiate(projectName=projectName, packages=packages,
                                       hostName=hostName, port=port).initiate_project_creation()

        else:
            pass
    except AttributeError as e:
        parser.print_usage()


if __name__ == "__main__":
    execute()
