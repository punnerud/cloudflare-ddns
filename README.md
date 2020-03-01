# cloudflare-ddns
Use Cloudflare as a DDNS with your own domain name, using Python.

Replace 123123123 and example.com in update.py with your credentials, zone-ID and record-ID.
Example here for more information: https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record

Run update.py regulary to watch for changes in the IP-address.
Example using crontab on Mac and Ubuntu, or Scheduler on Windows.

Example for Mac/Ubuntu:
*/ * * * * cd /folder/where/your/program/live/ && timeout 20 python3 update.py
