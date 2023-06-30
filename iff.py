import openai
from dotenv import load_dotenv,find_dotenv
_ = load_dotenv(find_dotenv())
import os
import json



openai.api_key  = os.environ['OPENAI_API_KEY']
  
fragrances = {
    "Lavender Vanilla Perfume": {
        "fragranceNotes": [
            "Top Note: Lavender",
            "Middle Note: Jasmine",
            "Middle Note: Bergamot",
            "Base Note: Vanilla",
            "Base Note: Musk"
        ]
    },
    "Citrus Cologne": {
        "fragranceNotes": [
            "Top Note: Lemon",
            "Top Note: Lime",
            "Middle Note: Neroli",
            "Middle Note: Orange Blossom",
            "Base Note: White Musk"
        ]
    },
    "Rose Eau de Parfum": {
        "fragranceNotes": [
            "Top Note: Rose Petals",
            "Middle Note: Peony",
            "Middle Note: Lily of the Valley",
            "Base Note: Amber",
            "Base Note: White Musk"
        ]
    },
    "Forest Pine Candle": {
        "fragranceNotes": [
            "Top Note: Pine Needles",
            "Middle Note: Eucalyptus",
            "Middle Note: Cedar",
            "Base Note: Sandalwood",
            "Base Note: Earth"
        ]
    },
    "Ocean Breeze Room Spray": {
        "fragranceNotes": [
            "Top Note: Sea Salt",
            "Middle Note: Marine",
            "Middle Note: Jasmine",
            "Base Note: Musk",
            "Base Note: Driftwood"
        ]
    },

}

 
def show_fragrance_with_same_note(note_name):
    returnString = ""
    for fragrance, notes in fragrances.items():
        
        for note in notes["fragranceNotes"]:
            if(note == note_name):
                #print("Fragrance:", fragrance)
                #print("note:", note)
                returnString += f"Fragrance:  {fragrance} note:  {note}"
    return returnString
           


def get_fragrance_matches(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": str({query})}],
        functions=[
            {
                "name": "show_fragrance_with_same_note",
                "description": "shows fragrances that have the same note as the note passed in",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "note_name": {
                            "type": "string",
                            "description": "note of the fragrance, e.g.'Middle Note: Bergamot'",
                        }
                    },
                    "required": ["note_name"],
                },
            }        
        ],
        function_call="auto",
    )

    message = response["choices"][0]["message"]
    #print("message" + str(message))

    # Step 2, check if the model wants to call a function
    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        note_name = json.loads(message["function_call"]["arguments"]).get("note_name")

        # Step 3, call the function
        # Note: the JSON response from the model may not be valid JSON
        function_response = show_fragrance_with_same_note(
            note_name=note_name
        )
  

        # Step 4, send model the info on the function call and function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": str({query})},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )

        return second_response["choices"][0]["message"]

    return message

  

response = get_fragrance_matches("Only Show me the name of fragrances that have a middle note of jasmine. Keep your response brief with not explanation. Do not format the answer in json. Just simple short text answer. ")
print(response)