import pandas as pd
import cx_Oracle
conn =cx_Oracle.connect('SYSTEM/system@localhost/orcl')
cur =conn.cursor()

confirmtable=[]
recovertable=[]
deathtable=[]
datetable=[]
finalquerytable=[]



countrytable=[]
idtable=[]

table1=pd.read_csv('time_series_19-covid-Confirmed.csv', encoding= 'ISO-8859-1')
table1df = pd.DataFrame()
confirmed= table1df.append(table1,ignore_index=True)

table2=pd.read_csv('time_series_19-covid-Deaths.csv', encoding= 'ISO-8859-1')
table2df = pd.DataFrame()
death= table2df.append(table2,ignore_index=True)


table3=pd.read_csv('time_series_19-covid-Recovered.csv', encoding= 'ISO-8859-1')
table3df = pd.DataFrame()
recovery= table3df.append(table3,ignore_index=True)

#inner table requirement
for x,y in confirmed.iterrows():  
    temp=[y['1/22/2020'],y['1/23/2020'],y['1/24/2020'],y['1/25/2020'],y['1/26/2020'],y['1/27/2020'],y['1/28/2020'],y['1/29/2020'],y['1/30/2020'],y['1/31/2020'],y['2/1/2020'],y['2/2/2020'],y['2/3/2020'],y['2/4/2020'],y['2/5/2020'],y['2/6/2020'],y['2/7/2020'],y['2/8/2020'],y['2/9/2020'],y['2/10/2020'],y['2/11/2020'],y['2/12/2020'],y['2/13/2020'],y['2/14/2020'],y['2/15/2020'],y['2/16/2020'],y['2/17/2020'],y['2/18/2020'],y['2/19/2020'],y['2/20/2020'],
          y['2/21/2020'],y['2/22/2020'],y['2/23/2020'],y['2/24/2020'],y['2/25/2020'],y['2/26/2020'],y['2/27/2020'],y['2/28/2020'],y['2/29/2020'],y['3/1/2020'],y['3/2/2020'],y['3/3/2020'],y['3/4/2020'],y['3/5/2020'],y['3/6/2020'],y['3/7/2020'],y['3/8/2020'],y['3/9/2020'],y['3/10/2020'],y['3/11/2020'],y['3/12/2020'],y['3/13/2020'],y['3/14/2020'],y['3/15/2020'],y['3/16/2020'],y['3/17/2020'],y['3/18/2020'],y['3/19/2020'],y['3/20/2020'],y['3/21/2020']] 
    confirmtable.append(temp)

for x,y in death.iterrows():  
    temp=[y['1/22/2020'],y['1/23/2020'],y['1/24/2020'],y['1/25/2020'],y['1/26/2020'],y['1/27/2020'],y['1/28/2020'],y['1/29/2020'],y['1/30/2020'],y['1/31/2020'],y['2/1/2020'],y['2/2/2020'],y['2/3/2020'],y['2/4/2020'],y['2/5/2020'],y['2/6/2020'],y['2/7/2020'],y['2/8/2020'],y['2/9/2020'],y['2/10/2020'],y['2/11/2020'],y['2/12/2020'],y['2/13/2020'],y['2/14/2020'],y['2/15/2020'],y['2/16/2020'],y['2/17/2020'],y['2/18/2020'],y['2/19/2020'],y['2/20/2020'],
          y['2/21/2020'],y['2/22/2020'],y['2/23/2020'],y['2/24/2020'],y['2/25/2020'],y['2/26/2020'],y['2/27/2020'],y['2/28/2020'],y['2/29/2020'],y['3/1/2020'],y['3/2/2020'],y['3/3/2020'],y['3/4/2020'],y['3/5/2020'],y['3/6/2020'],y['3/7/2020'],y['3/8/2020'],y['3/9/2020'],y['3/10/2020'],y['3/11/2020'],y['3/12/2020'],y['3/13/2020'],y['3/14/2020'],y['3/15/2020'],y['3/16/2020'],y['3/17/2020'],y['3/18/2020'],y['3/19/2020'],y['3/20/2020'],y['3/21/2020']] 
    deathtable.append(temp)
    
for x,y in recovery.iterrows():  
    temp=[y['1/22/2020'],y['1/23/2020'],y['1/24/2020'],y['1/25/2020'],y['1/26/2020'],y['1/27/2020'],y['1/28/2020'],y['1/29/2020'],y['1/30/2020'],y['1/31/2020'],y['2/1/2020'],y['2/2/2020'],y['2/3/2020'],y['2/4/2020'],y['2/5/2020'],y['2/6/2020'],y['2/7/2020'],y['2/8/2020'],y['2/9/2020'],y['2/10/2020'],y['2/11/2020'],y['2/12/2020'],y['2/13/2020'],y['2/14/2020'],y['2/15/2020'],y['2/16/2020'],y['2/17/2020'],y['2/18/2020'],y['2/19/2020'],y['2/20/2020'],
          y['2/21/2020'],y['2/22/2020'],y['2/23/2020'],y['2/24/2020'],y['2/25/2020'],y['2/26/2020'],y['2/27/2020'],y['2/28/2020'],y['2/29/2020'],y['3/1/2020'],y['3/2/2020'],y['3/3/2020'],y['3/4/2020'],y['3/5/2020'],y['3/6/2020'],y['3/7/2020'],y['3/8/2020'],y['3/9/2020'],y['3/10/2020'],y['3/11/2020'],y['3/12/2020'],y['3/13/2020'],y['3/14/2020'],y['3/15/2020'],y['3/16/2020'],y['3/17/2020'],y['3/18/2020'],y['3/19/2020'],y['3/20/2020'],y['3/21/2020']] 
    recovertable.append(temp)  
    
datetable=['22-JAN-2020','23-JAN-2020','24-JAN-2020','25-JAN-2020','26-JAN-2020','27-JAN-2020','28-JAN-2020','29-JAN-2020','30-JAN-2020','31-JAN-2020','1-FEB-2020','2-FEB-2020','3-FEB-2020','4-FEB-2020','5-FEB-2020','6-FEB-2020','7-FEB-2020','8-FEB-2020','9-FEB-2020','10-FEB-2020','11-FEB-2020','12-FEB-2020','13-FEB-2020','14-FEB-2020','15-FEB-2020','16-FEB-2020','17-FEB-2020','18-FEB-2020','19-FEB-2020','20-FEB-2020',
          '21-FEB-2020','22-FEB-2020','23-FEB-2020','24-FEB-2020','25-FEB-2020','26-FEB-2020','27-FEB-2020','28-FEB-2020','29-FEB-2020','1-MAR-2020','2-MAR-2020','3-MAR-2020','4-MAR-2020','5-MAR-2020','6-MAR-2020','7-MAR-2020','8-MAR-2020','9-MAR-2020','10-MAR-2020','11-MAR-2020','12-MAR-2020','13-MAR-2020','14-MAR-2020','15-MAR-2020','16-MAR-2020','17-MAR-2020','18-MAR-2020','19-MAR-2020','20-MAR-2020','21-MAR-2020']


#maintable requirement
for x,y in confirmed.iterrows():  
    countrytable.append(y['Country'])

table4=pd.read_csv('id.csv', encoding= 'ISO-8859-1')
table4df = pd.DataFrame()
idtab= table4.append(table4,ignore_index=True)    
    
for x,y in idtab.iterrows():  
    idtable.append(y['cid'])   

#print countriea
#m=0
#while(m<482):
#    print(countrytable[m])
#    m=m+1

#file = open("testfile.txt","w") 
#m=0
#while(m<482):
#    l=0
#    while(l<60):
       
#        ara=countrytable[m]+"status_t('"+str(datetable[l])+"'"+","+str(confirmtable[m][l])+","+str(deathtable[m][l])+","+str(recovertable[m][l])+")"    
#        file.write(ara+"\r\n") 
#        l=l+1
                  
#    m=m+1
    
    
    
    











#file = open("testfile.txt","w") 
#m=0
#while(m<482):
#    l=0
    
#    while(l<60):
       
#        ara="status_t('"+str(datetable[l])+"'"+","+str(confirmtable[m][l])+","+str(deathtable[m][l])+","+str(recovertable[m][l])+")"    
#        statustable.append(ara)
#        l=l+1                  
#    m=m+1
    
#county=['srilanka','india']
    
#print("insert into covid19_all values(covid19_all_t("+str(idtable[2])+","+"'"+county[0]+"'"+","+"covid19_status_t("+statustable[0]+","+statustable[1]+","+statustable[2]+")))")  

    





m=0
while(m<482):
    statustable=[]
    l=0
    while(l<60):
       
        ara="status_t('"+str(datetable[l])+"'"+","+str(confirmtable[m][l])+","+str(deathtable[m][l])+","+str(recovertable[m][l])+")"    
        statustable.append(ara)
        l=l+1
                  
    
           
    finalquery="insert into covid19_all values(covid19_all_t("+str(idtable[m])+","+"'"+countrytable[m]+"'"+","+"covid19_status_t("+statustable[0]+","+statustable[1]+","+statustable[2]+","+statustable[3]+","+statustable[4]+","+statustable[5]+","+statustable[6]+","+statustable[7]+","+statustable[8]+","+statustable[9]+","+statustable[10]+","+statustable[11]+","+statustable[12]+","+statustable[13]+","+statustable[14]+","+statustable[15]+","+statustable[16]+","+statustable[17]+","+statustable[18]+","+statustable[19]+","+statustable[20]+","+statustable[21]+","+statustable[22]+","+statustable[23]+","+statustable[24]+","+statustable[25]+","+statustable[26]+","+statustable[27]+","+statustable[28]+","+statustable[29]+","+statustable[30]+","+statustable[31]+","+statustable[32]+","+statustable[33]+","+statustable[34]+","+statustable[35]+","+statustable[36]+","+statustable[37]+","+statustable[38]+","+statustable[39]+","+statustable[40]+","+statustable[41]+","+statustable[42]+","+statustable[43]+","+statustable[44]+","+statustable[45]+","+statustable[46]+","+statustable[47]+","+statustable[48]+","+statustable[49]+","+statustable[50]+","+statustable[51]+","+statustable[52]+","+statustable[53]+","+statustable[54]+","+statustable[55]+","+statustable[56]+","+statustable[57]+","+statustable[58]+","+statustable[59]+")))"     
    finalquerytable.append(finalquery)


    m=m+1
    
    
  






entertodb=0
while(entertodb<482):
    cur.execute(finalquerytable[entertodb])
    conn.commit()
    entertodb = entertodb + 1
    
    
 
 
    
 


