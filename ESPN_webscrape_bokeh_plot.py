from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, ranges
from bs4 import BeautifulSoup as bs4
import requests, pandas

title='NBA Player Scoring Per Game Statistics'
year=[int(2015+i) for i in range(4)]
#create a loop that will go thru each year printing out a new chart 

for current_year in year:
    base_url='http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/avgPoints/year/{}/seasontype/2'.format(current_year)
    response=requests.get(base_url)
    soup=response.content
    html_soup=bs4(soup,'html.parser')

    table_rows=html_soup.findAll('tr')[1:]
    player_table_data=[[i.text for i in table_rows[x] ] for x in range(len(table_rows)) ] #extracts all table data from tr attribute
    player_names_lc=[i.text.strip() for i in html_soup.findAll('a') if 'http://www.espn.com/nba/player/' in i['href']] #locate matching tags with href attr
    column_names_lc=[cn.text for cn in html_soup.findAll('td',limit=12)] #retrieve column headers for dataframe

    #clean up dataframe 
    df=pandas.DataFrame(player_table_data,columns=column_names_lc)
    df=df.drop(df.index[10::11]) #drop intermediate repeating rows with text "RK	PLAYER	TEAM FGM-FGA	FG%	3PM-3PA	3P%	FTM-FTA	FT%"
    df['PLAYER']=player_names_lc #clean & replace the 'PLAYER column with just only the players name, not position
    df['GP']=df['GP'].apply(pandas.to_numeric,errors='coerce') 
    df['PTS']=df['PTS'].apply(pandas.to_numeric,errors='coerce')
    df['MPG']=df['MPG'].apply(pandas.to_numeric,errors='coerce')
    df['INDEX']=df.index  #create an index column needed for Column Data Source 

    #create columnDataSource 
    cds=ColumnDataSource(df)

    p=figure(x_axis_type='auto',y_axis_label='Average_Points_Per_Game',title="{} {}-{}".format(title,current_year, current_year +1),
    x_minor_ticks=2,plot_width=888, plot_height=888)

    #set text for vertical bars to equal player name
    p.text(x=df.index,y=df['PTS'],text=df['PLAYER'],angle=45,text_font='casual',text_font_size={'value':'10pt'})

    #implement hovertool, hover tool is mapped to the values and columns you wish to show for each vertical bar 
    hover=HoverTool(tooltips=[("PLAYER","@PLAYER"),("PTS","@PTS"),("GP","@GP"),("MPG","@MPG")]) 
    p.add_tools(hover)


    p.vbar(x='INDEX', width=0.5, bottom=0, top='PTS', color="firebrick",source=cds) #source maps to columns in dataframe
    output_file('vbar.html')
    show(p)


#Python Exercises implementing BeautifulSoup,  Pandas and Bokeh libs ; Elliott Arnold 3-25-19