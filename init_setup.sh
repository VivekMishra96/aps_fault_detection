echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8.15 version" 
conda create --prefix ./env python=3.8.15 -y
echo [$(date)]: "activating the environment" 
source activate ./env 
pip install -r requirements.txt
echo [$(date)]: "END"