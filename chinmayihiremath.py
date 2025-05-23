import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer
import pandas as pd
from st_social_media_links import SocialMediaIcons
from streamlit_gsheets  import GSheetsConnection
from streamlit_clickable_images import clickable_images
import base64
import os

st.set_page_config(page_title="ChinmayiHiremath", layout="wide", page_icon="👩🏻‍💼")

page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://png.pngtree.com/background/20210715/original/pngtree-blue-gradient-watercolor-background-picture-image_1284318.jpg");
background-size: cover;
background-color: #ffffff10;
backdrop-filter: blur(50px); 
}          

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>"""

st.markdown(page_bg_image, unsafe_allow_html=True)

#Removing Hamburger/Deploy option in web app
# hamburg_remove = """
# <style>
# .st-emotion-cache-147n6fk.ef3psqc6 {
#    visibility: hidden;
# }
# .st-emotion-cache-125megu.ef3psqc5 {
#    visibility: hidden;
# }
# .st-emotion-cache-kgpedg.e1dbuyne10 {
#    visibility: hidden;
# }
# .stAppHeader.st-emotion-cache-am3w00.e10jh26i0 {
#    visibility: hidden;
# }
# </style>
# """
# st.markdown(hamburg_remove, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("### Chinmayi")

with col2:
    choice = option_menu(
    menu_title = None,
    options = ["Home", "About", "Experience", "Resume", "Contact"],
    icons= ["house-door", "search-heart-fill", "file-person", "pencil-square", "telephone-outbound-fill"],
    menu_icon = "cast",
    default_index=0,
    orientation="horizontal")  
st.write("---")   
     
if choice == "Home":    
    st.write("")
    intro, image = st.columns([10,4])
    intro.markdown("<H2 style = 'text-align: center;'>Hi, </h2>", unsafe_allow_html=True)
    intro.markdown("<H2 style = 'text-align: center;'>I'm Chinmayi Hiremath </h2>", unsafe_allow_html=True)
    intro.markdown("<H4 style = 'text-align: center;'><em>A Devops Engineer</em></h4>", unsafe_allow_html=True)
    intro.markdown("<H5 style = 'text-align: center;'>Enable faster and more reliable software delivery through infrastructure automation, CI/CD pipelines, and cloud-native practices to drive informed engineering and business strategies.</h5>", unsafe_allow_html=True)

    image.image("Chinmayi_photo-.png")
    st.write("")
    st.write("---") 
    st.write("")

    collect, clean, explore, modelling   = st.columns(4)
    
    collect.markdown("#### :basket: Collect")
    collect.write("Data collection is my systematic approach to gathering information from various sources to create a comprehensive dataset for analysis and informed decision-making.")
    
    clean.markdown("#### :broom: clean")
    clean.write("Data cleaning is my process of identifying and correcting errors and inconsistencies in datasets to ensure their accuracy and reliability for analysis.")

    explore.markdown("#### :telescope: Explore")
    explore.write("Data exploration is an essential part of my workflow, where I analyze and visualize datasets to understand their structure, patterns, and relationships, guiding further analysis.")
    
    modelling.markdown("#### :snowflake: Modelling")
    modelling.write("Data modeling is my process of creating a conceptual representation of data structures and relationships, defining data types and interactions, and establishing rules to organize data effectively for analysis and efficient querying in databases.")

    visualize, interpretation, report  = st.columns(3)
    
    visualize.markdown("#### :bar_chart: Visualize")
    visualize.write("Data visualization involves my creation of visual formats, such as charts and dashboards, to represent data and communicate insights clearly, making complex information more accessible for decision-making.")

    interpretation.markdown("#### :brain: Interpretation")
    interpretation.write("Data interpretation is my process of analyzing and making sense of data to draw meaningful conclusions and translate findings into actionable insights for decision-making.")
    
    report.markdown("#### :bookmark_tabs: Report")
    report.write("Reporting is my process of organizing and presenting data and analysis results in a structured format to communicate insights and recommendations effectively to stakeholders.")

    st.write("")
    st.write("---") 
    st.write("")

elif choice == "About":
    st.write("")
    st.markdown("### Inspired by the Data and Coding")
    st.text("""Inspired by the Data and coding which can be used to analyse with many functionalities and make better and benificial decisions. experiments and works to make it easier for people to understand the code and use data effectively. primarily uses python to explore the Data and coding.
             
               

               worked at Amer UID Smart Services, Dubai. As Junior Data Analyst over a year of experience explored various facets of data helping the management to make better and efficient decisions.""")
    st.write("---")

      
    with st.expander("Certifications"):
        col1, col2 = st.columns(2)
        with col1:
            panel = st.container(height=580, border=True)
            with panel:
                st.image("IBM_Certification.jpg", caption="Data Visualization")
        
        with col2:
            panel = st.container(height=780, border=True)
            with panel:
                st.image("MeriSKILL.jpg", caption="Data Analyst")
        
        col3, col4 = st.columns(2)
        with col3:
            panel = st.container(height=780, border=True)
            with panel:
                st.image("AI Variant.jpg", caption="Data Analytics")

        with col4:
            panel = st.container(height=780, border=True)   
            with panel:
                st.image("Excelr.jpg", caption="Data Analyst Certification")     
     
    with st.expander("Education"):
          st.markdown("#### :book: Education")
          st.text("""Graduated in Computer Application from the Karnataka Univercity, Dharwad - India.
                  Completed PU in Commerce from R L S COMP PU College, Dharwad.""")

    with st.expander("Skills"):
          st.markdown("#### :wrench: Skills")
          st.write("- Languages :  English (Professional), Kannada (Native), Hindi (Proficient)")
          st.write("- Programming :  Python (Professional), SQL (Professional)")        
          st.write("- Libraries/Frameworks :  Pandas, Matplotlib, Seaborn, Streamlit")
          st.write("- Tools :  VS Code, PyCharm, Jupyter, Google colab, MySQL, SQL Server, Git & Github")          
          st.write("- Visualization Tools :  Tableau (professional), Power BI (professional)")
    
elif choice == "Experience":
    st.write("")
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Function to switch pages
    def switch_page(target_page):
        st.session_state.page = target_page
    
    # Function to encode image as base64
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    def bank_info_page():
        st.markdown("#### Bank Loan Applications Reports")
        st.write("Report 1")
        st.image("bankloanimages/Bank Loan Applications.png")
        st.write("""This report provides an analysis of the bank loan applications based on key metrics such as loan types, demographics, housing
        situations, employment details, education levels, and organization types. The visual analysis further highlights patterns and trends 
        across these categories.""")

        st.write("Report 2")
        st.image("bankloanimages/Bank Loan Defaulters.png")
        st.write("""This dashboard titled \"Loan Defaulters vs Repayers\" provides an in-depth analysis of loan default patterns among a total of 307,511 applicants, with 24,825 (8.07%) identified as defaulters. The visualization categorizes defaulters by gender, age, contract type, income type, education, family status, housing type, employment year, and organization type.""")

        st.write("Report 3")
        st.image("bankloanimages/Bank Loan repayers.png")
        st.write("This dashboard titled \"Loan Defaulters vs Repayers\" provides an in-depth analysis of loan repayment patterns among a total of 307,511 applicants, with 2,82,686 (91.93%) identified as repayers. The visualization categorizes repayers by gender, age, contract type, income type, education, family status, housing type, employment year, and organization type, offering valuable insights into repayment behaviors.")
    
        st.write("Report 4")
        st.image("bankloanimages/Bank Loan credit, good price and income correlations.png")
        st.write("This dashboard titled \"Credit, Goods Price, and Income Correlations\" analyzes the relationships among credit amount, goods price, and income for 307,511 applicants. It highlights a strong positive correlation between credit amount and goods price, limited impact of income on credit size, and the distribution of applicants by family size (majority with 0 or 1 child). Additionally, it examines the variability of annuity amounts relative to income and employment.")

        st.write("Report 5")
        st.image("bankloanimages/Bank Loan Comprehensive financial overview.png")
        st.write("The \"Comprehensive Financial Overview\" report examines financial patterns across 307,511 applicants, focusing on credit amount, goods price, and income distribution. It reveals cash loans as the most utilized contract type, with females receiving higher credit amounts on average than males. Credit levels peak among individuals aged 30–50, with employment durations of up to 20 years correlating with higher credit and goods prices. Repayers consistently secure higher financial benefits compared to defaulters.")

        st.write("Report 6")
        st.image("bankloanimages/Bank Loan Comprehensive financial overview2.png")
        st.write("The report reveals that credit and goods price utilization is highest among married individuals, those with secondary or higher education, and working professionals, particularly in managerial roles. Credit levels peak for applicants aged 30–50, with longer employment durations correlating with greater financial engagement. Private business entities and individuals living in houses or apartments report the highest credit and goods price activity. Minimal engagement is seen among students, unemployed individuals, and those with unknown or unstable family and housing statuses.")
    
        st.write("Report 7")
        st.image("bankloanimages/Bank Loan Privious application status based on applicants.png")
        st.write("The report highlights cash loans as the most common contract type, with repairs and electronics leading in loan purposes and purchases. Connectivity and consumer electronics dominate seller industries, while cash payments through banks are the preferred method. Middle-yield applicants and cash portfolios account for the majority of activity. Approval rates are high, but refusals and unused offers indicate potential for improvement.")
        st.write("---")
        st.write("If you are more intrested please hit the below links for more information:")
        st.markdown(":bank: [Bank Loan Analysis](https://github.com/SantoshRottayyanavar/Bank-Loan-Analysis---Tableau-and-Python)")
        st.markdown(":bar_chart: [Bank Loan Analysis Dashboard](https://public.tableau.com/app/profile/santosh.rottayyanavar2698/viz/BankloanAnalysisextract/BankLoanApplicantions)")
        st.markdown(":bookmark_tabs: [Bank Loan Analysis Final Report](https://github.com/SantoshRottayyanavar/Bank-Loan-Analysis---Tableau-and-Python/blob/main/Bank%20Loan%20Analisis%20Final%20Report.pdf)")     
        if st.sidebar.button("Back to Home"):  
            switch_page("home") 
    
    def hr_info_page():
        st.markdown("#### HR Data Analysis Reports")
        st.image("hrimagesfolder/HRmain.jpg")
        st.write("This image showcases an HR Data Analysis dashboard with a clean and professional layout. The title, \"HR Data Analysis,\" is prominently displayed at the top, and a \"Main Page\" button is centered for navigation. The left side lists key HR metrics, such as Employee Distribution, Monthly Hours, Turnover Rate, and Workplace Accidents. A visual illustration on the right complements the theme, enhancing its appeal.")

        st.write("Report 1")
        st.image("hrimagesfolder/HR1 Employee_distribution.jpg")
        st.write("This dashboard provides an overview of employee distribution and HR metrics. Key highlights include:")
        st.write("\* Turnover and attrition rates are 31.25% and 23.81%, respectively, with a retention rate of 76.19%.")
        st.write("\* The sales department has the highest number of employees (4,140), while management has the least (630).")
        st.write("\* Most employees fall under the low to medium salary categories, with only 8.25% earning high salaries.")
        st.write("\* The distribution of projects shows the sales department leading with over 7,800 projects, followed by technical and support teams.")
    
        st.write("Report 2")
        st.image("hrimagesfolder/HR2Employee Avg Monthly Hrs and satisfaction.jpg")
        st.write("This dashboard analyzes average monthly hours and satisfaction levels:")
        st.write("\* The sales department logs the highest average monthly hours (832K) and satisfaction levels (2.54K), followed by technical and support departments.")
        st.write("\* Employees with medium salaries work the most hours (48.76%), while high salary groups show the highest satisfaction levels (47.82%).")
        st.write("\* Management and HR departments have the lowest satisfaction levels and average monthly hours.")
        st.write("\* There is a positive correlation between average monthly hours and satisfaction in departments like sales, technical, and support.")
    
        st.write("Report 3")
        st.image("hrimagesfolder/HR3 Employees Precence.jpg")
        st.write("This dashboard provides an analysis of employee presence and related metrics, structured into six main sections. Key highlights include:")
        st.write("\* Employees who stayed tend to work more hours, especially in sales, technical, and support departments.")
        st.write("\* Higher satisfaction levels correlate with employee retention across all departments.")
        st.write("\* Most employees who left had low to medium salaries, whereas retention is higher among medium-salary employees.")
        st.write("\* Longer time spent in the company is linked to higher retention, especially in departments with strong workforce stability like sales and technical teams.")

        st.write("Report 4")
        st.image("hrimagesfolder/HR4 Turnover Rate.jpg")
        st.write("This dashboard provides insights into employee turnover rates and related metrics. Key highlights include:")
        st.write("\* The total turnover rate is 31.25%, reflecting a significant portion of the workforce leaving.")
        st.write("\* The HR department has the highest turnover rate at 41.03%, followed by accounting (36.23%) and technical (34.45%). Management has the lowest turnover rate (16.88%), suggesting better retention strategies.")
        st.write("\* Employees with low satisfaction levels (0.31–0.4) account for the highest turnover, indicating dissatisfaction as a key driver of attrition.")
        st.write("\* Turnover is highest among employees with low salaries (42.22%), while high-salary employees experience the least turnover (7.10%)")
        st.write("\* Employees who were not promoted in the last five years show significantly higher turnover rates (83.44%), highlighting the importance of career progression.")
        st.write("\* Turnover is slightly higher among employees with no accidents (36.08%) compared to those with accidents (8.45%).")

        st.write("Report 5")
        st.image("hrimagesfolder/HR5 Workplace Accident.jpg")
        st.write("This dashboard provides insights into workplace accidents and their impact across departments and salary levels. Key observations include:")
        st.write("\* A total of 2,169 accidents occurred, with 13,000 employees not affected and 2,000 experiencing accidents.")
        st.write("\* The sales department has the highest number of accidents (265), followed by technical (195) and support (174). Most accidents occurred among employees with low (47.95%) and medium salaries (43.2%), while high-salary employees are the least affected (8.85%).")
        st.write("\* Sales, technical, and support departments show a high correlation between workplace accidents and employee turnover.")
        st.write("\* Departments like sales and technical show higher accident counts with longer employee tenure. Shorter-tenured departments (e.g., marketing and IT) exhibit fewer accidents.")
        st.write("\* Employees involved in accidents show lower satisfaction levels compared to others.")

        st.write("Report 6")
        st.image("hrimagesfolder/HR6 Promotion.jpg")
        st.write("This report visualizes key metrics related to employee promotions over the last five years. Here's an analysis of each section:")
        st.write("\* Only 2.13% of employees were promoted (0.32K), while 97.87% (14.68K) were not promoted.Promotions are rare, indicating either a highly selective process or limited opportunities for promotion.")
        st.write("\* Employees with medium salaries saw the highest promotion rate (56.74%, 181 employees, High-salary employees followed at 22.57% (72 employees). Employees with low salaries were least likely to be promoted (20.69%, 66 employees). This suggests a potential bias toward mid-salary employees for promotions.")
        st.write("\* Employees with higher satisfaction levels (e.g., 0.71-0.8) had higher promotion rates (59 promotions). Lower satisfaction levels (e.g., 0-0.1) corresponded to minimal promotions. Satisfaction may be a contributing factor in promotion decisions, possibly reflecting better performance or attitude.")
        st.write("\* The Sales department leads with the most promotions (100), followed by Management (69) and Marketing (43). Departments like IT (3) and Product Management (0) had very few or no promotions, indicating disparities in promotion opportunities across departments.")
        st.write("\* Most promotions (94.04%, 300 employees) were given to those who stayed with the company. Only 5.96% (19 employees) of promotions went to those who eventually left. This indicates the company prioritizes retention when promoting.")
        st.write("\* Employees without work accidents had a significantly higher promotion rate (76.18%, 243 employees). Those who had work accidents were less likely to be promoted (23.82%, 76 employees). This could indicate a preference for employees with consistent performance and no interruptions due to accidents.")
        st.write("---")
        st.write("If you are more intrested please hit the below links for more information:")
        st.markdown(":female-office-worker: [HR Data Analysis](https://github.com/SantoshRottayyanavar/HR-Data-Analysis)")
        st.markdown(":bar_chart: [HR Data Analysis Dashboard](https://app.powerbi.com/links/TnhGzXJmRC?ctid=1f982a31-2757-47db-99bd-779e54f6229f&pbi_source=linkShare&bookmarkGuid=1b7c33f1-d00a-4997-ba1f-2cd9b28cfb03)")
        st.markdown(":bookmark_tabs: [HR Data Analysis Final Report](https://github.com/SantoshRottayyanavar/HR-Data-Analysis/blob/main/HR%20Data%20Analysis%20Final%20Report.pdf)")
        if st.sidebar.button("Back to Home"):  
            switch_page("home") 
    
    def electronic_sales_info():
        st.markdown("#### Electronic Sales Analysis Report")
        st.markdown("###### Received Data in Excel's CSV file")
        st.write("I received these datasets from 'Meriskill' shared as 'Excel Comma-Separated Values (CSV) files,' and was instructed to analyze the electronics sales data, including quantity, orders, cost, and sales.")
        st.image("Elecronic_Sales/Unclened_Dataset.png")
        st.markdown("###### Importing into Python's Pandas Library")
        st.write("I analyzed the datasets by importing them into Python's Pandas library, applied Exploratory Data Analysis (EDA).")
        st.image("Elecronic_Sales/Python_file.png")
        st.markdown("###### Converted Cleaned Data Into Excel CSV Format")
        st.write("Converted the cleaned data into Excel Comma-Separated Values (CSV) files.")
        st.image("Elecronic_Sales/Cleaned_dataset.png")
        st.markdown("###### Imported Dataset Into Power BI Desktop")
        st.write("I imported the cleaned dataset into Power BI Desktop and created a data model based on the common keys available in each file.")
        st.markdown("**Report 1**")
        st.image("Elecronic_Sales/Quantity_Analysis.png")
        st.write("The report provides electronic sales information and includes multiple visual elements such as cards, KPI cards, slicers, bar charts, maps, and line charts. Each card displays different values, including total customers, total orders, total quantity, total revenue, gross profit, sales per customer, sales per product, and profit percentage. The KPI cards highlight total sales, total cost, and total profit. The slicers allow filtering by continent, country, state, year, and month. The bar chart shows the quantity of brands, categories, subcategories, and colors. The map chart visualizes quantities by country, state, and city, while the line chart displays quantities by month.")
        st.write("\* Total Customers: 15.3K - Represents the total number of unique customers.")
        st.write("\* Total Orders: 63K - Indicates the total number of orders placed.")
        st.write("\* Total Quantity: 198K - Shows the total quantity of items sold.")
        st.write("\* Total Revenue: $55.8M - The total revenue generated from the sales.")
        st.write("\* Gross Profit: $32.7M - Highlights the profit after deducting costs.")
        st.write("\* Sales per Customer: 58.8 - Average sales per customer.")
        st.write("\* Sales per Product: 356.8 - Average sales per product.")
        st.write("\* In the KPI card, we can see that the total sales, cost, and profit  is $898,141, $526,492, and 371,649 respectively.")
        st.write("\* Percentage of Profit: 141.66% - Indicates the profit margin.")
        st.write("1. Quantity by Brand:")
        st.write("The top brand is \"Contoso\" with a quantity of 50K. Other notable brands include \"Wide World\" (27K) and \"Southridge\" (25K).")
        st.write("2. Quantity by Category:")
        st.write("\"Computers\" is the leading category with 44K items sold, followed by \"Cell phones\" (31K) and \"Music, Movies, and TV\" (29K).")
        st.write("3. Quantity by Subcategory:")
        st.write("\"Televisions\" (6K) and \"Laptops\" (5K) are the most sold subcategories, with other subcategories contributing smaller quantities.")
        st.write("4. Quantity by Color:")
        st.write("\"Black\" is the most popular color with 52K items sold, followed by \"Silver\" (38K) and \"White\" (36K).")
        st.write("5. Map Charts:")
        st.write("\* By Country and State: Highlights sales distribution globally, with concentrated sales in North America and Europe.")
        st.write("\* By City: Provides detailed city-level data for sales distribution.")
        st.write("6. Quantity by Month (Line Chart):")
        st.write("Sales peaked in February (24K) and November (27K). There is a noticeable dip in sales in March (10K), with a gradual recovery afterward.")
        
        st.markdown("**Report 2**")
        st.image("Elecronic_Sales/Order_Analysis.png")
        st.write("1. Orders by Brand:")
        st.write("The leading brand is Contoso with 16K orders. Other significant brands include Wide World Importers (9K), Southridge (8K), and The Phone Company (6K).")
        st.write("2. Orders by Category:")
        st.write("Computers dominate with 14K orders. Cell Phones (10K) and Music, Movies, and TV (9K) follow as other high-performing categories.")
        st.write("3. Orders by Subcategory:")
        st.write("Televisions and Laptops are the most ordered subcategories, each with 2K orders. Other subcategories, such as Projectors & Screens and Camcorders, have smaller contributions.")
        st.write("4. Orders by Color:")
        st.write("Black is the most popular color, accounting for 17K orders. Silver and White both have 12K orders each.")
        st.write("5. Map Charts:")
        st.write("\* Orders by Country: The map highlights that most sales occur in North America, Europe, and Australia.")
        st.write("\* Orders by State: Dense clusters of orders are visible in specific states across North America and Europe.")
        st.write("\* Orders by City: A detailed view shows sales distribution in urban areas, with significant clusters in key cities.")
        st.write("6. Orders by Month (Line Chart):")
        st.write("Sales reached a peak in January and April, with around 8K orders each. A noticeable dip occurred in March, where orders dropped to 1K, followed by a recovery in subsequent months.")
        
        st.markdown("**Report 3**")
        st.image("Elecronic_Sales/Cost Analysis.png")
        st.write("1. Costs by Brand: Contoso leads with the highest cost at \$85.93K, followed by Fabrikam (\$66.29K) and Litware (\$53.62K). Other notable contributors include Adventure Works (\$40.2K) and Proseware (\$31.65K).")
        st.write("2. Costs by Category: Home Appliances dominate with a total cost of \$149.1K, followed by Computers (\$81.28K). Cameras and Accessories rank third with \$59.03K, while TV and Video contribute \$47.06K.")
        st.write("3. Costs by Subcategory: The top-performing subcategory is Washers and Dryers with \$55.36K, followed by Camcorders (\$30.89K) and Refrigerators (\$29.51K). Other significant subcategories include Projectors \& Screens (\$25.51K) and Home Theaters (\$22.69K).")
        st.write("4. Costs by Color: White emerges as the most preferred color in terms of cost, contributing \$76.15K, closely followed by Black (\$73.92K) and Silver (\$67.21K). Grey (\$33.81K) and Green (\$20.85K) also make notable contributions.")
        st.write("5. Costs by Country: The analysis highlights North America, Europe, and Australia as the key regions driving significant costs.")
        st.write("6. Costs by State: Dense clusters of costs are observed in several states across North America and Europe, marking these regions as strong contributors.")
        st.write("7. Costs by City: Major urban centers in North America and Europe display significant cost volumes, with prominent clusters in leading cities.")
        st.write("8. Costs by Month: Costs peaked in December with \$284.51K, followed by a high in April (\$276.13K). A sharp decline occurred in March (\$6.3K), with a steady recovery seen in the following months.")
        
        st.markdown("**Report 4**")
        st.image("Elecronic_Sales/Sales_Analysis.png")
        st.write("1. Sales by Brand: Contoso leads with the highest sales of \$204.26K, followed by Fabrikam (\$165.48K) and Litware (\$127.16K). Brands like Adventure Works (\$99.37K) and Proseware (\$77.92K) also made notable contributions.")
        st.write("2. Sales by Category: Home Appliances account for the largest sales at \$355.49K. Other significant categories include Computers (\$201.01K) and Cameras and Accessories (\$148.92K).")
        st.write("3. Sales by Subcategory: Washers and Dryers dominate with sales of \$126.82K, followed by Camcorders (\$77.51K) and Projectors and Screens (\$77.35K). Other high-performing subcategories include Refrigerators (\$54.77K) and Home Theaters ($50.61K).")
        st.write("4. Sales by Color: White products achieved the highest sales of \$185.15K, closely followed by Black (\$179.84K) and Silver (\$161.59K). Other notable colors include Blue (\$84.1K) and Grey (\$82.66K).")
        st.write("5. Sales by Country: The report highlights significant sales in North America, Europe, and Australia.")
        st.write("6. Sales by State: Dense clusters of sales were observed in various states within North America and Europe.")
        st.write("7. Sales by City: Major cities across North America and Europe contributed significantly to the overall sales performance.")
        st.write("8. Sales by Month: Sales peaked in December at \$690.8K, followed by April (\$672.58K). A noticeable dip occurred in March (\$42.03K), with steady recovery in subsequent months.")
        
        st.markdown("**Report 5**")
        st.image("Elecronic_Sales/Conclusion_Report.png")
        st.write("1. Top 5 and Least 5 Brands Sold:")
        st.write("Top 5 Brands:")
        st.write("Contoso: The top-performing brand with 204.26K sales, contributing 30.3% of total sales.")
        st.write("Fabrikam: Second highest with 165.48K sales (24.54%). he remaining brands in the top 5 (99.3K, 77.92K, and 127.16K sales) contribute a significant portion but trail behind Contoso and Fabrikam.")
        st.write("Least 5 Brands:")
        st.write("The Phone: The lowest performer with 6.88K sales (4.46%). Other least-performing brands, such as \"Northwind Traders,\" have sales of 34.73K and 38.15K, indicating areas for improvement.")
        st.write("2. Sales by Category:")
        st.write("Home Appliances dominates the sales with 355.49K, making it the most profitable category. Computers (201.01K) and Cameras and Camcorders (148.92K) follow as strong contributors. Games and Toys have the lowest sales (7.06K), indicating low demand or insufficient marketing.")
        st.write("3. Top 10 and Least 10 Subcategories:")
        st.write("Top Subcategories:")
        st.write("Washers: The leading subcategory with 126.82K sales. Camcorders and Projectors are also among the top subcategories, with sales of 77.51K and 77.35K, respectively.")
        st.write("Least Subcategories:")
        st.write("Boxes (0.38K) and Cell Phones (0.71K) are the weakest performers. Other subcategories like Fans (6.53K) and Bluetooth Devices (5.09K) indicate room for growth.")
        st.write("4. Top 10 and Least 10 Products:")
        st.write("Top Products:")
        st.write("Products from Fabrikam dominate the top 10, with each product contributing 3.2K sales.")
        st.write("Least Products:")
        st.write("Products such as Reusable and SV USBs have extremely low sales, ranging from 0.95K to 2.94K. Some products consistently underperform, suggesting the need for a reassessment of their relevance or promotion.")
        st.write("5. Top 10 and Least 10 Cities:")
        st.write("Top Cities:")
        st.write("Sales are concentrated in the United States, with purple markers showing high-performing cities.")
        st.write("Least Cities:")
        st.write("Red markers highlight underperforming cities across North America, Europe, and parts of Australia. These regions may need targeted strategies to increase sales.")
        st.write("6. Sales by Year:")
        st.write("Sales peaked in 2020 (1M), but there was a sharp decline to 0.42M in 2021. A consistent sales trend from 2016 to 2019 (~0.7M to ~0.8M) suggests stability before the drop in 2021, possibly due to market changes or external factors like the pandemic.")
        if st.sidebar.button("Back to Home"):
            switch_page("home")

    def sales_info_page():
        st.markdown("#### Sales Data Analysis")
        st.write("I got this Business mail from 'steven', Steven's email highlights the need to enhance our internet sales reports by transitioning from static formats to visual dashboards. He emphasizes tracking product sales, client data, and performance against the 2024 budget while considering sales trends from the past two years.")
        st.image("Salesimages/BusinessRequestMailfromSteven.png")
        st.markdown("**Business demand overview**")
        st.image("Salesimages/Business demand overview.png")
        st.write("**Data Cleaned in SQL Server**")
        st.write("Following a successful data extraction process, The extracted data has been stored in an SQL Server database as a '.bak' file. The dataset comprises the tables 'Customer', 'Calendar', 'InternetSales', and 'Product' which require further manipulation and analysis.")
        sql1,sql2 = st.columns(2)
        sql1.image("Salesimages/Sqlserver.png")
        sql2.image("Salesimages/Sqlserver2.png")
        sql3, sql4 = st.columns(2)
        sql3.image("Salesimages/Sqlserver3.png")
        sql4.image("Salesimages/Sqlserver4.png")
        st.write("converted the cleaned data into Excel format for further reporting and visualization. Each dataset named 'Customer', 'Calendar', 'InternetSales', and 'Product' contains '18,485', '1,097', '58,169', and '607' respectively.")
        st.image("Salesimages/ExcelFiles.png") 
        st.write("Budget file has given in 'Excel file' it contains 19 rows.")
        st.image("Salesimages/Budget file.png")
        st.write("The Excel files have been imported into Power BI for further analysis.")
        
        st.write("**Report 1**")
        st.image("Salesimages/SalesOverview.png")
        st.write("The above report provides the Overview of 'sales'. It contains '3 years' of sales data which converted into a well detailed, organized, visually understandable information. It has different kinds of visuals, cards, and slicers, those are 'total 3 years slicer', 'Month slicer', 'total sales KPI card', 'Bar chart', 'Line chart', 'Map'.")
        st.write("\* The 'KPI card' shows over all total sales \$22,239,730, budget amount \$21,100,000, difference of sales and budget.")
        st.write("\* The 'donut chart' shows sales by product category, here product category of 'Bikes is showing high in sales, Accessories and clothing are low in sales.")
        st.write("\* The 'line chart' shows 'Sales and Budget amount by month', In the year of '2022' the sales went high in the month of 'december', In '2023' the sales and budget shows an overall upward trend in both sales and budget, with sales exceeding budget mid-year but falling short in December. in '2024' the sales has done in january. ")
        st.write("\* The 'Bar chart' shows sales by top 10 customers, who's over all sales in between \$9,911 and \$12,909.")
        st.write("\* The another 'Bar chart' shows sales by top 10 products, who's overall sales in between \$621,832 and \$1,371,420.")
        st.write("\* The MAP shows sales by city, In Europe, the 'london' city has highest sales \$693,517, the second highest sales happened in 'Paris' \$470,333. In North America the highest sales done in the city of Bellflower \$220,219. In Australia 'Wollnogong city has highest sales \$256,013. In Asia the business has been running in only one city named 'Malabar' \$129,371.")
        
        st.write("**Report 2**")
        st.image("Salesimages/CustomerDetails.png")
        st.write("The 2nd report provides the 'Customer' Details. It also contains '3 years' of customers sales data which converted into a well detailed, organized, visually understandable information. It has different kinds of visuals, cards, and slicers, those are 'Total 3 years slicer', 'Month slicer', 'cards', 'Bar chart', 'Line chart', 'Matrix table', 'Map'.")
        st.write("\* The 'cards' shows total sales \$22.24M and Total budget \$21M")
        st.write("\* The 'line chart' shows sales and budget amount by month, the sales and budget are vary over all year the sales didn't reached the budget in the first half and in the 2nd half sales went beyond the budget.")
        st.write("\* The 'Matrix table' shows sales amount by customer, that gives information regarding which customer purcheses in how many months.")
        st.write("\* The 'Map' shows 'customer city' here we can understnd that how many customer are staying in which city. the highest customers staying in 'london' nearly 500.")
        st.write("\* The 'Bar chart' shows top 10 sales by customers as mentioned in report 1.")
        
        st.write("**Report 3**")
        st.image("Salesimages/ProductDetails.png")
        st.write("The 3rd report provides the 'Product' Details. It also contains '3 years' of customers sales data which converted into a well detailed, organized, visually understandable information. It has different kinds of visuals, cards, and slicers, those are 'Total 3 years slicer', 'Month slicer', 'cards', 'Bar chart', 'Line chart', 'Matrix table', 'Map'.")
        st.write("\* The 'Map' shows 'customer city' here we can understnd that how many products are selling in which city. but here we understood that there are equal products selling in all the cities.")
        st.write("\* The 'Bar chart' shows top 10 sales by products as mentioned in report 1.")
        st.write("\* The 'Matrix table' shows sales amount by product, that gives information regarding which product sold how much in every months.")
        st.write("---")
        st.write("If you are more intrested please hit the below links for more information:")
        st.markdown(":package: [Sales Data Analysis data](https://github.com/SantoshRottayyanavar/Sales-Data-Analysis)")
        st.markdown(":moneybag: [Sales Data Analysis Reports](https://app.powerbi.com/groups/me/reports/e9b33f13-9873-4009-abfd-f0102cda2f5a/a84db2e002315c50c000?experience=power-bi)")
        st.markdown(":bookmark_tabs: [HR Data Analysis Final Report](https://github.com/SantoshRottayyanavar/HR-Data-Analysis/blob/main/HR%20Data%20Analysis%20Final%20Report.pdf)")
        if st.sidebar.button("Back to Home"):  
            switch_page("home") 
       
    def financial_complaints_page():
        st.markdown("#### **Financial Complaints**")
        st.markdown("""##### Project Overview:
        \n This project showcases my expertise in data analysis, visualization, and dashboard design. Using a dataset of over 75,000 financial complaints sourced from an Excel file, I created an interactive dashboard to provide insights into complaint trends, resolution efficiency, and customer satisfaction. The dashboard highlights key metrics and allows users to explore complaint data by category, submission method, and geographic location.""")
        st.markdown("##### Workflow:")
        st.markdown("""###### 1. Dataset Exploration:
        \n The dataset, stored in Excel, included information on financial complaints filed between 2011 and 2020. Key fields included:""")
        st.markdown("""* Complaint Issues (e.g., billing disputes, mortgage problems).
        \n * Submission Methods (e.g., web, phone, postal mail).
        \n * Resolution Outcomes (e.g., resolved at no cost).
        \n * Geographic Information (state-level data).    
        \n I explored the dataset in Excel to understand its structure and identify areas requiring data cleaning.""")
        st.image("Financial Complaints/Financial complaint excel file.png")
        st.markdown("###### 2. Data Cleaning and Preparation:")
        st.write("""To ensure the data was analysis-ready, I Excel and Tableau for:
        \n * Removing duplicate records and null values.
        \n * Standardizing dates to enable time-series analysis.
        \n * Creating calculated fields such as "Timely Response Rate" and "Disputed Rate.""")
        st.markdown("###### 3. Dashboard Design and Visualizations:")
        st.write("The dashboard was designed in Tableau with the following components:")
        st.image("Financial Complaints/Financial complaints report.png")  
        st.markdown("""**KPIs:**
        \n * Total Complaints: Displays the total number of complaints filed.
        \n * Timely Response Rate: Measures the percentage of complaints addressed promptly.
        \n * Resolved at No Cost: Highlights the percentage of complaints resolved without any cost to the customer.
        \n **Visualizations:**
        \n * Complaints by Issue: A bar chart showing the frequency of complaints by category.
        \n * Complaints by Submission Media: A breakdown of submission methods (web, phone, etc.).
        \n * Complaints by State: A geographic map visualizing complaint volume across U.S. states.
        \n * Customer Dispute Rate: A donut chart displaying the percentage of complaints disputed by customers.""")
        st.markdown("""###### 4. Insights Delivered:
        \n The dashboard provided actionable insights, such as:
        \n * The most common complaint issues, like "Managing an Account" and "Deposits and Withdrawals."
        \n * Web as the dominant submission method (50.37% of complaints).
        \n * California as the state with the highest complaint volume.
        \n * 98.1% of complaints received a timely response, showcasing efficient customer service.""")
        st.markdown("""###### Tools and Techniques Used:
        \n * Excel: For storing and exploring the dataset.
        \n * Tableau: For dashboard creation.
        \n * Calculated fileds (Data Analysis Expressions): For creating calculated fields and KPIs.""")
        st.write("""###### Project Goals:
        \n The primary objective of this project was to transform raw complaint data into meaningful insights that can drive business decisions. The dashboard is designed to help stakeholders understand trends, identify problem areas, and evaluate customer service performance.""")
        st.markdown("""###### Key Achievements:
        \n * Successfully visualized and analyzed over 75,000 complaint records.
        \n * Improved data quality through efficient cleaning and transformation.
        \n * Delivered an interactive and user-friendly dashboard that enhances decision-making.""")
        st.write("---")
        st.write("If you are more intrested please hit the below links for more information:")
        st.markdown(":heavy_dollar_sign: [Financial Complaints data](https://github.com/SantoshRottayyanavar/Financial-Complaints/blob/main/Financial%20Consumer%20Complaints.csv)")
        st.markdown(":dollar: [Financial Complaints Dashboard](https://public.tableau.com/app/profile/santosh.rottayyanavar2698/viz/Financecomplaint/Dashboard1)")
        if st.sidebar.button("Back to Home"):  
            switch_page("home") 

    def emrgency_room_page():
        st.markdown("#### **Emergency Room Visits**")
        st.markdown("""
        ##### Project Overview:
        The Emergency Room Visits Dashboard is a comprehensive visualization designed to analyze and present key metrics related to emergency room (ER) visits. 
        This project provides actionable insights to healthcare administrators, enabling them to optimize resource allocation, improve patient satisfaction, and ensure timely care delivery.
        """)

        st.markdown("""
        ###### 1: Data Extraction and Cleaning:
        - **Source Data**: Provided datasets in Excel format.
        - **Data Cleaning in Excel**: Removed duplicates, handled missing values, and corrected date format.
        """)
        st.image("Emergency Room/Emergency Room Excel Dataset.png", caption="Prepared Excel Dataset")

        st.markdown("""
        ###### 2: Importing Data into Tableau:
        Opened Tableau and connected to the prepared Excel file.
        """)
        st.image("Emergency Room/Emergency Room Dashboard.png", caption="Tableau Dashboard")
        st.markdown("""
        **Key Insights:**
        1. **Demographics and Patient Distribution**:
            - **Total Visits**: 9,216 patients visited the ER during the analyzed period.
            - **Gender Split**:
                - Male: 51.05%
                - Female: 48.69%
                - Non-Conforming: 0.26%
            - **Age Groups**:
                - The majority of patients belong to the 19–65 age group, with trends consistent over time. 

        2. **Wait Times and Satisfaction**:
            - **Average Wait Time**: 35.26 minutes, providing an opportunity to identify and address bottlenecks.
            - **Patient Satisfaction**: 4.99/10, indicating areas for improving patient experience.

        3. **Race Distribution**:
            - **Majority**: White (2,571)
            - **Other Significant Groups**: African American (1,951), Asian (1,060), and Pacific Islander (549).

        4. **Department Utilization**:
            - **Top Departments**:
                - General Practice: 1,840 visits
                - Orthopedics: 995 visits
                - Cardiology: 248 visits
            - Specialized areas like Neurology and Renal show lower utilization, highlighting opportunities for improvement.

        5. **Peak Hours and Weekly Trends**:
            - **Heatmap Analysis**:
                - High activity observed on Monday and Friday mornings, with peak wait times exceeding 38 minutes.
                - Weekends show reduced activity and shorter wait times.
        """)

        st.markdown("""
        **Tools and Techniques Used:**
        - **Data Preparation**:
            - Extracted and cleaned the data using Microsoft Excel to ensure data accuracy and completeness.
        - **Visualization Development**:
            - Imported the cleaned dataset into Tableau to design an interactive dashboard using advanced visualization features such as heatmaps, stacked area charts, and bar graphs.
        - **Analytical Insights**:
            - Conducted trend analysis on demographics, satisfaction scores, and department performance.
        """)

        st.markdown("""
        **Key Achievements:**
        - Designed a dashboard that enhances decision-making capabilities for hospital management.
        - Identified operational bottlenecks, such as high wait times during peak hours and low satisfaction scores, offering improvement recommendations.
        - Provided detailed demographic insights, enabling hospitals to tailor healthcare policies to their patient population.
        """)
        st.write("---")
        st.write("If you are more intrested please hit the below links for more information:")
        st.markdown(":medical_symbol: [Emergency Room Visits data](https://github.com/SantoshRottayyanavar/Emargency-Room-Visits/blob/main/Hospital%20ER.csv)")
        st.markdown(":stethoscope: [Emergency Room Visits Dashboard](https://public.tableau.com/app/profile/santosh.rottayyanavar2698/viz/HospitalEmargencyRoom/EmergencyRoomDashboard)")
        if st.sidebar.button("Back to Home"):
            switch_page("home")

    def accident_data_page(): 
        st.markdown("""#### **Accident Data**""")  
        st.image("Accident data/report.jpg")
        if st.sidebar.button("Back to Home"):
            switch_page("home")

    def patient_survey_page():
        st.image("Patient Survey/Patient_survey_dashboard.png")  
        if st.sidebar.button("Back to Home"):
            switch_page("home")       

    def main():
        if st.session_state.page == "home":
            st.markdown("##### Internships")
            st.markdown("###### Company Name: AI Variant")
            st.write("AI Variant is an analytics firm, provides best-in-class products and solutions.It has deep analytics expertise as well as domain expertise in various industries. It's employees extremely passionate about taking on challenges that matter to the clients.")
            st.markdown("Click here to know more about [AI Variant](https://aivariant.com/)")
            st.markdown("###### Projects:")
            
            bank, empty, hr = st.columns(3)
            
            # Bank project front image and button
            with bank:
                image_path = "bankloanimages/Bankloanimage.png"
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64,{get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style={"margin": "0px", "height": "200px"},
                    )
                    if clicked > -1:
                        switch_page("bank_info")

            with hr:
                image_path = "hrimagesfolder/hrdataanalysis.png"
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64,{get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8"},
                        img_style={"margin": "0px", "height": "200px", "object-fit": "contain"},
                    )
                    if clicked > -1:
                        switch_page("hr_info")

        if st.session_state.page == "home":
            #Details of Practiced Projects
            st.write("---")
                #Practiced Project Part
            st.markdown("###### Company Name: MeriSKILL")
            st.markdown("""Our vision is to ensure that no student feels inexperienced to apply for a job role by providing immersive job experience through simulations, paving the way for confident and successful career transitions.
                           We are on a mission to equip students with the invaluable hands-on experience and skills they need to thrive in their chosen careers, even before securing their first professional role. """)
            st.markdown("Click here to know more about [MeriSKILL](https://meriskill.in/)")
            st.markdown("###### Project:")
            
            sales, empty, empty1 = st.columns(3)
            with sales:
                image_path = "Elecronic_Sales/Electronics_main page.png"
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")
                else:
                    clicked = clickable_images([f"data:image/png;base64,{get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style={"margin": "0px", "height": "200px"},
                            )
                    if clicked > -1:
                            switch_page("electronic_info")

        if st.session_state.page == "home":
            #Details of Practiced Projects
            st.write("---")
                #Practiced Project Part
            st.markdown("#### Practiced Projects")
            st.markdown("""Throughout my academic and professional journey, I have undertaken several hands-on projects that showcase my expertise in data analysis, visualization, and cloud technologies. These projects demonstrate my ability to apply analytical and technical skills to solve real-world problems, optimize workflows, and drive data-driven decisions.
                                By leveraging tools like Excel, Power BI, Tableau, Python, SQL, and Statistics, I have delivered impactful solutions in domains such as HR analytics, bank loan analysis, and sales optimization. My work reflects a commitment to quality, innovation, and adaptability to evolving business needs.""")
            
            a, b, c =st.columns(3)                
            with a:
                image_path = "Salesimages/PracticedSalesProjects.png"
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64,{get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style={"margin": "0px", "height": "200px"},
                    )
                    if clicked > -1:
                        switch_page("sales_info")

            with b:
                image_path = "Financial Complaints/Financial comlaint main page.png"
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64,{get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style={"margin": "0px", "height": "200px"},
                    )
                    if clicked > -1:
                        switch_page("finance_com_info")

            with c:
                image_path = "Emergency Room/Emergency room page.png"  
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")      
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64, {get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style={"margin": "0px", "height": "200px"},
                    )     
                    if clicked > - 1:
                        switch_page("emergency_room_info")

            d,e,f = st.columns(3)
            with d:
                image_path = "Accident data/accident main page.jpg"  
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")      
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64, {get_img_as_base64(image_path)}"],
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style={"margin": "0px", "height": "200px"},
                    )     
                    if clicked > - 1:
                        switch_page("accident_data_info")

            with e:
                image_path = "Patient Survey/patient_survey_main_image.png"
                if not os.path.exists(image_path):
                    st.error(f"Image not found at {image_path}")
                else:
                    clicked = clickable_images(
                        [f"data:image/png;base64, {get_img_as_base64(image_path)}"],
                        div_style = {"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "background-color": "#B1BED8", "background-size": "cover"},
                        img_style = {"margin": "0px", "height": "200px"},
                    )
                    if clicked > - 1:
                        switch_page("patient_survey_info")

        elif st.session_state.page == "bank_info":
            bank_info_page()
        elif st.session_state.page == "hr_info":
            hr_info_page()  
        elif st.session_state.page == "sales_info":
            sales_info_page()  
        elif st.session_state.page == "electronic_info":
            electronic_sales_info()    
        elif st.session_state.page == "finance_com_info":
            financial_complaints_page()
        elif st.session_state.page == "emergency_room_info":
            emrgency_room_page()   
        elif st.session_state.page == "accident_data_info":
            accident_data_page() 
        elif st.session_state.page == "patient_survey_info":
            patient_survey_page()


              
        
    # Run the app
    if __name__ == "__main__":
        main()

elif choice == "Resume":
    with open("CHINMAYI HIREMATH.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="CHINMAYI HIREMATH.pdf",
            mime="text/pdf"
        )
    pdf_viewer("CHINMAYI HIREMATH.pdf")

#contact details section
elif choice == "Contact":
    st.markdown("### :handshake: Get in Touch")
    st.write("")
    st.text("Feel free to reach out to me! trough")
    st.write("")
    
    st.markdown("santoshrottayyanavar81@gmail.com")
    social_media_links = [
        "https://www.linkedin.com/in/santosh-rottayyanavar-/",
        "https://github.com/SantoshRottayyanavar",
    ]
    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render()
   
    st.write("---")

    #Contact form
    st.markdown("### :postbox: Message Box")
    st.write("write to me for any collaborations / Suggestions to improve")
    
     # google sheets connection
    if 'conn' not in st.session_state:
        st.session_state.conn = st.connection("gsheets", type=GSheetsConnection)

    if "Message_df" not in st.session_state:
        st.session_state.Message_df = st.session_state.conn.read(worksheet="Portfolio_Feedback")
      
    if "msg_df" not in st.session_state:
       st.session_state.msg_df = pd.DataFrame()

    with st.form(key="contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        text = st.text_area("Message")
        col1, col2, col3, col4 = st.columns(4)
        submit_button = col4.form_submit_button("Send")

        if submit_button:
            if (name == "") or (email == "") or (text == ""):
                st.error("Please fill all the fields")
            else:
                st.success(f"Thank you, {name}! I'll get back to you soon if any.")
                
                message = [{"Name": name,
                            "Mail ID": email,
                            "Message": text}]
                
                st.session_state.msg_df = pd.DataFrame(message)
                st.session_state.Message_df = pd.concat([st.session_state.Message_df, st.session_state.msg_df], ignore_index = True)
                st.session_state.conn.update(worksheet="Portfolio_Feedback", data=st.session_state.Message_df)


