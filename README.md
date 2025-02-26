# CASP16-CAPRI MassiveFold Data

MassiveFold data generated for CASP16-CAPRI and provided to all predictors for phase 2. All data are available for download 
[here](https://entrepot.recherche.data.gouv.fr/dataverse/casp16mf).

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
our top 5 and made the ensemble of predictions available to all predictors for a CASP16 phase 2 prediction
round where they could use our predictions in any way they wanted to submit an updated top 5.
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


## Monomeric targets

## Multimeric targets
