import plotly.express as px

# Modern color palette matching the dashboard theme
COLOR_PALETTE = ['#2563eb', '#3b82f6', '#60a5fa', '#93c5fd', '#10b981', '#34d399', '#f59e0b', '#fbbf24']

def sales_by_region(df):
    data = df.groupby("Region", as_index=False)["Sales"].sum()
    fig = px.bar(
        data,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=True,
        color="Region",
        color_discrete_sequence=COLOR_PALETTE
    )
    fig.update_layout(
        margin=dict(t=50, b=40, l=40, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#1e293b', size=12),
        title_font=dict(size=16, color='#1e293b', family='Inter'),
        xaxis=dict(
            title_font=dict(color='#1e293b', size=12),
            tickfont=dict(color='#1e293b', size=11)
        ),
        yaxis=dict(
            title_font=dict(color='#1e293b', size=12),
            tickfont=dict(color='#1e293b', size=11),
            gridcolor='#e2e8f0'
        ),
        autosize=True,
        height=400,
        showlegend=False
    )
    fig.update_traces(textfont_size=12, textfont_color='#1e293b', textposition='outside')
    return fig

def age_distribution(df):
    fig = px.histogram(
        df,
        x="Customer Age",
        color="Customer Gender",
        title="Customer Age Distribution",
        nbins=20,
        color_discrete_map={"Male": "#2563eb", "Female": "#10b981"}
    )
    fig.update_layout(
        margin=dict(t=50, b=40, l=40, r=40),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#1e293b', size=12),
        title_font=dict(size=16, color='#1e293b', family='Inter'),
        xaxis=dict(
            title_font=dict(color='#1e293b', size=12),
            tickfont=dict(color='#1e293b', size=11)
        ),
        yaxis=dict(
            title_font=dict(color='#1e293b', size=12),
            tickfont=dict(color='#1e293b', size=11),
            gridcolor='#e2e8f0'
        ),
        legend=dict(
            font=dict(color='#1e293b', size=11),
            bgcolor='rgba(255,255,255,0.8)'
        ),
        autosize=True,
        height=400,
        barmode='overlay'
    )
    fig.update_traces(opacity=0.75)
    return fig

def gender_pie(df):
    gender_counts = df["Customer Gender"].value_counts().reset_index()
    gender_counts.columns = ["Customer Gender", "Count"]
    fig = px.pie(
        gender_counts,
        names="Customer Gender",
        values="Count",
        hole=0.4,
        title="Customer Gender Split",
        color="Customer Gender",
        color_discrete_map={"Male": "#2563eb", "Female": "#10b981"}
    )
    fig.update_layout(
        margin=dict(t=50, b=40, l=40, r=40),
        font=dict(color='#1e293b', size=12),
        title_font=dict(size=16, color='#1e293b', family='Inter'),
        legend=dict(
            font=dict(color='#1e293b', size=11),
            bgcolor='rgba(255,255,255,0.8)'
        ),
        autosize=True,
        height=400,
        showlegend=True,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff'
    )
    fig.update_traces(
        textinfo='percent+label',
        textfont=dict(color='#1e293b', size=12),
        pull=[0.03, 0.03]
    )
    return fig
