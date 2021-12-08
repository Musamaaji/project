import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'Jarma',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS student(
        ID INT NOT NULL AUTO_INCREMENT,
        phone INT ,
        name VARCHAR(255),
        age INT,
        DOB INT,
        student_id VARCHAR(255),
        maritual_status VARCHAR(255),
        address VARCHAR(255),
        city VARCHAR(255),
        PRIMARY KEY(ID)

        
    )
    """
)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS card(
        ID INT NOT NULL AUTO_INCREMENT,
        STUDENT_NAME VARCHAR(255),
        SUBJECT VARCHAR(255),
        EXAM_NO VARCHAR(255),
        SCORE VARCHAR(255),
        PRIMARY KEY(ID)   
    )
    """
)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS recordcard(
        ID INT NOT NULL AUTO_INCREMENT,
        RECORD_NUMBER INT ,
        SUBJECT VARCHAR(255),
        NAME INT,
        SCORE INT,
        PRIMARY KEY(ID)   
    )
    """
)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS EXAM(
        ID INT NOT NULL AUTO_INCREMENT,
        SUBJECT VARCHAR(255),
        EXAM_NO VARCHAR(255),
        PRIMARY KEY(ID)
    ) 
    """  
)




