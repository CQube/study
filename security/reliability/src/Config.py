import json


class ConfigReader:
	data = {}

	def __init__(self, path):
		try:
			with open(path, 'r') as f:
				self.data = json.load(f)

		except OSError:
			print("Cannot open file")


if __name__ != "__main__":
	cfg = ConfigReader('../resource/config.json')