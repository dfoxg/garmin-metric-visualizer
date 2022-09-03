import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import matplotlib.dates as mdates
import time


def showHelp():
    print("Usage:")
    print("run.py <garminfile>.json")


def getJSONContent(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def getFileType(elementOfFile):
    if "raceTimeMarathon" in elementOfFile:
        return "race_predictions"
    if "vo2MaxValue" in elementOfFile:
        return "max_met"
    return "unknown"


def showGraphMaxMet(elements):
    fig = plt.figure()
    fig.canvas.set_window_title('Max Met Data')
    plt.title("Max Met Data")

    plt.subplot(1, 2, 1)
    plt.plot(
        elements["calendarDate"].values,
        elements["vo2MaxValue"].values,
        color="red",
        label="Vo2Max",
        marker="o",
    )
    plt.legend()
    plt.grid(True)
    plt.title("Vo2Max")
    plt.xticks(rotation=45)

    plt.subplot(1, 2, 2)
    plt.plot(
        elements["calendarDate"].values,
        elements["fitnessAge"].values,
        color="blue",
        label="Fitness Age",
        marker="o",
    )
    plt.legend()
    plt.grid(True)
    plt.title("Fitness Age")
    plt.xticks(rotation=45)

    plt.show()


def parseSeconds(s, pos):
    if s > 3600:
        return time.strftime("%H:%Mh", time.gmtime(s))
    else:
        return time.strftime("%M:%Sm", time.gmtime(s))


def showGraphRunRace(elements):
    fig = plt.figure()
    plt.title("Run Race Predictions")
    fig.canvas.set_window_title('Run Race Predictions')

    secondsFormatter = matplotlib.ticker.FuncFormatter(parseSeconds)

    ax = plt.subplot(1, 4, 1)
    plt.plot(
        elements["calendarDate"].values,
        elements["raceTime5K"].values,
        color="red",
        label="5k",
        marker="o",
    )
    plt.legend()
    plt.grid(True)
    plt.title("5k")
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter(secondsFormatter)

    ax = plt.subplot(1, 4, 2)
    plt.plot(
        elements["calendarDate"].values,
        elements["raceTime10K"].values,
        color="red",
        label="10k",
        marker="o",
    )
    plt.legend()
    plt.grid(True)
    plt.title("10k")
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter(secondsFormatter)

    ax = plt.subplot(1, 4, 3)
    plt.plot(
        elements["calendarDate"].values,
        elements["raceTimeHalf"].values,
        color="red",
        label="Half",
        marker="o",
    )
    plt.legend()
    plt.grid(True)
    plt.title("Half Marathon")
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter(secondsFormatter)

    ax = plt.subplot(1, 4, 4)
    plt.plot(
        elements["calendarDate"].values,
        elements["raceTimeMarathon"].values,
        color="red",
        label="Full",
        marker="o",
    )
    plt.legend()
    plt.grid(True)
    plt.title("Marathon")
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter(secondsFormatter)

    plt.show()


def main():
    json = getJSONContent(sys.argv[1])
    if np.isscalar(json) == False:
        df = pd.DataFrame(json)
        # df['calendarDate'] = pd.to_datetime(df['calendarDate'], format="%Y-%m-%d")

        fileType = getFileType(json[0])
        if fileType == "race_predictions":
            showGraphRunRace(df)
        elif fileType == "max_met":
            showGraphMaxMet(df)
        else:
            print("cant detect file type!")
            exit(-1)
    else:
        print("json-file does not contain an array!")
        exit(-1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        showHelp()
        exit(-1)
    else:
        main()
