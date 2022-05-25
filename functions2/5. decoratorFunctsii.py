# def first_test():
#     print("Test function 1")
#
#
# def second_test():
#     print("Test function 2")
#
#
# def simple_decore(fn):
#     def wrapper():
#         print("Start function")
#
#     fn()
#     print("Stop function")
#     return wrapper
#
#
# # first_test_wrapped = simple_decore(first_test)
# # second_test_wrapped = simple_decore(second_test)
#
# @simple_decore
# def first_test():
#     print("Test function 1")                            - не работает

def help(fn):
    def wrapper(arg):
        print("start")
        fn(arg)
        print("stop")
    return wrapper
@help
def func(arg):
    return print(arg ** 2)
func(2)