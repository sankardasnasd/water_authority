/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 10.4.28-MariaDB : Database - water_authority2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`water_authority2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `water_authority2`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add area',7,'add_area'),
(26,'Can change area',7,'change_area'),
(27,'Can delete area',7,'delete_area'),
(28,'Can view area',7,'view_area'),
(29,'Can add charges',8,'add_charges'),
(30,'Can change charges',8,'change_charges'),
(31,'Can delete charges',8,'delete_charges'),
(32,'Can view charges',8,'view_charges'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add notification',10,'add_notification'),
(38,'Can change notification',10,'change_notification'),
(39,'Can delete notification',10,'delete_notification'),
(40,'Can view notification',10,'view_notification'),
(41,'Can add user',11,'add_user'),
(42,'Can change user',11,'change_user'),
(43,'Can delete user',11,'delete_user'),
(44,'Can view user',11,'view_user'),
(45,'Can add userupload',12,'add_userupload'),
(46,'Can change userupload',12,'change_userupload'),
(47,'Can delete userupload',12,'delete_userupload'),
(48,'Can view userupload',12,'view_userupload'),
(49,'Can add usage',13,'add_usage'),
(50,'Can change usage',13,'change_usage'),
(51,'Can delete usage',13,'delete_usage'),
(52,'Can view usage',13,'view_usage'),
(53,'Can add payment',14,'add_payment'),
(54,'Can change payment',14,'change_payment'),
(55,'Can delete payment',14,'delete_payment'),
(56,'Can view payment',14,'view_payment'),
(57,'Can add meterreader',15,'add_meterreader'),
(58,'Can change meterreader',15,'change_meterreader'),
(59,'Can delete meterreader',15,'delete_meterreader'),
(60,'Can view meterreader',15,'view_meterreader'),
(61,'Can add complaint',16,'add_complaint'),
(62,'Can change complaint',16,'change_complaint'),
(63,'Can delete complaint',16,'delete_complaint'),
(64,'Can view complaint',16,'view_complaint'),
(65,'Can add assign_meter_reader',17,'add_assign_meter_reader'),
(66,'Can change assign_meter_reader',17,'change_assign_meter_reader'),
(67,'Can delete assign_meter_reader',17,'delete_assign_meter_reader'),
(68,'Can view assign_meter_reader',17,'view_assign_meter_reader'),
(69,'Can add district',18,'add_district'),
(70,'Can change district',18,'change_district'),
(71,'Can delete district',18,'delete_district'),
(72,'Can view district',18,'view_district'),
(73,'Can add public',19,'add_public'),
(74,'Can change public',19,'change_public'),
(75,'Can delete public',19,'delete_public'),
(76,'Can view public',19,'view_public'),
(77,'Can add bank',20,'add_bank'),
(78,'Can change bank',20,'change_bank'),
(79,'Can delete bank',20,'delete_bank'),
(80,'Can view bank',20,'view_bank');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','area'),
(17,'myapp','assign_meter_reader'),
(20,'myapp','bank'),
(8,'myapp','charges'),
(16,'myapp','complaint'),
(18,'myapp','district'),
(9,'myapp','login'),
(15,'myapp','meterreader'),
(10,'myapp','notification'),
(14,'myapp','payment'),
(19,'myapp','public'),
(13,'myapp','usage'),
(11,'myapp','user'),
(12,'myapp','userupload'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-17 05:07:17.999621'),
(2,'auth','0001_initial','2023-10-17 05:07:18.343374'),
(3,'admin','0001_initial','2023-10-17 05:07:18.406278'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-17 05:07:18.421915'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-17 05:07:18.421915'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-17 05:07:18.484413'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-17 05:07:18.515664'),
(8,'auth','0003_alter_user_email_max_length','2023-10-17 05:07:18.531295'),
(9,'auth','0004_alter_user_username_opts','2023-10-17 05:07:18.531295'),
(10,'auth','0005_alter_user_last_login_null','2023-10-17 05:07:18.562537'),
(11,'auth','0006_require_contenttypes_0002','2023-10-17 05:07:18.562537'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-17 05:07:18.578170'),
(13,'auth','0008_alter_user_username_max_length','2023-10-17 05:07:18.593791'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-17 05:07:18.609416'),
(15,'auth','0010_alter_group_name_max_length','2023-10-17 05:07:18.625039'),
(16,'auth','0011_update_proxy_permissions','2023-10-17 05:07:18.640666'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-17 05:07:18.656286'),
(18,'myapp','0001_initial','2023-10-17 05:07:19.078165'),
(19,'myapp','0002_district_alter_area_district','2023-10-17 05:07:19.156312'),
(20,'sessions','0001_initial','2023-10-17 05:07:19.171931'),
(21,'myapp','0002_remove_user_district_remove_user_place','2023-10-17 10:12:43.588629'),
(22,'myapp','0003_alter_charges_fromunit_alter_charges_tounit_and_more','2023-11-05 12:32:37.684007'),
(23,'myapp','0004_public','2023-11-07 09:26:38.909747'),
(24,'myapp','0005_bank','2023-11-07 10:11:52.972555');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('0spxecmttuemvv3v3dyam60lxervt5ue','eyJsaWQiOjI3LCJhaWQiOjEzfQ:1r4d81:u6etUfB4QdGZtrr0vtHZhO_WTRiUjIFOtb-dYQyMxeA','2023-12-03 08:26:05.369005'),
('25x0l54c2obiqnbei572877he0qgo3rr','.eJyrVsrJTFGyMtRRSgTRFjpKpWC-GZBRnJieGg_iGcF4II6SoYVSLQC42A_Q:1r0LvH:qZoG5dis0kIjiA-o_RQnctf8hvGCKVuQr7mAgQGRPvo','2023-11-21 13:15:15.435366'),
('4ofpd76bbfru83fx7cwj7mey1bnbub45','.eJyrVsrJzFOyUsovLVHSAbJTgGwgIxHEMDTTUSotTkxPBYsamwPFS0FMI2OoeDyIZ2JUCwCrPROY:1r7v27:F14sKMW6DDRAMICncJ77O1gYG-WbBv-P0v_IDS-6fiU','2023-12-12 10:09:35.866901'),
('68tm2j0d6cnx907he7leh7lmkmh6yuy2','eyJsaWQiOjF9:1r4a4I:LmDEzLNqmDzdjn1bn08fO1QzafMSpiOoyoe1L6XdoFo','2023-12-03 05:10:02.302735'),
('6d3jf16ewgovgsbv75re42l3nuzrolcl','eyJsaWQiOjEsInVzYWdlaWQiOiIyMSJ9:1r1lEO:H7CuP7mlQadzCZFvOjsFEJxl-cUZLpcNsGXALlM6iKg','2023-11-25 10:28:48.732674'),
('b76rl67oc8lazy2szg6250la43463g5h','eyJsaWQiOjE1fQ:1r1kNw:cu1Ooselx4gZED1NujVGc8_z-mFJGLr3g2MEXt1E65g','2023-11-25 09:34:36.434740'),
('d7b8p9tha93relueodi7xyee9o7bjou5','eyJsaWQiOjUsImFpZCI6Nn0:1qzDxb:DBVRP4lTvXR1gvzB3MtB5wcSbBLmh__xwDPRx867GXc','2023-11-18 10:32:59.811175'),
('ekb2octypcpkfg7nquny1j0fm5jq3xpt','eyJsaWQiOjF9:1r1hkt:u_M8dRZpjVH44ek8j7B1xwp5fbnyr7MnWXcqbUmFARc','2023-11-25 06:46:07.604405'),
('euhih2jfe4iry82zjzntypysr107rbeg','eyJ1aWQiOjE3LCJ1c2FnZV9pZCI6MjcsImxpZCI6MSwiYWlkIjo4fQ:1r4Zyj:FThxBDJKQWWKhtaS5ckr_z1tf9TOrq_h6dR6PKiIcAg','2023-12-03 05:04:17.242280'),
('f6gt0g7eea3sl79byu7bz8nka88o9p5g','eyJsaWQiOjF9:1r3cjm:QPtgcW719-BnACEhx2D30-Htt1sWvlwHVHLB4YHDkgE','2023-11-30 13:48:54.804019'),
('ff1rplplevn25mubi0t9x5vn8xxhelsx','.eJyrVsrJTFGyMtRRSgTTxjpKpSCGEVCktDgxPTUexDM2hvJAHCUjSyUdoLY8IBNI1AIAgu0TAA:1r5KtA:OJE4FXRP8Wiu-gb5c89lTyrZbb9sKfZoqrS4bB2G-4E','2023-12-05 07:09:40.881105'),
('j8y3gzbs0plfupcxr3adysa2iy9colxn','eyJsaW4iOiJpbiIsImxpZCI6MX0:1r9eEH:R7af8j9MQl99QTHBLFUC6vecgSGVxy1LWcfY0nuoxW0','2023-12-17 04:37:17.949281'),
('kjnjr61a0nzv0larfbbgzy1al49tnlsn','eyJsaW4iOiJpbiIsImxpZCI6MSwiYWlkIjoxNn0:1r9kZX:hQ11ra-7jORMmjJBGwexQrWWkG27gfbpKdyoeQg4hxY','2023-12-17 11:23:39.831477'),
('mkuvfgs2rq6tz40g4zrjqzykhu6cnpbt','eyJsaWQiOjEsInVpZCI6NCwidXNhZ2VfaWQiOjR9:1qsimd:y9LORWsLb0eWvBK8glxIdH3U1nq-4pU_6vd9Pr0YsrQ','2023-10-31 12:02:47.807524'),
('t591fijj297cex8l65rvovvkmy0iyvpa','.eJyrVsrJzFOyUgISOkBmipKViaGOUmlxYnoqiKNkbAIULwUxjYyg4vEQVbUA-nkQ9A:1r5UdD:naLKqI9uqC7EAuHqwYCRQO0UrBg9qE8jnKyS2yRBAhQ','2023-12-05 17:33:51.704946'),
('t6bt2opzfq7lmqbhmpzbp3xsyk80mjwl','eyJsaWQiOjF9:1r4Zzx:6gFIERNCSYK20yu2bAt2dN0qXHlMQkWwrT8QxZcmhi4','2023-12-03 05:05:33.683040'),
('wugj1cialy3sulcd1x4qu2jrrozjfyjv','eyJsaWQiOjF9:1r4b1N:ot3SXoo61H5CLYAIAweZTd1mk_tNDOtROrZLtUAD1G8','2023-12-03 06:11:05.780967'),
('x5wbzvha72h0j6r6qalp26w71fo4cum0','eyJsaW4iOiJpbiIsImxpZCI6MX0:1r9e91:aeX-CEw6nuK0xWoIp-Ls6OnM5TBWXBs54xlsu-z8ggM','2023-12-17 04:31:51.299022'),
('ymbn1i6pm8p3etkk8jihynxzmhzvjelw','eyJsaW4iOiJpbiIsImxpZCI6MX0:1r9ikd:HCDjiBFDUgq6IbsuGCDH5lYtZqR5gmBRGp3OL3SN3no','2023-12-17 09:26:59.407066');

/*Table structure for table `myapp_area` */

DROP TABLE IF EXISTS `myapp_area`;

CREATE TABLE `myapp_area` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `District_id` bigint(20) NOT NULL,
  `Place` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_area_District_id_3ceaccc8` (`District_id`),
  CONSTRAINT `myapp_area_District_id_3ceaccc8_fk_myapp_district_id` FOREIGN KEY (`District_id`) REFERENCES `myapp_district` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_area` */

insert  into `myapp_area`(`id`,`District_id`,`Place`) values 
(16,16,'Edathara'),
(17,16,'Mannalur'),
(18,17,'Palazhi'),
(19,16,'Kadalundi'),
(20,17,'Koduvali'),
(21,17,'Kotooli'),
(22,19,'Kalpatta'),
(23,18,'Pattakalam');

/*Table structure for table `myapp_assign_meter_reader` */

DROP TABLE IF EXISTS `myapp_assign_meter_reader`;

CREATE TABLE `myapp_assign_meter_reader` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `AREA_id` bigint(20) NOT NULL,
  `METRERREADER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_assign_meter_reader_AREA_id_2c5792f6_fk_myapp_area_id` (`AREA_id`),
  KEY `myapp_assign_meter_r_METRERREADER_id_973525e0_fk_myapp_met` (`METRERREADER_id`),
  CONSTRAINT `myapp_assign_meter_r_METRERREADER_id_973525e0_fk_myapp_met` FOREIGN KEY (`METRERREADER_id`) REFERENCES `myapp_meterreader` (`id`),
  CONSTRAINT `myapp_assign_meter_reader_AREA_id_2c5792f6_fk_myapp_area_id` FOREIGN KEY (`AREA_id`) REFERENCES `myapp_area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_assign_meter_reader` */

insert  into `myapp_assign_meter_reader`(`id`,`AREA_id`,`METRERREADER_id`) values 
(31,16,16),
(32,16,17),
(33,18,19);

/*Table structure for table `myapp_bank` */

DROP TABLE IF EXISTS `myapp_bank`;

CREATE TABLE `myapp_bank` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Accno` varchar(100) NOT NULL,
  `Ifsc` varchar(100) NOT NULL,
  `Balance` varchar(100) NOT NULL,
  `Cvv` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_bank` */

insert  into `myapp_bank`(`id`,`Accno`,`Ifsc`,`Balance`,`Cvv`) values 
(1,'123','123','99991775.58000001','123');

/*Table structure for table `myapp_charges` */

DROP TABLE IF EXISTS `myapp_charges`;

CREATE TABLE `myapp_charges` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Fromunit` double NOT NULL,
  `Tounit` double NOT NULL,
  `Amount` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_charges` */

insert  into `myapp_charges`(`id`,`Fromunit`,`Tounit`,`Amount`) values 
(2,0,5000,'432.5'),
(3,5000,10000,'695.6'),
(4,10000,15000,'876.8'),
(9,15000,20000,'4556');

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Complaint` varchar(100) NOT NULL,
  `Reply` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `FROM_id` bigint(20) NOT NULL,
  `TO_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_FROM_id_382d2e31_fk_myapp_user_id` (`FROM_id`),
  KEY `myapp_complaint_TO_id_fa3c2908_fk_myapp_meterreader_id` (`TO_id`),
  CONSTRAINT `myapp_complaint_FROM_id_382d2e31_fk_myapp_user_id` FOREIGN KEY (`FROM_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `myapp_complaint_TO_id_fa3c2908_fk_myapp_meterreader_id` FOREIGN KEY (`TO_id`) REFERENCES `myapp_meterreader` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_complaint` */

/*Table structure for table `myapp_district` */

DROP TABLE IF EXISTS `myapp_district`;

CREATE TABLE `myapp_district` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Dis_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_district` */

insert  into `myapp_district`(`id`,`Dis_name`) values 
(16,'Palakkad'),
(17,'Kozhikode'),
(18,'Kannur'),
(19,'Wayanad'),
(20,'Idukki');

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`Username`,`Password`,`Type`) values 
(1,'akashmohan940@gmail.com','123','admin'),
(37,'sakthi@gmail.com','123','meterreader'),
(38,'adarsh@gmail.com','9400712178','meterreader'),
(39,'anandhu@gmail.com','9765534555','meterreader'),
(40,'Krishnapriya@gmail.com','8657775456','meterreader'),
(41,'mariya@gmail.com','115','user'),
(42,'rena@gmail.com','123','user'),
(43,'rena@gmaiil.com','123','user'),
(44,'hiran@gmail.com','1234','pending'),
(45,'mariyathomas650@gmail.com','Mariya@123','user'),
(46,'lintu@gmail.com','8756675677','meterreader');

/*Table structure for table `myapp_meterreader` */

DROP TABLE IF EXISTS `myapp_meterreader`;

CREATE TABLE `myapp_meterreader` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Dob` varchar(100) NOT NULL,
  `Place` varchar(100) NOT NULL,
  `District` varchar(100) NOT NULL,
  `Pincode` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_meterreader_LOGIN_id_ab6180d4_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_meterreader_LOGIN_id_ab6180d4_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_meterreader` */

insert  into `myapp_meterreader`(`id`,`Name`,`Gender`,`Dob`,`Place`,`District`,`Pincode`,`Phone`,`Email`,`Photo`,`LOGIN_id`) values 
(16,'Sakthi','Male','2000-04-05','Kadalundi','Kozhikode','673010','9080150931','sakthi@gmail.com','/media/meter_reader/20231121111842.jpg',37),
(17,'Adarsh','Male','1998-11-09','Methottuthazham','Kozhikode','673007','9400712178','adarsh@gmail.com','/media/meter_reader/20231121112159.jpg',38),
(18,'Anandu','Male','2001-11-19','Palazhi','Kozhikode','673004','9765534555','anandhu@gmail.com','/media/meter_reader/20231121112320.jpg',39),
(19,'Krishna Priya','Female','2015-12-02','Karaparamb','Kozhikode','673010','8657775456','Krishnapriya@gmail.com','/media/meter_reader/20231121114324.jpg',40),
(20,'Lintu','Female','2001-09-12','Pattakalm','kannur','756548','8756675677','lintu@gmail.com','/media/meter_reader/20231128152451.jpg',46);

/*Table structure for table `myapp_notification` */

DROP TABLE IF EXISTS `myapp_notification`;

CREATE TABLE `myapp_notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Notification` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_notification` */

insert  into `myapp_notification`(`id`,`Date`,`Notification`) values 
(11,'2023-12-03','Heelo');

/*Table structure for table `myapp_payment` */

DROP TABLE IF EXISTS `myapp_payment`;

CREATE TABLE `myapp_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Amount` varchar(100) NOT NULL,
  `REQUESTID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payment_REQUESTID_id_1d32cf05_fk_myapp_usage_id` (`REQUESTID_id`),
  CONSTRAINT `myapp_payment_REQUESTID_id_1d32cf05_fk_myapp_usage_id` FOREIGN KEY (`REQUESTID_id`) REFERENCES `myapp_usage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_payment` */

insert  into `myapp_payment`(`id`,`Date`,`Amount`,`REQUESTID_id`) values 
(5,'2023-11-21','695.6',34);

/*Table structure for table `myapp_public` */

DROP TABLE IF EXISTS `myapp_public`;

CREATE TABLE `myapp_public` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Complaint` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_public` */

insert  into `myapp_public`(`id`,`Date`,`Complaint`,`email`,`status`) values 
(3,'2023-12-03','gxctvyuhlikjhjvjhjhkjlk;m','akashmohan9400@gmail.com','Pending');

/*Table structure for table `myapp_usage` */

DROP TABLE IF EXISTS `myapp_usage`;

CREATE TABLE `myapp_usage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Year` varchar(100) NOT NULL,
  `Month` varchar(100) NOT NULL,
  `Usage` double NOT NULL,
  `Amount` varchar(100) NOT NULL,
  `Payment_status` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_usage_USER_id_454bb0de_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_usage_USER_id_454bb0de_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_usage` */

insert  into `myapp_usage`(`id`,`Date`,`Year`,`Month`,`Usage`,`Amount`,`Payment_status`,`Type`,`USER_id`) values 
(32,'2023-11-21','2023','November',0,'750','Done','New_Connection',20),
(33,'2023-11-21','2023','November',0,'750','Done','New_Connection',21),
(34,'2023-11-21','2023','January',0,'750','Done','Monthly Bill',19),
(37,'2023-11-21','2023','January',8778,'695.6','Pending','Monthly Bill',21),
(40,'2023-11-21','2023','January',788,'432.5','Pending','Monthly Bill',19),
(41,'2023-11-21','2023','November',0,'750','Done','New_Connection',22),
(42,'2023-11-28','2023','November',0,'750','Done','New_Connection',23);

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Dob` varchar(100) NOT NULL,
  `Panchayath` varchar(100) NOT NULL,
  `Pincode` varchar(100) NOT NULL,
  `Photo` varchar(300) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Village` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `ConnectionsStatus` varchar(100) NOT NULL,
  `AREA_id` bigint(20) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_AREA_id_5f8eeda4_fk_myapp_area_id` (`AREA_id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_AREA_id_5f8eeda4_fk_myapp_area_id` FOREIGN KEY (`AREA_id`) REFERENCES `myapp_area` (`id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`Name`,`Gender`,`Dob`,`Panchayath`,`Pincode`,`Photo`,`Email`,`Village`,`Phone`,`ConnectionsStatus`,`AREA_id`,`LOGIN_id`) values 
(19,'Mariya','Female','2023-11-01','Edathara','Edathara','/media/user/20231121120725.jpg','mariya@gmail.com','Edathara','8655776575','Active',16,41),
(20,'Rena','Female','2023-11-08','Palazhi','674566','/media/user/20231121120951.jpg','rena@gmail.com','Palazhi','9876797656','Active',18,42),
(21,'Rena','Male','2001-06-07','Edathara','Edathara','/media/user/20231121123932.jpg','rena@gmaiil.com','Edathara','8564545677','Active',16,43),
(22,'Hiran','Male','2023-11-09','Kotooli','564654','/media/user/20231121175239.jpg','hiran@gmail.com','Kotooli','957894556','New_connection',21,44),
(23,'Liya Mariya Thomas','Female','2001-05-15','Naduvil','670571','/media/user/20231128151609.jpg','mariyathomas650@gmail.com','Vellad','7012872007','Active',23,45);

/*Table structure for table `myapp_userupload` */

DROP TABLE IF EXISTS `myapp_userupload`;

CREATE TABLE `myapp_userupload` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Photo` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_userupload_USER_id_85294a66_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_userupload_USER_id_85294a66_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_userupload` */

insert  into `myapp_userupload`(`id`,`Date`,`Photo`,`USER_id`) values 
(7,'2023-11-21','/media/userupload/20231121171207.jpg',19);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
