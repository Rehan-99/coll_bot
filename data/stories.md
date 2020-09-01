## criteria for the addmission
* greet
  - utter_how_can_i_help
* eligibility_criteria
* courses
  - action_eligibility_tracker
<!-- * courses 
  - action_eligibility_tracker -->
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
 
* goodbye
  - utter_goodbye  
<!-- ## enroll process for unaided
* greet
  - utter_how_can_i_help
* addmission_process  
  - utter_ask_course_category
* addmission_process
  - utter_ask_field 
* addmission_process   
  - utter_form_unaided
* goodbye
  - utter_goodbye

## enroll process for aided
* greet
  - utter_how_can_i_help
* addmission_process
  - utter_ask_field   
* addmission_process  
  - utter_ask_course_category
* addmission_process   
  - utter_form_aided
* goodbye
  - utter_goodbye -->

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

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
