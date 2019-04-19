#!/bin/bash
#
# Project FlaskSkeleton
#
# Created By: Fahad Ahammed
# Date: 2018-12-17_12-06
#
#
# This script will create the necessary folders and files with environment.
# -------------------------------------------------------------------------

echo -e "This is a Flask project initiator or generator with a predefined structure I always prefer to use.\n"

ScriptDirectory=$(pwd)


# Base Folder
BaseFolder=Projects
if [ ! -d "$BaseFolder" ]; then
  echo -e "Folder not exists.\n";
  echo -e "Creating Folder...\n";
  mkdir -p "$BaseFolder";
fi


# Packages for requirements
Packages=(
flask
passlib
sqlalchemy
mysqlclient
Flask_Caching
gunicorn
redis
requests
Flask-Limiter
setproctitle
python-dateutil
skpy
)

# SecretKey
SecretKey=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 40 ; echo '')


# Project Author
ProjectAuthor="Fahad Ahammed"
# read -p "Enter Project Author Name: " ProjectAuthor


# Project Name
if [ -z "$1" ]
then
	echo "No argument supplied";
	read -p "Enter Project Name: " projectname
	projectname=$(echo $projectname | tr -s ' ' '_' )
else
  projectname=$1
  projectname=$(echo $projectname | tr -s ' ' '_' )
fi

if [ -z "$projectname" ]
then
	exit;
fi

echo -e "Project Name: $projectname \n"
PROJECT_NAME_FOR_DB=(echo $projectname | awk '{print toupper($0)}')

# CACHE_KEY_PREFIX
CACHE_KEY_PREF=$(echo $projectname | tr '[:upper:]' '[:lower:]')
CACHE_KEY_PREFIX=$(echo '@'"$CACHE_KEY_PREF")


# Project Version
ProjectVersion=$(echo "$projectname_"`date +%Y-%m-%d_%H-%M-%S` | awk '{print tolower($0)}')
echo -e "Project Version: $ProjectVersion \n"

# Host
if [ -z "$2" ]
then
	echo "No Host specified.";
	read -p "Enter Host: " host
else
  host=$2
fi

if [ -z "$host" ]
then
	exit;
fi

# Port
if [ -z "$3" ]
then
	echo "No Port specified.";
	read -p "Enter Port: " port
else
  port=$3
fi

if [ -z "$port" ]
then
	exit;
fi



# Functions
#----------

# MetaData
function addmeta {
	echo -e "Adding Metadata.\n"
	if [ -n "$1" ]
	then
		echo -e "File $1 passed to add metadata.\n";
		file=$1;
		echo "# -----------------------------" >> $file;
		echo "#" >> $file;
                echo "# Project: $projectname" >> $file;
                echo "# Version: $ProjectVersion" >> $file;
		echo "#" >> $file;
		echo "# Date: "`date` >> $file;
                echo "# Created By: $ProjectAuthor" >> $file;
                echo "#" >> $file;
                echo "# -----------------------------" >> $file;
	else
		echo -e "No file passed.\n";
	fi
}

# remove junks
function removejunksF {
	echo -e "Removing Junks\n";

	if [ -d "$BaseFolder/$projectname" ];
	then
		rm -Rf $BaseFolder/$projectname;
	fi;

	if [ -d "$BaseFolder/$projectname/Logs" ];
        then
                rm -Rf "$BaseFolder/$projectname/Logs";
        fi;

	if [ -d "$BaseFolder/$projectname/Extras" ];
        then
                rm -Rf "$BaseFolder/$projectname/Extras";
        fi;

	if [ -f "$BaseFolder/$projectname/run.py" ];
	then
        	rm "$BaseFolder/$projectname/run.py";
	fi

}


removejunksF


# Create Folders
#--------------------------
echo -e "Creating Folders.\n"
mkdir -p "$BaseFolder/$projectname/$projectname/Configuration"
mkdir -p "$BaseFolder/$projectname/$projectname/Library"
mkdir -p "$BaseFolder/$projectname/$projectname/Model"
mkdir -p "$BaseFolder/$projectname/$projectname/Views"
mkdir -p "$BaseFolder/$projectname/$projectname/templates"
mkdir -p "$BaseFolder/$projectname/$projectname/static"
mkdir -p "$BaseFolder/$projectname/Logs"
mkdir -p "$BaseFolder/$projectname/Extras"

#--------------------------
echo -e "Creating Files.\n"
touch "$BaseFolder/$projectname/requirements.txt"
touch "$BaseFolder/$projectname/gunicorn.py"
touch "$BaseFolder/$projectname/run.py"
touch "$BaseFolder/$projectname/$projectname/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Configuration/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
touch "$BaseFolder/$projectname/$projectname/Configuration/connect.py"
touch "$BaseFolder/$projectname/$projectname/Library/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Model/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Views/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Views/home.py"


#-------------------------
echo -e "Adding Meta Data.\n"
find "$BaseFolder/$projectname" -type f -name "*.py" | while read f;
do
	addmeta $f;
done

#-------------Gunicorn-------------
cat Dependables/gunicorn.py >> "$BaseFolder/$projectname/gunicorn.py";
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/gunicorn.py";
sed -i "s|{HOST}|$host|g" "$BaseFolder/$projectname/gunicorn.py";
sed -i "s|{PORT}|$port|g" "$BaseFolder/$projectname/gunicorn.py";

#-------------Configuration-------------
cat Dependables/configuration.py >> "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
sed -i "s|{PROJECT_NAME_FOR_DB}|$PROJECT_NAME_FOR_DB|g" "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
sed -i "s|{PROJECT_NAME-RANDOM}|$SecretKey|g" "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
sed -i "s|{HOST}|$host|g" "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
sed -i "s|{PORT}|$port|g" "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"
sed -i "s|{CACHE_KEY_PREFIX}|$CACHE_KEY_PREFIX|g" "$BaseFolder/$projectname/$projectname/Configuration/configuration.py"

#--------------Connect------------------
cat Dependables/connect.py >> "$BaseFolder/$projectname/$projectname/Configuration/connect.py"
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/$projectname/Configuration/connect.py"

#------------Requirements-------------
echo ${Packages[@]} | sed 's| |\n|g' | while read f;
do
  echo $f >> "$BaseFolder/$projectname/requirements.txt";
done

#-----------RUN------------
cat Dependables/run.py >> "$BaseFolder/$projectname/run.py"
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/run.py"

#-------------INIT------------
cat Dependables/__init__.py >> "$BaseFolder/$projectname/$projectname/__init__.py"
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/$projectname/__init__.py"

#----------------------- VIEWS --------------------
cat Dependables/home.py >> "$BaseFolder/$projectname/$projectname/Views/home.py"
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/$projectname/Views/home.py"


# removejunksF



# Create Virtualizaion
#cd "$ScriptDirectory/$BaseFolder/$projectname/";
#virtualenv "$ScriptDirectory/$BaseFolder/$projectname/".virtualenvironment --python=python3
#source "$ScriptDirectory/$BaseFolder/$projectname/".virtualenvironment/bin/activate
#pip install -r "$ScriptDirectory/$BaseFolder/$projectname/"requirements.txt
#deactivate
