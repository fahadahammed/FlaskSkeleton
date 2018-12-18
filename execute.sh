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
Flask_Cache
gunicorn
redis
requests
Flask-Limiter
setproctitle
python-dateutil
)




# Project Author
ProjectAuthor="Fahad Ahammed"
# read -p "Enter Project Author Name: " ProjectAuthor


# Project Name
if [ -z "$1" ]
then
	echo "No argument supplied";
	read -p "Enter Project Name: " projectname
	projectname=$(echo $projectname | tr -s ' ' '_')
else
  projectname=$1
fi

if [ -z "$projectname" ]
then
	exit;
fi

echo -e "Project Name: $projectname \n"

# Project Version
ProjectVersion=$(echo "$projectname_"`date +%Y-%m-%d_%H-%M-%S` | awk '{print tolower($0)}')
echo -e "Project Version: $ProjectVersion \n"


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
mkdir -p "$BaseFolder/$projectname/$projectname/templates"
mkdir -p "$BaseFolder/$projectname/$projectname/static"
mkdir -p "$BaseFolder/$projectname/Logs"
mkdir -p "$BaseFolder/$projectname/Extras"

#--------------------------
echo -e "Creating Files.\n"
touch "$BaseFolder/$projectname/requirements.txt"
touch "$BaseFolder/$projectname/gunicorn.py";
touch "$BaseFolder/$projectname/run.py"
touch "$BaseFolder/$projectname/$projectname/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Configuration/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Library/__init__.py"
touch "$BaseFolder/$projectname/$projectname/Model/__init__.py"

#-------------------------
echo -e "Adding Meta Data.\n"
find "$BaseFolder/$projectname" -type f -name "*.py" | while read f;
do
	addmeta $f;
done

#-------------Gunicorn-------------
cat Dependables/gunicorn.py >> "$BaseFolder/$projectname/gunicorn.py";
sed -i "s|{PROJECT_NAME}|$projectname|g" "$BaseFolder/$projectname/gunicorn.py";


#-------------------------
echo ${Packages[@]} | sed 's| |\n|g' | while read f;
do
  echo $f >> "$BaseFolder/$projectname/requirements.txt";
done





removejunksF
