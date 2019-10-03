CREATE Database  api_svc ;

CREATE USER 'api753'@'%' IDENTIFIED BY 'api753_secret';

GRANT ALL PRIVILEGES ON *.* TO 'api753'@'%'
WITH
GRANT OPTION;

FLUSH PRIVILEGES;

USE  api_svc;

CREATE TABLE
IF NOT EXISTS  resource
(
   ExtID  int
(11) NOT NULL,
   Name  varchar
(50) CHARACTER
SET utf8
COLLATE utf8_general_ci NOT NULL,
   Value  varchar
(50) CHARACTER
SET utf8
COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB ;

CREATE TABLE
IF NOT EXISTS  users
(
   idUsers  int
(11) NOT NULL,
   FirstName  char
(50) NOT NULL,
   LastName  varchar
(45) NOT NULL,
   City  varchar
(45) NOT NULL,
   ZIP  varchar
(45) NOT NULL,
   ExtID  int
(11) DEFAULT NULL,
  PRIMARY KEY
( idUsers )
) ENGINE=InnoDB ;



INSERT INTO  users
  (
  idUsers , FirstName
  , LastName , City , ZIP , ExtID )
VALUES
  (1, "Lucky", "Luke", "Katy", "77450", 1974);
INSERT INTO  users
  (
  idUsers , FirstName
  , LastName , City , ZIP , ExtID )
VALUES
  (2, "Gimsy", "Bugzy", "Richardson", "34550", 2000);
INSERT INTO  users
  (
  idUsers , FirstName
  , LastName , City , ZIP , ExtID )
VALUES
  (3, "Jenny", "Jose", "Houston", "72000", 2019);

INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2000", "Role", "developer");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2000", "AccountNum", "22-3-1988");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2000", "Address", "281 Richardson Ln");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("1974", "HealtRecordNum", "20017_AB_3");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("1974", "BillingAddress", "531 Willow St #755");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("1974", "Role", "accountMng");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2019", "Math", "8.13");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2019", "Healt", "9.23");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2019", "Bio", "8.92");
INSERT INTO  resource
  (
  ExtID , Name
  , Value )
VALUES
  ("2019", "Geo", "9.55");

commit;