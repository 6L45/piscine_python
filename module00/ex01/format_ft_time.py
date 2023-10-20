#! /bin/python3

import time

seconds_since_epoch = time.time()

formatted_seconds = "{:,.3f}".format(seconds_since_epoch)
scientific_seconds = "{:.2e}".format(seconds_since_epoch)

formatted_date = time.strftime("%b %d %y")

print("Seconds since January 1, 1970:", formatted_seconds,
      "or", scientific_seconds, "in scientific notation")
print(formatted_date)
