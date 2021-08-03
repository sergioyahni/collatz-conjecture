import plotly.express as px
import pandas as pd

n = 1
while n != 0:
    n = int(input("N: "))
    list1 = list()
    while n > 1:
        if n % 2 != 0:
            n = n * 3 + 1
        else:
            n = n / 2
        list1.append(int(n))
    list2 = [n + 1 for n in range(len(list1))]

    df = pd.DataFrame(dict(number=list1, position=list2))

    # Use column names of df for the different parameters x, y, color, ...
    fig = px.line(df, x="position", y="number", title="Collatz conjecture",
                  labels={"position": "value at position"}  # customize axis label
                  )

    fig.show()
