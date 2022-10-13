-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: recetas
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` text,
  `instructions` text,
  `date_made` date DEFAULT NULL,
  `under_30` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `image` varchar(45) DEFAULT NULL COMMENT 'agregado para ejercitar el almacenamiento de imagenes en bd. Debe ser texto\\n',
  PRIMARY KEY (`id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (7,'TORTA RED VELVET','Para el bizcocho:\r\n\r\n270 gr harina sin polvos\r\n½ cucharadita de Bicarbonato de Sodio Gourmet\r\n1 cucharadita de Polvos de Hornear Gourmet\r\n25 gr de Cacao Amargo en Polvo Gourmet\r\n250 ml de leche entera\r\n1 cucharada de jugo de limón o vinagre blanco\r\n¾ taza de aceite vegetal\r\n300 gr de azúcar\r\n2 huevos\r\n¼ cucharadita de Sal de Mar Gourmet\r\n2 cucharaditas de Esencia de Vainilla Gourmet\r\n2 cucharadas de Colorante Rojo Gourmet\r\nPara el frosting:\r\n\r\n400 gr de queso crema a temperatura ambiente\r\n180 gr de mantequilla sin sal a temperatura ambiente\r\n160 gr de azúcar flor','Para el bizcocho:\r\n\r\nPrecalentar el horno a 170°.\r\nEnmantequillar y enharinar 2 moldes de 15 cms. de diámetro.\r\nEn un bol, cernir la harina, agregarle el Bicarbonato de Sodio Gourmet, Polvos de Hornear, Cacao Amargo en Polvo y reservar.\r\nMezclar la leche entera y el jugo de limón o vinagre y dejar reposar por 10 minutos.\r\nEn un recipiente, agregar el aceite vegetal y el azúcar. Batir y agregar los huevos, Sal de Mar, Esencia de Vainilla, Colorante Rojo.\r\nBatir hasta obtener una mezcla homogénea y luego agregar los ingredientes secos cernidos.\r\nVerter la mezcla de leche con limón e integrar.\r\nDividir la mezcla en 2 moldes y hornear por 40-45 minutos o hasta que estén cocidos.\r\nDejar enfriar 15 minutos antes de desmoldar.\r\n \r\n\r\nPara el frosting:\r\n\r\nEn un recipiente, batir el queso crema.\r\nAgregar la mantequilla, el azúcar flor y seguir batiendo hasta integrar.\r\n \r\n\r\nPara montar la torta:\r\n\r\nCortar cada bizcocho en 2 partes iguales.\r\nPoner el frosting en cada piso de la torta.\r\nCubrir con frosting por todos lados.\r\nDecorar con migas de bizcocho.','2022-02-11',0,'2022-10-06 19:09:55','2022-10-06 19:10:18',3,NULL),(8,'STROGONOFF','400 g de filete picado en tiras\r\nSal de Mar Gourmet y Mix de Pimientas Gourmet\r\n3 cdas de harina\r\nAceite vegetal\r\n1 cda de mantequilla\r\n½ cebolla blanca picada finamente\r\n400 g de champiñones laminados\r\n1 sobre de Caldo en polvo de Carne Gourmet\r\n1 taza de agua\r\n½ taza crema de leche\r\nPerejil picado','Salpimentar el filete y mezclarlo con 2 de las cucharadas de harina.\r\nPrecalentar una olla a fuego medio-alto y agregar el aceite vegetal.\r\nAgregar suficiente carne para llenar la base de la olla y dorarla por ambos lados.\r\nReservar y repetir con el resto de la carne.\r\nAgregar mantequilla a la sartén y la cebolla.\r\nSofreír hasta que la cebolla esté translúcida.\r\nUsar la cebolla para raspar los trocitos dorados que queden pegados en la olla.\r\nAgregar la cucharada de harina restante y mezclar.\r\nAgregar los champiñones y mezclar.\r\nAgregar el Caldo en polvo de Carne, la carne, el agua y la crema de leche.\r\nDejar cocinar hasta que tome consistencia.\r\nProbar y ajustar el nivel de sal.\r\nServir con perejil picado.','2022-09-05',1,'2022-10-06 19:16:00','2022-10-07 11:41:39',1,NULL),(10,'PESCADO A LO MACHO','Para el pescado\r\n\r\n2 filetes de pescado\r\nSal de Mar Gourmet y Mix de Pimientas Gourmet\r\n6 cdas harina\r\n6 cdas aceite vegetal\r\n \r\n\r\nPara la salsa a lo macho\r\n\r\n½ cebolla morada picada finamente\r\n½ pimiento rojo picado finamente\r\n2 dientes de ajo picados finamente\r\n1 cda de pasta de ají amarillo\r\n150 ml de vino blanco\r\n120 g tomate enlatado y picado\r\n200 g aros de calamar\r\n200 g camarones pelados y limpios\r\nSal de Mar Gourmet y Mix de Pimientas Gourmet','Salpimentar el pescado por ambos lados.\r\nEsparcir la harina sobre un plato y cubrir los filetes, dándole golpecitos para retirar el exceso.\r\nPrecalentar una sartén a fuego medio-alto y agregar el aceite.\r\nFreír el pescado por ambos lados y reservar.\r\nRetirar el exceso de aceite de la sartén con cuidado y agregar la cebolla y pimiento. Sofreír hasta que la cebolla se suavice y ponga translúcida.\r\nAgregar el ají amarillo y mezclar por 30 segundos.\r\nAgregar el vino blanco y dejar que hierva hasta que se haya evaporado por completo.\r\nAgregar los tomates y mezclar hasta que rompa hervor.\r\nAgregar los calamares, camarones y ajustar el nivel de sal y pimienta.\r\nPoner los filetes en una fuente y servir la salsa encima.','2022-09-19',0,'2022-10-06 19:24:39','2022-10-06 19:24:39',2,NULL),(11,'POLLO TIKKA MASALA','Para el arroz basmati\r\n\r\n1 cdta de aceite vegetal\r\n2 tazas de arroz basmati\r\n1 ¼ taza de agua\r\n1 cdta de sal\r\n \r\n\r\nPara marinar el pollo\r\n\r\n3 pechugas de pollo en cubos de 3 cm\r\n150 g deyogurt natural\r\n2 cdas de limón\r\n1 cdta de Comino Molido Gourmet\r\n1 cdta de garam masala\r\n1 diente de ajo molido o rallado finamente\r\n5 g jengibre pelado y rallado finamente\r\nSal de Mar Gourmet y Mix de Pimientas Gourmet\r\n \r\n\r\nPara el pollo tikka masala\r\n\r\n2 cdas de aceite vegetal\r\n1 cebolla blanca picada finamente\r\n2 dientes de ajo rallados finamente\r\n10 g jengibre pelado y rallado finamente\r\n½ cdta de Comino Molido Gourmet\r\n1 cdta de Ají de Color Gourmet\r\n2 cdas de concentrado de tomate\r\n2 cdtas de garam masala\r\n200 g de passata de tomate\r\n½ taza de crema de leche\r\nSal de Mar Gourmet y Mix de Pimientas Gourmet','Para el arroz basmati\r\n\r\nPrecalentar una olla a fuego medio y agregar el aceite.\r\nAgregar el arroz y mezclar constantemente por 1 minuto.\r\nAgregar el agua y sal y mezclar. Dejar que rompa hervor y tapar.\r\nDejar cocinar por 15 minutos.\r\nDestapar y mezclar con un tenedor para separar los granos.\r\n \r\n\r\nPara marinar el pollo\r\n\r\nMezclar el pollo con el resto de los ingredientes y marinar por una hora.\r\nPrecalentar una olla a fuego medio y agregar el aceite. Sellar el pollo y reservar.\r\nAgregar más aceite de ser necesario y agregar la cebolla, mezclar hasta que se ponga translúcida y usar la cebolla para raspar los trocitos de pollo que puedan haber quedado pegados en la olla.\r\nAgregar el ajo, jengibre, Comino Molido, Ají de Color, garam masala y concentrado de tomate y mezclar constantemente por 1 minuto.\r\nAgregar la passata, crema de leche, pollo y mezclar.\r\nDejar cocinar por 5-10 minutos o hasta que tome consistencia.\r\nProbar y agregar la Sal de Mar y Mix de Pimientas\r\nServir con el arroz.','2022-03-31',1,'2022-10-07 15:58:31','2022-10-07 16:20:29',4,NULL),(12,'receta con imagen','ddd','ddd','2022-05-10',0,'2022-10-11 11:25:31','2022-10-11 11:25:31',1,'1.jpg');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Marcela','Rubio','mrubiob@gmail.com','$2b$12$15UoA6kWITca9qlbYtVKPezXHXp9qTwEELKfeclzG5keHt2a12Pqy','2022-10-06 10:00:21','2022-10-06 10:00:21'),(2,'Elena','De Troya','etroya@gmail.com','$2b$12$JBEvAZY4SAKwVuoeJqk31.ZVpeLbcTuZmn0N.z5QexBRUBsG1qoLW','2022-10-06 10:00:46','2022-10-06 10:00:46'),(3,'Araceli','Ortiz','aortiz@gmail.com','$2b$12$P7f.SV4QLRZyyQ1UJAQ3w.tAESCxnd848Akgpj404VxYUfTE0acby','2022-10-06 19:08:52','2022-10-06 19:08:52'),(4,'Mauricio','Ortiz','mortiz@gmail.com','$2b$12$6hHxaNM9.oFYkS23NRaWXOd4PquEcr8FQpbhbNPDsLeNalvAjqCQS','2022-10-07 15:57:12','2022-10-07 15:57:12');
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

-- Dump completed on 2022-10-12 23:42:30
