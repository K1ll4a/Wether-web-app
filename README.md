Here’s the `README.md` for your project, written in English with badges and professional formatting:

---

# 🌦️ **Weather Forecast**

![Flask](https://img.shields.io/badge/Flask-v2.0-blue) 
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenWeather](https://img.shields.io/badge/API-OpenWeather-orange)

A web application built with Flask to fetch weather forecasts using the OpenWeather API. It allows users to check current weather, a 5-day forecast, and detailed information about a selected day.

---

## 🚀 **Features**
- 🌍 **Current Weather**: Get real-time temperature and weather conditions.
- 📅 **5-Day Forecast**: View concise weather summaries for the upcoming 5 days.
- 🔍 **Detailed View**: Access a dedicated page with in-depth details for a specific day, including temperature, wind speed, and humidity.
- 🎨 **Modern Design**: Responsive interface with a minimalistic style and smooth animations.

---

## 🛠️ **Technologies**
- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) — A lightweight Python framework for web development.
  - [OpenWeather API](https://openweathermap.org/api) — For retrieving weather data.
- **Frontend**:
  - HTML5, CSS3, JavaScript.
- **Deployment**:
  - Compatible with platforms like Render, Railway, Deta, and more.

---

## 📦 **Installation and Setup**

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. **Install Dependencies**
Ensure Python 3.8 or higher is installed. Install the dependencies using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. **Configure the API Key**
- Sign up at [OpenWeather](https://openweathermap.org/api) to get an API key.
- Add the API key to the `app.py` file:
  ```python
  API_KEY = 'your_openweather_api_key'
  ```

### 4. **Run the Application**
```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🌐 **Deploying the Application**
### Deploying on [Render](https://render.com):
1. Create a new repository on GitHub and push your project there.
2. Log in to Render and create a new Web Service.
3. Specify the launch command:
   ```bash
   gunicorn app:app
   ```
4. Once deployed, Render will provide you with a URL for your application.

---

## 📋 **Usage Examples**

### Main Page:
- Enter the name of a city to get the current weather and a 5-day forecast.

![Main Page](screenshots/main_page.png)

### Detailed Forecast:
- Click on a specific day to view detailed information, such as temperature, wind speed, and humidity.

![Detailed Forecast](screenshots/details_page.png)

---

## 🛠️ **Planned Improvements**
- ✅ Add geolocation support for automatic city detection.
- ✅ Develop a fully mobile-friendly interface.
- ✅ Improve error handling (e.g., incorrect city names).

---

## 🤝 **Contributing**
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 📜 **License**
This project is licensed under the [MIT License](LICENSE).

---

