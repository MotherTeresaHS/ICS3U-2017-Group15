# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from game_scene import *
from help_scene import *


class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'yellow', 
                                     parent = self, 
                                     size = self.size)
                                     
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
        
        
        
        
        self.high_score_position = Vector2()
        self.high_score_position.y = self.screen_center_y - 100
        self.high_score_position.x = self.screen_center_x
        
        self.high_score = LabelNode(text = "High Score: " + str(config.highscore),
                                    parent = self,
                                    position =self.high_score_position,
                                    color = 'black')
        
        
        self.last_score_position = Vector2()
        self.last_score_position.y = self.screen_center_y
        self.last_score_position.x = self.high_score_position.x
        self.last_score = LabelNode(text = "Your final score is: " + str(config.score),
                                    parent = self,
                                    position = self.last_score_position,
                                    color = 'black')
                                    
        
        self.gameover_label_position = Vector2()
        self.gameover_label_position.y = self.screen_center_y + 150
        self.gameover_label_position.x = self.screen_center_x
        
        self.gameover_label = LabelNode(text = "Game Over",
                                        parent = self,
                                        color = "red",
                                        position = self.gameover_label_position)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        if config.game_over == True:
            self.present_modal_scene(GameOverScene())
            config.game_over = False
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
        
    
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


