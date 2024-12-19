CREATE DATABASE  IF NOT EXISTS `systemsusers` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `systemsusers`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: systemsusers
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `apprentice`
--

DROP TABLE IF EXISTS `apprentice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apprentice` (
  `apprentice_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `ficha_id` int NOT NULL,
  `state_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`apprentice_id`),
  KEY `fk_users_apprentice` (`user_id`),
  KEY `fk_fichas_apprentice` (`ficha_id`),
  KEY `fk_subitems_apprentice` (`state_id`),
  CONSTRAINT `fk_fichas_apprentice` FOREIGN KEY (`ficha_id`) REFERENCES `fichas` (`ficha_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_subitems_apprentice` FOREIGN KEY (`state_id`) REFERENCES `sub_items` (`sub_items_id`),
  CONSTRAINT `fk_users_apprentice` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apprentice`
--

LOCK TABLES `apprentice` WRITE;
/*!40000 ALTER TABLE `apprentice` DISABLE KEYS */;
/*!40000 ALTER TABLE `apprentice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assign_ficha_instructor`
--

DROP TABLE IF EXISTS `assign_ficha_instructor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assign_ficha_instructor` (
  `assign_ficha_instructor_id` int NOT NULL AUTO_INCREMENT,
  `instructor_id` int NOT NULL,
  `ficha_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`assign_ficha_instructor_id`),
  KEY `fk_fichas_assign_instructor` (`instructor_id`),
  CONSTRAINT `fk_fichas_assign_instructor` FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`instructor_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assign_ficha_instructor`
--

LOCK TABLES `assign_ficha_instructor` WRITE;
/*!40000 ALTER TABLE `assign_ficha_instructor` DISABLE KEYS */;
INSERT INTO `assign_ficha_instructor` VALUES (1,1,1,1,'2024-03-18 14:22:18','2024-03-18 14:22:18'),(2,1,2,1,'2024-03-18 14:37:31','2024-03-18 14:37:31'),(4,1,3,0,'2024-03-18 15:57:00','2024-03-18 16:01:09'),(5,2,3,1,'2024-04-01 14:30:01','2024-04-01 14:30:01');
/*!40000 ALTER TABLE `assign_ficha_instructor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `apprentice_attendance_id` int NOT NULL AUTO_INCREMENT,
  `apprentice_id` int NOT NULL,
  `ficha_id` int NOT NULL,
  `state_attendance` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`apprentice_attendance_id`),
  KEY `fk_attendance_apprenticce` (`apprentice_id`),
  KEY `fk_attendance_ficha` (`ficha_id`),
  KEY `fk_attendance_subitems` (`state_attendance`),
  CONSTRAINT `fk_attendance_apprenticce` FOREIGN KEY (`apprentice_id`) REFERENCES `apprentice` (`apprentice_id`),
  CONSTRAINT `fk_attendance_ficha` FOREIGN KEY (`ficha_id`) REFERENCES `fichas` (`ficha_id`),
  CONSTRAINT `fk_attendance_subitems` FOREIGN KEY (`state_attendance`) REFERENCES `sub_items` (`sub_items_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fichas`
--

DROP TABLE IF EXISTS `fichas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fichas` (
  `ficha_id` int NOT NULL AUTO_INCREMENT,
  `program_id` int NOT NULL,
  `number_ficha` bigint NOT NULL,
  `alias` varchar(50) NOT NULL,
  `status_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ficha_id`),
  KEY `fk_fichas_programs` (`program_id`),
  KEY `fk_fichas_subitems` (`status_id`),
  CONSTRAINT `fk_fichas_programs` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`),
  CONSTRAINT `fk_fichas_subitems` FOREIGN KEY (`status_id`) REFERENCES `sub_items` (`sub_items_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fichas`
--

LOCK TABLES `fichas` WRITE;
/*!40000 ALTER TABLE `fichas` DISABLE KEYS */;
INSERT INTO `fichas` VALUES (1,1,2672190,'TS35',4,1,'2024-02-22 11:33:48','2024-02-22 11:33:48'),(2,1,267190,'TS36',4,1,'2024-02-22 16:30:00','2024-03-18 14:39:06'),(3,1,25888,'TS6',4,1,'2024-03-14 10:18:29','2024-03-19 09:25:11');
/*!40000 ALTER TABLE `fichas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `function_group_relation`
--

DROP TABLE IF EXISTS `function_group_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `function_group_relation` (
  `function_group_relation_id` int NOT NULL AUTO_INCREMENT,
  `function_group_id` int NOT NULL,
  `function_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`function_group_relation_id`),
  KEY `fk_fgr_function` (`function_group_id`),
  KEY `fk_fgr_function_group` (`function_id`),
  CONSTRAINT `fk_fgr_function` FOREIGN KEY (`function_group_id`) REFERENCES `function_groups` (`function_group_id`),
  CONSTRAINT `fk_fgr_function_group` FOREIGN KEY (`function_id`) REFERENCES `functions` (`function_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `function_group_relation`
--

LOCK TABLES `function_group_relation` WRITE;
/*!40000 ALTER TABLE `function_group_relation` DISABLE KEYS */;
INSERT INTO `function_group_relation` VALUES (1,1,1,1,'2024-01-29 14:05:24','2024-01-29 14:05:24'),(2,1,2,1,'2024-01-29 14:05:24','2024-01-29 14:05:24'),(3,1,3,1,'2024-03-07 23:31:42','2024-03-07 23:31:42'),(4,1,13,1,'2024-03-07 23:34:47','2024-03-07 23:34:47'),(5,1,10,1,'2024-03-07 23:35:15','2024-03-07 23:35:15'),(6,1,7,1,'2024-03-07 23:35:52','2024-03-07 23:35:52'),(7,1,17,1,'2024-03-07 23:56:58','2024-03-07 23:56:58'),(8,1,14,1,'2024-03-07 23:56:58','2024-03-07 23:56:58'),(9,1,4,1,'2024-03-12 11:12:45','2024-03-12 11:12:45'),(10,1,5,1,'2024-03-12 11:12:45','2024-03-12 11:12:45'),(11,1,6,1,'2024-03-12 11:12:45','2024-03-12 11:12:45'),(12,1,8,1,'2024-03-12 11:12:45','2024-03-12 11:12:45'),(13,1,9,1,'2024-03-12 11:12:45','2024-03-12 11:12:45'),(14,1,11,1,'2024-03-12 11:22:43','2024-03-12 11:22:43'),(15,1,12,1,'2024-03-12 11:22:43','2024-03-12 11:22:43'),(16,1,18,1,'2024-03-12 11:22:43','2024-03-12 11:22:43'),(17,1,19,1,'2024-03-12 11:22:43','2024-03-12 11:22:43'),(18,1,20,1,'2024-03-12 11:26:47','2024-03-12 11:26:47'),(19,1,21,1,'2024-03-13 11:58:41','2024-03-13 11:58:41'),(20,1,22,1,'2024-03-14 09:50:03','2024-03-14 09:50:03'),(21,1,23,1,'2024-03-14 09:53:20','2024-03-14 09:53:20'),(22,1,24,1,'2024-03-14 09:53:20','2024-03-14 09:53:20'),(23,1,25,1,'2024-03-14 09:53:20','2024-03-14 09:53:20'),(24,1,26,1,'2024-03-14 10:21:38','2024-03-14 10:21:38'),(25,1,27,1,'2024-03-14 10:24:16','2024-03-14 10:24:16'),(26,1,28,1,'2024-03-15 18:22:25','2024-03-15 18:22:25'),(27,1,29,1,'2024-03-18 15:40:55','2024-03-18 15:40:55'),(28,1,30,1,'2024-03-31 11:53:39','2024-03-31 11:53:39'),(29,1,31,1,'2024-03-31 11:57:21','2024-03-31 11:57:21'),(30,1,32,1,'2024-04-01 15:01:38','2024-04-01 15:01:38'),(31,1,34,1,'2024-04-01 15:25:14','2024-04-01 15:25:14'),(32,1,35,1,'2024-04-01 15:25:14','2024-04-01 15:25:14'),(33,1,36,1,'2024-04-01 20:32:52','2024-04-01 20:32:52'),(34,1,37,1,'2024-04-07 13:07:31','2024-04-07 13:07:31');
/*!40000 ALTER TABLE `function_group_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `function_groups`
--

DROP TABLE IF EXISTS `function_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `function_groups` (
  `function_group_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`function_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `function_groups`
--

LOCK TABLES `function_groups` WRITE;
/*!40000 ALTER TABLE `function_groups` DISABLE KEYS */;
INSERT INTO `function_groups` VALUES (1,'FUNCTIONS_ROUTE',1,'2024-01-29 14:05:07','2024-02-03 21:30:36'),(2,'FUNCTIONS_ADMIN',1,'2024-02-01 16:24:45','2024-02-26 15:35:03'),(3,'FUNCTIONS_INSTRUCTOR',1,'2024-02-07 10:01:24','2024-02-26 15:35:03'),(4,'FUNCTIONS_APRENDIZ',1,'2024-02-07 10:54:06','2024-02-26 15:35:03');
/*!40000 ALTER TABLE `function_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `functions`
--

DROP TABLE IF EXISTS `functions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `functions` (
  `function_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `path` varchar(50) NOT NULL,
  `method` varchar(50) NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`function_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `functions`
--

LOCK TABLES `functions` WRITE;
/*!40000 ALTER TABLE `functions` DISABLE KEYS */;
INSERT INTO `functions` VALUES (1,'REGISTER_USER_ROLE','/user_rol/register','POST',1,'2024-01-29 14:04:46','2024-02-01 16:28:44'),(2,'REGISTER_USER','/user/register','POST',1,'2024-01-29 14:04:46','2024-03-07 20:21:02'),(3,'REGISTER_FUNCTION','/function/register','POST',1,'2024-01-30 10:42:01','2024-02-01 16:28:44'),(4,'DESACTIVATE-USER-ROLE','/user_rol/delete','POST',1,'2024-01-30 15:06:05','2024-01-30 15:06:05'),(5,'GET-USER-ROLE','/user_rol/list','GET',1,'2024-01-30 15:12:33','2024-01-30 15:12:33'),(6,'UPDATE-USER-ROLE','/user_rol/update','PUT',1,'2024-01-30 15:13:00','2024-01-30 15:13:00'),(7,'GET-FUNCTION','/function/list','GET',1,'2024-01-30 15:13:50','2024-01-30 15:13:50'),(8,'UPDATE-FUNCTION','/function/update','PUT',1,'2024-01-30 15:16:29','2024-01-30 15:16:29'),(9,'DESACTIVATE-FUNCTION','/function/delete','POST',1,'2024-01-30 15:19:57','2024-04-01 14:50:31'),(10,'REGISTER-FUNCTION-GROUP','/function_group/register','POST',1,'2024-01-30 15:23:22','2024-04-01 14:52:01'),(11,'GET-FUNCTION-GROUP','/function_group/list','GET',1,'2024-01-30 15:24:08','2024-01-30 15:24:08'),(12,'UPDATE-FUNCTION-GROUP','/function_group/update','PUT',1,'2024-01-30 15:24:40','2024-01-30 15:24:40'),(13,'REGISTER-FUNCTION-RELATION','/function_group/function_assign','POST',1,'2024-02-05 11:10:16','2024-02-05 11:10:16'),(14,'GET-FUNCTION-RELATION','/function_group/get_function_relation','GET',1,'2024-02-05 11:13:40','2024-02-05 11:13:40'),(17,'USER-PERMISSION-ASSING','/user/function_asign','POST',1,'2024-02-15 18:49:57','2024-02-15 18:49:57'),(18,'REGISTER_NEW_FICHA','/fichas/register_ficha','POST',1,'2024-02-26 13:34:32','2024-03-07 23:33:19'),(19,'CHANGE_STATUS_FICHA','/fichas/change_status','POST',1,'2024-03-07 23:32:06','2024-03-07 23:32:06'),(20,'GET_FICHAS_ASIGNED_INSTRUCTOR','/instructor/get_fichas_asigned_instructor','POST',1,'2024-03-12 11:11:19','2024-03-18 15:59:29'),(21,'ASSIGN_PERMISSION_USER','/user/user_permission_assign','POST',1,'2024-03-13 11:57:59','2024-03-13 11:57:59'),(22,'GET_USER','/user/list','GET',1,'2024-03-14 09:49:09','2024-03-14 09:49:09'),(23,'REGISTER_INSTRUCTOR','/instructor/register','POST',1,'2024-03-14 09:51:24','2024-03-14 09:51:24'),(24,'GET_INSTRUCTORS','/instructor/list','GET',1,'2024-03-14 09:52:19','2024-03-14 09:52:19'),(25,'DESACTIVATE_INSTRUCTORS','/instructor/delete','POST',1,'2024-03-14 09:52:50','2024-03-14 09:52:50'),(26,'GET_FICHAS','/fichas/list','GET',1,'2024-03-14 10:21:17','2024-03-14 10:21:17'),(27,'GET_STATUS_FICHA','/fichas/get_status','GET',1,'2024-03-14 10:24:05','2024-03-14 10:24:05'),(28,'GET_FICHAS_ASIGNED_INSTRUCTOR','/instructor/get_fichas_asigned_instructor','POST',1,'2024-03-15 18:22:04','2024-03-15 18:22:04'),(29,'ASSIGN_FICHAS','/instructor/assign_ficha','POST',1,'2024-03-18 15:40:43','2024-03-18 15:40:43'),(30,'DESACTIVATE_USER','/user/delete_user','POST',1,'2024-03-31 11:53:15','2024-03-31 11:53:15'),(31,'UPDATE_USER','/user/update_user','PUT',1,'2024-03-31 11:57:10','2024-03-31 11:57:10'),(32,'DESACTIVATE-FUNCTION-GROUP','/function_group/delete','POST',1,'2024-04-01 15:01:26','2024-04-01 15:01:26'),(33,'REGISTER_PROGRAM','/programs/list','POST',0,'2024-04-01 15:23:45','2024-04-01 15:24:30'),(34,'GET_PROGRAMS','/programs/list','GET',1,'2024-04-01 15:24:19','2024-04-01 15:24:19'),(35,'REGISTER_PROGRAM','/program/register_program','POST',1,'2024-04-01 15:25:02','2024-04-01 15:25:02'),(36,'DESACTIVATE_PROGRAM','/programs/delete','POST',1,'2024-04-01 20:32:23','2024-04-01 20:32:23'),(37,'MASSIVE_USER_INSERTION','/user/insert_masive','POST',1,'2024-04-07 13:07:18','2024-04-08 01:03:30');
/*!40000 ALTER TABLE `functions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `functions_group_auth_role`
--

DROP TABLE IF EXISTS `functions_group_auth_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `functions_group_auth_role` (
  `function_auth_role_id` int NOT NULL AUTO_INCREMENT,
  `user_role_id` int NOT NULL,
  `function_group_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`function_auth_role_id`),
  KEY `fk_auth_role` (`user_role_id`),
  KEY `fk_auth_role_function` (`function_group_id`),
  CONSTRAINT `fk_auth_role` FOREIGN KEY (`user_role_id`) REFERENCES `users_roles` (`user_role_id`),
  CONSTRAINT `fk_auth_role_function` FOREIGN KEY (`function_group_id`) REFERENCES `function_groups` (`function_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `functions_group_auth_role`
--

LOCK TABLES `functions_group_auth_role` WRITE;
/*!40000 ALTER TABLE `functions_group_auth_role` DISABLE KEYS */;
INSERT INTO `functions_group_auth_role` VALUES (1,1,1,1,'2024-01-29 14:06:01','2024-01-29 14:06:01');
/*!40000 ALTER TABLE `functions_group_auth_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instructor`
--

DROP TABLE IF EXISTS `instructor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `instructor` (
  `instructor_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`instructor_id`),
  KEY `fk_users_instructor` (`user_id`),
  CONSTRAINT `fk_users_instructor` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instructor`
--

LOCK TABLES `instructor` WRITE;
/*!40000 ALTER TABLE `instructor` DISABLE KEYS */;
INSERT INTO `instructor` VALUES (1,7,1,'2024-03-15 11:17:08','2024-03-15 11:17:08'),(2,8,1,'2024-04-01 14:29:11','2024-04-01 14:29:11');
/*!40000 ALTER TABLE `instructor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(50) DEFAULT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'Type Document',1,'2024-01-26 22:08:17','2024-04-01 17:58:04'),(2,'State Ficha',1,'2024-01-26 22:08:17','2024-01-26 22:08:17'),(3,'State Apprentice',1,'2024-01-26 22:08:17','2024-04-01 17:58:04');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `programs`
--

DROP TABLE IF EXISTS `programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `programs` (
  `program_id` int NOT NULL AUTO_INCREMENT,
  `name_program` varchar(200) NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programs`
--

LOCK TABLES `programs` WRITE;
/*!40000 ALTER TABLE `programs` DISABLE KEYS */;
INSERT INTO `programs` VALUES (1,'TECNICO EN PROGRAMACION DE SOFTWARE',1,'2024-02-20 09:36:42','2024-04-01 17:58:47'),(3,'Tecnico en procesos de manofactura',0,'2024-04-01 15:42:02','2024-04-01 20:34:10'),(4,'TECNICO COCINA INTERNACIONAL',1,'2024-04-01 15:50:29','2024-04-01 15:50:29');
/*!40000 ALTER TABLE `programs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_items`
--

DROP TABLE IF EXISTS `sub_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sub_items` (
  `sub_items_id` int NOT NULL AUTO_INCREMENT,
  `item_id` int NOT NULL,
  `description` varchar(50) NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`sub_items_id`),
  KEY `fk_sub_items` (`item_id`),
  CONSTRAINT `fk_sub_items` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_items`
--

LOCK TABLES `sub_items` WRITE;
/*!40000 ALTER TABLE `sub_items` DISABLE KEYS */;
INSERT INTO `sub_items` VALUES (1,1,'CC',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(2,1,'CE',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(3,1,'PEP',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(4,2,'FORMACION',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(5,2,'FINALIZADA',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(6,2,'CANCELADA',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(7,3,'FORMACION',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(8,3,'MATRICULADO',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(9,3,'CANCELADO',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(10,3,'FINALIZADO',1,'2024-01-26 22:10:43','2024-01-26 22:10:43'),(11,1,'TARJETA DE IDENTIDAD',1,'2024-04-07 12:26:32','2024-04-07 12:26:32');
/*!40000 ALTER TABLE `sub_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_permission`
--

DROP TABLE IF EXISTS `user_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_permission` (
  `user_permission_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `function_id` int NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_permission_id`),
  KEY `fk_user_function_permison` (`user_id`),
  KEY `fk_function_permison_id` (`function_id`),
  CONSTRAINT `fk_function_permison_id` FOREIGN KEY (`function_id`) REFERENCES `functions` (`function_id`),
  CONSTRAINT `fk_user_function_permison` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_permission`
--

LOCK TABLES `user_permission` WRITE;
/*!40000 ALTER TABLE `user_permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `type_doc` int NOT NULL,
  `document` bigint NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `number` bigint NOT NULL,
  `user_role_id` int NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  KEY `fk_users_roles` (`user_role_id`),
  KEY `fk_users_subitems` (`type_doc`),
  CONSTRAINT `fk_users_roles` FOREIGN KEY (`user_role_id`) REFERENCES `users_roles` (`user_role_id`),
  CONSTRAINT `fk_users_subitems` FOREIGN KEY (`type_doc`) REFERENCES `sub_items` (`sub_items_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,1,1043664494,'Eyner','Acosta','eyneracosta96@gmail.com',3103533759,1,'eyner_03','scrypt:32768:8:1$S66c8W0XVbxuFr6k$7bf0d34514413cb273020e955c00a451d9771d10fb34e36e1b820a3805caa49bac8d8a9b07035d115ebc3cc62c06e2bceae4a1c8068c4bde26072ae43bab2e52',1,'2024-01-26 22:13:05','2024-01-28 11:54:56'),(6,2,1043664494,'juan','Misat','eynerdsjdj@gmail.com',3105893759,1,'juan12355','scrypt:32768:8:1$y3CCexIc9HU4WyKM$280654d570a2655c3e5f4a08476c5ee8a6c433415b6a6b7d3a9f12ad02131422a34d17e489b21c3ebdba53cb042977539c99cd9890850724ad23db78ddc40c17',1,'2024-03-07 20:04:56','2024-03-07 20:04:56'),(7,2,1043664494,'juan','Misat','eynerdsjdj@gmail.com',3105893759,2,'juan1258','scrypt:32768:8:1$En6PcD9oaOgio7DO$6823d130c9001f76ba7795e909fbd813cb2965a7e033b8fd2232bbb7f5edc86438bba1843a085142f10b9234831a0c013bac6c768f9f0a1712b7cb7d0dd6c910',1,'2024-03-09 10:26:50','2024-03-09 10:26:50'),(8,2,1055555,'carlos','perez','carlos@gmail.com',45,2,'carlos6','$6823d130c9001f76ba7795e909fbd813cb2965a7e033b8fd2232bbb7f5edc86438bba1843a085142f10b9234831a0c013bac6c768f9f0a1712b7cb7d0dd6c910',1,'2024-03-18 16:50:02','2024-03-18 16:50:02'),(9,3,2672190,'carlos','Perez','perezc@gmail.com',3207611081,3,'carlos12','scrypt:32768:8:1$ynij7ozCqTglZvwv$a5b73ac23046702a64ce55b62e7711d4ec5c6e2cdb564e07a10c7f8851e59eb9d92379ec34e95728823928a7b97bd42ef9ee842d1ec5d3bd47740b9460bcafea',0,'2024-03-31 11:47:53','2024-03-31 11:53:48'),(10,1,231121,'chupa','misat','chuapa@gmail.com',232515,3,'chupa','scrypt:32768:8:1$QIuIyKhO9Ep8W1d9$000f884bd702fcc9756fd539d86d34a1a6ec075ce28f98022c979d655ca937d62aeeb9bdadeee4fa4a0e851f2e9d4921dc294a185578de83578045f42567f041',1,'2024-04-08 00:39:20','2024-04-08 00:39:20'),(11,11,5655,'sharol','acosta','sharol@gmial.com',685446,2,'sharol','scrypt:32768:8:1$mo9DOiv8ZSjtX878$17d9a1a3684e01b0d3ca0566c31a297bdb26cf77092e3e6ef400e368c380dc48bb01dc14f314b264c2a58c887f39dac6a848aa42980c3905c30f48f36ad5c1c8',1,'2024-04-08 00:39:20','2024-04-08 00:39:20'),(12,1,231121,'andres','misat','andres@gmail.com',232515,3,'andres12','scrypt:32768:8:1$N6oLKRsUcqAuuCEX$ca9c3c6c7a4bb013b5f3e7c9198263554f5b432fd1abb335b7022a1fb5cf90d435ceb2108734efdec9e7ed730bd0d1d2918b0dc739656f88b252687441f82e64',1,'2024-04-08 00:42:59','2024-04-08 00:42:59'),(13,3,5655,'yuris','acosta','yuris@gmial.com',685446,2,'yuris89','scrypt:32768:8:1$12fdxE1wSajycFNP$ec249aa5fa0644199981c4183f9ebe8434f5d47d577c61be401461ccab5f4e985ecd495bd6e6e9fd7abecf8193ecb26fc9b85421ce9c03e61af0c977aa04fd1d',1,'2024-04-08 00:42:59','2024-04-08 00:42:59'),(14,3,231121,'diego','costa','costad@gmail.com',232515,3,'costa56','scrypt:32768:8:1$m1gjQ1k99ZGUupvr$8d536376101d6d939e7feb32d043cad2316393a97ee7cef2968c0e574e942d4839bb4674d0217851ecea05e315f96ffe039839b3c10351bf411968948e9714b2',1,'2024-04-08 14:46:24','2024-04-08 14:46:24'),(15,2,555655,'david','rangel','rangel@gmial.com',685446,2,'david34','scrypt:32768:8:1$Pt2UftfVcVpQCxpe$5479e77377472f8718c8bc5db135a226b3c877774ce09a26a20959838117a2337e99b36807601d1792fb027e9d510d3d8148f62f297b18816bb570f4f63c3cfb',1,'2024-04-08 14:46:24','2024-04-08 14:46:24'),(16,1,99898,'juan','pablo','pablojuan@gmail.com',98797,3,'pablo98','scrypt:32768:8:1$Lf4DNJKZyrJW6TVm$492b68f7ba059eb8582c96fe329fd9687b9d7c32fae41a451dbabd09700f479ea49a20532ee883a5a7aa62827f02f6cb17c1468f1587728186f7b95230f3eb03',0,'2024-04-08 14:46:24','2024-04-08 14:50:16'),(17,1,1043664494,'eyner','misat','eyner123@gmail.com',98989898,3,'eyner_656','scrypt:32768:8:1$jY10Oeae5r5GTRCK$f0a8f4e39827b28ec7b48f6a0ac01c1b1076c04b63c614c988b97cb0372d1635e010b56eb38c5711ec2cb6bf8c39f9887091fcad5eabfdd11298642048654c88',1,'2024-04-08 21:14:28','2024-04-08 21:14:28'),(18,3,1043664494,'eyner','misat','eyner123@gmail.com',98989898,3,'hjghh','scrypt:32768:8:1$iwl8mRzu8m3CJ7La$2be015740d2556bb11fced21e69a77ed5e46bd70d75964e5c9067035a87320b008f2ddfe48b404170e99c8a75d44f24371a8d5d2dbcc418d31f5398f06041f94',1,'2024-04-08 21:28:14','2024-04-08 21:28:14'),(19,3,9558898,'bhbhjbhj',' hjbhjbhj','bhjhjhjbhj@gmail',99999999,3,'eynnnn9','scrypt:32768:8:1$QnO8tt1ctZDavdRO$d127b7cbf452982478b81e35b08d76c24536eb4f6edab4b45d60d0376af0af26f17450f4e170b0ab004092ee248d227bbd8730880e622d2243e2c41720e76a6d',1,'2024-04-08 21:31:48','2024-04-08 21:31:48'),(20,11,9558898,'bhbhjbhj','misat','eyner123@gmail.com',98989898,3,'eyner_89','scrypt:32768:8:1$Ji4kjiPpyJqmeXvs$95cf5a15be076eb21253e8d76d33bac6f37cad8081e341337eab4532f65db1daca46b931c7668b884c7b11e598d4bfc6d054e3074f8b4b40a5b24a62794b142e',1,'2024-04-08 21:48:51','2024-04-08 21:48:51'),(21,1,1043664494,'bhbhjbhj','misat','eyner123@gmail.com',98989898,3,'eyner_56','scrypt:32768:8:1$JrEFfI8GUdpszDiO$9617849daec79733a225134d84420acbf1c9e5a8ea497a76b81bca9913f8b54fd49eb4a8242d0ee4a4a906086f79d67173e10f23ba6883ca73f1121a9a089cad',1,'2024-04-08 21:50:28','2024-04-08 21:50:28'),(22,1,1043664494,'eyner','misat','eyner123@gmail.com',99999999,3,'eyner_03','scrypt:32768:8:1$OijkRymAAaShiFhz$d603b0cb5c8df06946d80cb77f7d5fac469e2f97b5079bf953b3b7c453505337f6dc9990bcc361602471ef19949aafc715dcb482d9544967f3c79262da3daa96',1,'2024-04-08 22:03:00','2024-04-08 22:03:00'),(23,1,1043664494,'eyner','misat','eyner123@gmail.com',99999999,3,'eyner_0389','scrypt:32768:8:1$VNaCscfqZri0WGfs$a8f6d64d4fd189cf3a265b2fda521f2ef0ad50b2c2067970b919cc8eda06b377cd16213b04619555c48025ddce281587a83014197cd035d8aea0dc88629d4675',1,'2024-04-08 23:20:10','2024-04-08 23:20:10'),(24,1,1043664494,'eyner','misat','eyner123@gmail.com',99999999,3,'eyner_038988','scrypt:32768:8:1$dB1R9j1xqUH5rT1a$127b29a7600cd0b2e71b597bcc24d1a779a1e4fea2f0f29a44c84c398409117eecbad43c58add4d3b870f1f675f99894e3b90e51d59999e9072d93c1e7835655',1,'2024-04-08 23:21:12','2024-04-08 23:21:12'),(25,1,1043664494,'eyner','misat','eyner123@gmail.com',98989898,3,'eyner_0356','scrypt:32768:8:1$8EU5zRe4hVTPIr01$90d21c3334d7fe9445a38ff52846534ef9b6d0fbb3f16a186392a1277e6523d11917df1224efc35fa3ba567c36e36503719c0fc1c18b14510a85ea9bdafc4575',1,'2024-04-09 15:59:05','2024-04-09 15:59:05'),(26,1,1043664494,'eyner','misat','eyner123@gmail.com',98989898,3,'eyner_03898823','scrypt:32768:8:1$IvliAv7m1pUPSNsO$c3423b8aa7f77906aa77fbb8d20dd1f29583d72e9853019356d033927c26990c9c7135455ad84aeca0915bfadaf65050d754f84a0f5b2e089112ba15b47d1401',1,'2024-04-09 16:02:45','2024-04-09 16:02:45'),(27,1,1043664494,'eyner','misat','eyner123@gmail.com',99999999,3,'eyner_035555','scrypt:32768:8:1$0oFaIs4GTmEK4Lh1$b88676d268c3274e9f7556ce6499a4d6ddecae3b401786e91333d72803cd15ecfbcfd8767d7f2e7ea395c23a2b3415a6f42b0aa85b49a9169890d414e973c542',1,'2024-04-09 16:21:08','2024-04-09 16:21:08'),(28,1,1043664494,'eyner','misat','eyner123@gmail.com',98989898,3,'eyner_0382.2','scrypt:32768:8:1$yGp9juP82agIu07Z$832c529dfa4e76869d58b07cf2efb4797282e0a10cf11dc268507da1dbfe9b7414648839c957378cc1d0ca29db0eb18f559ad1e6fd1dba83ec2af1972df02446',1,'2024-04-09 16:37:31','2024-04-09 16:37:31'),(29,1,1043664494,'ewdew','erewr','dfsf@gmail.com',666,3,'weqeq3w','scrypt:32768:8:1$By1A7xDOlVRxhIOq$2f99a0986db7fe874dfeed5ffe8dd29de3b0973d7ef82639ee425a7606540ecb95ead94d10b978edc67721c5fec0cdd741d298758e041a75252d41e32ae1f969',1,'2024-04-11 13:00:07','2024-04-11 13:00:07'),(30,3,2672190,'pedro','sanchez','perezc@gmail.com',3207611081,3,'sanchez10','scrypt:32768:8:1$vf71XyfUsNtUqCiF$1fac147b5221f610e434746a54398a0aa8e973d41676d90d3c0f43886aa0d7d4d954932fc4d0a0af6f2c79074a0b4a687a27e98f2f4f0a2a12c6af540fc4e4a2',1,'2024-09-13 00:33:33','2024-09-13 00:33:33'),(31,3,2672197,'jhon','hernandez','hernandezjhon@gmail.com',3207610141,3,'jhonher11','scrypt:32768:8:1$2a1DnNb4NbxTaMwL$30b1738f1f18718ba3912b76d26c475f05f6a854b09636e83e830a519dc80aaae86063dd520ff7a7a33f095f3f13eb014c7767ab5d8b3b768ff95b82318b1d91',0,'2024-09-13 11:31:23','2024-09-13 11:31:40');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_roles`
--

DROP TABLE IF EXISTS `users_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_roles` (
  `user_role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(50) NOT NULL,
  `active` int NOT NULL DEFAULT (1),
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_roles`
--

LOCK TABLES `users_roles` WRITE;
/*!40000 ALTER TABLE `users_roles` DISABLE KEYS */;
INSERT INTO `users_roles` VALUES (1,'ROOT',1,'2024-01-26 22:07:07','2024-01-26 22:07:07'),(2,'INSTRUCTOR',1,'2024-01-29 17:20:48','2024-04-01 14:44:03'),(3,'APRENDIZ',1,'2024-01-29 17:23:15','2024-01-29 17:23:15');
/*!40000 ALTER TABLE `users_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'systemsusers'
--

--
-- Dumping routines for database 'systemsusers'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-19  1:50:07
