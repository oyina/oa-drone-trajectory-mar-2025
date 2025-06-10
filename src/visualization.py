"""Utility to visualize photo plans.
"""

import typing as T

import plotly.graph_objects as go

from src.data_model import Waypoint


def plot_photo_plan(photo_plans: T.List[Waypoint]) -> go.Figure:
    """Plot the photo plan on a 2D grid.

    Args:
        photo_plans (T.List[Waypoint]): List of waypoints for the photo plan.

    Returns:
        T.Any: Plotly figure object.
    """
    x_vals, y_vals, speed_vals = [], [], []

    #build data axis
    for plan in photo_plans:
        x_vals.append(plan.x)
        y_vals.append(plan.y)
        speed_vals.append(round(plan.speed, 3))

    # Creating trace1
    trace1 = go.Scatter(
        x = x_vals,
        y = y_vals,
        mode = "lines+markers",
        name = "flight",
        marker = dict(color = 'green'),
        line=dict(dash='dot')

    )

    #creating drone trace
    drone = go.Scatter(
        x= [x_vals[0]], 
        y= [y_vals[0]],
        text= speed_vals,
        mode="markers",
        marker=dict(color="blue", size=20, symbol="x-dot"),
        name="drone ground midpoint")

    data = [trace1,drone]

    # Create figure
    fig = go.Figure(
        data=[
            trace1,drone
        ]
    )
    
    #layout settings
    fig.update_layout(
        #width=600,
        #height=450,
        xaxis=dict(range=[x_vals[0], x_vals[-1]], autorange=True, zeroline=False),
        yaxis=dict(range=[y_vals[0], y_vals[-1]], autorange=True, zeroline=False),
        margin=dict(l=50, r=50, t=50, b=50),
        title_text="Drone Flight Plan at {0:.3f} m/s".format(speed_vals[0]),
        title_x=0.5,
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        args=[
                            None,
                            {
                                "frame": {"duration": 1000, "redraw": False},
                                "fromcurrent": True,
                                "transition": {"duration": 1000},
                            },
                        ],
                        label="Play",
                        method="animate",
                    )
                ],
            )
        ],
    )
    #animations
    fig.update(
        frames=[
            go.Frame(
                data=[go.Scatter(x=[x_vals[k]], y=[y_vals[k]])], traces=[1]
            )  # fig.data[1] is updated by each frame
            for k in range(len(x_vals))
        ]
    )

    return fig