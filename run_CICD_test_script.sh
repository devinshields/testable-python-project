#!/bin/bash
#
# source: 
#        http://www.alexconrad.org/2011/10/jenkins-and-python.html?m=1
#
# target:
#       this script ends up as a build step inside a Jenkins Job definition.
#
# NOTE: when deployed via Jenkins, the server provides build scripts with
#       path information in the form of a $WORKSPACE variable.
#
# NOTE: this testing suite is built assuming that there's a setup.py
#       in your project's top level dir.
#


# PARAMETER - primary module from the python project under testing
NAME_OF_PROJECT_CODE_MODULE='amazmodule'


# when $WORKSPACE isn't defined, use the local directory - it means I'm testing locally.
WORKSPACE=${WORKSPACE-.}


# virtualenv 
VENV_HOME=$WORKSPACE/venv/


# Delete previously built virtualenv
if [ -d $VENV_HOME ]; then
    rm -rf $VENV_HOME
fi


# create virtualenv and install necessary packages
virtualenv $VENV_HOME
source $VENV_HOME/bin/activate


# install some packages
pip install --quiet nosexcover
pip install --quiet pylint


# install project-code as a module:
#
#       "$WORKSPACE/setup.py" is you repo's installer module
#
pip install --quiet $WORKSPACE/  # where your setup.py lives


# limit unit testing to project-code only:
#       https://nose.readthedocs.org/en/latest/usage.html?highlight=cover-package#cmdoption--cover-package
#
nosetests --with-xcoverage --with-xunit --cover-package=$NAME_OF_PROJECT_CODE_MODULE --cover-erase


# export unit testing and code quality results to an output file
pylint -f parseable $NAME_OF_PROJECT_CODE_MODULE/ | tee pylint.out



