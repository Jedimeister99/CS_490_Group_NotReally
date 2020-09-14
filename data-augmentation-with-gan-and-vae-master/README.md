# data-augmentation-with-gan-and-vae :100:

[Vincent Fortin](https://github.com/vincentfortin) and I are using the [UTK Faces dataset](http://aicip.eecs.utk.edu/wiki/UTKFace) to for the project in the [_Machine Learning I_](https://www.hec.ca/en/courses/detail/?cours=MATH80629A) project. 

Unbalanced classes is one of the most frequent struggle when dealing with real data. Is it better to down/upsample, or do nothing at all? Another approach is to generate samples resembling the smallest class. In this project, we are using Variational AutoEncoders (VAEs) and Generative Adversarial Networks (GANs) to generate samples of the smallest class. Using human faces, we will determine if a convolutional neural network (CNN) will be trained better with generated samples, or without.  

## PROGRESS
1. [First we trained a VAE](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Variational%20Auto%20Encoder.ipynb) to generate human faces
2. [Then we trained a ConvNet with Pytorch](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Pytorch%20ConvNet%20Distinguishing%20Men%20and%20Women.ipynb) but it didn't work.
3. So we tried with Keras to see if our architecture was the problem. It's not. [We reached 90% accuracy](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Keras%20CNN%20Benchmark.ipynb). 
4. Here is the [Adversarial Auto Encoder](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Adversarial%20Auto%20Encoder.ipynb). The results are very clear.
5. Here is the [Wasserstein GAN](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Wasserstein%20GAN.ipynb).
6. The [Softmax GAN](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Softmax%20GAN.ipynb) worked out pretty well.
7. The [Deep Convolutional GAN](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Deep%20Convolutional%20GAN.ipynb) has worked but its performance is quite low.
8. Finally fixed the [Pytorch CNN](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Pytorch%20ConvNet%20Distinguishing%20Men%20and%20Women.ipynb), with 92% accuracy!
9. The CNN was able to classify generated samples, when trained on the original samples, with [100% accuracy](https://github.com/nicolas-gervais/data-augmentation-with-gan-and-vae/blob/master/Pytorch%20CNN%20to%20Test%20on%20the%20Generated%20Samples.ipynb).
## TO DO
- [x] Train a Tensorflow convolutional neural network as classifier
- [x] Create a GAN to generate human faces
- [x] Explore other generative methods
- [ ] Train CNNs to see if the accuracy is better with the generative methods
- [x] Fix the Pytorch CNN
- [ ] Use Keras and Pydot to plot the chosen architecture
- [x] Use generated samples as test set to see if there is untapped information
## PROJECT PLAN
1. Create various sample generators
2. Establish a benchmark CNN classifier, trained with 10% of the female samples (smaller class)
3. Train classifiers on 10% of the female samples, and add generated samples. Finally, compare performance.
    - VAE
    - GAN
    - other
4. Compare performance, plot 
5. Determine if the generated samples have information that is not contained in the original pictures
## Example of the Adversarial Auto Encoder Learning
![Alt Text](https://media.discordapp.net/attachments/552684049588682752/632967292946350080/sickgif.gif)

This is the output (generated faces) of the adversarial autoencoder.
