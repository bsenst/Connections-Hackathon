# Connections-Hackathon
Submission to the Streamlit Connections Hackathon to demonstrate the experimental streamlit connector to connect the streamlit app to the Milvus vector database. The adapted connector can be found in the `connection.py` script.

For the time of the Hackathon the app connected to the database backend can be reached at https://connections-hackathon-ltar9bp4kpm2hssniappyvr.streamlit.app/

![image_showing_streamlit_cloud_app_medium_semantic_search](https://github.com/bsenst/Connections-Hackathon/assets/8211411/932af0fc-2ad1-4141-ae64-6dda163b3874)

# Local Deployment
Follow these steps to deploy the app locally.

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
streamlit run local_app.py
```

![image_showing_streamlit_running_milvus_queries](https://github.com/bsenst/Connections-Hackathon/assets/8211411/9ad40426-26b3-44c9-b996-83710234afb3)

## 3. Clean up

Stop the streamlit app by pressing `Ctrl-C`.

Stop the docker container and remove the database data:

```bash
sudo docker-compose down
sudo rm -rf  volumes
```
