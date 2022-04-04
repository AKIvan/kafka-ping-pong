# PING PONG KAFKA TEST

Three files are involved to run the ping pong test. 
* docker-compose.yaml - is used to download the images and run the kafaka and zookeeper as services locally. 
* produce.py - is used to simulate messages to kafka 
* consumer.py - is used to read the messages and act on the give values.
* requirements.txt - is used to install libraries for the code to run - libraries for kafka and other stuf.  

## How to run
In order to run this scenario you need to follow the procedure:

1. Create an virtual envirnment - `pipenv install --three`
2. Activate the virtual env. - `pipenv shell`
3. Install the libraries - `pip install -r requirements.txt`
4. Install docker if its not [present](https://docs.docker.com/get-docker/)
5. Run the docker compose - this will download the kafka and zookeeper images and run them with the default ports and settings. - `docker-compose -f docker-compose.yml up -d`
6. Once the images are up and ready you can start the produce.py script with the proper message - `python produce.py`
7. Open a new terminal and start the consumer - `python consume.py`


You should see the result in real time if both terminals are open and run properlly. 
