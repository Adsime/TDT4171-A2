import functions as f

D = [[0.7, 0.3], [0.3, 0.7]]
O = [[[0.1, 0.0], [0.0, 0.8]], [[0.9, 0.0], [0.0, 0.2]]]

f.set_vars(D, O)


def show_res(task, res):
    f.announcement("Start", task, None)
    f.announcement("End", task, res)


show_res("B:1", f.task_b([1, 1]))
show_res("B:2", f.task_b([1, 1, 0, 1, 1]))
show_res("C:1", f.forward_backward([1, 1]))
show_res("C:2", f.forward_backward([1, 1, 0, 1, 1]))