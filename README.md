# Deep learning techniques for COVID-19 diagnosis using CT images

The dataset used is made available for research purposes by the authors of “Open resource of clinical data from patients with pneumonia for the prediction of COVID-19 outcomes via deep learning” https://www.nature.com/articles/s41551-020-00633-5. This is multimodal and for each patient of 1342 contains a CT, biological values and comorbidities.

<h3>1. Scraping and preprocessing</h3>
All CT images are available for download, so we used https://www.httrack.com/ application to automate the process of downloading. Other data (biological values, basic info and comorbidities) is available in a txt file named patient.txt, we write and used structure_data.ipybn in order to obtain JSON encoded file: <bold>patient.json</bold>.
