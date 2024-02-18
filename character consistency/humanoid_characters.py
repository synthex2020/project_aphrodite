#   CHARACTER CONSISTENCY IS CREATED AND MAINTAINED THROUGH SET PROMPTS
#   HERE WE USE PROMPTING THROUGH OUR NLP TO CREATE THE CHARACTER PAIRED BY REFERENCE IMAGES
#   CHARACTER JSON => [ NAME, BACKGROUND, STORY, RACE, AGE, REFERENCE_IMAGES, OTHER, PHYSICAL CHARACTERISTICS,
#                       BODY TYPE, ]

class HumanoidCharacters:

    def __init__(self):
        self.language_model = 'Dolphin'

    #   CREATE NEW CHARACTER AND SAVE THE CHARACTER
    def create_new_character(self, character):
        pass

    def process_character_prompt(self, prompt):
        pass

    def save_new_character(self, character):
        #   [ KEYS : _ID, NAME, STORY, IMAGES, DESCRIPTION ]
        pass

    #   EDIT AND MODIFY THE CHARACTER
    def edit_character(self, character_edits):
        #   PASS THE EDITS AS PROMPT TO NLP WITH PREVIOUS CHARACTER INFORMATION
        pass
