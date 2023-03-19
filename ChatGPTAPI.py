import openai
openai.api_key="AUTHORISATION_KEY"
model_engine="text-davinci-002"
while True:
        prompt=str(input("ENTER YOUR PROMPT :"))
        completion=openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature>        response=completion.choices[0].text
        print(response)
