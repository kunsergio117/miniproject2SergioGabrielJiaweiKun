# INF601 - Advanced Programming in Python
# Sergio Gabriel Jiawei Kun
# Mini Project 2

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.

import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go # for graphing geographical heatmaps


# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.

### How many Majors in the STEM field are in each state in the age range of 40 to 65 years?

# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
degrees = pd.read_csv('Bachelor_Degree_Majors.csv')

degrees = degrees[["State", "Sex", "Science and Engineering", "Science and Engineering Related Fields", "Age Group"]]
degrees = degrees[degrees["Age Group"] == "40 to 64"] # narrowing down to my desired age groups
degrees = degrees[degrees["Sex"] == "Total"] # narrowing to only the total for Sex, since the csv file has rows called males, females and total.
# now adding together the 2 columns that combine to reflect the total STEM field Majors into 1 column
# the numbers are strings originally with commas in them so remove commas and typecast to integers
degrees["STEM field Majors"] = degrees["Science and Engineering"].str.replace(',', '').astype(int) + degrees["Science and Engineering Related Fields"].str.replace(',', '').astype(int)
degrees = degrees[["State", "STEM field Majors"]] # removing Sex and Age Group since no relevance anymore
# print(degrees.head())

# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

# bar graph
plt.figure(figsize=(19, 6))
plt.title('STEM field Majors in the US by State')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.ylabel('Degree holders (in  millions)')
plt.bar(degrees["State"], degrees["STEM field Majors"], width=0.8, align="center")
plt.show()

# creating the 'charts' folder if it does not exist already
if not os.path.exists('charts'):
    os.makedirs('charts')
png = f"charts/degreesbystates_bar_graph.png"
if os.path.exists(png):  # removes the old graph if there is one
    os.remove(png)
plt.savefig(png)
plt.close()

# geographical heatmap
state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}
fig = go.Figure(data=go.Choropleth(
    locations= degrees["State"].map(state_abbreviations), # this parameter requires the 2 letter abbreviations for the states, hence using the dictionary above.
    locationmode='USA-states',
    z=degrees["STEM field Majors"],
    colorscale='Magma', # use 'Viridis' for printing in black and white.
    colorbar_title= 'Color scale',
))

# Update the layout to set the title and show the figure
fig.update_layout(
    title_text='State-based Heatmap',
    geo_scope='usa',
)
fig.show() # this generates a webpage to show a map of the US

# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.
