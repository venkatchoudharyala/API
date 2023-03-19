#Importing openAI Library into the runtime
import openai
#Setting the API AUTHORISATION_KEY
openai.api_key="AUTHORIZATION_KEY" #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
#Defining model engine
model_engine="text-davinci-002"
#An infinite Loop for successful chat
while True:
        prompt=str(input("ENTER YOUR PROMPT :"))
        completion=openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.9)
        response=completion.choices[0].text
        print(response)
