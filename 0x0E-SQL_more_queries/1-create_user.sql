-- Create the user user_0d_1 with all privilage.
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILAGES
   ON *.*
   TO 'user_0d_1'@'localhost';
