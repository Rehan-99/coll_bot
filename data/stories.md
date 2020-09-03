## criteria for the addmission
* greet
  - utter_how_can_i_help
* eligibility_criteria
* courses
  - action_eligibility_tracker
* college_info
  - utter_give_info
* college_campus
  - utter_give_campus   
* goodbye
  - utter_goodbye

## location of college
* greet
  - utter_how_can_i_help
* eligibility_criteria
  - action_eligibility_tracker
* location_college{"facility_type":"college","location":"address"}
  - action_location
  - slot{"address":"B.k.Birla College Road nearby shivsena office ,Kalyan West"}
* college_info
  - utter_give_info
* college_campus
  - utter_give_campus
* goodbye
  - utter_goodbye

## criteria and location
* greet
    - utter_how_can_i_help
* location_college{"location":"location","facility_type":"college"}
    - slot{"location":"location"}
    - action_location
    - slot{"address":"B.k.Birla College Road nearby shivsena office ,Kalyan West"}
* eligibility_criteria{"ug_course":"Bsc","eligible":"eligibility criteria"}
    - slot{"eligible":"eligibility criteria"}
    - slot{"ug_course":"Bsc"}
    - action_eligibility_tracker
* eligibility_criteria{"pg_course":"Msc"}
    - slot{"pg_course":"Msc"}
    - action_eligibility_tracker
* eligibility_criteria{"eligible":"Criteria","ug_course":"Bmm"}
    - slot{"eligible":"Criteria"}
    - slot{"ug_course":"Bmm"}
    - action_eligibility_tracker
* out_of_scope
    - action_default_fallback
* goodbye
    - utter_goodbye
 
* goodbye
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* deny
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
