# -*- coding: utf-8 -*-


import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/MALAV/Downloads/ds_salary_proj-master (1)/ds_salary_proj-master/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)