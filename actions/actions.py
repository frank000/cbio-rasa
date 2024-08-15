from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionSendInfoToEndpoint(Action):

    def name(self) -> str:
        return "action_send_info"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> List[Dict[Text, Any]]:
         
        info = tracker.get_slot('info')
        # url = "https://api.exemplo.com/processar_info"
        
        # # Dados a serem enviados para o endpoint
        # payload = {"info": info}
        
        # # Faça a requisição POST
        # response = requests.post(url, json=payload)
        
        # # Suponha que o retorno seja JSON com uma chave "resultado"
        # result = response.json().get("resultado")
        
        # Envie a resposta ao usuário
        dispatcher.utter_message(text="Oppaaa O resultado é: {}".format(info))
        
        # Opcional: resetar o slot
        return []
        



# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
