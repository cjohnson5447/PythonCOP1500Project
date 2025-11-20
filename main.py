from weather_api import get_weather
from weather_api import forecast
from weather_api import astronomical
from weather_api import weather_location
from datetime import datetime

#current time in hours and minutes using the 12-hour clock format
current_time = datetime.now().strftime("%I:%M %p")

#loop to enter the preferred city and check that it is correct
while True:
#get location for weather data
    city = input("Please enter your city's zip code: ")
    weather = get_weather(city)
    forecasted = forecast(city)
    sunrise_set = astronomical(city)

#define variables for location
    city_name = weather["location"]["name"]
    region_name = weather["location"]["region"]

    location_obj = weather_location(city_name, region_name)

    print("The city you entered is: ", location_obj.full_location())
    confirm = input("Is this correct? (yes/no): ")
    if confirm == "yes":
        break
    else:
        print("No problem. Try again.")

#loop to see if the user wants to check the current and/or forecast weather data
while True:
    what_weather = input("Do you want to see the 'current' weather or today's 'forecast'? Type 'exit' to exit: " )
    if what_weather == "current":
        print("The current temperature is: ", weather["current"]["temp_f"], "degrees Fahrenheit.")
        print("The current humidity is: ", weather["current"]["humidity"], "%")
        print("The current conditions are: ", weather["current"]["cloud"], "% cloud cover,", weather["current"]["precip_in"], "inches of rain.")

    elif what_weather == "forecast":
        print("Today's high will be: ", forecasted["forecast"]["forecastday"][0]["day"]["maxtemp_f"], "degrees Fahrenheit.")
        print("Today's low will be: ", forecasted["forecast"]["forecastday"][0]["day"]["mintemp_f"], "degrees Fahrenheit.")
        print("The chance of rain is: ", forecasted["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"], "%.")
        print("The time of sunrise is: ", sunrise_set["astronomy"]["astro"]["sunrise"])
        print("The time of sunset is: ", sunrise_set["astronomy"]["astro"]["sunset"])
    elif what_weather == "exit":
        ride = input("Are you going to ride your horse today? (yes/no): ")
        if ride == "yes":
            # the user said they will ride their horse
            # conditions are safe for riding your horse...
            # if sum of temp and humidity is less than 130, it is safe to ride
            # if sum is between 130-150, reduce workload and monitor horse health
            # if sum is above 150, it is risky, do light work only
            # if sum is greater than 180, do not ride

            def ride_today():
                temperature = weather["current"]["temp_f"]
                humidity = weather["current"]["humidity"]
                sunrise = sunrise_set["astronomy"]["astro"]["sunrise"]
                sunset = sunrise_set["astronomy"]["astro"]["sunset"]
                print("The heat index is the sum of the current temperature and the current humidity. \n"
                      "The current heat index is: ", temperature + humidity)

                if temperature + humidity < 130:
                    print("The heat index is below 130, and is safe for your horse to do normal work during your ride. \n"
                          "Have a great ride!")
                elif temperature + humidity > 130 < 150:
                    print("The heat index is moderate, but below 150, so monitor your horse's sweat and breathing during your ride. \n"
                          "Take plenty of breaks.")
                elif temperature + humidity > 150 < 180:
                    print("The heat index is below 180, do minimal work as it may be difficult for your horse. \n"
                          "Enjoy your ride, and don't forget to cool out at the end!")
                elif temperature + humidity > 180:
                    print("The heat index is above 180, which is too high for your horse's health to be doing any work. \n"
                          "Go chill inside!")

                #determine if the arena lights are currently on or off
                print("The current time is: ", current_time)
                if current_time > sunset:
                    print("The arena lights are on. They turned on at: ", sunset)
                elif current_time < sunrise:
                    print("The arena lights are off. They turned off at: ", sunrise)

                return "Thanks for checking in!"

            print(ride_today())

        elif ride == "no":
            print("No more questions! The program will end.")
        break
    else:
        print("Invalid option. Please type 'current', 'forecast', or 'exit'.")
print("Program has ended.")

