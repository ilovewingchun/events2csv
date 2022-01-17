# events2csv
This script converts VMware NSX Defender exported JSON data into CSV format.
<br>
Usage:
```
cat <JSON event data> | python 3 events2csv.py <CSV file output>
```
Finally, open the newly saved CSV file with your favorite app.
<br>
<br>
Example:
<br>
```
% cat list-network.json | python3 events2csv.py > event.csv
% file event.csv 
event.csv: CSV text
```
