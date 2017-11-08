from Pubtest import PubTest

def update(msg):
    print msg

pub  = PubTest()
pub.register(update)
pub.notify('yo')