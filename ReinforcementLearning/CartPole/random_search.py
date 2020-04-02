# -*- coding: utf-8 -*-
# Author: Sakib Chowdhury

import numpy as np
import gym 
#import matplotlib.pyplot as plt
#import time


def create_action(observation, param):
    return 1 if observation.dot(param)>0 else  0



def one_episode_avg(env, param):
 
    i = 0
    reward_array = np.empty(100)
    
    
    while i in range(100):
        observation = env.reset()
        t = 0
        total_reward = 0
        done = False
           
        while not done and t<200:
            #env.render()
            
            action = create_action (observation,param)
            observation,reward,done,info = env.step(action)
            t+=1
            
            total_reward += reward
            
            #print ('params : ', param, '  total reward: ', total_reward)
            #time.sleep (1/20)
            
        reward_array[i] = total_reward
        #print ('total reward: ', total_reward, 'index: ', i)
        i+=1
            
    return reward_array.mean()
        
        
        

def learn (env,  generation):
    
    rewards = np.empty(100)
    param_list = np.empty((100,4))
    best_score = 0
    for t in range (generation):
        param = np.random.random(4)*2-1
        rewards[t] = one_episode_avg(env,param)
        param_list[t] = param
        
        print ('params: ',param, ' successfull generation: ', t , 'score: ', rewards[t])
        if rewards[t] > best_score:
            best_score = rewards[t]
            
            
            if best_score >= 200:
                break
            
    return param, param_list
     
env = gym.make ('CartPole-v0')
#one_episode (env, )

param, param_list = learn (env , 100)
    
    

env.close()

