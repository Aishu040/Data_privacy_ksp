from flask import Flask, request, render_template, redirect, url_for
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('options'))  # Redirect to options.html after login form submission
    return render_template('login.html')

@app.route('/options', methods=['GET', 'POST'])
def options():
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        if form_type == 'FIR':
            return redirect(url_for('FIR'))
        elif form_type == 'ChargeSheet':
            return redirect(url_for('ChargeSheet'))
        elif form_type == 'Arrested':
            return redirect(url_for('Arrested'))
        elif form_type == 'Accused':
            return redirect(url_for('Accused'))
    return render_template('options.html')

@app.route('/FIR1', methods=['GET', 'POST'])
def FIR():
    if request.method == 'POST':
        form_data = [
            request.form['District_Name'],
            request.form['UnitName'],
            request.form['FIRNo'],
            request.form['RI'],
            request.form['Year'],
            request.form['Month'],
            request.form['Offence_From_Date'],
            request.form['Offence_To_Date'],
            request.form['FIR_Reg_DateTime'],
            request.form['FIR_Date'],
            request.form['FIR_Type'],
            request.form['FIR_Stage'],
            request.form['Complaint_Mode'],
            request.form['CrimeGroup_Name'],
            request.form['CrimeHead_Name'],
            request.form['Latitude'],
            request.form['Longitude'],
            request.form['ActSection'],
            request.form['IOName'],
            request.form['KGID'],
            request.form['IOAssigned_Date'],
            request.form['Internal_IO'],
            request.form['Place_of_Offence'],
            request.form['Distance_from_PS'],
            request.form['Beat_Name'],
            request.form['Village_Area_Name'],
            request.form['Male'],
            request.form['Female'],
            request.form['Boy'],
            request.form['Girl'],
            request.form['Age_0'],
            request.form['VICTIM_COUNT'],
            request.form['Accused_Count'],
            request.form['Arrested_Male'],
            request.form['Arrested_Female'],
            request.form['Arrested_Count_No'],
            request.form['Accused_ChargeSheeted_Count'],
            request.form['Conviction_Count'],
            request.form['FIR_ID'],
            request.form['Unit_ID'],
            request.form['Crime_No']
        ]
        # Process form_data if necessary
        return redirect(url_for('maskfir'))
    return render_template('FIR1.html')

@app.route('/Accused1', methods=['GET', 'POST'])
def Accused():
    if request.method == 'POST':
        try:
            form_data = {
                'District_Name': request.form['District_Name'],
                'UnitName': request.form['UnitName'],
                'FIRNo': request.form['FIRNo'],
                'Year': request.form['Year'],
                'Month': request.form['Month'],
                'AccusedName': request.form['AccusedName'],
                'Person_Name': request.form['Person_Name'],
                'age': request.form['age'],
                'Caste': request.form['Caste'],
                'Profession': request.form['Profession'],
                'Sex': request.form['Sex'],
                'PresentAddress': request.form['PresentAddress'],
                'PresentCity': request.form['PresentCity'],
                'PresentState': request.form['PresentState'],
                'PermanentAddress': request.form['PermanentAddress'],
                'PermanentCity': request.form['PermanentCity'],
                'PermanentState': request.form['PermanentState'],
                'Nationality_Name': request.form['Nationality_Name'],
                'DOB': request.form['DOB'],
                'Person_No': request.form['Person_No'],
                'Arr_ID': request.form['Arr_ID'],
                'crime_no': request.form['crime_no']
            }
            # Process form_data if necessary
            print(form_data)  # For debugging
            return redirect(url_for('maskaccused'))
        except KeyError as e:
            return f"Missing form field: {e}", 400
    return render_template('Accused1.html')

@app.route('/ChargeSheet1', methods=['GET', 'POST'])
def ChargeSheet():
    if request.method == 'POST':
        form_data = [
            request.form['District_Name'],
            request.form['UnitName'],
            request.form['FIRNo'],
            request.form['RI'],
            request.form['Year'],
            request.form['Month'],
            request.form['FIR_Date'],
            request.form['Report_Date'],
            request.form['Final_Report_Date'],
            request.form['Report_Type'],
            request.form['FIR_ID'],
            request.form['Unit_ID'],
            request.form['Crime_No'],
            request.form['FR_ID']
        ]
        # Process form_data if necessary
        return redirect(url_for('maskchargesheet'))
    return render_template('ChargeSheet1.html')

@app.route('/Arrested1', methods=['GET', 'POST'])
def Arrested():
    if request.method == 'POST':
        form_data = {
                'District_Name': request.form['District_Name'],
                'UnitName': request.form['UnitName'],
                'FIRNo': request.form['FIRNo'],
                'Year': request.form['Year'],
                'Month': request.form['Month'],
                'Name': request.form['Name'],
                'age': request.form['age'],
                'Caste': request.form['Caste'],
                'Profession': request.form['Profession'],
                'Sex': request.form['Sex'],
                'PresentAddress': request.form['PresentAddress'],
                'PresentCity': request.form['PresentCity'],
                'PresentState': request.form['PresentState'],
                'PermanentAddress': request.form['PermanentAddress'],
                'PermanentCity': request.form['PermanentCity'],
                'PermanentState': request.form['PermanentState'],
                'Nationality_Name': request.form['Nationality_Name'],
                'DOB': request.form['DOB'],
                'Person_No': request.form['Person_No'],
                'Crime_No': request.form['Crime_No'],
                'Arr_ID': request.form['Arr_ID'],
                'Charge_Sheeted': request.form['Charge_Sheeted'],
                'Charge_Sheet_Number': request.form['Charge_Sheet_Number']
            }
        # Process form_data if necessary
        return redirect(url_for('maskarrested'))
    return render_template('Arrested1.html')



@app.route('/maskfir', methods=['GET', 'POST'])
def maskfir():
    # Dummy list of form attributes for testing
    form_attributes = ['District_Name', 'UnitName', 'FIRNo', 'RI', 'Year', 'Month', 'Offence_From_Date', 'Offence_To_Date', 'FIR_Reg_DateTime', 'FIR_Date', 'FIR_Type', 'FIR_Stage', 'Complaint_Mode', 'CrimeGroup_Name', 'CrimeHead_Name', 'Latitude', 'Longitude', 'ActSection', 'IOName', 'KGID', 'IOAssigned_Date', 'Internal_IO', 'Place_of_Offence', 'Distance_from_PS', 'Beat_Name', 'Village_Area_Name', 'Male', 'Female', 'Boy', 'Girl', 'Age_0', 'VICTIM_COUNT', 'Accused_Count', 'Arrested_Male', 'Arrested_Female', 'Arrested_Count_No', 'Accused_ChargeSheeted_Count', 'Conviction_Count', 'FIR_ID', 'Unit_ID', 'Crime_No']

    # Print form attributes to console
    print("Form attributes from fir.html:", form_attributes)

    return render_template('maskfir.html', form_attributes=form_attributes)


@app.route('/maskaccused', methods=['GET', 'POST'])
def maskaccused():
    if request.method == 'POST':
        return redirect(url_for('summary'))  # Redirect to summary.html after masking form submission
    
    # Define form_attributes list containing form field names
    form_attributes = [
        'District_Name', 'UnitName', 'FIRNo', 'Year', 'Month',
        'AccusedName', 'Person_Name', 'age', 'Caste', 'Profession', 'Sex',
        'PresentAddress', 'PresentCity', 'PresentState', 'PermanentAddress', 'PermanentCity',
        'PermanentState', 'Nationality_Name', 'DOB', 'Person_No', 'Arr_ID',
        'crime_no'
    ]

    # Print form attributes to console
    print("Form attributes for maskaccused.html:", form_attributes)

    return render_template('maskaccused.html', form_attributes=form_attributes)

@app.route('/maskchargesheet', methods=['GET', 'POST'])
def maskchargesheet():
    if request.method == 'POST':
        return redirect(url_for('summary'))  # Redirect to summary.html after masking form submission
    
    # Dummy list of form attributes for testing
    form_attributes = ['District_Name', 'UnitName', 'FIFIRNoRNo', 'RI', 'Year', 'Month', 'FIR_Date',
                    'Report_Date', 'Final_Report_Date', 'Report_Type', 'FIR_ID', 'Unit_ID', 'Crime_No', 'FR_ID']

    # Print form attributes to console
    print("Form attributes for chargesheet:", form_attributes)

    return render_template('maskchargesheet.html', form_attributes=form_attributes)

@app.route('/maskarrested', methods=['GET', 'POST'])
def maskarrested():
    # Dummy list of form attributes for testing
    form_attributes = [
        'District_Name', 'UnitName', 'FIRNo', 'Year', 'Month', 'Name','age','Caste',
        'Profession','Sex','PresentAddress','PresentCity', 'PresentState', 'PermanentAddress', 'PermanentCity',
        'PermanentState', 'Nationality_Name', 'DOB', 'Person_No', 'Crime_No','Arr_ID','Charge_Sheeted','Charge_Sheet_Number'
    ]

    # Print form attributes to console
    print("Form attributes from arrestedform_data:", form_attributes)

    if request.method == 'POST':
        return redirect(url_for('summary'))  # Redirect to summary.html after masking form submission

    return render_template('maskarrested.html', form_attributes=form_attributes)


@app.route('/summary')
def summary():
    return render_template('summary.html', data=None)  # Render the summary page with no data

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process the form data here
    # After processing, redirect to the summary page
    return redirect(url_for('summary'))

@app.route('/ocr', methods=['GET', 'POST'])
def ocr_form():
    if request.method == 'POST':
        # Handle the OCR form submission here
        return redirect(url_for('ocr'))  # Redirect to the OCR page after processing the form
    else:
        return render_template('ocr.html')

if __name__ == '__main__':
    app.run(debug=True)
