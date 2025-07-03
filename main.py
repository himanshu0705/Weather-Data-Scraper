import requests
from datetime import datetime
import os
import pycountry

class WeatherScraper:
    def __init__(self):
        self.API_KEY = "a34cdf5beb075b10cc92d93ff40f84d0"
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        self.log_file = "weather_log.txt"

    def get_weather_data(self,city):
        try:
            url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}&units=metric"
            response = requests.get(url)

            if(response.status_code == 200):
                data = response.json()

                if data.get('cod') == 200:
                    return data
                
                else:
                    print(f"Error: {data.get('message','City not found!')}")
                    return None

            else:
                print(f"HTTP Error : {response.status_code}")
                return None
        
        except requests.Timeout:
            print("Error: Request timed out. Check your internet connection!")
            return None
        
        except requests.ConnectionError:
            print("Error: Unable to connect weather service!")
            return None
        
        except requests.RequestException as e:
            print(f"Error fetching weather data {e}")
            return None
        
        except requests.JSONDecodeError:
            print("Error: Invalid response from weather service!")
            return None
        
    def get_country_name(self, country_code):
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            return country.name if country else country_code
        except:
            return country_code
    
    def display_weather_data(self, data, city):
        try:
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            sys = data['sys']

            country_name = self.get_country_name(sys.get('country', 'UNKNOWN'))

            print(f"\n {'-'*50}")
            print(f"WEATHER REPORT FOR {city.upper()}")
            print(f"\n {'-'*50}")
            print(f"Temperature : {main['temp']}°C (feels like {main['feels_like']}°C)")
            print(f"Description : {weather['description'].title()}")
            print(f"Humidity : {main['humidity']}%")
            print(f"Pressure : {main['pressure']} hPa")
            print(f"Wind Speed : {wind['speed']} m/s")
            print(f"Country : {country_name}")  # Now shows full country name
            print(f"Retrieved : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\n {'-'*50}")

            return True
        except KeyError as e:
            print(f"Error displaying weather data. Missing key {e}")
            return False
        except Exception as e:
            print(f"Error displaying weather data {e}")
            return False
        
    def save_to_log(self,data,city):
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            log_entry = f'''
--- Weather Log Entry---
Timestamp : {timestamp}
City : {city.title()}
Temperature : {data['main']['temp']}°C
Description : {data['weather'][0]['description'].title()}
Humdidty : {data['main']['humidity']}%
Pressure : {data['main']['pressure']} hPa
{"-"*100}
'''
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(log_entry)

            print(f"Weather data saved to {self.log_file}")

        except Exception as e:
            print(f"Error saving to file: {e}")

    def get_history(self):
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content:
                        entries = content.split('-' * 100)
                        valid_entries = [entry.strip() for entry in entries if entry.strip()]
                        last_3_entries = valid_entries[-3:] if len(valid_entries) >= 3 else valid_entries
                        
                        if last_3_entries:
                            print("\nLast 3 Weather Searches:\n")
                            for entry in last_3_entries:
                                print(entry)
                                print('-' * 100)
                                print()
                        
                        else:
                            print("No weather history found")
                    
                    else:
                        print("No weather history found")
            
        except Exception as e:
            print(f"Error reading weather history: {e}")

    def clear_history(self):
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
                print("Weather history cleared")
            
            else:
                print("No history file to clear")

        except Exception as e:
            print(f"Error clearing history: {e}")

    def run(self):
        print("--------|| WEATHER DATA SCRAPER ||--------")
        print("Commands:")
        print("-> Enter city name to get weather")
        print("-> 'history' to view recent searches")
        print("-> 'clear' to clear history")
        print("-> 'quit' to exit")
        while True:
            command = input("Enter city name : ").strip().lower()

            if command == 'quit':
                print('Goodbye!')
                break

            elif command == 'history':
                self.get_history()

            elif command == 'clear':
                self.clear_history()

            elif command:
                data = self.get_weather_data(command)
                self.display_weather_data(data,command)
                self.save_to_log(data,command)

            else:
                print('Enter valid command or city name!')

if __name__ == '__main__':
    scraper = WeatherScraper()
    scraper.run()