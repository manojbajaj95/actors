import replicate

from config import get_settings

class ReplicateImageActor:
  client =None
  system_prompt: str = ""

  def __init__(self) -> None:
    settings = get_settings()
    if not settings.REPLICATE_API_TOKEN:
      raise Exception("Missing OPEN_AI Api key. Please ensure environment variables are set correctly")
    self.client = replicate.Client(api_token=settings.REPLICATE_API_TOKEN)

  def act(self, prompt):
    output = self.client.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
      input={
        "width": 1024,
        "height": 512,
        "prompt": prompt,
        "scheduler": "K_EULER",
        "num_outputs": 1,
        "guidance_scale": 7.5,
        "num_inference_steps": 50
      }
    )
    return output[0]