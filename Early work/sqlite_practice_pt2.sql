-- Creating table and importing data
CREATE TABLE dataset(
  "CO_ANO" INTEGER,
  "CO_MES" INTEGER,
  "CO_NCM" INTEGER,
  "CO_UNID" INTEGER,
  "CO_PAIS" TEXT,
  "SG_UF_NCM" TEXT,
  "CO_VIA" TEXT,
  "CO_URF" TEXT,
  "QT_ESTAT" INTEGER,
  "KG_LIQUIDO" INTEGER,
  "VL_FOB" INTEGER
);

.mode csv
.separator ;
.import C:/Users/mathe/Documents/EXP_2019.csv dataset 

--Delete the duplicate header, since the skip 1 command didn't work
DELETE FROM dataset WHERE rowid in (select rowid FROM dataset LIMIT 1);

--Changing back to list mode, easer to read
.mode list

--Just trying to identify everything algae related
SELECT DISTINCT CO_NCM FROM keys
WHERE NO_NCM_POR LIKE '%carragen%' OR NO_NCM_POR LIKE '% algas%')
--optional command, helped me figuring out the exitence of duplicates
ORDER by NO_NCM ASC;

--the actual query that leads do the desired result
SELECT CO_NCM, SUM(VL_FOB) FROM dataset
WHERE CO_NCM IN (SELECT DISTINCT CO_NCM FROM keys
  WHERE NO_NCM_POR LIKE '%carragen%' OR NO_NCM_POR LIKE '%algas%')
GROUP BY CO_NCM;

/*COMMENT SECTION 

Don't know why, but the --skip 1 command doesn't seem to work
Still trying to figure it out, but I believe that it has something to do 
with sqlite version


To be  improved:
Proper indexing;
Removal of duplicates;
Maybe search optmizations*/