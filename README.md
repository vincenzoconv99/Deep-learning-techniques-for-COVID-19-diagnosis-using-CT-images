# Deep learning techniques for COVID-19 diagnosis using CT images

The dataset used is made available for research purposes by the authors of “Open resource of clinical data from patients with pneumonia for the prediction of COVID-19 outcomes via deep learning” on the site http://ictcf.biocuckoo.cn/. This is multimodal and for each patient of 1342 contains a CT, biological values and comorbidities. 
iCTCF site offers also an indipendent dataset <b>nCTpCTNiCT</b> created for training a CNN that can classify a CT slice in three categories:
<ul>
  <li>nCT (negative CT): CT slice belonging to a negative patient</li>
  <li>pCT (positive CT): CT slice belonging to a positive patient</li>
  <li>NiCT: CT slice not catpuring lung's area</li>
</ul>

<h3>1. Scraping and preprocessing</h3>
All CT images are available for download, so we used https://www.httrack.com/ application to automate the process of downloading. Other data (biological values, basic info and comorbidities) is available as a txt file named patient.txt, we wrote and used structure_data.ipybn in order to obtain JSON encoded file: <b>patient.json</b>.
