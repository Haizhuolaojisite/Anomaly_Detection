"""
Any config specific to data processing step goes here.
"""

### extract_turbines method uses this list to create subset 
GROUP_TURBINE_NAME_LIST = ['1528-07','1528-22','1528-43']

### calculate mean variables
## The list of turbine names to be excluded from calculation. If it is empty, all turbines in turbine_group will be used
EXCLUDE_FROM_MEAN_LIST = ["1528-22"]
## A string with the suffix of the feature to be used for calculation. i.e. "MDY01-CT009-XQ50", it will be imputed.
FEATURE_ID = 'MDY01-CT009-XQ50'

### impute_feature variables
## A string with the name of the turbine (i.e. "1528-22")
TURBINE_NAME = '1528-22'

### model variables
## model name (ssdo or pbad)
MODEL_NAME = "pbad"
#MODEL_NAME = "ssdo"

## A list that specifies turbine names, date range and labels. 
## This is a list of lists. Each item has the name of the turbine, and the associated list of labels
## 1 is normal, -1 is anomaly, and 0 is unknown
LABEL_LIST =[
    ["1528-07",
        ['2020-01-11 23:50:00', '2020-01-12 01:30:00', 1], 
        ['2020-01-21 23:20:00', '2020-01-22 14:00:00', 1],
        ['2020-01-24 15:50:00', '2020-01-26 02:30:00', 1],
        ['2020-01-27 15:50:00', '2020-01-27 18:40:00', 1],
        ['2020-02-01 13:30:00', '2020-02-01 20:20:00', 1],
        ['2020-02-14 22:00:00', '2020-02-16 00:50:00', 1],
        ['2020-03-02 12:40:00', '2020-03-03 09:20:00', 1],
        ['2020-10-23 10:00:00', '2020-10-26 12:30:00', 1],
        ['2020-10-21 09:00:00', '2020-10-22 03:30:00', 1],
        ['2020-10-09 03:40:00', '2020-10-11 04:40:00', 1],
        ['2020-04-16 07:00:00', '2020-04-17 18:00:00', 1],
        ['2020-06-01 00:50:00', '2020-04-17 19:50:00', 1],
        ['2020-06-14 17:20:00', '2020-06-14 20:20:00', 1],
        ['2020-01-12 06:30:00', '2020-01-13 23:40:00', 1],
        ['2020-03-07 15:10:00', '2020-03-07 20:20:00', 1]
    ],
    ["1528-22",
        ['2020-08-04 06:20:00', '2020-08-10 08:40:00', 1], 
        ['2020-08-18 09:50:00', '2020-08-19 06:50:00', 1]
    ],
    ["1528-43",
        ['2020-10-11 20:20:00', '2020-10-12 18:20:00', 1], 
        ['2020-10-12 20:50:00', '2020-10-13 12:00:00', 1],
        ['2020-10-29 15:20:00', '2020-10-30 06:00:00', 1]
    ],
    ["1528-43",
        ['2020-03-30 02:40:00', '2020-04-12 06:00:00', -1]
    ],
    ["1528-07",
        ['2020-05-02 00:00:00', '2020-05-04 00:00:00', -1],
        ['2020-10-22 14:40:00', '2020-10-23 09:40:00', -1],
        ['2020-10-26 12:50:00', '2020-10-28 17:40:00', -1],
        ['2020-10-29 06:20:00', '2020-10-30 21:40:00', -1]
    ],
    ["1528-22",
        ['2020-05-04 03:50:00', '2020-06-01 00:30:00', -1],
        ['2020-03-31 13:30:00', '2020-04-03 12:00:00', -1],
        ['2020-11-24 11:50:00', '2020-11-27 00:10:00', -1]
    ],
    ["1528-07",
        ['2020-05-04 03:50:00', '2020-06-01 00:30:00', 0]
    ],
    ["1528-22",
        ['2020-01-01 00:10:00', '2020-01-03 01:00:00', 0]
    ],
    ["1528-43",
        ['2020-01-01 00:10:00', '2020-01-03 01:00:00', 0]
    ]
]



