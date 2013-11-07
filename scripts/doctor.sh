#!/bin/bash

#
# Doctor script to check for application status
# - Checks for outdated requirements
#

# Configuration
VIRTUALENV_NAME="virtualenv_doctor"
VIRTUALENV_CMD="virtualenv-2.7"

# Return value
RETURN=0

# Check requirements
echo "========================================================================"
echo " REQUIREMENTS"
echo "========================================================================"

echo "=> Create virtualenv ($VIRTUALENV_NAME)"
$VIRTUALENV_CMD -q .$VIRTUALENV_NAME
source .$VIRTUALENV_NAME/bin/activate

echo "=> Installing requirements"
# Only main requirements
pip install -q -r requirements.txt

echo -n "=> Checking for outdated requirements: "
RESULT=`pip list -o`

if [ "${RESULT}" != "" ]
then
    echo "outdated requirements!"
    echo $RESULT
    RETURN=1
else
    echo "up to date!"
fi

echo "=> Removing virtualenv..."
rm -rf .$VIRTUALENV_NAME

# Finished doctor scripts

echo "========================================================================"
if [ $RETURN == 0 ]; then
    echo "= FINISHED OK"
else
    echo "= FINISHED WITH ERRORS"
fi
echo "========================================================================"


exit $RETURN
