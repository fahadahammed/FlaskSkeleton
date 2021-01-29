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
import shutil


# Helper Functions
def progress_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print("✓ {0:<8}".format(func.__name__))
        print(" Took {0}seconds.\n".format(end - start))
        return func_return_val

    return wrapper


# Variables
ApplicationName = an = "flaskeleton"
version = 1.2
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
*.log
"""


class flaSkeletonInitiate:
    def __init__(self, projectName, hostName, port):
        self.projectName, self.hostName, self.port = projectName, hostName, port

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
            11: "pika",
            12: "pymongo",
            13: "apscheduler",
            14: "uwsgi",
            15: "jwt"
        }
        self.project_directory = self.pd = self.od + "/" + self.projectName
        self.project_inner_directory = self.pind = self.pd + "/" + self.projectName
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
                        x[1] not in ("mysqlclient", "pika", "gunicorn")]
            if pack == "mongo":
                packages = [x[1] for x in self.ap.items() if x[1] not in ("mysqlclient", "skpy")]
            if pack == "mysql":
                packages = [x[1] for x in self.ap.items() if x[1] not in ("mongo", "skpy")]
            if pack == "gunicorn":
                packages = [x[1] for x in self.ap.items() if x[1] not in ("mysqlclient", "skpy", "uwsgi")]
            if pack == "all":
                packages = [x[1] for x in self.ap.items() if x[1]]
        else:
            packages = [x[1] for x in self.ap.items() if x[1] not in ("mysqlclient", "pika", "gunicorn")]

        return packages

    @progress_wrapper
    def create_folder_structure(self):
        folders_to_create = (self.od, self.pd, self.cfgd, self.libd, self.modd, self.vied, self.statd, self.temd)

        # Folder Creation
        def create_folders(folder):
            if not os.path.exists(folder):
                os.makedirs(folder)
        for i in folders_to_create:
            create_folders(folder=i)

        return "True"

    @progress_wrapper
    def create_requirements_file(self):
        for i in self.select_package_names(pack="all"):
            self.file_writer(file_name=self.pd + "/requirements.txt", content=i+"\n", mode="append")
        return True

    @progress_wrapper
    def create_gitignore_file(self):
        self.file_writer(file_name=self.pd + "/.gitignore", content=gitignore)
        return True

    @progress_wrapper
    def create_run_files(self):
        run_files = (
            "gunicorn.py",
            "uwsgi.ini",
            "run.py"
        )
        for i in run_files:
            old_loc = "Dependables/" + i
            new_loc = self.pd + "/" + i
            with open(old_loc, 'r', encoding='utf-8') as old_f:
                for _i in old_f.readlines():
                    self.file_writer(file_name=new_loc,
                                     content=_i.replace("PROJECTNAMEFSKLTN",
                                                        self.projectName).replace("_FSKLTN_PORT",
                                                                                  str(self.port)).replace("_FSKLTN_UWSGI_STATS_PORT", str(int(self.port)+1))
                                     ,
                                     mode="append")
        return True

    @progress_wrapper
    def create_init_files(self):
        polders = (self.pind, self.cfgd, self.libd, self.modd, self.vied)
        for _f in polders:
            if _f != self.pind:
                os.mknod(_f + "/__init__.py")
            else:
                old_loc = "Dependables/" + "__init__.py"
                new_loc = _f + "/" + "__init__.py"
                with open(old_loc, 'r', encoding='utf-8') as old_f:
                    for _i in old_f.readlines():
                        self.file_writer(file_name=new_loc, content=_i.replace("PROJECTNAMEFSKLTN", self.projectName),
                                         mode="append")

        return True

    @progress_wrapper
    def create_configuration_files(self):
        if True:
            old_loc = "Dependables/" + "configuration.py"
            new_loc = self.cfgd + "/configuration.py"
            with open(old_loc, 'r', encoding='utf-8') as old_f:
                for _i in old_f.readlines():
                    self.file_writer(file_name=new_loc,
                                     content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                         "PROJECTNAMEFSKLTN", self.projectName
                                     ).replace("_FSKLTN_HOST", self.hostName).replace("_FSKLTN_PORT", str(self.port)),
                                     mode="append")
        return True

    @progress_wrapper
    def create_library_files(self):
        if True:
            old_loc = "Dependables/" + "MongoDatabaseLibrary.py"
            new_loc = self.libd + "/MongoDatabaseLibrary.py"
            with open(old_loc, 'r', encoding='utf-8') as old_f:
                for _i in old_f.readlines():
                    self.file_writer(file_name=new_loc,
                                     content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                         "PROJECTNAMEFSKLTN", self.projectName
                                     ),
                                     mode="append")

            old_loc = "Dependables/" + "MySQLDatabaseLibrary.py"
            new_loc = self.libd + "/MySQLDatabaseLibrary.py"
            with open(old_loc, 'r', encoding='utf-8') as old_f:
                for _i in old_f.readlines():
                    self.file_writer(file_name=new_loc,
                                     content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                         "PROJECTNAMEFSKLTN", self.projectName
                                     ),
                                     mode="append")

            old_loc = "Dependables/" + "TimeCalculator.py"
            new_loc = self.libd + "/TimeCalculator.py"
            with open(old_loc, 'r', encoding='utf-8') as old_f:
                for _i in old_f.readlines():
                    self.file_writer(file_name=new_loc,
                                     content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                         "PROJECTNAMEFSKLTN", self.projectName
                                     ),
                                     mode="append")
        return True

    @progress_wrapper
    def create_model_files(self):
        old_loc = "Dependables/" + "_m_Home.py"
        new_loc = self.modd + "/_m_Home.py"
        with open(old_loc, 'r', encoding='utf-8') as old_f:
            for _i in old_f.readlines():
                self.file_writer(file_name=new_loc,
                                 content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                     "PROJECTNAMEFSKLTN", self.projectName
                                 ),
                                 mode="append")
        return True

    @progress_wrapper
    def create_view_files(self):
        old_loc = "Dependables/" + "_v_Home.py"
        new_loc = self.vied + "/_v_Home.py"
        with open(old_loc, 'r', encoding='utf-8') as old_f:
            for _i in old_f.readlines():
                self.file_writer(file_name=new_loc,
                                 content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                     "PROJECTNAMEFSKLTN", self.projectName
                                 ),
                                 mode="append")
        return True

    @progress_wrapper
    def create_template_files(self):
        for i in ("Home.html", "Head.html", "Foot.html", "Navigation.html"):
            old_loc = "Dependables/" + i
            new_loc = self.temd + "/" + i
            with open(old_loc, 'r', encoding='utf-8') as old_f:
                for _i in old_f.readlines():
                    self.file_writer(file_name=new_loc,
                                     content=_i.replace("kPROJECTNAMEFSKLTN", self.projectName.upper()).replace(
                                         "PROJECTNAMEFSKLTN", self.projectName
                                     ),
                                     mode="append")
        return True

    def initiate_project_creation(self):
        self.create_folder_structure()
        self.create_init_files()
        self.create_requirements_file()
        self.create_gitignore_file()
        self.create_run_files()
        self.create_configuration_files()
        self.create_library_files()
        self.create_model_files()
        self.create_view_files()
        self.create_template_files()
        return True


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
    parser_init.add_argument('--projectName', '--pn', nargs=1, help="Name of the project", required=True)
    parser_init.add_argument('--hostName', '--hn', nargs=1, help="Project Hostname")
    parser_init.add_argument('--port', '--pt', nargs=1, help="Project Port")
    parser_init.set_defaults(parser="init")

    # Arguments
    args = parser.parse_args()
    try:
        # Check
        if args.parser == "init":

            if args.projectName:
                projectName = str(args.projectName[0])
            elif args.pn:
                projectName = str(args.pn[0])
            else:
                exit()

            if args.hostName:
                hostName = str(args.hostName[0])
            elif args.hn:
                hostName = str(args.hn[0])
            else:
                hostName = "127.0.0.1"

            if args.port:
                port = str(args.port[0])
            elif args.pt:
                port = str(args.pt[0])
            else:
                port = int(random.randrange(21000, 21999))

            return flaSkeletonInitiate(projectName=projectName,
                                       hostName=hostName, port=port).initiate_project_creation()

        else:
            pass
    except AttributeError as e:
        parser.print_usage()


if __name__ == "__main__":
    execute()
