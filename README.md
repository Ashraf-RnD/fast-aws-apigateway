# Environment Setup -- classic

Creating virtual environment :
```
conda create --name pyenv
```

Activate the virtual environment :

```
conda activate pyenv
conda config --append channels conda-forge
conda install --file requirements.txt
conda install -n pyenv uvicorn

```

Run the docker-compose : `docker-compose up -d` <br>
Start the web server :
```
uvicorn main:app --host localhost --port 9501
or just run dev.sh
```
Deactivate the virtual environment : `deactivate` <br>
List all running localstack services : `localstack status services`

# Environment Setup -- Docker containerization

run ```sh deploy.sh```

Swagger docs : http://localhost:9501/docs

