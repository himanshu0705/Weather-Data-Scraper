# Weather Data Scraper 🌤️

A simple yet polished full‑stack project that serves **real‑time weather information** for any city worldwide using the [OpenWeatherMap API](https://openweathermap.org/api), a Flask REST backend, and a responsive vanilla‑HTML + CSS + JS frontend.

<p align="center">
  <img src="docs/demo.gif" alt="Weather Data Scraper demo" width="700"/>
</p>

---

## ✨ Features

* **Instant weather lookup** – current temperature, humidity, pressure, wind, and sky conditions.
* **Country name resolution** – converts ISO country codes to full names via *pycountry*.
* **Search history** with the 10 most recent queries and one‑click purge.
* **Server‑side logging** to `weather_log.txt` for auditing/debugging.
* **Graceful error handling** for missing city names, network issues, and API failures.
* **Responsive UI** – mobile‑first layout that scales cleanly up to desktop (\~1200 px max‑width).
* Deployed in a single lightweight Flask application (`app.py`).

---

## 🗂️ Project Structure

```
weather-data-scraper/
├─ app.py            # Flask application & API routes
├─ main.py           # WeatherScraper class (API calls, logging, helpers)
├─ requirements.txt  # Python package list
├─ templates/
│   └─ index.html    # Front‑end (HTML + CSS + JS)
├─ weather_log.txt   # Auto‑generated log file (ignored in .gitignore)
└─ README.md         # You are here 🌍
```

---

## 🚀 Quick Start

### 1 . Clone & Create Env

```bash
# Clone
$ git clone https://github.com/<himanshu0705>/Weather-Data-Scraper.git
$ cd Weather-Data-Scraper

# Create & activate virtual env (Windows cmd)
> python -m venv venv
> venv\Scripts\activate

# … or (Uni*x/macOS)
$ python -m venv venv
$ source venv/bin/activate
```

### 2 . Install Dependencies

```bash
(venv)$ pip install -r requirements.txt
```

> **requirements.txt**
>
> ```
> Flask
> requests
> pycountry
> ```

### 3 . Add Your OpenWeatherMap API Key

1. Sign up at [https://openweathermap.org/api](https://openweathermap.org/api) and grab a **Free API Key**.
2. Edit `main.py` and replace `#Enter your api key here` with your key :

### 4 . Run Locally

```bash
(venv)$ python app.py
```

Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser – you’re live! 🔥

---

## 🙏 Acknowledgements

* [OpenWeatherMap](https://openweathermap.org/) for the API.
* [Font Awesome](https://fontawesome.com/) for icons.
* The awesome open‑source community ❤️


