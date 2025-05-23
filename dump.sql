-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: mis_trapitos
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrador` (
  `id_administrador` int(11) NOT NULL AUTO_INCREMENT,
  `id_empleado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_administrador`),
  KEY `id_empleado` (`id_empleado`),
  CONSTRAINT `administrador_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` VALUES (1,23);
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_categoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'blusas'),(2,'pantalones'),(3,'shorts');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` varchar(100) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(320) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Calle 123 #45-67, Ciudad de México','Laura González','+52 55 1234 0000','laura.gonzalez@email.com'),(2,'Av. Siempre Viva 742, Buenos Aires','Carlos Ramírez','+54 11 5678 1111','c.ramirez@email.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_articulo`
--

DROP TABLE IF EXISTS `detalle_articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detalle_articulo` (
  `id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) DEFAULT NULL,
  `precio_unitario` decimal(10,2) DEFAULT NULL,
  `descuento_aplicado` decimal(10,2) DEFAULT NULL,
  `id_venta` int(11) DEFAULT NULL,
  `id_variacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `id_venta` (`id_venta`),
  KEY `id_variacion` (`id_variacion`),
  CONSTRAINT `detalle_articulo_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`),
  CONSTRAINT `detalle_articulo_ibfk_2` FOREIGN KEY (`id_variacion`) REFERENCES `variacion_producto` (`id_variacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_articulo`
--

LOCK TABLES `detalle_articulo` WRITE;
/*!40000 ALTER TABLE `detalle_articulo` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_articulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empleado` (
  `id_empleado` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `telefono` varchar(12) DEFAULT NULL,
  `email` varchar(320) DEFAULT NULL,
  PRIMARY KEY (`id_empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (23,'Mauricio','3313414747','mau_jauregui@alumnos.udg.mx'),(26,'joce','3312469879','as@gmail.com'),(27,'Jocelyn','6692061759','jo@gmail.com');
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) DEFAULT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `oferta` varchar(50) DEFAULT NULL,
  `porc_desc` int(11) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `fecha_ini_oferta` timestamp NULL DEFAULT NULL,
  `fecha_fin_oferta` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Blusa Floral','Blusa de manga corta con estampado floral, 100% algodón.',25.99,'Descuento',20,1,'2025-05-15 06:00:00','2025-05-31 06:00:00'),(2,'Blusa Elegante','Blusa de seda color crema, ideal para ocasiones formales.',45.00,'',0,1,NULL,NULL),(3,'Jeans Ajustados','Pantalón de mezclilla entallado con acabado desgastado.',55.00,'',0,2,NULL,NULL),(4,'Pantalón Cargo','Pantalón cargo con bolsillos laterales, color verde oliva.',40.50,'Descuento',50,2,'2025-05-18 06:00:00','2025-06-01 06:00:00'),(5,'Short Deportivo','Short ligero para entrenamiento, con cintura elástica.',20.00,'Cantidad: 5X4',0,3,'2025-05-20 06:00:00','2025-05-30 06:00:00'),(6,'Short de Jean','Short de mezclilla azul claro, corte alto.',28.99,'',0,3,NULL,NULL);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_proveedor`
--

DROP TABLE IF EXISTS `producto_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto_proveedor` (
  `id_pp` int(11) NOT NULL AUTO_INCREMENT,
  `id_producto` int(11) DEFAULT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_pp`),
  KEY `id_producto` (`id_producto`),
  KEY `id_proveedor` (`id_proveedor`),
  CONSTRAINT `producto_proveedor_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  CONSTRAINT `producto_proveedor_ibfk_2` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_proveedor`
--

LOCK TABLES `producto_proveedor` WRITE;
/*!40000 ALTER TABLE `producto_proveedor` DISABLE KEYS */;
INSERT INTO `producto_proveedor` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,2),(5,5,2),(6,6,2);
/*!40000 ALTER TABLE `producto_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proveedor` (
  `id_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(320) DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'Moda Urbana S.A.','+54 11 4455-8899','contacto@modaurbana.com'),(2,'Estilo y Diseño Textil','+52 55 1234-5678','ventas@estiloydiseno.com');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variacion_producto`
--

DROP TABLE IF EXISTS `variacion_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `variacion_producto` (
  `id_variacion` int(11) NOT NULL AUTO_INCREMENT,
  `talla` varchar(10) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  `cantidad_stock` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_variacion`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `variacion_producto_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variacion_producto`
--

LOCK TABLES `variacion_producto` WRITE;
/*!40000 ALTER TABLE `variacion_producto` DISABLE KEYS */;
INSERT INTO `variacion_producto` VALUES (1,'S','Rojo',10,1),(2,'M','Rojo',15,1),(3,'M','Crema',8,2),(4,'32','Azul Oscuro',12,3),(5,'34','Negro',6,3),(6,'L','Verde Oliva',20,4),(7,'M','Gris',18,5),(8,'S','Azul Claro',5,6),(9,'M','Azul Claro',9,6);
/*!40000 ALTER TABLE `variacion_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_venta` date DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `metodo_de_pago` varchar(50) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_empleado` (`id_empleado`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-21  2:11:00
