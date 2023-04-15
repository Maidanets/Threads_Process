import datetime
import threading
from multiprocessing import Process

calc_file0 = []


def calc0():
    b = 0
    for i in list(range(0, 10000000)):
        b += i % 4
        calc_file0.append(b)


def calc1():
    calc0()
    with open("calc1.txt", mode="w") as file_txt1:
        file_txt1.write(str(calc_file0))


def calc2():
    calc0()
    with open("calc2.txt", mode="w") as file_txt2:
        file_txt2.write(str(calc_file0))


def calc3():
    calc0()
    with open("calc3.txt", mode="w") as file_txt3:
        file_txt3.write(str(calc_file0))


def calc4():
    calc0()
    with open("calc4.txt", mode="w") as file_txt4:
        file_txt4.write(str(calc_file0))


if __name__ == '__main__':

    thread1 = threading.Thread(target=calc1)
    thread2 = threading.Thread(target=calc2)

    datetime1 = datetime.datetime.now()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    datetime2 = datetime.datetime.now()
    print(datetime2 - datetime1)

    proces3 = Process(target=calc3)
    proces4 = Process(target=calc4)

    datetime1 = datetime.datetime.now()

    proces3.start()
    proces4.start()

    proces3.join()
    proces4.join()

    datetime2 = datetime.datetime.now()
    print(datetime2 - datetime1)
