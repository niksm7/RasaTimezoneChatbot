# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from geopy.geocoders import Nominatim
import pytz
from tzwhere import tzwhere

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city = tracker.get_slot("city")
        
        geolocator = Nominatim(user_agent="codeSignal")
        location = geolocator.geocode(city,timeout=1000000)
        x = location.latitude
        y = location.longitude
        tzwh= tzwhere.tzwhere()
        timezone_str = tzwh.tzNameAt(x,y) # Seville coordinates
        q = datetime.now(pytz.timezone(timezone_str))
        output = "{} falls under timezone of {} and the time is {}".format(city,timezone_str,q)

        dispatcher.utter_message(text=output)

        return []
