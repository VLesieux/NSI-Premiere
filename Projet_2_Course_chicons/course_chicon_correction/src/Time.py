from collections import namedtuple

Time = namedtuple('Time', ['hours', 'minutes', 'seconds'])

def create (hours, minutes, seconds):
    """    
    :param hours: value of time in hours
    :type name: int
    :param minutes: value of time in minutes
    :type name: int
    :param seconds: value of time in seconds
    :type name: int
    :return: a new time for a competitor
    :rtype: Time
    :UC: hours > 0 
    """
    return Time(hours,minutes,seconds)

p=create(5,28,10)
#p.hours=5
#p[0]=5
q=create(5,28,12)
#q.seconds=12
#q[2]=12


def compare(time1,time2):
    '''
    Renvoie 1 si time1>time 2
    0 si time1=time2
    -1 si time1<time2
    '''
    if time1.hours==time2.hours:        
        if time1.minutes==time2.minutes:            
            return (time1.seconds>time2.seconds)-(time1.seconds<time2.seconds)        
        else:            
            return (time1.minutes>time2.minutes)-(time1.minutes<time2.minutes)        
    else:
        return (time1.hours>time2.hours)-(time1.hours<time2.hours)

#compare(q,p)=1
#compare(p,q)=-1
    
def to_string(time):
    return ' {hours}h {minutes}mn {seconds}s'.format(hours=time.hours,minutes=time.minutes,seconds=time.seconds)

#to_string(p)=' 5h 28mn 10s'
        