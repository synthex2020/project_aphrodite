from persistence.building_environment_logs import BuildingEnvironment
from persistence.humaniod_character_logs import HumanoidCharacterLogs
from persistence.prompting_log import PromptingLog
from persistence.structured_environment_logs import StructuredEnvironmentLogs


class PersistenceBuildingEnvironment:
    def __init__(self):
        self.database = BuildingEnvironment()

    def get_environments(self):
        return self.database.get_environments()

    def get_environment_by_id(self, env_id):
        return self.database.get_environment_by_id(env_id)

    def get_environment_by_name(self, name):
        return self.database.get_environment_by_name(name)

    def get_environment_by_type(self, env_type):
        return self.database.get_environments_by_type(env_type)

    def add_environment(self, environment):
        return self.database.add_environment(environment)

    def delete_environment(self, env_id):
        return self.database.delete_environment(env_id)

    def update_environment(self, environment):
        return self.database.update_environment(environment)


class PersistenceStructuredEnvironmentLogs:
    def __init__(self):
        self.database = StructuredEnvironmentLogs()

    def get_environments(self):
        return self.database.get_environments()

    def get_environment_by_id(self, env_id):
        return self.database.get_environment_by_id(env_id)

    def get_environment_by_name(self, name):
        return self.database.get_environment_by_name(name)

    def get_environment_by_type(self, env_type):
        return self.database.get_environments_by_type(env_type)

    def add_environment(self, environment):
        return self.database.add_environment(environment)

    def delete_environment(self, env_id):
        return self.database.delete_environment(env_id)

    def update_environment(self, environment):
        return self.database.update_environment(environment)


class PersistenceHumanoidCharacterLogs:
    def __init__(self):
        self.database = HumanoidCharacterLogs()

    def get_characters(self):
        return self.database.get_characters()

    def get_character_by_id(self, character_id):
        return self.database.get_character_by_id(character_id)

    def get_character_by_name(self, name):
        return self.database.get_character_by_name(name)

    def get_characters_by_story(self, story):
        return self.database.get_characters_by_story(story)

    def add_character(self, character):
        return self.add_character(character)

    def delete_character(self, character_id):
        return self.database.delete_character(character_id)

    def update_character(self, character):
        return self.database.update_character(character)


class PersistencePromptingLogs:
    def __init__(self):
        self.database = PromptingLog()

    def get_prompts(self):
        return self.database.get_prompts()

    def get_prompt_by_id(self, prompt_id):
        return self.database.get_prompt_by_id(prompt_id)

    def get_prompt_by_timestamp(self, timestamp):
        return self.database.get_prompt_by_timestamp(timestamp)

    def add_prompt(self, prompt):
        return self.database.add_prompt(prompt)

    def delete_prompt(self, prompt_id):
        return self.delete_prompt(prompt_id)

