# Deep learning techniques for COVID-19 diagnosis using CT images

The dataset used is made available for research purposes by the authors of the article “Open resource of clinical data from patients with pneumonia for the prediction of COVID-19 outcomes via deep learning” on the site http://ictcf.biocuckoo.cn/. This is multimodal and for each patient of 1342 contains a CT, biological values and comorbidities. 
iCTCF site offers also an indipendent dataset <b>nCT_pCT_NiCT</b> created for training a CNN that can classify a CT slice in three categories:
<ul>
  <li>nCT (negative CT): CT slice belonging to a negative patient (5705 images)</li>
  <li>pCT (positive CT): CT slice belonging to a positive patient (4001 images)</li>
  <li>NiCT (Non informative CT): CT slice not catpuring lung's area (9979 images)</li>
</ul>

<h3>1. Scraping and preprocessing</h3>
All CT images are available for download, so we used https://www.httrack.com/ application to automate the process of downloading. Other data (biological values, basic info and comorbidities) is available as a txt file named patient.txt, we wrote and used <b>structure_data.ipybn</b> in order to obtain JSON encoded file: <b>patient.json</b>.
<h4>1.1 Preprocessing images</h4>
We improved the segmentation process using similar technologies but ![preprocessing_onlybody](https://user-images.githubusercontent.com/32338761/132377979-ee6d297c-d253-47af-bd78-2fe506b70368.JPG)
