import cgi
import mysql.connector
datos = cgi.FieldStorage()
print('Content-Type: text/html')
print('<p>'+str(datos)+'</p>')

nombre=datos.getvalue('nombre')
contraseña =datos.getvalue('contra')
try:
    conex=mysql.connector.connect(database='usuarios', host='localhost',user='santiago', password='admin1234' )
    cursor = conex.cursor()
    insert = "insert into registrado (username,pass) values (%s,%s)"
    contraseña='sha('+contraseña+')' 
    cursor.execute(insert,(nombre,contraseña))
    cursor.commit()
    cursor.close()
    conex.close()
except mysql.connector.Error as e:
    print('<h1>Error: '+str(e)+'</h1>')
except:
    print('<h1>Error inesperado</h1>')
#print('<h1>This is my test! {}</h1>'.format(datos.getvalue('nombre')))
#print(datos.getvalue('nombre'))
