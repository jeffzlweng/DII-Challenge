# Reproducibility Project Instructions for CS598 DL4H in Spring 2022

## Citation to the original paper

Zhang, D., Yin, C., Hunold, K.M., Jiang, X., Caterino, J.M. and Zhang, P., 2021.
An interpretable deep-learning model for early prediction of sepsis in the emergency department. Patterns, 2(2), p.100196.

## Link to the original paper’s repo

https://github.com/yinchangchang/DII-Challenge


## Dependencies
-	use below instruction to install all the dependencies for this project
	
		pip install -r requirement.txt

## Data download instruction
-	Data are in the below folder
		
		./file/...
## Preprocessing code + command

-	command to creat result folder for data preprocessing results

		mkdir result
		mkdir data
		mkdir data/models

-	command to generate json files 

		cd preprocessing
		python gen_master_feature.py --master-file ../file/master.csv
		python gen_feature_time.py --vital-file ../file/vital.csv				# only for task1
		python gen_vital_feature.py --vital-file ../file/vital.csv
		python gen_label.py --label-file ../file/label.csv

## Training + Evaluation command
-	the best model will saved in ../data/models/
		
		python main.py --task task1		# for case1
		python main.py --task task2		# for case2

#	You can also run the code by:

		python run.py --label-file ../file/label.csv --vital-file ../file/vital.csv --master-file  ../master.csv --task case1


## Pretrained model
-       the pretrained model are in the below location
       		
		/data/models/

## Table of results # Reproducibility Project Instructions for CS598 DL4H in Spring 2022

## Citation to the original paper

Zhang, D., Yin, C., Hunold, K.M., Jiang, X., Caterino, J.M. and Zhang, P., 2021.
An interpretable deep-learning model for early prediction of sepsis in the emergency department. Patterns, 2(2), p.100196.

## Link to the original paper’s repo

https://github.com/yinchangchang/DII-Challenge


## Dependencies
-	use below instruction to install all the dependencies for this project
	
		pip install -r requirement.txt

## Data download instruction
-	Data are in the below folder
		
		./file/...
## Preprocessing code + command

-	command to creat result folder for data preprocessing results

		mkdir result
		mkdir data
		mkdir data/models

-	command to generate json files 

		cd preprocessing
		python gen_master_feature.py --master-file ../file/master.csv
		python gen_feature_time.py --vital-file ../file/vital.csv				# only for task1
		python gen_vital_feature.py --vital-file ../file/vital.csv
		python gen_label.py --label-file ../file/label.csv

## Training + Evaluation command
-	the best model will saved in ../data/models/
		
		python main.py --task task1		# for case1
		python main.py --task task2		# for case2

#	You can also run the code by:

		python run.py --label-file ../file/label.csv --vital-file ../file/vital.csv --master-file  ../master.csv --task case1


## Pretrained model
-       the pretrained model are in the below location
       		
		/data/models/

## Table of results for main reproducibility result 

### Case 1
	
|     Metric    |    Value      |
| ------------- | ------------- |
|      AUC      |     0.988     |
|      F1       |     0.941     |
|    Accuracy   |     0.944     |
|    Recall     |     1.000     |
|    Precision  |     0.888     |
		
### Case 2

|     Metric    |    Value      |
| ------------- | ------------- |
|      AUC      |     0.931     |
|      F1       |     0.758     |
|    Accuracy   |     0.723     |
|    Recall     |     0.950     |
|    Precision  |     0.631     |
		
		


### Case 1
	
|     Metric    |    Value      |
| ------------- | ------------- |
|      AUC      |     0.988     |
|      F1       |     0.941     |
|    Accuracy   |     0.944     |
|    Recall     |     1.000     |
|    Precision  |     0.888     |
		
### Case 2

|     Metric    |    Value      |
| ------------- | ------------- |
|      AUC      |     0.931     |
|      F1       |     0.758     |
|    Accuracy   |     0.723     |
|    Recall     |     0.950     |
|    Precision  |     0.631     |
		
		

