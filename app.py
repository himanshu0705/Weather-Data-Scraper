from flask import Flask, render_template, request, jsonify
from main import WeatherScraper
import json

app = Flask(__name__)
scraper = WeatherScraper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    try:
        city = request.json.get('city')
        if not city:
            return jsonify({'error': 'City name is required'}), 400
        
        weather_data = scraper.get_weather_data(city)
        
        if weather_data:
            formatted_data = {
                'city': city.title(),
                'temperature': weather_data['main']['temp'],
                'feels_like': weather_data['main']['feels_like'],
                'description': weather_data['weather'][0]['description'].title(),
                'humidity': weather_data['main']['humidity'],
                'pressure': weather_data['main']['pressure'],
                'wind_speed': weather_data['wind']['speed'],
                'country': scraper.get_country_name(weather_data['sys'].get('country', 'UNKNOWN')),
                'icon': weather_data['weather'][0]['icon']
            }
            
            scraper.save_to_log(weather_data, city)
            
            return jsonify({'success': True, 'data': formatted_data})
        else:
            return jsonify({'error': 'Weather data not found for this city'}), 404
            
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/history')
def get_history():
    try:
        import os
        history_data = []
        
        if os.path.exists(scraper.log_file):
            with open(scraper.log_file, 'r', encoding='utf-8') as file:
                content = file.read()
                if content:
                    entries = content.split('-' * 100)
                    valid_entries = [entry.strip() for entry in entries if entry.strip()]
                    last_10_entries = valid_entries[-10:] if len(valid_entries) >= 10 else valid_entries
                    
                    for entry in reversed(last_10_entries):  
                        if entry:
                            history_data.append(entry)
        
        return jsonify({'history': history_data})
        
    except Exception as e:
        return jsonify({'error': f'Error reading history: {str(e)}'}), 500

@app.route('/clear-history', methods=['POST'])
def clear_history():
    try:
        scraper.clear_history()
        return jsonify({'success': True, 'message': 'History cleared successfully'})
    except Exception as e:
        return jsonify({'error': f'Error clearing history: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)