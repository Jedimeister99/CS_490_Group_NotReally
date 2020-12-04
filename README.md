Applications of Data Augmentation for Existing Databases

Contributors: Brandon Horton, Gregory Patti, Hannah Szmurlo, Dr. Michael J. Reale

Overview:

This is the repository for Applications of Data Augmentation for Existing Databases. This is a part of the CS 490/548 course taught by
Dr. Michael J. Reale at SUNY Polytechnic in Fall 2020.

Dependencies and Setup:

DeepFakes/Faceswap:

Link: https://github.com/deepfakes/faceswap

- requires an Anaconda environment to be set up
- Python 3 
- Tensorflow
- Faceswap GUI or CLI needs to be set up

PRNet:

Link: https://github.com/YadiraF/PRNet

- requires an Anaconda environment to be set up
- Python 2.7 (numpy,skimage,scipy)
- Tensorflow >= 1.4
- optional: dlib, opencv

Face3D:

Link: https://github.com/YadiraF/face3d

- requires an Anaconda environment to be set up
- Python 2 or 3
- Python packages: numpy, skimage, scipy, matplotlib, Cython

Running the Project:

Faceswap:

Primary Files:

- faceswap.py: using the CLI/GUI, this is the main file that calls the extraction, training and conversion scripts
- extract.py: script that performs the extraction process
- convert.py: script that performs the conversion process
- train.py: script that performs the training process
- CKSwap.py: cycles through the CK+ dataset and:
  
  - creates a copy of the dataset, but making the removing the sequence folders from the file structure
  - indivudally calls the extraction, conversion, and training scripts for every possible combination of subjects

How to Run:

- options are extraction, convert, train
- CLI: python faceswap.py extract 
- GUI: follow guide from DeepFakes repository (https://github.com/deepfakes/faceswap#gui)

PRNet:

Primary Files:

- main.py: main.py will recursively run through the CK+ Dataset and generate .obj files for each image

How to Run:

- python main.py: this will recursively run through the CK+ Dataset and generate .obj files for each image.
- After obtaining the CK+ Dataset, change CKfilePath to the appropriate path. Change save_folder to your desired save location
- Additional parsers can be added. For example: python main.py --isDlib True. Full list of parsers can be found at the bottom of main.py

Face3D:

Primary Files:

- 4_light.py: python 4_light.py, will add light & estimate light to 3Dmm. Output is a gif
- 3_transform.py: transform mesh & estimate matrix. Output is a gif

How to Run:

- Prepare BFM Data (see https://github.com/YadiraF/face3d/blob/master/examples/Data/BFM/readme.md)
- Change filepath to desired location. Default output folder is /face3d/examples/results/(light or transform)
- python 3_transform.py
- python 4_light.py

















