import syslog
import sqlite3
from sqlite3 import Error
from datetime import datetime
import syslog
from urllib import request, parse

''' Breaks OCP

class Logger:
    def WriteLogToSystem(self, message):
        syslog.syslog(syslog.LOG_ERR, message)

class ErrorLogger(Logger):
    def WriteLogToFile(self, message):
        with open('log.txt','a') as writer:
            writer.write(message + '\n')
            writer.flush()

    def WriteLogToDB(self, message):
        con = sqlite3.connect('sqldb.db')
        sql = "insert into ErrorLog(Message) values ('{0}')".format(message)
        con.execute(sql)
        con.commit()

    #Write to log agggregator server (Violation of OCP)
    def WriteLogToServer(self, message):
        pass

'''

class Logger:
    def WriteLogToSystem(self, message):
        syslog.syslog(syslog.LOG_ERR, message)


class FileLogger(Logger):
    def WriteLogToFile(self, message):
        with open('log.txt','a') as writer:
            writer.write(message + '\n')
            writer.flush()

class DBLogger(Logger):
    
    def WriteLogToDB(self, message):
        con = sqlite3.connect('sqldb.db')
        sql = "insert into ErrorLog(Message) values ('{0}')".format(message)
        con.execute(sql)
        con.commit()

class ServerLogger(Logger):

    def WriteLogToServer(self, message):
        data = parse.urlencode(message).encode()
        req =  request.Request("https://log.myserver.com/error", data=data)
        resp = request.urlopen(req)


if __name__ == "__main__":

    '''Breaks OCP
    try:
        a = int(input('Enter Value for No1 : '))
        b = int(input('Enter Value for No2 : '))
        result = a / b
        print(f"{a} / {b} = {result}")
    except Exception as ex:
        el = ErrorLogger()
        message = f'From OCP.py Program:\nError : Error Occurred while performing calculations. please check the inputs\nDate Time: {datetime.now()}\n---------------------'
        el.WriteLogToSystem(message)
        el.WriteLogToFile(message)
        el.WriteLogToDB(message)
        print(f'Error : {message}')

    '''

    error_log = f"Some random error Log !"
    
    sys_log = Logger()
    sys_log.WriteLogToSystem(error_log)
    
    file_logger = FileLogger()
    file_logger.WriteLogToFile(error_log)

    db_logger = DBLogger()
    db_logger.WriteLogToDB(error_log)

    server_logger = ServerLogger()
    server_logger.WriteLogToServer(server_logger)

