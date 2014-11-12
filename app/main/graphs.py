import pygal
from pygal import Config as PygalConfig
from pygal.style import LightColorizedStyle as lcstyle
from pygal.style import LightenStyle


def make_stackedbar(title,plan,forecast,opp,height=330,width=500):
    # plt.style.use('ggplot')
    plan /=100000
    round(plan,0)
    forecast /=100000
    round(forecast)
    opp/=100000
    round(opp,0)
    assert title and plan and forecast and opp, "missing params"
    bar_chart = pygal.StackedBar(style=pygal.style.RedBlueStyle, width=500, height=height,
        label_font_size=12, legend_box_size=6, value_font_size=12)
    bar_chart.title = title
    bar_chart.x_labels = ['Plan','Forecast']
    bar_chart.add('Plan', [plan, None])
    bar_chart.add('Forecast', [None, forecast])
    bar_chart.add('Oppty', [None, opp])
    return bar_chart.render(is_unicode=True)

def make_wklybar(title,plan,forecast,opp):
    # plt.style.use('ggplot')
    assert title and plan and forecast and opp, "missing params"
    bar_chart = pygal.StackedBar(style=pygal.style.RedBlueStyle, height=400)
    bar_chart.title = title
    bar_chart.x_labels = map(str,range(12))
    bar_chart.add('Actual', [10,12,8,14,12,11,0,0,0,0,0,0])
    bar_chart.add('Forecast', [0,0,0,0,0,0,12,12,11,14,15,13])
    return bar_chart.render(is_unicode=True)