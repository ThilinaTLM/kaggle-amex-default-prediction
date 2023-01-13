#!/bin/bash

DATASET_NAME='munumbutt/amexfeather'

mkdir data 
cd data
kaggle datasets download $DATASET_NAME
unzip amexfeather.zip
