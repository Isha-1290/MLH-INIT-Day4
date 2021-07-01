from plyer import notification as n #pip install plyer  
import time

def notification1():
    while True:
      n.notify(

        title="1 hour completed",
        message="Drinking water is very good for health\n\nGo and Drink Water",
        # app_icon='Location of Your Ico File',
        timeout=10
      )
      time.sleep(60*60)
