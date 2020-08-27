"""DevJoke is a cli program that returns programming jokes randomly. (Internet required)"""

import sys
import json
import requests
import properties

class DevJoke:
    """DevJoke main class - DevJoke program starts from this class."""

    def __init__(self):
        """INIT"""

        self.joke = ""

        self.getTheJoke()

        print(self.joke)

    def getTheJoke(self):
        """This method sends GET request to API_URL defined in property.py"""

        try:

            response = requests.get(properties.API_URL).text
            data = json.loads(response)

            self.joke = data["joke"]

        except:

            print("Can't connect to the server baby!! Go and complete your project, dead-line comes soon!")
            sys.exit(1)

if __name__ == "__main__":
    app = DevJoke()
