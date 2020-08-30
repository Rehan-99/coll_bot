
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

ENDPOINTS = {
    "base": "/home/linux-unversei/Documents/college_bot/ugcb.json",
    "ugcb": {
        "name_course": "?name={}",
        "eligibility_query": "?eligibility={}",
        
    }
}

COURSE_TYPES = {
    "ug_course":
        {
            "name": "ug course",
            "resource": "ugcb"
        }   
}

def _create_path(base: Text, resource: Text,
                 query: Text, values: Text) -> Text:
    """Creates a path to find provider using the endpoints."""

    if isinstance(values, list):
        return (base + query).format(
            resource, ', '.join('"{0}"'.format(w) for w in values))
    else:
        return (base + query).format(resource, values)


def _find_facilities(ug_course: Text, resource: Text) -> List[Dict]:
    """Returns json of facilities matching the search criteria."""

    if str.isdigit(location):
        full_path = _create_path(ENDPOINTS["base"], resource,
                                 ENDPOINTS[resource]["zip_code_query"],
                                 location)
    else:
        full_path = _create_path(ENDPOINTS["base"], resource,
                                 ENDPOINTS[resource]["city_query"],
                                 location.upper())
    #print("Full path:")
    #print(full_path)
    results = requests.get(full_path).json()
    return results



def _resolve_name(eligibility, resource) ->Text:
    for key, value in .items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""



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
       

# class ActionLocation(Action):

#     def name(self) -> Text:
#         return "action_eligible"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         facility = tracker.get_slot("ug_course")

#         msg = "For admission B.M.M Degree course the candidate should have passed Standard XII Examination conducted by the Maharashtra State Board of Secondary and Higher Secondary education or its equivalent from the Arts, Science or Commerce Stream."

#         dispatcher.utter_message("Here is the criteria  for {}:{}".format(facility,msg))

#         return [SlotSet("msg",msg)]
               
class Geteligibility(Action):
    """This action class retrieves the elibility criteria for the course."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "facility_eligible"
    
    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        
        ugc = tracker.get_slot('ug_course')
        eligibility = tracker.get_slot('eligible')
        
        full_path = _create_path(ENDPOINTS["base"], ugc,
                                 ENDPOINTS[ugc]["eligibility_query"],
                                 eligibility)
        results = requests.get(full_path).json()
        if results:
            selected = results[0]
            if ugc == COURSE_TYPES["ug_course"]["resource"]:
                address = "{}, {}".format(selected["name"].title(),
                                                 selected["eligibility"].title())
            elif ugc == COURSE_TYPES["pg_course"]["resource"]:
                address = "{}, {}".format(selected["name"].title(),
                                                 selected["eligibility"].title())
            else:
                print("Not Found")
          
        else:
            print("No course found. Most likely this action was executed "
                  "before the user choose a course facility from the "
                  "provided list. "
                  "If this is a common problem in your dialogue flow,"
                  "using a form instead for this action might be appropriate.")

            return [SlotSet("facility_eligible", "not found")]   
                                                 
                                                
        
        
        
        
        
        
        
        
        
class FacilityForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "eligible_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ug_course","eligible"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"ug_course": self.from_entity(entity="ug_course",
                                                  intent=["courses",
                                                          "eligibility_criteria"]),
                "eligible": self.from_entity(entity="eligible",
                                                  intent=["courses",
                                                          "eligibility_criteria"])}         

    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        ugc = tracker.get_slot('ug_course')
        eligibility = tracker.get_slot('eligible')

        results = _find_facilities(eligibility,ugc)
        button_name = _resolve_name(COURSE_TYPES, ugc)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              ugc.title()))  
            return []
        buttons = []
        # limit number of results to 3 for clear presentation purposes
        for r in results[:2]:
            if eligibility == COURSE_TYPES["ug_course"]["resource"]:
                criteria = r["eligibility"]
                name = r["name"]
            elif eligibility == COURSE_TYPES["pg_course"]["resource"]:
                facility_id = r["eligibility"]
                name = r["name"]
            else:
                print(None)    
            

            payload = "/inform{\"facility_id\":\"" + facility_id + "\"}"
            buttons.append(
                {"title": "{}".format(name.title()), "payload": payload})

        

        

        return []
                                                                                                  
                
