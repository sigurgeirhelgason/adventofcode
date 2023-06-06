import os
import sys

# Get the path to the root folder of the project
root_path = os.path.dirname(os.path.abspath(__file__))

# Add the root folder to the Python path
sys.path.append(root_path)

# Import any modules that are needed by multiple scripts
import src.calander.utils as utils