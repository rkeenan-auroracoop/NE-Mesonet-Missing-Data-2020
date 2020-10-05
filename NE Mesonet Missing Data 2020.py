

locationDictionary = {}

with open(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\NE Mesonet Missing Data 2020\ross_keenan_202007-08.csv') as readFile:
    with open(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\NE Mesonet Missing Data 2020\ross_keenan_202007-08(fixed).csv', 'w') as writeFile:
        writeFile.write('Name' + '\t' + 'Valid_time' + '\t' + 'Temperature' + '\t' + 'Dewpoint' + '\t' + 'Relative_Humidity' +
                        '\t' + '4inch_Soil_Temperature' + '\t' + 'Incoming_Solar_Radiation' + '\t' + 'Wind_Speed' + '\t' + 'Wind_Gust' + '\t' + 'Wind_Direction' + '\t' + 'Mean_Sea_Level_Pressure' + '\t' + 'Hourly_Precipitation' + '\t' + 'Heat_Index' + '\t' + 'Wind_Chill' + '\n')
    for line in readFile:
        listOfData = line.split(",")
        LOCATION = listOfData[0]
        VALID_TIME = listOfData[1]
        TEMPERATURE = listOfData[2]
        DEW_POINT = listOfData[3]
        RELATIVE_HUMIDITY = listOfData[4]
        FOUR_INCH_SOIL_TEMP = listOfData[5]
        INCOMING_SOLAR_RADIATION = listOfData[6]
        WIND_SPEED = listOfData[7]
        WIND_GUST = "Null"
        WIND_DIRECTION = listOfData[8]
        MEAN_SEA_LEVEL_PRESSUE = listOfData[9]
        HEAT_INDEX = listOfData[10]
        WINDCHILL_TEMPERATURE = listOfData[11]
        HOURLY_PRECIPITATION = listOfData[12]
        with open(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\NE Mesonet Missing Data 2020\ross_keenan_202007-08(fixed).csv', 'a') as writeFile:
            writeFile.write(LOCATION + '\t' + VALID_TIME + '\t' + TEMPERATURE + '\t' + DEW_POINT + '\t' + RELATIVE_HUMIDITY + '\t' + FOUR_INCH_SOIL_TEMP + '\t' + INCOMING_SOLAR_RADIATION +
                            '\t' + WIND_SPEED + '\t' + WIND_GUST + '\t' + WIND_DIRECTION + '\t' + MEAN_SEA_LEVEL_PRESSUE + '\t' + HOURLY_PRECIPITATION + '\t' + HEAT_INDEX + '\t' + WINDCHILL_TEMPERATURE + '\n')

print('Your write file is finished!')
