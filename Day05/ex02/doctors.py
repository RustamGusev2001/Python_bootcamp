import threading
import time


class Doctor(threading.Thread):
    def __init__(self, index, screwdriverOnLeft, screwdriverOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.screwdriverOnLeft = screwdriverOnLeft
        self.screwdriverOnRight = screwdriverOnRight
        self.ready = True

    def run(self):
        while (self.ready):
            time.sleep(1)
            self.dine()

    def dine(self):
        screwdriver1, screwdriver2 = self.screwdriverOnLeft, self.screwdriverOnRight
        while self.ready:
            screwdriver1.acquire()
            locked = screwdriver2.acquire(False)
            if locked:
                break
            screwdriver1.release()
        self.working()
        screwdriver2.release()
        screwdriver1.release()

    def working(self):
        time.sleep(1)
        print('Doctor %s: BLAST!' % self.index)
        self.ready = False


def main():
    screwdrivers = [threading.Semaphore() for n in range(9, 14)]
    doctors = [Doctor(i, screwdrivers[i % 5], screwdrivers[(i + 1) % 5])
               for i in range(9, 14)]

    for p in doctors:
        p.start()


if __name__ == "__main__":
    main()
