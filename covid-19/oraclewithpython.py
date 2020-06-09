import cx_Oracle
conn =cx_Oracle.connect('SYSTEM/system@localhost/orcl')
cur =conn.cursor()


#insert single
#cur.execute("INSERT INTO student_t_l3 VALUES ('S004', 'medika','16-AUG-1972')")
#conn.commit()



# Insert default rows
#rows = [('S005', 'Kim','16-FEB-1999'),('S006', 'Jhn','10-MAR-1909')]
#cur.executemany("insert into student_t_l3(sno, sname,dob) values (:1, :2, :3)",rows)
#conn.commit()



#select all
#cur.execute('select * from student_t_l3 s')
#for line in cur:
#        print(line)
#cur.close()
#conn.close()



#select member function
#cur.execute('select s.age() from student_t_l3 s')
#for line in cur:
#        print(line[0])
#cur.close()
#conn.close()



#delete
#cur.execute("delete student_t_l3 s where s.sno='S006'")
#conn.commit()
#cur.close()
#conn.close()



