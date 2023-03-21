from time import sleep
import pyautogui as pt
import pyperclip as pc

def move_to_text_input(message):
    position = pt.locateOnScreen('images/gallery.png', confidence=.8)
    new_position = pt.center(position)
    positionx = new_position[0]
    positiony = new_position[1]
    pt.moveTo(positionx, positiony, duration=1)
    pt.moveRel(-100, 3, duration=.5)
    pt.doubleClick(interval=.3)
    pt.typewrite(message, interval=.04)
    # pt.typewrite('\n') this sends the message

def get_messages():
    position = pt.locateOnScreen('images/smiley.PNG', confidence=.9)
    new_position = pt.center(position)
    positionx = new_position[0]
    positiony = new_position[1]
    pt.moveTo(positionx, positiony, duration=.5)
    pt.moveRel(40, -60, duration=.5)
    pt.click()
    sleep(2)

    position = pt.locateOnScreen('images/threedots.PNG', confidence=.8)
    new_position = pt.center(position)
    positionx = new_position[0]
    positiony = new_position[1]
    pt.moveTo(positionx, positiony, duration=.5)
    pt.click()

    position = pt.locateOnScreen('images/copy.PNG', confidence=.8)
    new_position = pt.center(position)
    positionx = new_position[0]
    positiony = new_position[1]
    pt.moveTo(positionx, positiony + 2, duration=.5)
    pt.click()

    user_text = pc.paste()
    return user_text

def process_message(message):
    msg = str(message).lower()

    if msg == 'hello':
        return 'go away'
    elif msg == 'sup':
        return "hello gangsta"
    else:
        return "that is nonsense"

last_message, last_response = "",""

def insta_chatbot():
    global last_message, last_response

    current_message = get_messages()

    if current_message != last_message:
        last_message = current_message
        print(f"Last copied message: {current_message}")

        if current_message == last_message:
            response = process_message(current_message)
            last_response = response
            print(f"Bot: {response}")
            move_to_text_input(response)

    else:
        print("no new messages")

# while True:
    # try:
insta_chatbot()
    # sleep(10)
    # except Exception as e:
    #     print(f"Exception: {e}")
    #     sleep(10)




