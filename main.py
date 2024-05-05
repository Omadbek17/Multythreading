#Threading Examples

#1 example
# import logging
# import threading
# import time
#
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: done", name)
#
#
# if __name__ == '__main__':
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
#
#     logging.info("Main  : before creating thread")
#     x = threading.Thread(target=thread_function, args=("1",))
#     logging.info("Main  : before running thread")
#     x.start()
#     logging.info("Main : wait for the thread to finish")
#     x.join()
#     logging.info("Main  : all done")






#2 example
# import threading
# import time
#
# import pyttsx3
#
#
# def say_hello(name):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.say(f"Salom {name} men sizga siz kiritgan raqamlarni kvadrat darajalarini korsatib beraman") #Bu qismida text to speechdan foydalandim
#     engine.runAndWait()
#     time.sleep(1)
#
# def func(n):
#     for i in range(2, n):
#         print(i ** 2)
#         time.sleep(0.5)
#
# t1 = threading.Thread(target=say_hello, args=("Omadbek",))
# t2 = threading.Thread(target=func, args=(10,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()