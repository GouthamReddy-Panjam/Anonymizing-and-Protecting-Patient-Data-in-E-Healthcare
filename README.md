# **Anonymizing and Protecting Patient Data in E Healthcare**

### **ABSTRACT** ###

Medical sector has a vast amount of data and every tiny bit of it can be sensitive enough to cause trouble for a person. This report aims to help the privacy protection of the medical and healthcare data so that hospitals can share their vital data for research without hesitating of any misuse of data. The algorithm presented in this report makes data clearer and also, masksthe direct identifiers along with listing down the quasi- identifiers that might be risky for the sharing of data.

### **OBJECTIVES** ###

* Medical institutions should not be hesitant to share their data involving their patients to the government or research institutions.
* Protecting the confidentiality of the patients by scrubbing the unnecessary data.
* Scrubbing the data in such a manner that the dataset becomes clearer to the required researcher and the utility is maintained.
* Scrubbing mechanism will use a selective search algorithm for identifying explicit identifiable attribute.
* The mechanism will alter or remove data depending upon the need of the data required and to whom the data needs to be supplied.

### **REQUIREMENTS** ###
* ##### SOFTWARE REQUIREMENTS #####
![image](https://user-images.githubusercontent.com/88433888/197378506-f7e3566d-b332-4c0d-a9f3-b46999b04e5a.png)

### **PHASE-1 DESIGN** ###
![image](https://user-images.githubusercontent.com/88433888/197378583-a9605dee-7042-414f-b4af-cc2d2656be51.png)

In phase -1, as shown in Flowchart-1, we are masking the explicit identifiers on the resultbased on the search from a list of explicit identifiers given as List-1 and then cleaning the data making it more useful as we are imputing the missing values using regression techniques.

### **PHASE-2 DESIGN** ###
![image](https://user-images.githubusercontent.com/88433888/197378640-59dcacac-66b1-49c7-a7a1-61b88fa69c42.png)

In phase-2, as shown in Flowchart-2, we are identifying the primary quasi-identifiers on the result based on the search from a list of quasi identifiers given as list-2. We then calculate uniqueness and influence of each of these primary quasi-identifiers.

Uniqueness denotes how many unique values does a column contain, as more uniqueness will result in more risk of re-identification.

Influence of a column denotes how much does removing of that column affect the entire dataset as we need to maintain a good level of utility.

### **FLOWCHART OF THE PROCESS CARRIED OUT IN PHASE-1** ###
![image](https://user-images.githubusercontent.com/88433888/197378731-7e30c99b-69bf-42e2-b23b-1efd13f63c13.png)

### **FLOWCHART OF THE PROCESS CARRIED OUT IN PHASE-2** ###
![image](https://user-images.githubusercontent.com/88433888/197378752-4029cdc6-1f01-42b0-b5ef-ecfd033efb5a.png)

### **ALGORITHM OF PHASE-1** ###

* Get the input raw data as a csv file.
* Search for the explicitly identifiable(EI) column names from a list of explicitly identifiable tags stored in the program.
* If any EI: Remove those columns by converting all the values into ‘#’.
* Compute missing values in the data for cleaning.
* If missing values > =50% of the total size : Remove the entire column.
* Else , if the data is continuous, apply regression algorithm to impute the missing values with accuracy.
* Else, if the data is categorical, impute the missing values by substituting them with the mode of this column.
* Form a new directory called Output_files and store this new masked data into a csv file with the output name given by the user.

### **ALGORITHM OF PHASE-2** ###

* Get the processed data after phase – 1.
* Identify primary quasi-identifiers(QI) by searching from a list of quasi-identifiable tags stores in the program.
* If any primary QI found: Calculate uniqueness and influence of these identifiers on the data in order to calculate the risk for each of them.
* Uniqueness of a column = No. of values that occur only once in the column / Total no. of values in the column.
* Influence of a column = 1 – No. Of equivalence classes without this column / Total no. of equivalence classes in the data.
* Calculate risk factor by taking the mean of uniqueness and influence of primary Qis.
* Verify a additional 3 factors.
    * Trust in the organization receiving the data
    * Possibility of linkage of our data using public databases
    * Working period given by the receiving organization for out database
* Calculate threshold risk on the basis of all the above parameters.
* Check if the risk of primary QI >= threshold risk: Add them to secondary QI.
* Output the secondary QI as the risky quasi-identifiers.

### **RESULTS ANALYSIS** ###

#### INPUT ####
![image](https://user-images.githubusercontent.com/88433888/197379086-4bbfc355-53c3-4748-904d-3c6565eaa005.png)

The dataset taken in this paper is named as ‘ohit-ehr-payments-to-providers-july-2018.csv’ and Figure 1 shows top 26 values with some of the columns in the dataset.

#### PROCESSING ####
![image](https://user-images.githubusercontent.com/88433888/197379138-1a331f64-b141-4819-a172-477680c2dc5a.png)

Figure 2 and Figure 3 illustrate the running of our source code and Figure 3 shows how we are taking additional verification of the organization as inputs in order to modify our threshold risk and calculate results more accurately.

#### OUTPUT ####
![image](https://user-images.githubusercontent.com/88433888/197379208-872abacb-3dc9-4097-8911-2ad346e027c6.png)

Figure 4.1 shows how our source code created a directory called Output_files and created a csv file of the name given by the user in it. Figure 4.2 shows that phase-1 of our algorithm worked with full efficiency and every direct identifier has been masked by converting into ‘#’.

![image](https://user-images.githubusercontent.com/88433888/197379241-2e478908-f8b6-4349-bcfa-8d39a1254bc9.png)

Figure 5 is the result of the phase-2 algorithm and the keywords given are the column names of the data which were analyzed as risky to the privacy of the data.

Now, the data anonymizer can easily use algorithms like k-anonymity on these columns to anonymize the data.

One important point to note down is that phase-2 algorithm started with many quasiidentifiers and ended up with only the ones mentioned in Figure-5. This states that we are not anonymizing all the columns and hence, data can be of more use. This helps in keeping a good balance between privacy as well as utility of the data after anonymization.














