from actors.human import HumanActor
from actors.openai import OpenAIImageActor, OpenAIChatActor 
import wget

from actors.replicate import ReplicateImageActor
  

class BlogWorkflow:
  human = HumanActor()
  chat = OpenAIChatActor()
  image =  ReplicateImageActor() # OpenAIImageActor()

  # Generate topic, toc, content, image and write mdx file
  def work(self):
    blog_topic = self.chat.act("Suggest a blog topic for Micro SaaS founders. Limit your response to just one topic. Respond with only the topic and nothing else.")
    blog_topic = blog_topic.strip().strip("\"")
    title = "-".join(blog_topic.lower().split(" "))
    image = self.image.act(f"A blog hero image for topic: {blog_topic}")

    blog_toc = self.chat.act(f"For the topic {blog_topic}, suggest sections to be covered including background, introduction and conclusion. Limit to 8-10 topic. Return the topic in a comma separated list. Do not respond with anything else apart from topics.")
    topics = "\n".join([t.strip() for t in blog_toc.strip().split(",") ])
    blog = self.chat.act(f'''For the topic {blog_topic} and given list of topics. Create a blog article in Markdown Format convering all the topics in a separate section. Genrate a table of content in the beginning. Topics: {topics}''')
    import os
    os.mkdir(f"blog/{title}")
    with open(f"blog/{title}/content.md", "w") as f:
      f.write(blog)
    wget.download(image, out=f"blog/{title}/image.png")
    return
    
    