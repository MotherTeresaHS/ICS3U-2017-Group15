# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui
import config
from main_menu_scene import *
import time

class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        
        self.instruction_label_position = Vector2()
        self.instruction_label_position.x = self.screen_center_x
        self.instruction_label_position.y = self.screen_center_y
        self.Instruction_label = LabelNode('FX sounds are ON right now',
                                            parent = self,
                                            position = self.instruction_label_position,
                                            color = 'black')
        
        self.line_one_position = Vector2()
        self.line_one_position.x = self.screen_center_x
        self.line_one_position.y = self.screen_center_y + 200
        self.line_one = LabelNode(text = 'Design by: Francisco Lee',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      color = 'black',
                                      position = self.line_one_position,
                                      scale = 0.75)
                                      
        
        self.line_two_position = Vector2()
        self.line_two_position.x = self.screen_center_x
        self.line_two_position.y = self.screen_center_y + 150
        self.line_two = LabelNode(text = 'You could move your character by press button and press red button to fire',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      color = 'black',
                                      position = self.line_two_position,
                                      scale = 0.75)
        
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
        
        self.sound_on_button_position = Vector2()
        self.sound_on_button_position.x = self.screen_center_x + 180
        self.sound_on_button_position.y = self.screen_center_y - 200
        self.sound_on_button = SpriteNode('./assets/sprites/sound_on.png',
                                          position = self.sound_on_button_position,
                                          parent = self,
                                          scale = 0.5)
        
        self.sound_off_button_position = Vector2()
        self.sound_off_button_position.x = self.screen_center_x - 100
        self.sound_off_button_position.y = self.screen_center_y - 200
        self.sound_off_button = SpriteNode('./assets/sprites/sound_off.png',
                                          position = self.sound_off_button_position,
                                          parent = self,
                                          scale = 0.6)
        
        
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        #stop the music if sound is off
        if config.sound_on == False:
            sound.stop_effect(config.background_music)
        
        # to make sure user knows if the sound is on or off
        if config.sound_on == True:
            if self.Instruction_label.text != 'FX sounds are ON right now' and self.Instruction_label.color != 'black':
                self.Instruction_label.text = 'FX sounds are ON right now'
            self.Instruction_label.color = 'black'
            
        elif config.sound_on == False:
            if self.Instruction_label.text != 'FX sounds are OFF right now' and self.Instruction_label.color != 'red':
                self.Instruction_label.text = 'FX sounds are OFF right now'
            self.Instruction_label.color = 'red'
        
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if back button is pressed, goto main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        
        # if user touched sound on or off turn it on or off and tell the user you have done it 
        if self.sound_on_button.frame.contains_point(touch.location):
            config.sound_on = True
            config.background_music = sound.play_effect('./assets/sounds/game_music.wav')
            config.music_start_time = time.time()
            self.Instruction_label.text = 'FX sounds are ON right now'
            self.Instruction_label.color = 'black'
            
            
        
        if self.sound_off_button.frame.contains_point(touch.location):
            config.sound_on = False
            self.Instruction_label.text = 'FX sounds are OFF right now'
            self.Instruction_label.color = 'red'
            sound.stop_effect(config.background_music)
    
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
    
