

import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
df = pd.read_csv("C:/Users/pankaj/Desktop/agrim/coding/c97/medium_data.csv")
data = df["reading_time"].tolist()
population_mean=statistics.mean(data)
print("Mean of Data = ", population_mean)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        i = i
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list,mean1,first_std_deviation_end,first_std_deviation_start,second_std_deviation_end,second_std_deviation_start,third_std_deviation_end,third_std_deviation_start):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x = [population_mean,population_mean],y = [0,0.17], mode = "lines", name = "Mean of Raw Data"))
    fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17], mode = "lines", name = "Mean of Sample Data"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start],y = [0,0.17], mode = "lines", name = "First Standard Deviation Start"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end],y = [0,0.17], mode = "lines", name = "First Standard Deviation End"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end],y = [0,0.17], mode = "lines", name = "Second Standard Deviation End"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start],y = [0,0.17], mode = "lines", name = "Second Standard Deviation Start"))
    fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end],y = [0,0.17], mode = "lines", name = "Third Standard Deviation End"))
    fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start],y = [0,0.17], mode = "lines", name = "Third Standard Deviation Start"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    mean1 = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print("Standard Deviation = ", std_deviation)
    first_std_deviation_start, first_std_deviation_end = mean1-std_deviation, mean1+std_deviation
    second_std_deviation_start, second_std_deviation_end = mean1-(2*std_deviation), mean1+(2*std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean1-(3*std_deviation), mean1+(3*std_deviation)
    show_fig(mean_list,mean1,first_std_deviation_end,first_std_deviation_start,second_std_deviation_end,second_std_deviation_start,third_std_deviation_end,third_std_deviation_start)
    print("Mean of Sample Data = ",mean1)
    z_score = (mean1-population_mean)/std_deviation
    print("Z-score = ",z_score)
setup()
