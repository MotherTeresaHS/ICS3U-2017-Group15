# Created by: Francisco Lee
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui

from numpy import random

import sound
import config
import time

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        self.left_button_down = False
        self.right_button_down = False
        self.man_move_speed = 20.0
        self.bullets = []
        self.zombies = []
        self.zombie_attack_rate = 2
        self.zombie_attack_speed = 30.0
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        gunman_position = Vector2()
        gunman_position.x = self.size_of_screen_x - 100
        gunman_position.y = 80
        self.gunman = SpriteNode('./assets/sprites/new_gunman.PNG',
                                    parent = self,
                                    position = gunman_position,
                                    scale = 0.6)
                                       
                                       
        fire_button_position = Vector2()
        fire_button_position.x = self.size_of_screen_x - 100
        fire_button_position.y = 250
        self.fire_button = SpriteNode('./assets/sprites/red_button.png',
                                      parent = self,
                                      position = fire_button_position,
                                      alpha = 0.4,
                                      scale = 0.65)
        
        self.score_position = Vector2()
        self.score_position.x = 80
        self.score_position.y = self.size_of_screen_y - 50
        
        self.score_label = LabelNode(text = 'Score: ',
                                     parent = self,
                                     position = self.score_position,
                                     color = 'black')
                                     
        
        
        self.highscore_position = Vector2()
        self.highscore_position.x = 80
        self.highscore_position.y = self.size_of_screen_y -100
        
        self.highscore_label = LabelNode(text = 'Highscore: ' + str(config.highscore),
                                         parent = self,
                                         position = self.highscore_position,
                                         color = 'black')
                                         
        
        left_button_position = Vector2()
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5,
                                      scale = 0.5)
                                       
        right_button_position = Vector2()
        right_button_position.x = 300
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5,
                                       scale = 0.5)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # background music
        
        
        
        # move gunman if button down
        if self.left_button_down == True :
            
            gunmanMove = Action.move_by(-1*self.man_move_speed, 
                                           0.0, 
                                           0.1)
            self.gunman.run_action(gunmanMove)
        
        if self.right_button_down == True:
            gunmanMove = Action.move_by(self.man_move_speed, 
                                           0.0, 
                                           0.1)
            self.gunman.run_action(gunmanMove)
        
        # every update, randomly check if a new alien should be created
        zombie_create_chance = random.randint(1, 120)
        if zombie_create_chance <= self.zombie_attack_rate:
            self.add_zombie()
            
        # check every update if a missile is off screen
        for bullet in self.bullets:
            if bullet.position.x < 0:
                bullet.remove_from_parent()
                self.bullets.remove(bullet)
                #print('missile removed')
        
        # check every update if an alien is off screen
        #print(len(self.aliens))
        for zombie in self.zombies:
            if zombie.position.y < -50:
                zombie.remove_from_parent()
                self.zombies.remove(zombie)
                # you might want to end the game, or take points away
        
        # check every update to see if a missile has touched a space alien
        if len(self.zombies) > 0 and len(self.bullets) > 0:
            #print('missile check')
            for zombie in self.zombies:
                for bullet in self.bullets:
                    if zombie.frame.contains_rect(bullet.frame):
                        bullet.remove_from_parent()
                        self.bullets.remove(bullet)
                        zombie.remove_from_parent()
                        self.zombies.remove(zombie)
                        config.score = config.score + 100
                        
                        # since you destroyed one, make more show up
                        #self.alien_attack_rate = self.alien_attack_rate + 1
        else:
            pass
            #print(len(self.aliens))
        
        # check every update to see zombie touches gunman
        if len(self.zombies) > 0:
            #print('checking')
            for zombie_hit in self.zombies:
                #print('alien ->' + str(alien_hit.frame))
                #print('man  ->' + str(self.gunman.frame))
                if zombie_hit.frame.intersects(self.gunman.frame):
                    #print('a hit')
                    self.gunman.remove_from_parent()
                    zombie_hit.remove_from_parent()
                    self.zombies.remove(zombie_hit)
                    
                    if config.game_over != True:
                        config.game_over = True
                        if config.sound_on == True:
                            sound.play_effect('./assets/sounds/game_over.wav')
                        self.dismiss_modal_scene()
                    # since game over, move to next scene
        else:
            pass
            #print(len(self.aliens))
        
        
        # update score
        if self.score_label.text != 'score:' + str(config.score):
            self.score_label.text = 'score:' + str(config.score)
            
            
            if config .score > config.highscore:
                config.highscore = config.score
                if self.highscore_label.text != 'Highscore:' +str(config.highscore):
                    self.highscore_label.text = 'Highscore:' + str(config.highscore)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if left or right button is down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.fire_button.frame.contains_point(touch.location):
            self.create_new_bullet()
        else:
            # if I removed my finger, then no matter what gunman
            #    should not be moving any more
            self.left_button_down = False
            self.right_button_down = False
    
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
    
    def create_new_bullet(self):
        # when the user hits the fire button
        
        bullet_start_position = Vector2()
        bullet_start_position.x = self.gunman.position.x - 10
        bullet_start_position.y = self.gunman.position.y + 60
        
        bullet_end_position = Vector2()
        bullet_end_position.x = - 20
        bullet_end_position.y = self.gunman.position.y + 100
        
        self.bullets.append(SpriteNode('./assets/sprites/bullet.PNG',
                             position = bullet_start_position,
                             parent = self,
                             scale = 0.034))
        
        if config.sound_on == True:
            sound.play_effect('./assets/sounds/shooting.wav')
        
        # make missile move forward
        bulletMoveAction = Action.move_to(bullet_end_position.x, 
                                           bullet_end_position.y, 
                                           1.0)
        self.bullets[len(self.bullets)-1].run_action(bulletMoveAction)
        
    def add_zombie(self):
        # add a new alien to come down
        
        zombie_start_position = Vector2()
        zombie_start_position.x = - 100
        zombie_start_position.y = 100
        
        zombie_end_position = Vector2()
        zombie_end_position.x = 1000
        zombie_end_position.y = 100
        
        self.zombies.append(SpriteNode('./assets/sprites/zombie2.PNG',
                             position = zombie_start_position,
                             parent = self,
                             scale = 0.5))
        
        # make missile move forward
        zombieMoveAction = Action.move_to(zombie_end_position.x, 
                                         zombie_end_position.y, 
                                         self.zombie_attack_speed,
                                         TIMING_SINODIAL)
        self.zombies[len(self.zombies)-1].run_action(zombieMoveAction)
