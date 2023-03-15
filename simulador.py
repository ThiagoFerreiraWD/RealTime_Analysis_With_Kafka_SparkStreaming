import re
import sys
import random
import string
import datetime
from random import randrange
   
# Definition of default message number, if not explicitly specified.
num_msgs = int(sys.argv[1]) if len(sys.argv) > 1 else 10

# Creation of the dictionary with initial data.
dic_temp_sensores = {f'sensor{sensor:02d}': round(random.uniform(10, 90), 1) for sensor in range(1, 51)}

# Base ID for each sensor.
id_base_sensor = "Sensor-1503-"

# Base ID for each equipment.
id_base_equipamento = "Equipament-0323XH-"

# Sensor reading standard format.
padrao_leitura = "iot:leitura:sensor:temp"

# Uppercase alphabet letter list.
letras = string.ascii_uppercase

# String with the format of each sensor reading.
header_leitura_iot = '{ "id_sensor": "%s",  "id_equipamento": "%s",  "sensor": "%s", '
header_leitura_iot = '{ "id_sensor": "%s",  "id_equipamento": "%s",  "sensor": "%s", '
iotmsg_data_evento = '"data_evento": "%sZ", '
iotmsg_formato = '"padrao": {"formato": "%s", '
iotmsg_dado = '"leitura": { "temperatura": %.1f  }}}'

# Mapping dictionary from id to sensor.
dic_map_sensor_id = dict()

# Dictionary to record the most recent temperature measured by each sensor.
dic_temperatura_atual = dict()

# Generates the output file in JSON format.
if __name__ == '__main__':
	
	for counter in range(0, num_msgs):

		# Generates a combination of 3 random numbers.
		rand_num = str(random.randrange(0, 9)) + str(random.randrange(0, 9)) + str(random.randrange(0, 9))

		# Generates a combination of 2 random letters.
		rand_letter = random.choice(letras) + random.choice(letras)

		# Generates a random value for temperature following a uniform distribution.
		rand_valor_temperatura = random.uniform(-10, 5)

		# Generates one more random value for temperature following a uniform distribution.
		rand_valor_temperatura_delta = random.uniform(-1, 1)

		# The sensor id receives the base value plus the previously generated random values.
		id_sensor = id_base_sensor + rand_num + rand_letter 

		# The equipment id receives the base value plus the previously generated random values.
		id_equipamento = id_base_equipamento + rand_num + rand_letter 

		# Randomly selects a sensor from the sensors dictionary.
		sensor = random.choice(list(dic_temp_sensores.keys())) 

		# If the base sensor is not yet associated with a sensor from the dictionary, we make the association.
		if (not id_sensor in dic_map_sensor_id): 			
			dic_map_sensor_id[id_sensor] = sensor 
			dic_temperatura_atual[id_sensor] = dic_temp_sensores[sensor] + rand_valor_temperatura
			
		# If the sensor is not in the final list of sensors, then we include it.
		elif (not dic_map_sensor_id[id_sensor] == sensor):		
			sensor = dic_map_sensor_id[id_sensor]

		# Randomizes the temperature even more..
		temperatura = dic_temperatura_atual[id_sensor] + rand_valor_temperatura_delta
		dic_temperatura_atual[id_sensor] = temperatura

		# Formats the current date of script execution to use as the event date.
		today = datetime.datetime.today() 
		data_evento = today.isoformat()

		# Prints the result using regular expressions to generate the file in JSON format.
		print(re.sub(r"[\s+]", "", header_leitura_iot) % (id_sensor, id_equipamento, sensor),
				re.sub(r"[\s+]", "", iotmsg_data_evento) % (data_evento),
				re.sub(r"[\s+]", "", iotmsg_formato) % (padrao_leitura),
				re.sub(r"[\s+]", "", iotmsg_dado) % (temperatura))