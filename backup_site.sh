#!/bin/bash

echo "This script will create a mysqldump of a single database and an archive of a single website's filesystem.  Please follow the prompts."

#Global Stuff

date=$(date +"%d-%b-%Y")
read -p 'Backup Location (no traling slash): ' backup_location

#Get DB Info

read -p 'Database Name: ' db_name

read -p 'Database Host: ' host

read -p 'Database User: ' user

read -p 'Database Password: ' password

#MySQL Dump

mysqldump --user=$user --password=$password --host=$host $db_name > $backup_location/$db_name-$date.sql

#Get Web Directory Info

read -p 'Site Name (arbitrary filename for backup): ' site_name
read -p 'Path to web root: ' web_root

#Archive File System

tar -czvf $backup_location/$site_name-$date.tar.gz $web_root

echo "db backup and webroot tar.gz can be found at $backup_location. Please confirm successful backup before making changes to the database or filesystem"
