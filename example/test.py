from TensorNow import Now
import threading, time
import numpy as np

WAIT_TIME_SECONDS = 1

ticker = threading.Event()

now = Now('test', 
'A7qrnuCA2a9Spn5tYw9o50i15MwdWE',
'Keras')

now.log_permission = True
now.clear_all_custom_flags()
now.clear_all_projects()


CONVERGENCE_FLAG = now.create_custom_flag('My personal definition of model convergence.')
GRADIENT_VANISHING_FLAG = now.create_custom_flag("Gradient Vanishing")


def get_loss_val(count):
	while not ticker.wait(WAIT_TIME_SECONDS):
		calc = np.exp(-1 * (count/100))
		return calc


def train():
	now.start_training('Small boy test')
	for i in range(0,1000000):
		if(i==10):
			now.flag(CONVERGENCE_FLAG)
		if(i==20):
			now.flag(GRADIENT_VANISHING_FLAG)

		loss_val = get_loss_val(i)**2
		now.log_loss(loss_val)

train()


