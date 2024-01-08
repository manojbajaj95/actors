from config import get_settings
from openai import OpenAI

class OpenAIChatActor:
  client =None
  system_prompt: str = ""

  def __init__(self) -> None:
    settings = get_settings()
    if settings.OPENAI_KEY:
      self.client = OpenAI(
          # This is the default and can be omitted
          api_key=settings.OPENAI_KEY,
      )
    else:
      raise Exception("Missing OPEN_AI Api key. Please ensure environment variables are set correctly")

  def act(self, prompt):
    completion = self.client.chat.completions.create(
      messages=[
         {
          "role": "system",
          "content": self.system_prompt,
        },
        {
          "role": "user",
          "content": prompt,
        }
      ],
      model="gpt-3.5-turbo",
    )
    message = completion.choices[0].message.content
    return message
  
class OpenAIImageActor:
  client =None
  system_prompt: str = ""

  def __init__(self) -> None:
    settings = get_settings()
    if settings.OPENAI_KEY:
      self.client = OpenAI(
          # This is the default and can be omitted
          api_key=settings.OPENAI_KEY,
      )
    else:
      raise Exception("Missing OPEN_AI Api key. Please ensure environment variables are set correctly")

  def act(self, prompt):
    response = self.client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1792x1024",
      quality="standard",
      n=1,
    )

    image_url = response.data[0].url
    
    return image_url