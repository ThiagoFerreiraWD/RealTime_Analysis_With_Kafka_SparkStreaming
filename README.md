# <p align=center>Real-Time Analysis with Apache Kafka and Spark Streaming</p>

For the present project, we need to perform a real-time analysis of the temperature of several equipment available in a specific company. Each equipment has an identification code and generates logs at regular intervals with some information, including the temperature at which it is operating through sensors.

The idea is to perform a real-time analysis of these logs (which are generated in txt format) and identify the equipment that presents an elevated average temperature, since the equipment that exceeds a certain temperature for a long time may have its useful life reduced, generating additional maintenance costs or even the need for equipment replacement.

The Operations Department wishes to have a real-time data analysis solution that calculates the average temperature of each equipment from the data emitted by IoT sensors. Once these devices are identified, we must notify the responsible department via email so that the necessary actions can be taken.

*Note: Project developed and improved based on the Big Data Real Time & Analytics course from Data Science Academy.*

# <p align=center>Data Pipeline Architecture</p>
<p align="center">
  <img src="https://github.com/ThiagoFerreiraWD/RealTime_Analysis_With_Kafka_SparkStreaming/blob/main/architecture.jpg?raw=true">
</p>

***


## Tools and languages used:
<div>
<img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachekafka/apachekafka-original.svg" />
<img width=40 src="https://spark.apache.org/images/spark-logo-trademark.png" />
<img width=40 src="https://cdn.iconscout.com/icon/free/png-512/powershell-3628993-3030218.png?f=avif&w=256" />
<img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" />
<img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
</div>

## Description of the files:

1. **ApacheKafka_SparkStreaming.ipynb:** Notebook containing the code for creating the dataframe, reading the Kafka streaming topic, and sending an email to the responsible department;
1. **architecture.jpg:** Designed architecture;
1. **dados_sensores.txt:** Data generated in batch by the generator_streaming.bat file;
1. **email_notification.jpg:** Demonstrative image of the notification email sent from the notebook's output.
1. **generator_streaming.bat:** Streaming generator, executes the simulator.py program, generating 10000 lines in the output to the txt file;
1. **simulador.py:** Program responsible for randomizing the output of the sensors; and
1. **steps.jpg:** Image containing the steps of Kafka bootstrapping and streaming consumption.


## Contacts:
<div>   
  <a href="https://www.linkedin.com/in/tferreirasilva/">
    <img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" />
  </a> 
  <a href = "mailto:thiago.ferreirawd@gmail.com">
      <img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" />
  </a>  
  <a href = "https://www.facebook.com/thiago.ferreira.50746">
    <img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/facebook/facebook-original.svg" />
  </a> 
  <a href = "https://github.com/ThiagoFerreiraWD">
    <img width=40 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />
  </a>     
</div>
