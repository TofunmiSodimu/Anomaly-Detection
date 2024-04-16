# Anomaly-Detection

- 'Training_Data_Rooms_Only' contains the 'Time', 'Obj_ID', 'Obj_name', 'Room_ID', 'Room_name', and associated 'Activity' for a 51 days of a person in Household A's routine.
- 'Uncorrupt_Testing_Data_Rooms_Only' contains the 'Time', 'Obj_ID', 'Obj_name', 'Room_ID', 'Room_name', and associated 'Activity' for 24 days of a person in Household A's routine.
-  'Corrupt_Testing_Data_Rooms_Only' contains the corrupted 'Time', 'Obj_ID', 'Obj_name', 'Room_ID', 'Room_name', and associated 'Activity' for 24 days of a person in Household A's routine. Corrupted implies that the 'Room_ID' and 'Room_name' values have been randomly changed to simulate a misplaced object.
-  'CorruptTestingData.ipynb' - this may be used for corrupting the testing data to get the files in 'Corrupt_Testing_Data_Rooms_Only'.
-  'CreateTrainingandTestingData.ipynb' - this may be used to grab data from the HOMER_PLUS dataset (https://github.com/Maithili/HOMER_PLUS/tree/main)
- Model1 - Anomaly Detection using Local Outlier Factor
- Model2 - Anomaly Detection using CNN
