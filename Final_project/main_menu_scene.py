# Created by: Francisco Lee
# Created on: January 2018
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from game_scene import *
from help_scene import *
from game_over_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'black', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.start_button = SpriteNode('./assets/sprites/start.png',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.5)
                                       
        help_button_position = self.size/2
        help_button_position.y = help_button_position.y - 100
        self.help_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = help_button_position,
                                       scale = 0.5)
        
        config.background_music = sound.play_effect('./assets/sounds/game_music.wav')
        config.music_start_time = time.time()
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        if config.game_over == True:
            self.present_modal_scene(GameOverScene())
            config.game_over = False
        
        if config.sound_on == True and (time.time() - config.music_start_time >= 50):
            config.background_music = sound.play_effect('./assets/sounds/game_music.wav')
            config.music_start_time = time.time()
        
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            config.score = 0
            
        # if start button is pressed, goto game scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
