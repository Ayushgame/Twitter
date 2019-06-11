import pandas as pd  
   
# list of name, degree, score 
name = ["mobile", "pankaj", "sudhir", "Geeku"] 
degree = ["MBA", "BCA", "M.Tech", "MBA"] 
score = [90, 40, 80, 98] 
   
# dictionary of lists  
dict = {'nme': name, 'deg': degree, 'scr': score}  
     
df = pd.DataFrame(dict) 
  
# saving the dataframe 
df.to_csv(r'C:\\Users\Ayush mahajan\Desktop\csv1.csv', index=False) 
df
