#   THIS IS WHERE WE WILL GENERATE THE NECESSARY PROMPTS FOR NEEDED KEY FRAMES
#   NLP - [ DOLPHIN MIXTRAL ]
#   USER INPUT STRUCTURE:
#       [
#           KEY FRAME IMAGE ( PNG, JPEG),
#           SUBJECT DETAILS ( state, physical characteristics, intent, direction)
#           BACKGROUND ( lighting, environment )
# `          CAMERA ( angle, position, transition )
#           FEELING ( style, setting, tone)
#           OTHER ( other missed details)
#       ]
from tqdm import tqdm as progress_bar
from matplotlib import pyplot as plt
import cv2 as open_cv
import os


class KeyFramesGeneration:

    def __init__(self, language_model):
        self.language_model = language_model
        self.prompt_cache = None

    #   TAKE INPUT FROM THE USER
    def get_user_input(self):
        #   TODO: SET CURRENT DIR AS WORKING DIR
        #   NAME OF NLP IN USE
        lan_model = self.language_model
        print(lan_model)

        user_input = []

        #   OBTAIN USER INPUT
        control = True
        number_of_frames = input("How many key frames do you have?")
        count = 0
        while control:
            #   GET THE IMAGE FROM THE USER
            file_name = input("Enter the name ( including the path if not in home dir) of the image")
            file_image = None
            if os.path.exists(file_name):
                file_image = open_cv.imread(file_name)
            else:
                print("File not found terminating script")
                break

            #   GET DETAILS FROM THE USER
            subject_state = input("Please enter the subject's physical state in the frame in detail")
            #   TODO: CHECK IF THE SUBJECT PHYSICAL CHARACTERISTICS ARE ALREADY SAVED
            subject_physical_characteristics = input("Please enter in detail the subject's physical characteristics")
            background_environment = input("Please describe the subject's background in detail. How is the subject "
                                           "currently interacting with the background")
            background_lighting = input("Please describe the lighting and color of the frame ")
            camera_position = input("Please describe in detail the position of the camera in the frame")
            feeling_style = input("Please describe the style in which the generation to be done")
            feeling_tone = input("Please describe the tone meant to be generated by the frame")
            other = input("Are they any other details you wish to add around the frame? If not just press enter")

            #   ADD DETAILS TO ARRAY
            user_input.append({
                "image": file_image,
                "subject_state": subject_state,
                "subject_physical": subject_physical_characteristics,
                "background_environment": background_environment,
                "background_lighting": background_lighting,
                "camera_position": camera_position,
                "feeling_style": feeling_style,
                "feeling_tone": feeling_tone,
                "other": other
            })
            count += 1
            if count > int(number_of_frames):
                control = False

        print("All frames have been recorded, displaying results")
        return user_input

    #   PROCESS THE INPUT INTO FRAME PROMPTS
    def process_input(self, key_frames):
        #   TODO: SEND THE INPUTS TO THE REQUIRED NLP
        pass

    #   SEND THE PROMPTS AND SHOW USER RESPONSE
    def key_frames_generation(self, key_frames):
        #   TODO: SEND PROMPTS PLUS IMAGE TO MODEL ONE BY ONE AND SAVE IMAGES TO RELEVANT DIRS
        results = []
        lan_model = self.language_model
        print(lan_model)
        for frame in progress_bar(key_frames):
            #   TODO: EACH FRAME IS IMAGE AND TEXT SEND THAT TO MODEL
            user_input_image = frame['image']
            generated_prompts = frame['prompt']
            #   TODO: RETURNS IMAGE FILE NAMES INSTEAD OF IMAGES THEY ARE STORED IN OUTPUT
            #   APPEND RESULTANT IMAGES BEFORE PROMPTING AGAIN
        #   DISPLAY RESULTS
        figure = plt.figure(figsize=(10, 7))
        rows = 2
        columns = 2
        counter = 1
        for resultant in results:
            image_read = open_cv.imread(resultant)
            figure.add_subplot(rows, columns, counter)
            # SHOWING THE IMAGE
            plt.imshow(image_read)
            plt.axis('off')
            plt.title(str(counter))
            counter += 1
        plt.show()
        return results


# if __name__ == '__main__':
#     figure = plt.figure(figsize=(10, 7))
#     columns = 2
#     counter = 1
#     results = [
#         '001.png',
#         '002.png',
#         '003.png',
#         '004.png',
#         '005.png'
#     ]
#     rows = len(results)
#     print(rows)
#     for resultant in progress_bar(results):
#         image_read = open_cv.imread(resultant)
#         figure.add_subplot(rows, columns, counter)
#         # SHOWING THE IMAGE
#         plt.imshow(image_read)
#         plt.axis('off')
#         plt.title(str(counter))
#         counter += 1
#     plt.show()
