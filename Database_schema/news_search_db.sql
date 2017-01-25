/*creates a database if it already exists it uses*/

CREATE DATABASE IF NOT EXISTS `newsdb`;

/*use the database*/

use `newsdb`;

/*creating a table newstype*/

CREATE TABLE IF NOT EXISTS `resolved_news_type` (
	`id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`resolved_news_type_name` VARCHAR(250) DEFAULT NULL UNIQUE, 
	CONSTRAINT pk_resolved_news_type_id PRIMARY KEY(id)
	) AUTO_INCREMENT=1;

/*creating a table unresolved_newtype*/

CREATE TABLE IF NOT EXISTS unresolved_news_type (
	`id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`unresolved_news_type_name` VARCHAR(250) DEFAULT NULL, 
	CONSTRAINT pk_unresolved_news_type_id PRIMARY KEY(id)
	) AUTO_INCREMENT=1;

/*creating resolved_newtype*/

CREATE TABLE IF NOT EXISTS map_unresolved_resolved_news_type (
	`id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`resolved_news_type_id` SMALLINT UNSIGNED NOT NULL ,
	`unresolved_news_type_id` SMALLINT UNSIGNED NOT NULL UNIQUE,
	CONSTRAINT pk_unresolved_news_type_id PRIMARY KEY(id),
	CONSTRAINT fk_news_type FOREIGN KEY(resolved_news_type_id) 
	REFERENCES resolved_news_type(id) ON DELETE NO ACTION,
	CONSTRAINT fk_unresolved_news_type FOREIGN KEY(unresolved_news_type_id) 
	REFERENCES unresolved_news_type(id) 
	ON DELETE NO ACTION
	) AUTO_INCREMENT=1;

/*creating table resolved_location*/

CREATE TABLE IF NOT EXISTS resolved_location (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	resolved_location_name VARCHAR(250) NOT NULL UNIQUE, 
	CONSTRAINT pk_resolved_location_id PRIMARY KEY(id)
	) AUTO_INCREMENT=1;

/*creating table unresolved_location*/

CREATE TABLE IF NOT EXISTS unresolved_location (
	`id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`unresolved_location_name` VARCHAR(250) DEFAULT NULL, 
	CONSTRAINT pk_unresolved_location_id PRIMARY KEY(id)
	) AUTO_INCREMENT=1;

/*creating table map_unresolved_resolved_location*/

CREATE TABLE IF NOT EXISTS map_unresolved_resolved_location (
	`id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`resolved_location_id` SMALLINT UNSIGNED NOT NULL ,
	`unresolved_location_id` SMALLINT UNSIGNED NOT NULL UNIQUE,
	CONSTRAINT pk_map_unresolved_resolved_location_id PRIMARY KEY(id),
	CONSTRAINT fk_resolved_location_id FOREIGN KEY(resolved_location_id) 
	REFERENCES resolved_location(id) ON DELETE NO ACTION,
	CONSTRAINT fk_unresolved_location_id FOREIGN KEY(unresolved_location_id) 
	REFERENCES unresolved_location(id) ON DELETE NO ACTION
	) AUTO_INCREMENT=1;

/*creating table source*/

CREATE TABLE IF NOT EXISTS source (
	`id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT ,
	`source_name` VARCHAR(250) NOT NULL UNIQUE,
	`source_url` VARCHAR(250) NOT NULL,
	CONSTRAINT pk_source_id PRIMARY KEY(id)
	) AUTO_INCREMENT=1;


/*creating table author*/

CREATE TABLE IF NOT EXISTS author (
	`id` SMALLINT(4) NOT NULL AUTO_INCREMENT ,
	`author_name` VARCHAR(250) NOT NULL UNIQUE,
	`source_id` SMALLINT UNSIGNED,
	CONSTRAINT pk_author_id PRIMARY KEY(id),
	CONSTRAINT fk_author_source_id FOREIGN KEY(source_id) 
	REFERENCES source(id) ON DELETE NO ACTION
	) AUTO_INCREMENT=1;

/*creating table article_download*/

CREATE TABLE IF NOT EXISTS article_download (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`local_file_path` VARCHAR(250) NOT NULL,
	`article_download_created_date` DATETIME NOT NULL,
	`article_download_last_updated_date` DATETIME NOT NULL,
	`is_parsed` tinyint(1) default 0,
	CONSTRAINT pk_article_main_id PRIMARY KEY(id))AUTO_INCREMENT=1;

/*creating table article_parsed*/

CREATE TABLE IF NOT EXISTS article_parsed (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`article_title` VARCHAR(250) NOT NULL,
	`unresolved_news_type_id` SMALLINT UNSIGNED NOT NULL,
	`url` VARCHAR(250) NOT NULL,
	`published_date` DATETIME NOT NULL,
	`created_date` DATETIME NOT NULL,
	`last_updated_date` DATETIME NOT NULL,
	`unresolved_location_id` SMALLINT UNSIGNED ,
	`author_id` SMALLINT(4) NOT NULL,
	`source_id` SMALLINT UNSIGNED NOT NULL,
	`unique_id` VARCHAR(250) NOT NULL UNIQUE,
	`article_download_id` INT UNSIGNED NOT NULL,
	
	CONSTRAINT pk_article_main_id PRIMARY KEY(id),
	CONSTRAINT fk_article_download_id FOREIGN KEY(article_download_id) 
	REFERENCES article_download(id) ON DELETE NO ACTION,
	CONSTRAINT fk_article_news_type FOREIGN KEY(unresolved_news_type_id) 
	REFERENCES unresolved_news_type(id) ON DELETE NO ACTION,
	CONSTRAINT fk_article_location_id FOREIGN KEY(unresolved_location_id) 
	REFERENCES unresolved_location(id) ON DELETE NO ACTION,
	CONSTRAINT fk_content_author_id FOREIGN KEY(author_id) 
	REFERENCES author(id) ON DELETE NO ACTION,
	CONSTRAINT fk_content_source_id FOREIGN KEY(source_id) 
	REFERENCES source(id) ON DELETE NO ACTION
	) AUTO_INCREMENT=1;

/*creating table article_content*/

CREATE TABLE IF NOT EXISTS article_content (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`article_parsed_id` INT UNSIGNED NOT NULL,
	`content` TEXT NOT NULL,
	CONSTRAINT pk_article_content_id PRIMARY KEY(id),
	CONSTRAINT fk_content_article_id FOREIGN KEY(article_parsed_id) 
	REFERENCES article_parsed(id) ON DELETE NO ACTION
	) AUTO_INCREMENT=1;





