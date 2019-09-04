# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here

data = pd.read_csv(path)
#print(data)

loan_status = data['Loan_Status'].value_counts()
#print(loan_status)

#plt.bar(loan_status, height = )

loan_status.plot(kind = 'bar',stacked = 'True',figsize=(15,10))



# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind = 'bar',stacked = 'False',figsize=(15,10))

plt.xlabel ('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)


# --------------
#Code starts here

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind = 'bar',stacked = 'True',figsize=(15,10))

plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind = 'density',label = 'Graduate')

not_graduate['LoanAmount'].plot(kind = 'density',label = 'Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3) = plt.subplots( 3, 1,figsize = (20,10))

ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
plt.title( 'Applicant Income')


data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
plt.title( 'Coapplicant Income')

ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
plt.title( 'Total Income')





#fig,(ax_1, ax_2) =  plt.subplots(1,2,figsize = (20,10))

#electric.plot.scatter('HP','Attack')


