def func_caller(func):
    print("OVER HERE")
    return func


@func_caller
def remote_control():
    print("I love lamp")
    return 0

remote_control()

#func_caller(remote_control)
