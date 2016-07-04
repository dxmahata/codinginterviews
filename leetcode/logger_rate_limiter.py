"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""

import collections

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__msg_set = set()
        self.__msg_queue = collections.deque()
        
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.__msg_queue and self.__msg_queue[0][0] <= timestamp - 10:
            element_for_removal = self.__msg_queue.popleft()
            self.__msg_set.remove(element_for_removal[1])
        if message in self.__msg_set:
            return False
        self.__msg_queue.append((timestamp, message))
        self.__msg_set.add(message)
        return True
        

if __name__ == "__main__":
    
    #Your Logger object will be instantiated and called as such:
    obj = Logger()
    print(obj.shouldPrintMessage(1, "foo"))
    print(obj.shouldPrintMessage(2, "bar"))
    print(obj.shouldPrintMessage(3, "foo"))
    print(obj.shouldPrintMessage(8, "bar"))
    print(obj.shouldPrintMessage(10, "foo"))
    print(obj.shouldPrintMessage(11, "foo"))