import sys
import json
import numpy as np


# computed optimal weights and bias from the linear regression model

feature_to_weight_map = {'age': np.float64(256.97570583119415),
 'sex': np.float64(-18.591691641035084),
 'bmi': np.float64(337.0925519487799),
 'children': np.float64(425.27878352429065),
 'smoker': np.float64(23651.128855761242),
 'region_northwest': np.float64(-370.6773262277853),
 'region_southeast': np.float64(-657.8642965646335),
 'region_southwest': np.float64(-809.7993541824919)}
bias = np.float64(-11931.219050326692)
try:
    # Load the JSON data from standard input
    input_json = json.load(sys.stdin)
    temp = {}
    res = 0
    # check if all the relevant keys are in or not
    if len(input_json) == len(feature_to_weight_map):
        for key in input_json:
            value = feature_to_weight_map[key] * input_json[key]
            res += value
        res += bias

        # Print the processed JSON to standard output
        if res > 0:
            temp["predicted insurance charge"] = res
        else:
            temp["predicted insurance charge"] = 0
        json.dump(temp, sys.stdout)

except Exception as e:
    # If an error occurs, print it to standard error
    print(f"Error processing JSON: {e}", file=sys.stderr)
    sys.exit(1)
