# Connections-Hackathon
Submission to the Streamlit Connections Hackathon to demonstrate the experimental streamlit connector to connect the streamlit app to the Milvus vector database. The adapted connector can be found in the `connection.py` script.

## 1. Set up Milvus Vector Database
Milvus is an open-source vector database under Apache-2 License.

https://milvus.io/docs/install_standalone-docker.md

Run the Milvus vector database docker container:

```bash
wget https://github.com/milvus-io/milvus/releases/download/v2.2.12/milvus-standalone-docker-compose.yml -O docker-compose.yml
sudo docker-compose up -d
sudo docker-compose ps
```

https://milvus.io/docs/example_code.md

Run the `hello_milvus.py` script and populate the database with dummy vector data:

```bash
python hello_milvus.py
```

## 2. Run the Streamlit Example

Create a virtual environment and install the requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Make sure streamlit you have a streamlit secrets file `secrets.toml` for optional secret variables if run locally.

Run the example streamlit app:

```bash
streamlit run streamlit_app.py
```

## 3. Clean up

Stop the streamlit app by pressing `Ctrl-C`.

Stop the docker container and remove the database data:

```bash
sudo docker-compose down
sudo rm -rf  volumes
```