from collections.abc import Iterable
import pygame
from pygame import font  # Import the pygame.font module
import time
from pygame.mixer import Sound, get_init, pre_init
from typing import Generic, TypeVar
import copy
pre_init(44100, -16, 1, 1024)
# check environment var

T = TypeVar("T")
class CountedElement(int):
    def __init__(self, value: T):
        super().__init__()
        self.comparison_count = 0

    def __ne__(self, other):
        self.comparison_count += 1
        return super().__ne__(other)

    def __gt__(self, other):
        self.comparison_count += 1
        return super().__gt__(other)
    def __le__(self, __value: int) -> bool:
        self.comparison_count += 1
        return super().__le__(__value)

    def __ge__(self, other):
        self.comparison_count += 1
        return super().__ge__(other)

class CountingListVisualizer(list):
    def __len__(self) -> int:
        # dontDelS = False
        # dontDelSound = False
        # if self.screen is None:
        #     dontDelS = True
        # if self.playing is None:
        #     dontDelSound = True

        # if not dontDelS:
        #     del self.screen
        # if not dontDelSound:
        #     del self.playing
        # length = super().__len__()
        # if not dontDelS:
        #     self.screen = pygame.display.set_mode((self.width, self.height))
        return super().__len__()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_last = (-1,-1) # we detect swaps by checking if the last set is the same as the current set
        self.access_count = 0
        self.comparison_count = 0
        self.set_count = 0
        self.swaps = 0
        self.width = 1000
        self.height = 800
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.playing = None
        for element in self:
            if not isinstance(element, CountedElement):
                super().__setitem__(self.index(element),CountedElement(element))
        for element in self:
            element.comparison_count = 0

    def __getitem__(self, index):
        self.access_count += 1
        
        item = super().__getitem__(index)
        save = self.screen
        saveN = self.playing
        del self.screen
        del self.playing
        cloned = copy.deepcopy(self)# whoever wrote this code is an idiot... oh wait
        self.playing = saveN
        self.screen = save

        # Change the color of the accessed item
        def extraData():
            color = (255, 0, 0)  # Green color for the accessed item
            bar_width = self.width // len(cloned) # this ishorrible... OH WELL!
            bar_height_ratio = self.height / max(cloned)

            bar_rect = pygame.Rect(index * bar_width, self.height - item * bar_height_ratio, bar_width, item * bar_height_ratio)
            pygame.draw.rect(self.screen, color, bar_rect)
        min_val = min(cloned)
        max_val = max(cloned)
        value_range = max_val - min_val
        normalized_value = (item - min_val) / value_range
        sound_frequency = 100 * (1.5* (normalized_value *7))+100

        if self.playing is None:
            self.playing = Note(sound_frequency)
            self.playing.play(-1)
        else:
            self.playing.stop()
            self.playing = Note(sound_frequency)
            self.playing.play(-1)
        self.draw(extraData)

        
       
        return super().__getitem__(index)
      
    def swap(self, i, j):
        """THIS IS NOT A NATIVE LIST FUNCTION THIS IS NOT CROSS COMPAITBLE WITH OTEHR LISTS"""
        self[i], self[j] = self[j], self[i]
        self.swaps += 1
        self.draw()

    def __setitem__(self, index, value):
        lastI, lastV = self.set_last
        if lastI == value and lastV == super().__getitem__(index):
            print("SWAP DETECTEDASHDHASHDKJSAH")
            self.swaps += 1

        self.set_count += 1
        self.draw()
        self.set_last = (super().__getitem__(index), value)
        if isinstance(value,CountedElement):
            return super().__setitem__(index, value)
        else:
            return super().__setitem__(index, CountedElement(value))

    def __lt__(self, other):
        self.comparison_count += 1
        self.draw()
        return super().__lt__(other)
 

    def draw(self, extra_data=None):
        self.comparison_count = sum([item.comparison_count for item in self])
        save = self.screen
        saveV = self.playing

        del self.screen
        del self.playing
        cloned= copy.deepcopy(self)
        self.screen = save
        self.playing = saveV
    # make a bar chart essentially with the index as the x axis and the value as the y axis
        
        bar_width = self.width // list.__len__(cloned)
        bar_height_ratio = self.height / max(cloned)
        #write text for the number of accesses and comparisons in top right
      


        self.screen.fill((255, 255, 255))  # Clear the screen
    

        min_val = min(cloned)
        max_val = max(cloned)
        value_range = max_val - min_val

        for i, value in enumerate(cloned):
            bar_height = value * bar_height_ratio
            bar_rect = pygame.Rect(i * bar_width, self.height - bar_height, bar_width, bar_height)
          
            normalized_value = (value - min_val) / value_range

            # Convert the normalized value to RGB color
            green = int(255 * normalized_value)
            blue = int(255 * (1 - normalized_value))
            red = int(255 * (1 - abs(normalized_value - 0.5) * 2))

            color = (red, green, blue)
            pygame.draw.rect(self.screen, color, bar_rect)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render(f"Accesses: {self.access_count}", True, (0, 0, 0))
        self.screen.blit(text, (self.width - 200, 0))
        text = font.render(f"Comparisons: {self.comparison_count}", True, (0, 0, 0))
        self.screen.blit(text, (self.width - 200, 40))
        text = font.render(f"Sets: {self.set_count}", True, (0, 0, 0))
        self.screen.blit(text, (self.width - 200, 80))
        text = font.render(f"Swaps: {self.swaps}", True, (0, 0, 0))
        self.screen.blit(text, (self.width - 200, 120))
        if extra_data:
            extra_data()
         

        pygame.display.flip()  # Update the screen



from array import array
from time import sleep

import pygame

from typing import Generic, TypeVar
T = TypeVar("T")
class ListElementWrapper(Generic[T]):
    def __init__(self):
        self.comparison_count = 0
    def __lt__(self, other):
        self.comparison_count += 1
        return self < other



class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

if __name__ == "asd":
    pre_init(44100, -16, 1, 1024)
    pygame.init()
    Note(440).play(-1)
    sleep(5)