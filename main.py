import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.GYUQjZSSJGs7H1-mSjD35lVLGhC8Kp3wI7gqfUhSAi-Nb28o7fNm7DAH9pYXNHPDwjl6GivKrvZIOKQTYHYZIQE8AjSxwQbrA3Zrn5iQL4pxXh9E7-TuLwCvbIEZBITbwjga5OI-wTGKqXU8vmlgBCDVuHE9IdI5Yi-7UBTwTJDISNjMwkKp2J4BIR6KHk_2XT8Nc2ATs7bAOgbZdquaSw")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id": 0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "hi":
                send_some_msg(id, "Hi friend!")
            elif msg == "Покажи список ишаков":
                send_some_msg(id, 'Hello')