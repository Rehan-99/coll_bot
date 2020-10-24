from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

import json
import logging
import os

import re

import warnings

from io import BytesIO as IOReader, StringIO
from pathlib import Path
from typing import Text, Any, Dict, Union, List, Type, Callable, TYPE_CHECKING, Match
from rasa.constants import ENV_LOG_LEVEL, DEFAULT_LOG_LEVEL, YAML_VERSION

class ActionLocation(Action):

    def name(self) -> Text:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        facility=tracker.get_slot("facility_type")
        address = "B.k.Birla College Road nearby shivsena office ,Kalyan West"
        dispatcher.utter_message("Here is the address  of the college: {}".format(address))

        return [SlotSet("address",address)]
        

class ActionPlacement(Action):

    def name(self) -> Text:
        return "action_placement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        Link = "https://www.bkbirlacollegekalyan.com/placementcell.aspx"
        dispatcher.utter_template("utter_placement_info", tracker,link=Link)

        return []


        
class ActionEligibilityTracker(Action):

     def name(self) -> Text:
         return "action_eligibility_tracker"
             
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response = open("/home/linux-unversei/Documents/college_bot/ugcb.json")
         content = json.load(response)
         
         entities = tracker.latest_message['entities']
         course = None
         
         for  e in entities:
                if e["entity"] == "ug_course":
         		        course = e['value']
                elif e["entity"] == "pg_course":
                        course = e['value']
                else:         
                        message = "Please enter the correct course name"		

         

         for  data in content["courses"]:
               if data["name"] == course.title():
                    print(data)
                    message = "Criteria: "+ data["text"]  
         print(message)				
         dispatcher.utter_message(message)


         

         
         
