import datetime
import pygame
import time


def alarm_sound_play():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        quitOption = input("Enter 'Q' for quit: ")
        if quitOption == "Q":
            exit()
        continue


def main():
    alarm_time: str = ""

    while True:
        alarm_time_input = input("Enter alerm time (HH:MM in 24hour format): ")

        if len(alarm_time_input) == 5:
            alarm_time = alarm_time_input
            break
        else:
            print("Invalid Input. Try again...")

    user_enterd_alerm_time = alarm_time.split(":")

    alarm_hour, alarm_minute = user_enterd_alerm_time

    while True:
        current_hour = datetime.datetime.now().hour
        current_minute = datetime.datetime.now().minute
        print("time chek hochhe ")
        if current_hour == int(alarm_hour) and current_minute == int(alarm_minute):
            print("alarm bajbe")
            alarm_sound_play()
            break

        time.sleep(1)


main()
