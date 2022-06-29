from pprint import pprint

readdata = open("pod.yaml", "r")

pprint(readdata.read())

readdata.close()