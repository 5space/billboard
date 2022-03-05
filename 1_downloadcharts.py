import billboard

def download_all_charts(start="2020-01-04"):
    chart = billboard.ChartData("hot-100", start)
    while chart.previousDate:
        with open("charts/" + chart.date + ".json", "w+") as file:
            file.write(chart.json())
        print("Saved", chart.date)
        chart = billboard.ChartData("hot-100", chart.previousDate)

download_all_charts()