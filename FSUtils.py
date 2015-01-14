import ConfigParser
def readConfiguration(configFile):
	settings = {}
	config = ConfigParser.ConfigParser()
	config.read(configFile)
	for section in config.sections():
		settings[section] = {}
		for option in config.options(section):
			settings[section][option] = config.get(section, option)
	return settings
