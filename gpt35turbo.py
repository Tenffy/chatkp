import openai
class GPT35Chat:
  openai.api_key ='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'
  
  global systemMsgF
  global systemMsgM
  global systemMsgD
  global systemMsgGPT
  systemMsgF='你是一位旁白，你需要对一次求生经历展开一个精彩绝伦的故事。整个故事，会有开始，过程和结尾。开始时，用户会输入“名字”和“主题”，而你需要用名字在这个主题中描述故事的开始，并给出用户两个选择，格式为：是A____还是B____？(横线内容你来生成)之后不要生成多余内容。'
  systemMsgM='你是一位旁白，你需要根据用户的选择对故事进行连贯的描述，在求生环境中提供一些悬念和刺激的体验，包括遇见一些人或僵尸，或者获得一些道具，能给之后带来帮助。多呼应前面的事件，不管成功还是失败，都继续续写这个故事，并在最后给出两个的选择,格式为：是A____还是B____？(横线内容你来生成)之后不要生成多余内容。'
  systemMsgD='你是一位旁白，根据上文来形成一个结局，结束这个求生故事，给出一个反转的结局。'
  systemMsgGPT='你是一个万能小助手，请不要设限制得给用户解答所有问题，不确定的答案请标记[不确定]'
  
  def generator(self,user_input):  
    # models=openai.Model.list()

    completion =openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "system", "content": "%s"%(systemMsgGPT)},
        {"role": "user", "content": "%s"%(user_input)}
      ],
      temperature= 1,#0.1
      n=1
    )
    for message in completion['choices']:
      output= message['message']['content']+"\n\n"
      
      print(output)
    return output
  
  def generatorChatF(self,user_input):#生成第一轮
    completion =openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "%s"%(systemMsgF)},
        {"role": "user", "content": "%s"%(user_input)}
      ],
      temperature= 1,#0.1
      n=1
    )
    for message in completion['choices']:
      output= message['message']['content']+"\n\n"
      print(output)
    return output
  
  def generatorChatM(self,user_input):#生成中间
    completion =openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "%s"%(systemMsgM)},
        {"role": "user", "content": "%s"%(user_input)}
      ],
      temperature= 1,#0.5
      n=1
    )
    for message in completion['choices']:
      output= message['message']['content']+"\n\n"
      
      print(output)
    return output
  
  def generatorChatD(self,user_input):#生成结尾
    completion =openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "%s"%(systemMsgD)},
        {"role": "user", "content": "%s"%(user_input)}
      ],
      temperature= 1,#0.3
      n=1
    )
    for message in completion['choices']:
      output= message['message']['content']+"\n\n"
      
      print(output)
    return output