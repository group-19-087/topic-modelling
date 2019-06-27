## Content
The code is split into three sections:

 1. Data preprocessing
 2. Topic Modeling using Latent Dirichlet Allocation (LDA)
 3. Segmenting text using Topic Tiling from Topic Models

### Data Preparation

Data fed into LDA should have the format as follows

> [M]  
> [document1]  
> [document2]  
> ...  
> [documentM]

in which the first line is the total number for documents [M]. Each line after that is one document. [documenti] is the ith document of the dataset that consists of a list of Ni words/terms.

> [documenti] = [wordi1] [wordi2] ... [wordiNi]

in which all [wordij] (i=1..M, j=1..Ni) are text strings and they are separated by the blank character.

#### Running the code:
```
python3 preprocessing.py
```
This will parse all text files in the **raw-data** folder and format it accordingly. The result will be stored as  **data.dat**

### Topic Modeling using Latent Dirichlet Allocation (LDA)
The input file (**data.data**) from the previous step is passed to the topic modelling program. Topic modelling is an unsupervised approach. To train the LDA model **lda.py** file need to be executed by specifying the no. of topics in the input file.
#### Running the code:
```
python3 lada.py <no. of topics>
```
### Topic Tiling from Topic Models
This section performs topictiling on the features obtained from topic models done in the previous step. Fix the number of topics that is deemed appropriate. Topic Tiling reads the input file contained in the folder **files_to_segment** and segment the text in a topic based manner using the lda model trained in the previous step. The code also stores the output file in a folder called **output**. Topic tiling requires following parameters

 - name of input file contained in files_to_segment

#### Running the code
```
python3 topic_tiling.py input-text
```

### References
- http://jgibblda.sourceforge.net/
- https://github.com/riedlma/topictiling
