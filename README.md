# Cambium PMP450i Configuration Creator

This python script will ingest a CSV file with location name, mac address, local ip address, subnet mask, and gateway and then create a <macAddress>.cfg for each row in the csv. All .cfg files will be outputted in the /configs directory.

Tested on Windows 7 Powershell with Python installed. Should work on Windows/MacOS/Linux.

This is used in zero-touch deployment of Cambium PMP450x devices. The .cfg files live on an HTTP server that is referenced in a DHCP Option 66. Further explanation of the zero-touch deployment process on Cambium can be obtained in their Configuration and User Guide: https://fccid.io/ANATEL/02739-14-07745/Manual/A8BC25E6-EDEF-4674-AE4D-C1A83A6668F6/PDF

## Requirements (to generate configs)

* Python
* Template configuration file for your Cambium devices

## Requirements (to run zero-touch deployment)

* HTTP/TFTP/FTP server
* DHCP rule 66

## Usage

1. `git clone` or copy the repository to your filesystem.
1. `cd` to the directory
1. Fill out `devices.csv` with your desired values. **NOTE: macAddress must not have any delineation (e.g. aa:bb:cc:dd:ee:ff should be aabbccddeeff). This should be easy if you used a barcode scanner on the Cambium devices like I did.**
1. Either edit template-example.json to suit your needs, or generate your own using the instructions provided by Cambium in the configuration guide linked above. I just ran a diff between the factory default configuration and my desired configuration by downloading the configuration from a factory defaulted device and a fully configured device.
1. Run the script with `python configurator.py devices.csv template.json` substituting any name changes you may have made.
1. You should now have your configuration files ready to be loaded on your FTP/HTTP/TFTP server for zero-touch deployment. I personally used a mini web-server to serve these.

### Zones
In devices.csv you might notice the Zone column. This assumes a two zone (color code) deployment, and the supplied template shows as much. If you specify 1, it will set color zone 1 as priority 1, and color zone 2 and priority 2. If you specify 2, color zone 2 will be set a priority 1. This is useful in active/failover multi-zone deployments. Cambium supports multiple zones and priorities but this is not supported at this time...feel free to open a PR :)
