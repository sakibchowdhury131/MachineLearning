#Author : Sakib Chowdhury
import time
#from gym import wrappers
#env = wrappers.Monitor(env, 'Video_folder')
observation = env.reset()
done = False
t = 0



while t<300 and not done :
    env.render()
    action = create_action(observation,param)
    observation, reward, done, info = env.step(action)
    time.sleep(1/10)
    t = t+1
    print (t)
    
    
    
env.close()


