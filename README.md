# events2csv
This script converts VMware NSX Defender exported JSON data into CSV format.
<br>
<b>
  Python3 is required in order to run this script perperly.
  </b>
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
<br>
<br>
<br>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
