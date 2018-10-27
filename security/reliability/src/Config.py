import json
import numpy as np

class ConfigReader:
    data = {}

    def __init__(self, path):
        try:
            with open(path, 'r') as f:
                self.data = json.load(f)

            for rate in self.data['denial_rates']:
                rate *= np.power(10.0, -8)

            self.data['beta'] *= 10

            self.data['time'] *= np.power(10, 4) 

            self.data['storing']['time'] *= np.power(10, 4)

            self.data['storing']['fail_rate_drop_factor'] * np.power(10, 2)

            self.data['cyclic_work']['time'] *= np.power(10, 4)

            self.data['dt'] *= np.power(10, 3)

        except OSError:
            print('Cannot open file')


if __name__ != '__main__':
    cfg = ConfigReader('../resource/config.json')