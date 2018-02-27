import numpy as np

d = None
o = None


def set_vars(a, b):
    global d
    global o
    d = a
    o = b


def task_b(e):
    global d
    global o
    chance_of_rain = [0.5, 0.5] # Initial chance of rain
    ret_val = "" # Containing the return value.
    for observation in e: # Loop over the input list
        chance_of_rain = forward(observation, chance_of_rain) # Updates the chance of rain based on oberservation.
        p = "Umbrella oberserved: " + ("Yes. " if observation else "No. ") + "Forward message: " + chance_of_rain.__str__() + "\n"
        ret_val += p
    ret_val += "\nAnswer: " + chance_of_rain.__str__()
    return ret_val


def forward_backward(e):
    global d
    global o
    fv = [[0.5, 0.5]]   # Initial forward step messages
    b = np.ones(len(fv[0])) # Initial backward representation of the backward message.
    sv = [] # List of smoothed estimates of steps. Will be filled as the input is iterated over
    ret_val = "" # Containing the return value.
    for i, obs in enumerate(e): # Loop over the input list
        fv.append(forward(obs, fv[i])) # Append the calculated smoothed forward message list.
    for i in range(len(e)-1, -1, -1):  # Loop backwards over the input list. Starting from n-1 and ending at 0
        sv.append(normalize(np.multiply(fv[i+1], b))) # Append the normalized result to the estimate list.
        b = backward(e[i], b) # update the backward message.
        ret_val += "Umbrella observed: " + ("Yes. " if e[i] else "No. ") + "Backward message B" + (i+1).__str__() \
                   + ":" + len(e).__str__() + " - " + b.__str__() + "\n"
    ret_val += "\nAnswer: " + sv[-1].__str__()
    return ret_val


def forward(observation, chance):
    """
    (Ot+1 . T^T) . f where f is the chance of rain based on previous knowledge.
    :param observation: integer
    :param chance: list
    :return: list
    """
    global d
    global o
    return normalize(np.dot(np.dot(o[observation], np.transpose(d)), chance))


def backward(observation, b):
    """
    (T . Ok+1) . bk+2:t where b is based knowledge from today and backwards.
    :param observation: integer
    :param b: list
    :return:list
    """
    global d
    global o
    return np.dot(np.dot(d, o[observation]), b)


def normalize(result):
    """
    Normalized the result by adding the results over the sum of the results
    :param result: list
    :return: list
    """
    return result/sum(result)


def announcement(when, part, result):
    if result:
        print(result)
    print("--------- " + when + " part " + part + " ---------" + ("\n\n" if when == "End" else ""))


