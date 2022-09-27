from flask import Flask , render_template , request
import requests

app = Flask('weather')





@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('loc')
        print(data)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={data}&appid=0f13613ef5315e070812a4138e41920d'
        api_data = requests.get(url)
        python_dict = api_data.json()

        atmosphere = python_dict['weather'][0]['description']

        wind = python_dict['wind']['speed']

        pressure = python_dict['main']['pressure']

        temperature = python_dict['main']['temp']

        humidity = python_dict['main']['humidity']

        country = python_dict['sys']['country']

        return render_template('index.html', data = data, atmosphere = atmosphere, wind = wind, pressure = pressure, temperature = temperature, humidity = humidity, country = country)
    else :
        return render_template('index.html')




app.run()