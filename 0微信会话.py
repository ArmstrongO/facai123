import uiautomation as ui
import pyperclip
import openai
wx=ui.WindowControl(Name="微信") #绑定名为微信的主窗口控件
wx.SwitchToThisWindow() # 切换窗口
hw=wx.ListControl(Name="会话") # 寻找会话控件绑定
while True:  #循环等待消息
    try:
        we=hw.TextControl(serchDepth=4) #查找未读信息
        if we.Name:
            we.Click(simulateMove=False) #点击未读信息
            lastMsg=wx.ListControl(Name="消息").GetChildren()[-1].Name
            print(lastMsg)
            # 如果想实现群聊机器人，就需要下面这行代码，然后把上面的代码往前缩进和if对齐即可。
            if "@chatgpt" in lastMsg:
                #填写自己的keys
                openai.api_key = "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"
                # 发送内容给chatgpt
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "你是一个AI机器人助手"},
                        {"role": "user", "content": lastMsg}
                    ]
                )
                msg = ""
                # 把chatgpt响应的内容提取出来
                for choice in response.choices:
                    msg += choice.message.content
                print(msg)
                # 发送内容
                pyperclip.copy(msg.replace('{br}', '\n'))
                wx.SendKeys("{Ctrl}v", waitTime=0)
                wx.SendKeys("{Enter}", waitTime=0)
                # 不显示聊天，等待下一条信息
                wx.TextControl(SubName=msg[:5]).RightClick()
                ment = ui.MenuControl(ClassName="CMenuWnd")
                ment.TextControl(Name="不显示聊天").Click()
    except Exception as e:
            pass

