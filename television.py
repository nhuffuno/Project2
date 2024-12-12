import tkinter as tk
from tkinter import messagebox
import random

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__loudness_threshold = 8

    def power(self) -> None:
        self.__status = not self.__status

    def mute(self) -> None:
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
            self.random_channel_message()

    def channel_down(self) -> None:
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
            self.random_channel_message()

    def volume_up(self) -> None:
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            if self.__volume >= self.__loudness_threshold:
                messagebox.showwarning("Warning", "That's too loud!")

    def volume_down(self) -> None:
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            if self.__volume == Television.MIN_VOLUME:
                messagebox.showinfo("Info", "Turn up the volume, I'm trying to listen.")

    def random_channel_message(self):
        messages = [
            "A nuke has dropped somewhere in the world",
            "An alien invasion is spreading in Europe",
            "An orangutan learned how to do math",
            "The asteroid colored the water blood red."
        ]
        messagebox.showinfo("Channel Change", random.choice(messages))

    def __str__(self) -> str:
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = MUTED"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


class TelevisionGUI:
    def __init__(self, root):
        self.tv = Television()

        root.title("Television Remote")
        root.geometry("300x400")

        self.status_label = tk.Label(root, text=self.tv.__str__(), wraplength=250)
        self.status_label.pack(pady=20)

        tk.Button(root, text="Power", command=self.toggle_power, width=20).pack(pady=5)
        tk.Button(root, text="Mute", command=self.mute, width=20).pack(pady=5)
        tk.Button(root, text="Channel Up", command=self.channel_up, width=20).pack(pady=5)
        tk.Button(root, text="Channel Down", command=self.channel_down, width=20).pack(pady=5)
        tk.Button(root, text="Volume Up", command=self.volume_up, width=20).pack(pady=5)
        tk.Button(root, text="Volume Down", command=self.volume_down, width=20).pack(pady=5)

    def update_status(self):
        self.status_label.config(text=self.tv.__str__())

    def toggle_power(self):
        self.tv.power()
        self.update_status()

    def mute(self):
        self.tv.mute()
        self.update_status()

    def channel_up(self):
        self.tv.channel_up()
        self.update_status()

    def channel_down(self):
        self.tv.channel_down()
        self.update_status()

    def volume_up(self):
        self.tv.volume_up()
        self.update_status()

    def volume_down(self):
        self.tv.volume_down()
        self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelevisionGUI(root)
    root.mainloop()
