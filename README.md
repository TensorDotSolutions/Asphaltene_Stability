# Asphaltene_Stability

The Asphaltene Stability testing on various combinations of Resin and Asphaltene rations (in percnts).
The output is either 'Stable' or 'Unstable'
There are range bounds given at the streamlit frontend of the application.

**A**
1. Create your project folder (e.g. 'test' using 'mkdir test' command)

2. clone repo here ('git clone https://github.com/TJDLML/Asphaltene_Stability.git')
*it is assumed git is installed on the system*
The cloned repo will appear in folder 'Asphaltene_Stability'.
you need to change to this folder.

3. Create an environment (e.g., 'conda create -n test python==3.10', and then 'conda activate test')
You need to install dependencies given in requirements.txt.
from within the environment, 'pip install -r requirements.txt'

**B**
The application would run from Python (tested on ver 3.10) as:
>> streamlit run stability_stapp.py
(The application would open in web browser)
