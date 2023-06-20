# OpenBCI UltraCortex

### VIRTUAL ENVIRONMENT SET UP PROCEDURES

1. Install Python latest version

2. Open terminal or command prompt and change directory to the project folder.

$ cd project_folder_path

Here project folder name is src

3. Create a virtual environment in the folder and activate it.

3.1. On MacOS or Linux based distributions:
$ python3 -m venv myvenv
$ source myvenv/bin/activate

3.2. On Windows

$ python -m venv myvenv
$ myvenv\Scripts\activate

4. The following command will install the packages according to the configuration file requirements.txt present in the project folder.

$ pip install -r requirements.txt
