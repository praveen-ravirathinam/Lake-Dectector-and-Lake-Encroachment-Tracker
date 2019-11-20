# Lake-Dectector-and-Lake-Encroachment-Tracker
Simple programs for highlighting the boundary of a lake/pond from a satellite image and tracking the encroachment of a lake between two differents points in time

Prerequisites: OpenCV

Lake Detector:
![alt text](https://github.com/praveen-ravirathinam/Lake-Dectector-and-Lake-Encroachment-Tracker/blob/master/output_station2019.png)
(Boundary marked by thin red line)

USE: <br />
input format : $python3 <prog_name>.py -i <image1>.png -c <color> -n <numberofregions> <br />
example : $ python3 lakedetector.py -i station2019.png -c green -n 2 <br />

Lake Encroachment:
![alt_text](https://github.com/praveen-ravirathinam/Lake-Dectector-and-Lake-Encroachment-Tracker/blob/master/outputof_lake2007_lake2019.png)
(red line represents boundary in 2007, blue line represents boundary in 2019)

USE: <br />
input format : $python3 <prog_name>.py -i <image1>.png -o <image2.png> -co <color> -cn <color> -n <numberofregions> <br />
example : $ python3 encroachment.py -i lake2007.png -o lake2019.png -cn green -n 1 <br />
<br />
Choice of color is offered because technology has evolved over time and so the color of water may vary from image to image<br />
Image Sources: Google Earth
