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

ProjectAuthor="Fahad Ahammed"



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


ProjectVersion=$(echo "$projectname_"`date +%Y-%m-%d_%H-%M-%S` | awk '{print tolower($0)}')


echo -e "Project Name: $projectname \n"


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


function removejunksF {
	echo -e "Removing Junks\n";

	if [ -d "$projectname" ];
	then
		rm -Rf $projectname;
	fi;

	if [ -d "Logs" ];
        then
                rm -Rf Logs;
        fi;

	if [ -d "Extras" ];
        then
                rm -Rf Extras;
        fi;

	if [ -f "run.py" ];
	then
        	rm run.py;
	fi

}


removejunksF


#--------------------------
echo -e "Creating Folders.\n"
mkdir -p $projectname/Configuration
mkdir -p $projectname/Library
mkdir -p $projectname/Model
mkdir -p $projectname/templates
mkdir -p $projectname/static
mkdir -p Logs
mkdir -p Extras

#--------------------------
echo -e "Creating Files.\n"
touch run.py
touch $projectname/__init__.py
touch $projectname/Configuration/__init__.py
touch $projectname/Library/__init__.py
touch $projectname/Model/__init__.py

#-------------------------
echo -e "Adding Meta Data.\n"
find ./ -type f -name "*.py" | while read f;
do
	addmeta $f;
done




removejunksF
