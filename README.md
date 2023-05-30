Theme 1: Weather Forecasting Tool (Python)

Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

create env varible using python or refer this doc https://phoenixnap.com/kb/windows-set-environment-variable

        os.environ["OPENWEATHER_KEY"] = "<your open wheather api key>"

To check the env variable :

        import os

        print("The key-value pairs of all environment variables:")
        for key in os.environ:
            print(key, '=>', os.environ[key])


command to run the code :

        **python .\main.py**
