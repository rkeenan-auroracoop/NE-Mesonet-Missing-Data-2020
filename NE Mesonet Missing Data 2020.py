

with open(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\NE Mesonet Missing Data 2020\ross_keenan_202007-08.csv') as f1:
    for line in f1:
        # print(line)
        listOfData = line.split(",")
        # print(listOfData)
        LOCATION = listOfData[0]
        VALID_TIME = listOfData[1]
        TEMPERATURE = listOfData[2]
        DEW_POINT = listOfData[3]
        RELATIVE_HUMIDITY = listOfData[4]
        FOUR_INCH_SOIL_TEMP = listOfData[5]
        INCOMING_SOLAR_RADIATION = listOfData[6]
        WIND_SPEED = listOfData[7]
        WIND_GUST = None
        WIND_DIRECTION = listOfData[8]
        MEAN_SEA_LEVEL_PRESSUE = listOfData[9]
        HEAT_INDEX = listOfData[10]
        WINDCHILL_TEMPERATURE = listOfData[11]
        HOURLY_PRECIPITATION = listOfData[12]
