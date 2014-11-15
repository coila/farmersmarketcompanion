/*
 Navicat PostgreSQL Data Transfer

 Source Server         : test
 Source Server Version : 90300
 Source Host           : localhost
 Source Database       : farmerbrown
 Source Schema         : public

 Target Server Version : 90300
 File Encoding         : utf-8

 Date: 11/15/2014 08:51:14 AM
*/

-- ----------------------------
--  Sequence structure for food_idfood_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."food_idfood_seq";
CREATE SEQUENCE "public"."food_idfood_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;
ALTER TABLE "public"."food_idfood_seq" OWNER TO "emma";

-- ----------------------------
--  Sequence structure for linkeddata_idlinkeddata_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."linkeddata_idlinkeddata_seq";
CREATE SEQUENCE "public"."linkeddata_idlinkeddata_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;
ALTER TABLE "public"."linkeddata_idlinkeddata_seq" OWNER TO "emma";

-- ----------------------------
--  Sequence structure for place_idplace_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."place_idplace_seq";
CREATE SEQUENCE "public"."place_idplace_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;
ALTER TABLE "public"."place_idplace_seq" OWNER TO "emma";

-- ----------------------------
--  Sequence structure for season_idseason_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."season_idseason_seq";
CREATE SEQUENCE "public"."season_idseason_seq" INCREMENT 1 START 1 MAXVALUE 9223372036854775807 MINVALUE 1 CACHE 1;
ALTER TABLE "public"."season_idseason_seq" OWNER TO "emma";

-- ----------------------------
--  Table structure for food
-- ----------------------------
DROP TABLE IF EXISTS "public"."food";
CREATE TABLE "public"."food" (
	"foodname" varchar(255) COLLATE "default",
	"idfood" int8 NOT NULL DEFAULT nextval('food_idfood_seq'::regclass),
	"imgurl" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."food" OWNER TO "emma";

-- ----------------------------
--  Table structure for place
-- ----------------------------
DROP TABLE IF EXISTS "public"."place";
CREATE TABLE "public"."place" (
	"placename" varchar(255) COLLATE "default",
	"zipcode" int8,
	"idplace" int8 NOT NULL DEFAULT nextval('place_idplace_seq'::regclass)
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."place" OWNER TO "emma";

-- ----------------------------
--  Table structure for season
-- ----------------------------
DROP TABLE IF EXISTS "public"."season";
CREATE TABLE "public"."season" (
	"seasonname" varchar(255) COLLATE "default",
	"idseason" int8 NOT NULL DEFAULT nextval('season_idseason_seq'::regclass)
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."season" OWNER TO "emma";

-- ----------------------------
--  Table structure for linkeddata
-- ----------------------------
DROP TABLE IF EXISTS "public"."linkeddata";
CREATE TABLE "public"."linkeddata" (
	"fkfood" int8,
	"fkplace" int8,
	"fkseason" int8,
	"idlinkeddata" int8 NOT NULL DEFAULT nextval('linkeddata_idlinkeddata_seq'::regclass)
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."linkeddata" OWNER TO "emma";

-- ----------------------------
--  View structure for foodQ
-- ----------------------------
DROP VIEW IF EXISTS "public"."foodQ";
CREATE VIEW "public"."foodQ" AS  SELECT food.foodname, 
    food.idfood, 
    food.imgurl, 
    place.placename, 
    place.zipcode, 
    place.idplace, 
    season.seasonname, 
    season.idseason, 
    linkeddata.idlinkeddata
   FROM (((linkeddata
   JOIN food ON ((linkeddata.fkfood = food.idfood)))
   JOIN place ON ((linkeddata.fkplace = place.idplace)))
   JOIN season ON ((linkeddata.fkseason = season.idseason)));


-- ----------------------------
--  Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."food_idfood_seq" RESTART 1 OWNED BY "food"."idfood";
ALTER SEQUENCE "public"."linkeddata_idlinkeddata_seq" RESTART 1 OWNED BY "linkeddata"."idlinkeddata";
ALTER SEQUENCE "public"."place_idplace_seq" RESTART 1 OWNED BY "place"."idplace";
ALTER SEQUENCE "public"."season_idseason_seq" RESTART 1 OWNED BY "season"."idseason";
-- ----------------------------
--  Indexes structure for table food
-- ----------------------------
CREATE UNIQUE INDEX  "keyfood" ON "public"."food" USING btree(idfood ASC NULLS LAST);

-- ----------------------------
--  Indexes structure for table place
-- ----------------------------
CREATE UNIQUE INDEX  "keyplace" ON "public"."place" USING btree(idplace ASC NULLS LAST);

-- ----------------------------
--  Indexes structure for table season
-- ----------------------------
CREATE UNIQUE INDEX  "keyseason" ON "public"."season" USING btree(idseason ASC NULLS LAST);

-- ----------------------------
--  Indexes structure for table linkeddata
-- ----------------------------
CREATE UNIQUE INDEX  "keylinkeddata" ON "public"."linkeddata" USING btree(idlinkeddata ASC NULLS LAST);

-- ----------------------------
--  Foreign keys structure for table linkeddata
-- ----------------------------
ALTER TABLE "public"."linkeddata" ADD CONSTRAINT "fkfood" FOREIGN KEY ("fkfood") REFERENCES "public"."food" ("idfood") ON UPDATE NO ACTION ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE;
ALTER TABLE "public"."linkeddata" ADD CONSTRAINT "fkplace" FOREIGN KEY ("fkplace") REFERENCES "public"."place" ("idplace") ON UPDATE NO ACTION ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE;
ALTER TABLE "public"."linkeddata" ADD CONSTRAINT "fkseason" FOREIGN KEY ("fkseason") REFERENCES "public"."season" ("idseason") ON UPDATE NO ACTION ON DELETE NO ACTION NOT DEFERRABLE INITIALLY IMMEDIATE;

