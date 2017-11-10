import urllib.request
import urllib, json
import sqlite3
import datetime 

class homeSafe:

    def __init__(self):
        self.origin = "Merchandise+Mart+Chicago"
        self.destination = "Wicker+Park+Chicago"

    def reroute(self):
        o = input("Where do you want to start? ")
        d = input("Where do you want to go? ")
        self.origin = o.replace(" ", "+")
        self.destination = d.replace(" ", "+")
  
    def driving(self):
        count = 0
        url = ("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=driving" % (self.origin,self.destination))
        return(self.main(url,"Driving"))
                
    def transit(self):
        url = ("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=tranist" % (self.origin,self.destination))
        return(self.main(url,"Transit"))

    def rideshare(self):
        url = ("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=driving" % (self.origin,self.destination))
        return(self.main(url,"Rideshare"))

    def walking(self):
        url = ("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=walking" % (self.origin,self.destination))
        return(self.main(url,"Walking"))
    
    def biking (self):
        url = ("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=biking" % (self.origin,self.destination))
        return(self.main(url,"Biking"))

    def all (self):
        allModes = []
        allModes.append(("driving", self.driving()))
        allModes.append(("transit", self.transit()))
        allModes.append(("rideshare", self.rideshare()))
        allModes.append(("walking", self.walking()))
        allModes.append(("biking", self.biking()))
        return (allModes)
    
    def safetyMetric (self,count,mode):
        month = datetime.date.today().month
        hour = datetime.datetime.time(datetime.datetime.now()).hour
        seasonMultCar = 0
        seasonMultWalk = 0
        timeMult = 0
        modeMult = 0
        safety = 100
        if (month in [11,12,1,2,3]):
            seasonMultCar = 20
            seasonMultWalk = 80
        else:
            seasonMultCar = 90
            seasonMultWalk = 70
        if (hour in [18,19,20,21,22,23,0,1,2,3,4,5,6]):
            timeMult = 20
        else:
            timeMult = 90
        if (mode == "Driving"):
            modeMult = 70
            multiplier = (timeMult + seasonMultCar + modeMult) / 3
            if (count == 0):
                return ((multiplier / 100) * 5)
            else:
                safetyScore = count
                safetyScore = safetyScore * multiplier
            
        elif (mode == "Walking"):
            modeMult = 60
            multiplier = (timeMult + seasonMultWalk + modeMult) / 3
            if (count == 0):
                return ((multiplier / 100) * 5)
            else:
                safetyScore = count
                safetyScore = safetyScore * multiplier

        elif (mode == "Biking"):
            modeMult = 40
            multiplier = (timeMult + seasonMultWalk + modeMult) / 3
            if (count == 0):
                return ((multiplier / 100) * 5)
            else:
                safetyScore = count
                safetyScore = safetyScore * multiplier
            
        elif (mode == "Transit"):
            modeMult = 90
            multiplier = (timeMult + seasonMultCar + 5 + modeMult) / 3
            if (count == 0):
                return ((multiplier / 100) * 5)
            else:
                safetyScore = count
                safetyScore = safetyScore * multiplier
            
        elif (mode == "Rideshare"):
            modeMult = 80
            multiplier = (timeMult + seasonMultCar + modeMult) / 3
            if (count == 0):
                return ((multiplier / 100) * 5)
            else:
                safetyScore = count
                safetyScore = safetyScore * multiplier

        safetyScore = (safetyScore/100) * 5

        return(safetyScore)
    
    def main(self,xurl,tmode):
        if (tmode == "Biking"):
            mode = "CrimeWalking"
        else:
            mode = "Crime"+tmode
        url = xurl
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        latlng = []
            
        for i in data["routes"][0]["legs"][0]["steps"]:
            latlng.append((i["start_location"]["lat"],i["start_location"]["lng"]))
            try:
                for j in i["steps"]:
                    latlng.append((j["start_location"]["lat"],j["start_location"]["lng"]))
            except:
                continue

        tmp = []
        for i in latlng:
          if i not in tmp:
            tmp.append(i)
        latlng = tmp

        lat = []
        lng = []
        for i in latlng:
            lat.append(i[0])
            lng.append(i[1])

        conn = sqlite3.connect('homeSafeDB.db')
        c = conn.cursor()
        count = 0
        for i in range(len(lat)):
            for row in c.execute("""SELECT * \n
            FROM %s \n
            WHERE %s.Latitude LIKE '%s' \n
            AND %s.Longitude LIKE '%s'""" % (mode,mode,"%"+str(lat[i])[:5]+"%",mode,"%"+str(lng[i])[:6]+"%")):
                count += 1
        if (tmode == "Driving"):
            for i in range(len(lat)):
                for row in c.execute("""SELECT * \n
                FROM AritySafeAlerts \n
                WHERE AritySafeAlerts.latitude LIKE '%s' \n
                AND AritySafeAlerts.longitude LIKE '%s' \n
                AND AritySafeAlerts.severity = 'High'""" % ("%"+str(lat[i])[:5]+"%","%"+str(lng[i])[:6]+"%")):
                    count += 1
        #return (self.safetyMetric(count,tmode))
        return(count)

    def twitterAlert(self):
        conn = sqlite3.connect('homeSafeDB.db')
        c = conn.cursor()
        for row in c.execute("""SELECT *
FROM TwitterAlerts
WHERE Date IN (SELECT max(Date) FROM TwitterAlerts)"""):
            print(row)



