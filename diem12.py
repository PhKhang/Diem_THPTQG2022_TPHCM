# Import a shit ton of dependencies
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html
from rich.progress import track

#import sys

requests.packages.urllib3.disable_warnings()
URL = "https://diemthi.hcm.edu.vn/Home/Show"

def main():
    session_requests = requests.session()
    
    # Name of output file
    tenfile = "diemthi.csv"
    
    # Run through all the ID numbers in the range
    for x in track(range(2000000, 2085090 ), description="Processing...") : 
        # Add leading 0 of the ID
        sbd = "0" + str(x)
        
        # Create payload for POST request
        payload = {
            "SoBaoDanh": sbd
        }

        # Perform login
        result = session_requests.post(URL, data = payload, headers = dict(referer = URL), verify=False)
        soup = BeautifulSoup(result.text, "lxml")
        
        # Check if the ID is correct or not. If not, continue to next one
        if int(result.headers['content-length']) < 1010:
            continue

        table = soup.select('table')[0]
        
        table_df = pd.read_html(str(table))[0]
        
        pdsbd = pd.DataFrame([sbd])
        
        # Append data to file
        table_df.iloc[[1]].to_csv(tenfile, mode='a', index=False, header=False)
        pdsbd.to_csv(tenfile, mode='a', index=False, header=False)

if __name__ == '__main__':
    main()
