-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: defence_management
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `EquipmentID` int NOT NULL,
  `Type` varchar(255) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EquipmentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (1,'Assault Rifle','Available'),(2,'Submachine Gun','Available'),(3,'Sniper Rifle','Out of  Stock'),(4,'Shot Gun','Limited'),(5,'Pistol','Available'),(6,'Machine Gun','Available'),(7,'Bullet Proof Vest','Available'),(8,'Combat Helmet','Available'),(9,'Medical Kit','Available'),(10,'Night Vision goggles','Limited');
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logistics`
--

DROP TABLE IF EXISTS `logistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logistics` (
  `RequestID` int NOT NULL,
  `RequestedQuantity` int DEFAULT NULL,
  `DeliveryDate` date DEFAULT NULL,
  `PersonnelID` int DEFAULT NULL,
  `EquipmentID` int DEFAULT NULL,
  `UnitID` int DEFAULT NULL,
  PRIMARY KEY (`RequestID`),
  KEY `PersonnelID` (`PersonnelID`),
  KEY `EquipmentID` (`EquipmentID`),
  KEY `UnitID` (`UnitID`),
  CONSTRAINT `logistics_ibfk_1` FOREIGN KEY (`PersonnelID`) REFERENCES `personnel` (`PersonnelID`),
  CONSTRAINT `logistics_ibfk_2` FOREIGN KEY (`EquipmentID`) REFERENCES `equipment` (`EquipmentID`),
  CONSTRAINT `logistics_ibfk_3` FOREIGN KEY (`UnitID`) REFERENCES `units` (`UnitID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logistics`
--

LOCK TABLES `logistics` WRITE;
/*!40000 ALTER TABLE `logistics` DISABLE KEYS */;
INSERT INTO `logistics` VALUES (5,3,'2023-11-22',12,6,5),(6,1,'2023-11-22',12,8,5),(12,2,'2023-11-22',4,1,4);
/*!40000 ALTER TABLE `logistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `missions`
--

DROP TABLE IF EXISTS `missions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `missions` (
  `MissionID` int NOT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Description` text,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `UnitID` int DEFAULT NULL,
  PRIMARY KEY (`MissionID`),
  KEY `UnitID` (`UnitID`),
  CONSTRAINT `missions_ibfk_1` FOREIGN KEY (`UnitID`) REFERENCES `units` (`UnitID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `missions`
--

LOCK TABLES `missions` WRITE;
/*!40000 ALTER TABLE `missions` DISABLE KEYS */;
INSERT INTO `missions` VALUES (1,'Operation Alpha','Covert mission in enemy territory','2019-11-22','2024-11-11','Base A','Active',1),(2,'Reconnaissance Bravo','Gathering intel on enemy movements','2019-11-22','2022-11-01','Base B','Completed',2),(3,'Defense of Charlie Base','Protecting the base from potential threats','2017-11-12','2024-08-11','Base C','Active',3),(4,'Defense of Charlie Base','Protecting the base from potential threats','2017-11-12','2024-08-11','Base C','Active',4),(5,'Delta Strike','Swift and precise strike on enemy targets','2023-11-22','2025-12-23','Base D','Active',5);
/*!40000 ALTER TABLE `missions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personnel`
--

DROP TABLE IF EXISTS `personnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personnel` (
  `PersonnelID` int NOT NULL,
  `PersonnelName` varchar(255) DEFAULT NULL,
  `PersonnelRanking` varchar(50) DEFAULT NULL,
  `ContactInfo` varchar(255) DEFAULT NULL,
  `UnitID` int DEFAULT NULL,
  `MissionID` int DEFAULT NULL,
  `DeploymentHistory` text,
  PRIMARY KEY (`PersonnelID`),
  KEY `UnitID` (`UnitID`),
  KEY `MissionID` (`MissionID`),
  CONSTRAINT `personnel_ibfk_1` FOREIGN KEY (`UnitID`) REFERENCES `units` (`UnitID`),
  CONSTRAINT `personnel_ibfk_2` FOREIGN KEY (`MissionID`) REFERENCES `missions` (`MissionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personnel`
--

LOCK TABLES `personnel` WRITE;
/*!40000 ALTER TABLE `personnel` DISABLE KEYS */;
INSERT INTO `personnel` VALUES (1,'Smith','Captain','smith@usarmy',1,1,'missions x,y,z\nOngoing-operation Alpha'),(2,'Garrison','Soldier','Garrison@usarmy',1,1,'missions A\nOngoing-operation Alpha'),(3,'David','Soldier','David@usarmy',1,1,'Ongoing-operation Alpha'),(4,'Johnson','Major','Johnson@usarmy',2,2,'Missions a,b,c,d\nOngoing-Reconnaissance Bravo'),(5,'Mitchell','Soldier','Mitchell@usarmy',2,2,'Missions a,b,\nOngoing-Reconnaissance Bravo'),(6,'Patrick','Soldier','Patrick@usarmy',2,2,'\nOngoing-Reconnaissance Bravo'),(7,'Davis','Lieutenant ','Davis@usarmy',3,3,'Missions x,y\nOngoing-Reconnaissance Bravo'),(8,'Travis','Soldier','Travis@usarmy',3,3,'Missions x\nOngoing-Reconnaissance Bravo'),(9,'Alex','Soldier','Alex@usarmy',1,3,'Missions x,z\nOngoing-Reconnaissance Bravo'),(10,'Marsh','Captain','marsh@usarmy',4,4,'Missions x ,b,c\nOngoing-Defense of Charlie Base'),(11,'Mark','Soldier','mark@usarmy',4,4,'Missions x ,b,\nOngoing-Defense of Charlie Base'),(12,'Miller','Captain','miller@usarmy',5,5,'Missions x ,z,c,x,b\nOngoing-Delta Strike'),(13,'Markram','soldier','markram@usarmy',5,5,'Missions x ,z,\nOngoing-Delta Strike'),(14,'Jonty','soldier','jonty@usarmy',5,5,'\nOngoing-Delta Strike');
/*!40000 ALTER TABLE `personnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personnel_new`
--

DROP TABLE IF EXISTS `personnel_new`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personnel_new` (
  `PersonnelID` int NOT NULL AUTO_INCREMENT,
  `PersonnelName` varchar(255) DEFAULT NULL,
  `PersonnelRanking` varchar(50) DEFAULT NULL,
  `ContactInfo` varchar(255) DEFAULT NULL,
  `UnitID` int DEFAULT NULL,
  `MissionID` int DEFAULT NULL,
  `DeploymentHistory` text,
  PRIMARY KEY (`PersonnelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personnel_new`
--

LOCK TABLES `personnel_new` WRITE;
/*!40000 ALTER TABLE `personnel_new` DISABLE KEYS */;
/*!40000 ALTER TABLE `personnel_new` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainingcourses`
--

DROP TABLE IF EXISTS `trainingcourses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainingcourses` (
  `CourseID` int NOT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Description` text,
  `Instructor` varchar(255) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`CourseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainingcourses`
--

LOCK TABLES `trainingcourses` WRITE;
/*!40000 ALTER TABLE `trainingcourses` DISABLE KEYS */;
INSERT INTO `trainingcourses` VALUES (1,'Survival Skills','Learn essential survival skills in hostile environments','Lieutenant Johnson','2023-11-22','2023-11-30','Training room 1'),(2,'Tactical Leadership','Strategies for effective tactical leadership in the field','Captain Miller','2023-12-04','2023-12-11','Training room 4');
/*!40000 ALTER TABLE `trainingcourses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `units` (
  `UnitID` int NOT NULL,
  `UnitName` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `CommandingOfficer` varchar(255) DEFAULT NULL,
  `FormationDate` date DEFAULT NULL,
  PRIMARY KEY (`UnitID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
INSERT INTO `units` VALUES (1,'Alpha Company','BASE C','Captain Smith','2019-11-03'),(2,'Bravo Company','BASE B','Major Johnson','2019-08-13'),(3,'Charlie Company','BASE C','Lieutenant Davis','2017-08-09'),(4,'Charlie+ Company','BASE C','Captain Marsh','2017-08-09'),(5,'Delta Company','BASE D','Captain Miller','2014-05-12'),(6,'Example unit','BLR','CCCCCCCCC','2023-11-23');
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-24 12:28:45
