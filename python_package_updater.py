"""Simple python script to update all installed packages"""

# Import packages needed for the updater
import pkg_resources
from subprocess import call

# Identify and update all installed packages 
packages = [package.project_name for package in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)