import pymysql

conn = pymysql.connect(host='127.0.0.1', user ='root', password ='XXXX', db ='soloDB', charset ='utf8')


cur = conn.cursor()
#데이터베이스에 SQL 문을 실행하거나 실행된 결과 돌려받는 통로

cur.execute("CREATE TABLE userTable(id char(4), userName char(15),email char(20),birthYear int)")
#테이블을 만드는 SQL 문 : 커서 이름 .execute


