import logging
import sys
import time
from logging.handlers import SysLogHandler

from service import find_syslog, Service
import task


# class MyService(Service):
#     def __init__(self, *args, **kwargs):
#         super(MyService, self).__init__(*args, **kwargs)
#         self.logger.addHandler(SysLogHandler(address=find_syslog(),
#                                              facility=SysLogHandler.LOG_DAEMON))
#         self.logger.setLevel(logging.INFO)
#
#     def run(self):
#         task.task()


# def start():
#     if len(sys.argv) != 2:
#         sys.exit('Syntax: %s COMMAND' % sys.argv[0])
#
#     cmd = sys.argv[1].lower()
#     service = MyService('auto_change_dns', pid_dir='/tmp')
#
#     if cmd == 'start':
#         service.start()
#         time.sleep(1)
#         if service.is_running():
#             print("Service is running.")
#             print('pid: "%s"' % service.get_pid())
#             logging.info("Service is running.")
#             logging.info('pid: "%s"' % service.get_pid())
#         else:
#             logging.info('Service is stopping.')
#     elif cmd == 'stop':
#         service.stop()
#         time.sleep(1)
#         if service.is_running():
#             print("Service is running.")
#             print('pid: "%s"' % service.get_pid())
#         else:
#             print('Service is stopped.')
#             logging.info('Service is stopped.')
#     elif cmd == 'kill':
#         service.kill()
#         time.sleep(1)
#         if service.is_running():
#             print("Service is running.")
#             print('pid: "%s"' % service.get_pid())
#         else:
#             print('Service is stopped.')
#             logging.info('Service is stopped.')
#     elif cmd == 'status':
#         if service.is_running():
#             print("Service is running.")
#         else:
#             print("Service is not running.")
#
#     else:
#         sys.exit('Unknown command "%s".' % cmd)


if __name__ == '__main__':
    task.task()
    # 配置log
    # logging.basicConfig(filename="ddns.log", filemode="a", format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    #                     datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
    #
    #
    #
    # if len(sys.argv) != 2:
    #     sys.exit('Syntax: %s COMMAND' % sys.argv[0])
    #
    # cmd = sys.argv[1].lower()
    # service = MyService('my_service', pid_dir='/tmp')
    #
    # if cmd == 'start':
    #     service.start()
    # elif cmd == 'stop':
    #     service.stop()
    # elif cmd == 'kill':
    #     service.kill()
    # elif cmd == 'status':
    #     if service.is_running():
    #         print("Service is running.")
    #     else:
    #         print("Service is not running.")
    # else:
    #     sys.exit('Unknown command "%s".' % cmd)
