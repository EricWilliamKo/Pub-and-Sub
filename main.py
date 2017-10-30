from Subscriber import Subscriber
from Publisher import Publisher

if __name__ == '__main__':
    sub1 = Subscriber('fucker1')
    sub2 = Subscriber('fucker2')
    sub3 = Subscriber('fucker3')

    pub  = Publisher()
    pub.register(sub1)
    pub.register(sub2)
    pub.dispatch("go fuck!!")

