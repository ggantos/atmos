# ATMOS

Exploratory data analysis and machine learning on a freely available atmospheric research dataset.

---

## Data

A few different datasets were examined for use in this project. After examining the various sources, I chose to use data uploaded to Kaggle on March 29, 2020.

The data consists of hourly measurements of six pollutants surrounding Seoul for the years 2017-2019. Here's the link to the data uploaded by bappe and the corresponding CC BY-SA 4.0 license: https://www.kaggle.com/bappekim/air-pollution-in-seoul/metadata.

The original data is compressed small enough to be stored in this repo at `src/data/raw/raw_data.tar.gz`.

For every observation there exists a cooresponding instrument status code: 0: Normal, 1: Need for calibration, 2: Abnormal
4: Power cut off, 8: Under repair, 9: abnormal data.

---

## Data Exploration

The dataset consists of four files and I chose to first examine *Measurement_summary.csv* via the notebook *explore_data_summary*. After describing the dataframe and looking at pairplots, I noticed that some of the values are still -1 and that the pairplots were not very informative even once the negative values had been deleted.

Next I attempted to explore the original data to understand why there were still negatives in the dataset. I did this exploration in the notebook *explore_data_original*. Althought I was aware that there were instrument status codes for all observations, I assumed all pollutants shared the same code but this is not the case. Within the same hour at the same station (of which there are 25 unique stations), different pollutant sensors have different instrument status codes.

After this I attempted to mask the data in *Measurement_summary.csv* in the notebook *explore_data_masks*. However, this did not prove to be as useful as I originally planned.

Finally, I went to the file I should have used from the beginning, *Measurement_info.csv* and explored data by pollutant in the notebook *explore_data_by_pollutants*. Here it was possible to see the effects of the instrument statuses on the readings. From here it was time to move on to the modeling.

---

## Modeling

Starting with the very simplest of inputs, I attempted to predict a single hour in time further after being given the past 20 hours as input. I ran the model for both CO and SO2 and the model is constructed very simply of an LSTM layer and a Dense single output layer.


---

## Future questions that could be answered with this data

* can we predict future timeseries via historical timeseries?
* can we predict the instrument status?
    - all non-normal vs normal (excluding negative values)
    - 3-6 classes
* can we cluster neighborhoods in Seoul via their pollutants?
* can we predict values by station or with all stations at one time?


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**

---

## Acknowledgments

* Work in modelling notebooks heavily based off of: https://www.tensorflow.org/tutorials/structured_data/time_series#part_1_forecast_a_univariate_time_series
