# MobilityHackathonHomeSafe
Bosch Mobility Hackathon.  Project: HomeSafe

**HomeSafe**

*Value Proposition*

Looking at current landscape of multi-modal transportation apps (google maps, city mapper, etc.), they are very well equipped to help you choose the mode of transport that’s right based on a few criteria: namely, speed and price. However, as anyone who has survived a nerve-racking late night L transfer at a foreign stop can tell you, these aren’t always the most important criteria for every person on every trip.

While we may have a good idea of our safety where we’re coming from and where we’re headed, we’re often less familiar with the places in between. As a result, many people end up over-spending or going out of their way to make sure they get home safe; or worse, braving dangerous trips for the sake of time or money.

*Description*

HomeSafe can help you prioritize you available transit options based on the places you’ll stop and the modes you’ll take. It uses traffic and weather data to make sure you’re safe on the roads, and combines historical crime data with real-time twitter scraping to keep you safe on the sidewalk and in public transit. 

*Architecture*

For our hackathon prototype, we plan to build a demo application. Our application will query the Google Maps API based on a user’s input, and compare the returned routes to different portions of the crime database (sourced from the Chicago Data Portal as well as breaking alerts from the Twitter API) depending on the mode of transit (driving, ride sharing, transit, or walking). If it is a driving route, it will also compare to the driving risk database (sourced from the Arity Risk API). By comparing these routes to the relevant safety data, it will determine a safety score that will be used to prioritize the routes on our interface. Our interface will use the Google Maps API for mapping and route generation capabilities, with our own touch points layered on top to integrate the safety information.

*Technical details*

Our SQLITE 3 database will query the Google Maps API based on a user’s inputted start and end addresses, and receive a list of various possible routes and modes of transit. It compares the returned routes to different portions of the crime database (sourced from the Chicago Data Portal as well as breaking alerts from the Twitter API) depending on the mode of transit (driving, ride sharing, transit, or walking). If it is a driving route, it also feeds the route into the Arity Risk API and receives accident data for that route. By comparing each routes to the relevant safety data, it determines a safety score that is used to re-prioritize the routes before displaying them back to the user. Our interface is a reactive Origami mockup that displays actual results from our database; the results have been pre-loaded and the two elements are separately functional but not currently connected.

As of now the application is more of an API where our python file houses the working code which would be used for said API. It is in working order and using the test data which can be found on the repository. One can see how it would work, where it could be easily implemented into a web or mobile frontend. 

*API Methods"

homeSafe class:

initializes to with a route from merchandise mart to wicker park. 

methods:

.reroute:

user input for starting point and desired destination. Fully functional, will actually look up route using google API.

.driving:
Will look up the route specific to driving, will then use the json file pulled from the google API and scrape it for all the relevant LATLONGs it will then cross reference thos latlongs with the crime history in chicago specific to the mode of transport as well as Aritys risk factor API and the twitter information all stored in the database. It will then calculate a safety mark based on that information as well as other factors such as inherent safety/danger of transport mode, time of day, and time of year.

.transit:
Will look up the route specific to driving, will then use the json file pulled from the google API and scrape it for all the relevant LATLONGs it will then cross reference thos latlongs with the crime history in chicago specific to the mode of transport and the twitter information all stored in the database. It will then calculate a safety mark based on that information as well as other factors such as inherent safety/danger of transport mode, time of day, and time of year.

.rideshare:
Will look up the route specific to driving, will then use the json file pulled from the google API and scrape it for all the relevant LATLONGs it will then cross reference thos latlongs with the crime history in chicagospecific to the mode of transport as well as Aritys risk factor API and the twitter information all stored in the database. It will then calculate a safety mark based on that information as well as other factors such as inherent safety/danger of transport mode, time of day, and time of year.

.walking:
Will look up the route specific to driving, will then use the json file pulled from the google API and scrape it for all the relevant LATLONGs it will then cross reference thos latlongs with the crime history in chicago specific to the mode of transport and the twitter information all stored in the database. It will then calculate a safety mark based on that information as well as other factors such as inherent safety/danger of transport mode, time of day, and time of year.

.biking:
Will look up the route specific to driving, will then use the json file pulled from the google API and scrape it for all the relevant LATLONGs it will then cross reference thos latlongs with the crime history in chicago specific to the mode of transport and the twitter information all stored in the database. It will then calculate a safety mark based on that information as well as other factors such as inherent safety/danger of transport mode, time of day, and time of year.

.all:
will output the safety rating of all modes of transport from the desired route in a list

.twitterAlert:
will print the lates twitter alert relevant to routes and safety


