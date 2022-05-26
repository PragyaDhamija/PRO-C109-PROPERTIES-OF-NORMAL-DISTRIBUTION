import random
import pandas as pd
import plotly.figure_factory as pff
import statistics as st
import plotly.graph_objects as pgo

df = pd.read_csv("StudentsPerformance.csv")
data = df ["reading score"].tolist()

mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
std = st.stdev(data)

first_std_start, first_std_end = mean-std, mean+std
second_std_start, second_std_end = mean-(2*std), mean+(2*std)
third_std_start, third_std_end = mean-(3*std), mean+(3*std)

fig = pff.create_distplot([data] , ["reading scores"] , show_hist = False) 
fig.add_trace(pgo.Scatter(x = [mean , mean] , y = [0, 0.17], mode = "lines+markers", name = "MEAN"))
fig.add_trace(pgo.Scatter(x = [first_std_start , first_std_start] , y = [0, 0.17], mode = "lines+markers", name = "FIRST STANDARD DEVIATION start"))
fig.add_trace(pgo.Scatter(x = [first_std_end , first_std_end] , y = [0, 0.17], mode = "lines+markers", name = "FIRST STANDARD DEVIATION end"))
fig.add_trace(pgo.Scatter(x = [second_std_start , second_std_start] , y = [0, 0.17], mode = "lines+markers", name = "SECOND STANDARD DEVIATION start"))
fig.add_trace(pgo.Scatter(x = [second_std_end, second_std_end] , y = [0, 0.17], mode = "lines+markers", name = "SECOND STANDARD DEVIATION end"))
fig.add_trace(pgo.Scatter(x=[third_std_start,third_std_start], y=[0,0.17], mode = "lines+markers", name = "THIRD STANDARD DEVIATION start"))
fig.add_trace(pgo.Scatter(x=[third_std_end,third_std_end], y=[0,0.17], mode = "lines+markers", name = "THIRD STANDARD DEVIATION end"))
fig.show()

data_within_1std = [i for result in data if result>first_std_start and result<first_std_end]
data_within_2std = [i for result in data if result>second_std_start and result<second_std_end]
data_within_3std = [i for result in data if result>third_std_start and result<third_std_end]

print ("Mean of this data is {}".format(mean))
print ("Median of this data is {}".format(median))
print ("Mode of this data is {}".format(mode))
print ("Standard deviation of this data is {}".format(std_deviation))
print("{} % of data that lies within first std".format(len(data_within_1std)*100.0 / len(data)))
print("{} % of data that lies within second std".format(len(data_within_2std)*100.0 / len(data)))
print("{} % of data that lies within third std".format(len(data_within_3std)*100.0 / len(data)))

