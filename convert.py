import pandas as pd

header_df2 = ['SD_FRONT','SD_END','CLASS']
dataframe = pd.read_csv('./AllData/sensor_readings_2.data',header=None,names=header_df2)
print(dataframe.head())
dataframe.to_csv('./AllData/sensor_readings_2.csv',index=False)

header_df4 = ['SD_FRONT','SD_LEFT','SD_RIGHT','SD_BACK','CLASS']
dataframe4 = pd.read_csv('./AllData/sensor_readings_4.data',header=None,names=header_df4)
print(dataframe4.head())
dataframe4.to_csv('./AllData/sensor_readings_4.csv',index=False)



header_df24 = ['US1','US2','US3','US4','US5','US6','US7','US8','US9','US10','US11','US12','US13','US14','US15','US16','US17','US18','US19','US20','US21','US22','US23','US24','CLASS']
dataframe24 = pd.read_csv('./AllData/sensor_readings_24.data',header=None,names=header_df24)
print(dataframe24.head())
dataframe24.to_csv('./AllData/sensor_readings_24.csv',index=False)
