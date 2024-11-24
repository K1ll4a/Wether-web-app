from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ваш API-ключ
API_KEY = '82a7fea6bda8dfc78d32b8edf8f4f891'

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Получение данных о погоде
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'Не указано местоположение'}), 400

    try:
        # Получение текущей погоды
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY}'
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if weather_response.status_code != 200:
            return jsonify({'error': weather_data.get('message', 'Ошибка API')}), 400

        # Получение прогноза на 5 дней
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=ru&appid={API_KEY}'
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        if forecast_response.status_code != 200:
            return jsonify({'error': forecast_data.get('message', 'Ошибка API')}), 400

        # Формируем ответ
        result = {
            'current': {
                'temp': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'city': weather_data['name'],
            },
            'forecast': [
                {
                    'date': item['dt_txt'],
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description'],
                }
                for item in forecast_data['list']
            ]
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': 'Произошла ошибка на сервере'}), 500

@app.route('/details.html')
def details():
    return render_template('details.html')

if __name__ == '__main__':
    app.run(debug=True)
