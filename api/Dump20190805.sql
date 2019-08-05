-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: virtual_interview_process
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `interviews`
--

DROP TABLE IF EXISTS `interviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interviews` (
  `interview_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `company` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `feedback` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `latest_round_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`interview_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interviews`
--

LOCK TABLES `interviews` WRITE;
/*!40000 ALTER TABLE `interviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `interviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(45) DEFAULT NULL,
  `difficulty` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT 'coding',
  `problem_statement` varchar(45) DEFAULT NULL,
  `test_cases` varchar(45) DEFAULT NULL,
  `score` int(11) DEFAULT '100',
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (7,'facebook','medium','coding','test','dcfd',100),(8,'facebook','medium','coding','test','dcfd',100),(9,'facebook','medium','coding','test','dcfd',100),(10,'facebook','medium','coding','test','dcfd',50),(11,'facebook','medium','coding','test','dcfd',80),(12,'facebook','easy','coding','test','dcfd',80),(13,'facebook','easy','coding','test','dcfd',80),(14,'facebook','easy','coding','test','dcfd',100),(15,'facebook','easy','coding','test','dcfd',10);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `round_details`
--

DROP TABLE IF EXISTS `round_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `round_details` (
  `round_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `start_time` int(11) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `total_score` int(11) NOT NULL,
  `type` varchar(45) DEFAULT 'coding',
  `company` varchar(45) NOT NULL,
  `no_of_questions` int(11) DEFAULT NULL,
  `achieved_score` int(11) DEFAULT '0',
  PRIMARY KEY (`round_id`),
  UNIQUE KEY `round_id_UNIQUE` (`round_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `round_details`
--

LOCK TABLES `round_details` WRITE;
/*!40000 ALTER TABLE `round_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `round_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `round_questions`
--

DROP TABLE IF EXISTS `round_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `round_questions` (
  `round_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`round_id`,`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `round_questions`
--

LOCK TABLES `round_questions` WRITE;
/*!40000 ALTER TABLE `round_questions` DISABLE KEYS */;
/*!40000 ALTER TABLE `round_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rounds`
--

DROP TABLE IF EXISTS `rounds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rounds` (
  `company` varchar(45) NOT NULL,
  `position` varchar(45) NOT NULL,
  `difficulty` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT 'coding',
  `no_of_questions` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`company`,`position`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rounds`
--

LOCK TABLES `rounds` WRITE;
/*!40000 ALTER TABLE `rounds` DISABLE KEYS */;
/*!40000 ALTER TABLE `rounds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `submissions`
--

DROP TABLE IF EXISTS `submissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `submissions` (
  `round_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `submission_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(45) DEFAULT NULL,
  `Code` varchar(45) NOT NULL,
  `score` int(11) DEFAULT '0',
  `submission_time` int(11) NOT NULL,
  `language` varchar(45) NOT NULL,
  PRIMARY KEY (`submission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submissions`
--

LOCK TABLES `submissions` WRITE;
/*!40000 ALTER TABLE `submissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `submissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `dob` date DEFAULT NULL,
  `college` varchar(60) DEFAULT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(60) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('vatsalsonigara','Vatsal Sonigara','1998-03-04','DJ Sanghvi','pass@123','vatsalsonigara@gmail.com'),('vatsalsonigara1','Vatsal Sonigara','1998-03-04','DJ Sanghvi','pass@123','vatsalsonigara@gmail.com'),('vatsalsonigara2','Vatsal Sonigara','1998-03-04','DJ Sanghvi','pass@123','vatsalsonigara@gmail.com'),('vatsalsonigara3','Vatsal Sonigara','1998-03-04','DJ Sanghvi','pass@123','vatsalsonigara@gmail.com'),('vatsalsonigara7','Vatsal Sonigara','1998-03-04','DJ Sanghvi','pass@123','vatsalsonigara@gmail.com'),('vatsalsonigara8','Vatsal Sonigara','1998-03-04','DJ Sanghvi','pass@123','vatsalsonigara@gmail.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-05 19:34:11
