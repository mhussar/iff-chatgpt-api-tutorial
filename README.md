# iff-chatgpt-api-tutorial
Basic set up in python for ChatGPT API

06/30/23


Python Installation:
https://www.python.org/downloads/

Popular Python Package Manager/Environment manager:
https://www.anaconda.com/
https://conda.io/en/latest/miniconda.html -- prefer

IDE:
https://code.visualstudio.com/

Source control:
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


-install conda (package/environment manager to keep versions and dependencies separated)
-create new project folder
-open new folder in explorer
-type cmd in address bar + enter
-conda create -n apitut python=3.11.3 
-conda activate my-conda-env   
-conda install openai 
-conda install -c conda-forge python-dotenv
-open vs code and open the tutorial folder
-control + shift + P, Python:Select interpreter, search for conda environment you created to set VS code project to that env

 



-------------------------------------------------------------------------------------------------------
conda env list			             # list all virtual env
conda deactivate		             # deactivate virtual env
conda remove --name ENV_NAME --all   # delete virtual env
conda create -n my-conda-env         # creates new virtual env
conda activate my-conda-env          # activate environment in terminal
conda install jupyter                # install jupyter + notebook
jupyter notebook                     # start server + kernel inside my-conda-env





