# iff-chatgpt-api-tutorial
Basic set up in python for ChatGPT API

06/30/23


Python Installation:<br>
https://www.python.org/downloads/

Popular Python Package Manager/Environment manager:<br>
https://www.anaconda.com/<br>
https://conda.io/en/latest/miniconda.html -- prefer

IDE:<br>
https://code.visualstudio.com/

Source control:<br>
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git<br>


-----------------------------------SET UP-----------------------------------------------------<br>
-install conda (package/environment manager to keep versions and dependencies separated) <br>
-create new project folder<br>
-open new folder in explorer<br>
-type cmd in address bar + enter<br>
-conda create -n apitut python=3.11.3 <br>
-conda activate my-conda-env   <br>
-conda install openai <br>
-conda install -c conda-forge python-dotenv<br>
-open vs code and open the tutorial folder<br>
-control + shift + P, Python:Select interpreter, search for conda environment you created to set VS code project to that env<br>

 



-----------------------------------CHEAT SHEET-----------------------------------------------------<br>
conda env list			                    # list all virtual env<br>
conda deactivate		                   # deactivate virtual env<br>
conda remove --name ENV_NAME --all   # delete virtual env<br>
conda create -n my-conda-env         # creates new virtual env<br>
conda activate my-conda-env          # activate environment in terminal<br>
conda install jupyter                # install jupyter + notebook<br>
jupyter notebook                     # start server + kernel inside my-conda-env<br>





