import threading


# But, of course, RLock grants permission to reacquire a lock only to the thread that has already acquired it!
lock_obj = threading.RLock()

print('Acquire 1st time')
lock_obj.acquire()  # acquire 1st time

print('Acquire 2st time')
lock_obj.acquire()  # if Lock(): don't release, acquire 2nd time - Deadlock

print('Releasing')
lock_obj.release()


# def reentrance():
#     print('start')
#     lock_obj.acquire()
#     print('Acquired')
#     # Don't release after
#     reentrance()  # Deadlock
#
#
# reentrance()
