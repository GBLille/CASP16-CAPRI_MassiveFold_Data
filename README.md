# CASP16-CAPRI MassiveFold Data

<!-- TOC -->
* [CASP16 MassiveFold abstract](#casp16-massivefold-abstract)
* [Sets of parameters used](#sets-of-parameters-used)
* [Dataset download](#dataset-download)
  * [CASP Monomeric MassiveFold full data](#casp-monomeric-massivefold-full-data)
  * [CASP Multimeric MassiveFold full data](#casp-multimeric-massivefold-full-data)
  * [CASP Monomeric MassiveFold PDBs only](#casp-monomeric-massivefold-pdbs-only)
  * [CASP Multimeric MassiveFold PDBs only](#casp-multimeric-massivefold-pdbs-only)
  * [CAPRI MassiveFold scoring data](#capri-massivefold-scoring-data)
* [Decompress data](#decompress-data)
* [Rankings download](#rankings-download)
<!-- TOC -->

MassiveFold data generated for the CASP16-CAPRI experiment and provided to all predictors for phase 2. All data are available 
for download on the french Recherche Data Gouv repository [here](https://entrepot.recherche.data.gouv.fr/dataverse/casp16mf).

All targets are described on the CASP (Critical Assessment of Techniques for Protein Structure Prediction) website 
(https://predictioncenter.org/) and were generated with the collaboration of CAPRI (Critical Assessment of PRediction of Interactions)
(https://www.ebi.ac.uk/pdbe/complex-pred/capri/casp-capri/).

## CASP16 MassiveFold abstract
<p style="text-align: justify;">
The results of CASP15 have shown that increasing the number of predictions while including diversity in
the inference process led to a significant improvement for multimer predictions. However, this massive
sampling strategy requires access to a large GPU infrastructure to be able to generate the predictions in a
short period of time, and is therefore not accessible to all predictor groups.
For CASP16, we used <a href="https://github.com/GBLille/MassiveFold" target="_blank">MassiveFold</a>, which allows
massively expanding the sampling of structure predictions by optimizing the computing of AlphaFold
based predictions. It improves the parallelization of the structure inference by splitting the computing on
CPU for alignments, running automated batches of structure prediction on GPU, and gathering the results
in a single output directory, with a consolidated ranking and a variety of plots. MassiveFold uses
<a href="https://github.com/GBLille/AFmassive" target="_blank">AFmassive</a> inference engine, an updated version of AFsample
that offers additional diversity parameters for massive sampling. MassiveFold can also use ColabFold.
We used a large GPU cluster to generate 8040 predictions for the majority of the targets, submitted
our top 5 and <b>made the ensemble of predictions available to all predictors for a CASP16 phase 2 prediction
round</b> where they could use our predictions in any way they wanted to submit an updated top 5.
</p>

More details available in [MassiveFold_CASP16_Abstract.pdf](MassiveFold_CASP16_Abstract.pdf)

## Sets of parameters used

Only protein targets were considered. For each monomeric and oligomeric target, 8040 predictions were calculated, 
except for a few challenging ones, which are:
- H1217 (5878 residues): 395 predictions
- H1227 (5689 residues): 45 structures were generated and the top 5 were submitted for phase 1, but for phase 2, 
the structure was trimmed to 2101 residues and 8040 predictions were generated
- H1258 (3092 residues); T1257 (3789 residues) and H1265 (3924 residues): 2040 predictions
- T1271 subunits: 2680 predictions each
- T1295 (3752 residues) and T1269 (2820 residues): 4080 predictions

The 8040 predictions were generated with the 8 following sets of parameters, 1005 predictions per set: 

|                 Setup                 |  Dropout Evoformer  |  Dropout Structure Module  |  Templates  |  Recycles  |  Structure Inference Engine  |
|-------------------------------------|:-------------------:|:--------------------------:|:-----------:|:----------:|:----------------------------:|
|               afm_basic               |                     |                            |      X      |     21     |          AFmassive           |
|            afm_woTemplates            |                     |                            |             |     21     |          AFmassive           |
|           afm_dropout_full            |          X          |             X              |      X      |     21     |          AFmassive           |
|     afm_dropout_full_woTemplates      |          X          |             X              |             |     21     |          AFmassive           |
|    afm_dropout_full_woTemplates_r3    |          X          |             X              |             |     3      |          AFmassive           |
|     afm_dropout_noSM_woTemplates      |          X          |                            |             |     21     |          AFmassive           |
|            cf_woTemplates             |                     |                            |             |     21     |          ColabFold           |
|      cf_dropout_full_woTemplates      |          X          |             X              |             |     21     |          ColabFold           |

## Datasets download

Data for individual targets can be downloaded [here](https://entrepot.recherche.data.gouv.fr/dataverse/casp16mf). 

However, the main files can be downloaded using the scripts available in the `dataset_download` folder. These python3 
scripts can be run directly from the folder to download the data:
- `download_all_casp_massivefold_monomers.py` downloads all the MassiveFold.tar.gz files which contain all the 
predictions for each **monomeric** target divided into 8 folders named after the conditions; each one contains predictions 
as well as pickle files, sequence alignments, rankings and plots.
- `download_all_casp_massivefold_multimers.py` downloads all the MassiveFold.tar.gz files which contain all the 
predictions for each **multimeric** target
- `download_all_casp_massivefold_only_pdbs_monomers.py` downloads only all the PDBs of the MassiveFold set for each 
**monomeric** target
- `download_all_casp_massivefold_only_pdbs_multimers.py` downloads only all the PDBs of the MassiveFold set for each 
**multimeric** target
- `download_all_capri_massivefold_scoring.py` downloads all the CAPRI scoring files for MassiveFold data of each target

They rely on the csv files also located in the folder, which contain all the direct download links. The content of each 
csv is also listed below.

***N.B***: in case of error downloading a file, remove this file and run the script again; it will only download the 
missing files.

### CASP Monomeric MassiveFold full data

[casp_massivefold_files_monomers.csv](./dataset_download/casp_massivefold_files_monomers.csv)

| File Name | Download Link |
|-----------|----------------|
| T1207_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616526](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616526) |
| T1210_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616549](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616549) |
| T1212_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616561](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616561) |
| T1226_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616601](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616601) |
| T1231_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616614](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616614) |
| T1243_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617275](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617275) |
| T1246_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617282](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617282) |
| T1266_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617327](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617327) |
| T1269_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/YRPWXZ](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/YRPWXZ) |
| T1271s1_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616698](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616698) |
| T1271s2_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616700](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616700) |
| T1271s3_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616714](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616714) |
| T1271s4_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616711](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616711) |
| T1271s5_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616715](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616715) |
| T1271s6_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616703](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616703) |
| T1271s7_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616691](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616691) |
| T1271s8_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616705](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616705) |
| T1272s2_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617256](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617256) |
| T1272s3_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617243](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617243) |
| T1272s4_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617252](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617252) |
| T1272s5_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617259](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617259) |
| T1272s6_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617238](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617238) |
| T1272s7_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617260](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617260) |
| T1272s8_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617261](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617261) |
| T1272s9_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617237](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617237) |
| T1274_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/WFWMZ6](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/WFWMZ6) |
| T1276_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/GY46OH](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/GY46OH) |
| T1278_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/7XB2QF](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/7XB2QF) |
| T1279_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617637](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617637) |
| T1280_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617647](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617647) |
| T1284_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617660](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617660) |
| T1299_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/RIWWKK](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/RIWWKK) |

### CASP Multimeric MassiveFold full data

[casp_massivefold_files_multimers.csv](./dataset_download/casp_massivefold_files_multimers.csv)

| File Name | Download Link |
|-----------|----------------|
| H1202_T238_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/608722](https://entrepot.recherche.data.gouv.fr/api/access/datafile/608722) |
| H1204_T240_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/610428](https://entrepot.recherche.data.gouv.fr/api/access/datafile/610428) |
| H1208_T244_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612186](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612186) |
| H1213_T256_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612207](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612207) |
| H1215_T248_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612217](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612217) |
| H1217_T258_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612241](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612241) |
| H1220_T262_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614161](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614161) |
| H1222_T266_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614165](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614165) |
| H1223_T268_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614179](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614179) |
| H1225_T270_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615814](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615814) |
| H1227_T272_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615905](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615905) |
| H1229_T274_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615906](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615906) |
| H1230_T276_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616079](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616079) |
| H1232_T278_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616094](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616094) |
| H1233_T280_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616177](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616177) |
| H1236_T292_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616184](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616184) |
| H1244_T294_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616204](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616204) |
| H1245_T296_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616211](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616211) |
| H1258_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616222](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616222) |
| H1265_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616266](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616266) |
| H1267_T300_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616285](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616285) |
| T1201_T236_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616503](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616503) |
| T1206_T242_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616520](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616520) |
| T1218_T260_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616585](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616585) |
| T1219v1v2_MassiveFold_A12.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616592](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616592) |
| T1234_T288_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616633](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616633) |
| T1235_T290_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616648](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616648) |
| T1237_T282_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616665](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616665) |
| T1240_T286_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616685](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616685) |
| T1249_T250_T252_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/VZSMDC](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/VZSMDC) |
| T1257_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/TMDB4T](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/TMDB4T) |
| T1259_T298_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617318](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617318) |
| T1270_T302_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/PXERTO](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/PXERTO) |
| T1292_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617666](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617666) |
| T1294_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617708](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617708) |
| T1295_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617644](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617644) |
| T1298_T309_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617843](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617843) |

### CASP Monomeric MassiveFold PDBs only

[casp_massivefold_files_only_pdbs_monomers.csv](./dataset_download/casp_massivefold_files_only_pdbs_monomers.csv)

| File Name | Download Link |
|-----------|----------------|
| T1207_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616529](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616529) |
| T1210_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616543](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616543) |
| T1212_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616563](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616563) |
| T1226_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616603](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616603) |
| T1231_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616610](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616610) |
| T1243_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617273](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617273) |
| T1246_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617281](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617281) |
| T1266_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617330](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617330) |
| T1269_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/6RZJTZ](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/6RZJTZ) |
| T1271s1_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616717](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616717) |
| T1271s2_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616718](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616718) |
| T1271s3_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616704](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616704) |
| T1271s4_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616709](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616709) |
| T1271s5_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616697](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616697) |
| T1271s6_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616696](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616696) |
| T1271s7_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616694](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616694) |
| T1271s8_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616699](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616699) |
| T1272s2_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617240](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617240) |
| T1272s3_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617239](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617239) |
| T1272s4_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617247](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617247) |
| T1272s5_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617253](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617253) |
| T1272s6_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617255](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617255) |
| T1272s7_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617248](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617248) |
| T1272s8_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617249](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617249) |
| T1272s9_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617246](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617246) |
| T1274_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/CY3EWO](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/CY3EWO) |
| T1276_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/EQHCCM](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/EQHCCM) |
| T1278_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/FGOINF](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/FGOINF) |
| T1279_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617642](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617642) |
| T1280_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617649](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617649) |
| T1284_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617663](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617663) |
| T1299_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/LQY2PH](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/LQY2PH) |

### CASP Multimeric MassiveFold PDBs only

[casp_massivefold_files_only_pdbs_multimers.csv](./dataset_download/casp_massivefold_files_only_pdbs_multimers.csv)

| File Name | Download Link |
|-----------|----------------|
| H1202_T238_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/608723](https://entrepot.recherche.data.gouv.fr/api/access/datafile/608723) |
| H1204_T240_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/610466](https://entrepot.recherche.data.gouv.fr/api/access/datafile/610466) |
| H1208_T244_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612183](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612183) |
| H1213_T256_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612210](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612210) |
| H1215_T248_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612216](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612216) |
| H1217_T258_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612236](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612236) |
| H1220_T262_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612268](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612268) |
| H1222_T266_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614168](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614168) |
| H1223_T268_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614177](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614177) |
| H1225_T270_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614191](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614191) |
| H1227_T272_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615837](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615837) |
| H1229_T274_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615914](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615914) |
| H1230_T276_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616081](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616081) |
| H1232_T278_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616089](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616089) |
| H1233_T280_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616099](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616099) |
| H1236_T292_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616193](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616193) |
| H1244_T294_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616198](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616198) |
| H1245_T296_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616212](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616212) |
| H1258_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616219](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616219) |
| H1265_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616256](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616256) |
| H1267_T300_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616282](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616282) |
| T1201_T236_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616507](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616507) |
| T1206_T242_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616517](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616517) |
| T1218_T260_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616571](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616571) |
| T1219v1v2_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616593](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616593) |
| T1234_T288_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616635](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616635) |
| T1235_T290_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616653](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616653) |
| T1237_T282_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616660](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616660) |
| T1240_T286_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616677](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616677) |
| T1249_T250_T252_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/K7HVG2](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/K7HVG2) |
| T1257_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/TXD2NO](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/TXD2NO) |
| T1259_T298_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617324](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617324) |
| T1270_T302_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/NZZGCV](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/NZZGCV) |
| T1292_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617670](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617670) |
| T1294_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617711](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617711) |
| T1295_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617634](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617634) |
| T1298_T309_only_pdbs_MassiveFold.tar.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617845](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617845) |

### CAPRI MassiveFold scoring data

[capri_massivefold_scoring_files.csv](./dataset_download/capri_massivefold_scoring_files.csv)

| File Name | Download Link |
|-----------|----------------|
| T236_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616511](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616511) |
| T238_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/608718](https://entrepot.recherche.data.gouv.fr/api/access/datafile/608718) |
| T240_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/610420](https://entrepot.recherche.data.gouv.fr/api/access/datafile/610420) |
| T242_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616518](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616518) |
| T244_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612187](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612187) |
| T248_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612214](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612214) |
| T250_T252_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/S1SOMP](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/S1SOMP) |
| T256_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612209](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612209) |
| T258_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612233](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612233) |
| T260_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616569](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616569) |
| T262_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/612264](https://entrepot.recherche.data.gouv.fr/api/access/datafile/612264) |
| T266_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614166](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614166) |
| T268_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614175](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614175) |
| T270_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/614190](https://entrepot.recherche.data.gouv.fr/api/access/datafile/614190) |
| T272_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615832](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615832) |
| T274_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/615908](https://entrepot.recherche.data.gouv.fr/api/access/datafile/615908) |
| T276_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616077](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616077) |
| T278_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616090](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616090) |
| T280_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616098](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616098) |
| T282_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616658](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616658) |
| T286_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616676](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616676) |
| T288_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616628](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616628) |
| T290_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616645](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616645) |
| T292_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616188](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616188) |
| T294_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616197](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616197) |
| T296_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616206](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616206) |
| T298_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617322](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617322) |
| T300_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/616283](https://entrepot.recherche.data.gouv.fr/api/access/datafile/616283) |
| T302_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/LTTMCN](https://entrepot.recherche.data.gouv.fr/api/access/datafile/:persistentId?persistentId=doi:10.57745/LTTMCN) |
| T309_CAPRI_scoring.pdb.gz | [https://entrepot.recherche.data.gouv.fr/api/access/datafile/617846](https://entrepot.recherche.data.gouv.fr/api/access/datafile/617846) |

## Decompress data

Because the tar.gz files are very large, we recommend to use the `pigz` tool, to benefit from multicore decompression. 
For instance:
```
pigz -d -c H1202_T238_MassiveFold.tar.gz | tar -xvf -
```
The CAPRI scoring gz files can be uncompressed with `gunzip`.

## Rankings download

Each tar.gz archive contains a `ranking.csv` file with AlphaFold2 scores. The most complete ones are those included 
in the `only_pdbs` tar.gz archives. They contain:
- for monomers: the set of parameters used (condition), the model name, the AlphaFold2 confidence score, which is the 
mean plddts and ranking using the mean plddts
- for multimers: the set of parameters used (condition), the model name, the iptm value, the ptm value, the AlphaFold2 
confidence score which is 0.8\*iptm+0.2\*ptm and ranking using this score

For convenience, we provide here two archives which gather the `ranking.csv` files for all the targets:
- For monomers: [ranking_casp_massivefold_monomers.tar.gz](./ranking_casp_massivefold_monomers.tar.gz)
- For multimers: [ranking_casp_massivefold_multimers.tar.gz](./ranking_casp_massivefold_multimers.tar.gz)

## Assessments download

Data for individual targets can be downloaded [here](https://entrepot.recherche.data.gouv.fr/dataverse/casp16mf). 

But he CASP and CAPRI assessment files can be downloaded here:he main files can be downloaded using the scripts available in the `dataset_download` folder. These python3 
scripts can be run directly from the folder to download the data:
- `download_all_casp_massivefold_monomers.py` downloads all the MassiveFold.tar.gz files which contain all the 
predictions for each **monomeric** target divided into 8 folders named after the conditions; each one contains predictions 
as well as pickle files, sequence alignments, rankings and plots.
- `download_all_casp_massivefold_multimers.py` downloads all the MassiveFold.tar.gz files which contain all the 
predictions for each **multimeric** target
- `download_all_casp_massivefold_only_pdbs_monomers.py` downloads only all the PDBs of the MassiveFold set for each 
**monomeric** target
- `download_all_casp_massivefold_only_pdbs_multimers.py` downloads only all the PDBs of the MassiveFold set for each 
**multimeric** target
- `download_all_capri_massivefold_scoring.py` downloads all the CAPRI scoring files for MassiveFold data of each target
