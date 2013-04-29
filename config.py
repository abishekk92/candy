configs=open("server.config",'r').readlines()
config_set={}
for config in configs:
	config_splits=config.split('=>')
	config_set[config_splits[0]]=config_splits[1]
    
def get_hostname():
	return config_set['HOSTNAME']
def get_port():
    	return int(config_set['PORT'])

