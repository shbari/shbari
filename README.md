- 👋 Hi, I’m Sheikh
- 👀 This  repo contains all the codes I  wrote during my PhD journey.
- 📫 Visit my website at https://sites.google.com/view/shbari/?pli=1

<!---
shbari/shbari is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
#                                                   Manual
# Ratting curve
Some algorithom may gives local optima deviating from global best. The initial value plays an important rule in finding best parameters value. please check these fatcs before using any fitting algorithom
#example use:

fit_rating_curve(file_path) 
or 

fit_rating_curve('path/to/your/data.csv', a_initial=0.5, b_initial=1.0, maxfev=1000)


Please ensure that the CSV file contains three columns named 'Time", 'H' for river stage and 'Q' for discharge

