# QR Code Generator
A Program that generates QR Code Images from the given data.

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* qrcode
* datetime
* optparse
* time
* colorama

## Input
It takes the following arguments from the command that is used to run the Python Program:
* '-d', "--data" : Data to store in the QR Code
* '-s', "--save" : Name of the Image file to save the Generated QR Code
* '-l', "--load" : Load data from the given file

## Output
It generates the QR Code from the given data and saves it into an image with the specified name, or if the name is not specified then the image is saved with name as the current date and time.<br />
The Format of the Image File would be ".png".