# Time Series Classification

* In this project I have developed a Time Series classification model based on Fourier Transform. I have used three classifiers Random Forest, Logistic Regression and Neighourest Neighbour. After that I have compared their performances using scatter plots.

* The datasets used to make the models are present [here](/datasets/readme.md)

## Results

* [Results](/results.csv)

* These results show the error values each model has with the corresponding dataset.

* The three classifiers used are:
- Nearest Neighbour(ed)
- Random Forest(rf)
- Logistic Regression(lr)

* All three classifier are used with the following three values derived from fourier transform of orignal dataset:
- Phase and Amplitude(phase_amp)
- Real and Imaginary values(real_imag)
- Phase, Amplitude, Real and Imaginary values(real_imag_phase_amp)

## Wins,Losses And Ties (With Nearest Neighbour(DTW)) 

* These models are used on fourier transform of the given dataset.

#### 1) Nearest neighbour ( Euclidean Distance - Real, Imaginary, Phase and Amplitude)
* Wins=61<br>
 Tie=2<br>
 Loss=50<br>

#### 2) Nearest neighbour ( Euclidean Distance - Phase and Amplitude)
* Wins=55<br>
 Tie=1<br>
 Loss=57<br>
 
#### 3) Nearest neighbour ( Euclidean Distance - Real and Imaginary)
* Wins=62<br>
 Tie=1<br>
 Loss=50<br>
 
#### 4) Logistic Regression ( Real and Imaginary)
* Wins=37<br>
 Tie=4<br>
 Loss=72<br>
 
#### 5) Logistic Regression ( Real, Imaginary, Phase and Amplitude)
* Wins=48<br>
 Tie=4<br>
 Loss=61<br>
 
#### 6) Logistic Regression ( Phase and Amplitude)
* Wins=36<br>
 Tie=2<br>
 Loss=75<br>
 
#### 7) Random Forest ( Phase and Amplitude)
* Wins=54<br>
 Tie=3<br>
 Loss=56<br>
 
#### 8) Random Forest (Real and Imaginary)
* Wins=40<br>
 Tie=3<br>
 Loss=70<br>
 
#### 9) Random Forest (Real, Imaginary, Phase and Amplitude)
* Wins=53<br>
 Tie=2<br>
 Loss=58<br>
 

## Scatter plots

#### 1) Random Forest(1)
![Random Forest(1)](/scatter_plots/Random_Forest(1).jpg)

#### 2) Random Forest(2)
![Random Forest(2)](/scatter_plots/Random_Forest(2).jpg)

#### 3) Random Forest(3)
![Random Forest(2)](/scatter_plots/Random_Forest(3).jpg)

#### 4) Logistic Regression(1)
![Logistic Regression(2)](/scatter_plots/Logistic_Regression(1).jpg)

#### 5) Logistic Regression(2)
![Logistic Regression(2)](/scatter_plots/Logistic_Regression(2).jpg)

#### 6) Logistic Regression(3)
![Logistic Regression(3)](/scatter_plots/Logistic_Regression(3).jpg)

#### 7) Neighourest Neighbour(1)
![Neighourest Neighbour(1)](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Neighourest%20Neighbour(1).jpg)

#### 8) Neighourest Neighbour(2)
![Neighourest Neighbour(2)](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Neighourest%20Neighbour(2).jpg)

#### 9) Neighourest Neighbour(3)
![Neighourest Neighbour(3)](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Neighourest%20Neighbour(3).jpg)

#### 10) Random Forest Vs Logistic Regression
![Random Forest Vs Logistic Regression](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Random%20Forest_VS_Logistic%20Regression.jpg)

#### 11) Random Forest Vs Neighourest Neighbour
![ Random Forest Vs Neighourest Neighbour](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Neighourest%20Neighbour_VS_Random%20Forest.jpg)

#### 12) Logistic Regression Vs Neighourest Neighbour
![ Logistic Regression Vs Neighourest Neighbour](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Neighourest%20Neighbour_VS_Logistic%20Regression.jpg)

#### 13) Neighourest Neighbour(DTW) VS Neighourest Neighbour(Ed-on Fourier Transform)
![Neighourest Neighbour(DTW) VS Neighourest Neighbour(Ed-on Fourier Transform)](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/Neighourest%20Neighbour_VS_Logistic%20Regression.jpg)


#### 19) All Models
![All Models](https://github.com/Srishti013/Time_Series_Classification/blob/main/scatter_plots/All_models.jpg)









