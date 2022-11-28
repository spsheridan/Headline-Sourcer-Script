import csv
import random

with open('historicalHeadlines.csv', "r", newline = '', encoding = "utf8") as csvfile:

    with open('CompanyNames.csv', "r", newline = '', encoding = "utf8") as csvfile3:
        nameSourcer = csv.reader(csvfile3, delimiter = ',', quotechar = '|')

        names = []

        for row in nameSourcer:
            companyName = row[0]
            #if len(row) > 0 and companyName.find('Acquisition') == -1 and companyName.find('Merger') == -1:
            if companyName.find('Pharma') != -1 or companyName.find('Bioscience') != -1 or companyName.find('Therapeutics') != -1 or companyName.find('Life Sciences') != -1 or companyName.find('Biologics') != -1 or companyName.find('Biotechnologies') != -1 or companyName.find('Genetic Technologies') != -1 or companyName.find('Oncology Holdings') != -1 or companyName.find('Gilead') != -1 or companyName.find('Biogen') != -1 or companyName.find('Pfizer') != -1 or companyName.find('Novartis') != -1 or companyName.find('Novavax') != -1:    
                names.append(companyName)

        with open('headlines.csv', 'w', newline = '', encoding = "utf8") as csvfile2:
            writer = csv.writer(csvfile2, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
            sourcer = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            i = 0
            for row in sourcer:
                i += 1
                if i > 200:
                    break
                if len(row) > 1:
                    headline = row[2]
                    
                    companyName1 = random.choice(names)
                    companyName2 = random.choice(names)
                    companyName3 = random.choice(names)

                    numbersList = [1,2,3]
                    numberRandom = random.choice(numbersList)
                    numberRandom2 = random.choice(numbersList)
                    numberRandom3 = random.choice(numbersList)

                    countryList = ['the United States', 'Canada', 'China', 'England', 'Germany', 'Gabon', 'Costa Rica', 'Alaska', 'Russia', 'Venezuela', 'Brazil', 'India', 'South Africa']
                    countryName = random.choice(countryList)

                    diseaseList = ["Alzheimer's Disease", "Parkinson's", 'Lung Cancer', 'Non Small Cell Lung Cancer', 'Prostate Cancer', 'Liver Cirrhosis', 'Opioid Addiction', 'Hepatitis B', 'Malaria', 'Dengue', 'Tuberculosis', 'Influenza Virus', 'COVID-19 Virus', 'Syphilis', 'Norovirus', 'Salmonella', 'HIV and AIDS', 'Lyme Disease', 'Breast Cancer', 'Ovarian Cancer', 'Melanoma', 'Non-Hodgkin Lymphoma', 'Cystic Fibrosis', 'Kidney Cancer', 'Leukemia', 'Pancreatic Cancer']
                    diseaseName = random.choice(diseaseList)

                    drugList = ['Atorvastatin', 'Levothyroxine', 'Lisinopril', 'Metformin', 'Metoprolol', 'Amlodipine', 'Albuterol', 'Omeprazole', 'Losartan', 'Gabapentin', 'Hydrochlorothiazide', 'Sertraline', 'Simvastatin', 'Montelukast', 'Pantoprazole', 'Furosemide', 'Fluticasone', 'Escitalopram', 'Fluoxetine', 'Rosuvastatin', 'Bupropion', 'Amoxicillin', 'Trazodone', 'Duloxetine', 'Prednisone', 'Tamsulosin', '	Ibuprofen', 'Citalopram']
                    drugName1 = random.choice(drugList)
                    drugName2 = random.choice(drugList)

                    trialList = ['Dosing of First Patient', 'FDA Acceptance of NDA', 'Phase 2 Clinical Trial', 'Phase 3 Clinical Trial']
                    trialName = random.choice(trialList)

                    nameList = ['Brown McDermott', 'Sigrid Murphy', 'Lavonne Langworth', 'Beth Schmidt', 'Jamey Prosacco', 'Rashad Beahan', 'Noel Tillman', 'Julie Sporer', 'Chanel Hermann', 'Reinhold Weimann', 'Euna Swift', 'Estrella Bruen', 'Lynn Gleichner', 'Emelia Hessel', 'Kamille Mann', 'Vaughn Grady', 'Pinkie Kemmer', 'August Price', 'Alana Homenick']
                    randomName = random.choice(nameList)

                    bankList = ['Bank of America', 'Barclays', 'Bank of Montreal', 'Citigroup', 'Credit Suisse', 'JPMorgan Chase', 'Jefferies', 'Mitsubishi Financial', 'Goldman Sachs', 'Lehman Brothers', 'Soloman Brothers', 'Wells Fargo', 'UBS Group']
                    randomBank = random.choice(bankList)
                    randomBank2 = random.choice(bankList)

                    positionList = ['CEO', 'CFO', 'CMO', 'COO', 'CGO']
                    randomPosition = random.choice(positionList)

                    socialMedia = ['Twitter', 'Facebook', 'Youtube', 'Rumble', 'Tik Tok']
                    randomSocialMedia = random.choice(socialMedia)

                    exchangesList = ['NASDAQ', 'TSX.V', 'TSX', 'AMEX', 'NYSE']
                    randomExchange = random.choice(exchangesList)

                    ratingList = ['Buy', 'Sell', 'Hold', 'Overweight', 'Underweight', 'Outperform', 'Underperform', 'Sector Perform']
                    negativeRatingList = ['Sell', 'Hold', 'Underweight', 'Underperform', 'Sector Perform']
                    positiveRatingList = ['Buy', 'Hold', 'Overweight', 'Outperform', 'Sector Perform']
                    randomRating = random.choice(ratingList)
                    randomNegRating = random.choice(negativeRatingList)
                    randomPosRating = random.choice(positiveRatingList)

                    randomPrice = str(random.randint(10, 450))

                    ####NEUTRAL TRIAL RESULTS
                    #if (headline.find('Trial') != -1) and (headline.find('Data') != -1 or headline.find('Results') != -1) and (headline.find('Positive') == -1 and headline.find('Promising') == -1 and headline.find('Encouraging') == -1 and headline.find('Effective') == -1 and headline.find('Benefi') == -1) and (headline.find('Annual') == -1) and (headline.find('Conference') == -1) and (headline.find('Forum') == -1) and (headline.find('Symposium') == -1) and (headline.find('ESMO') == -1) and (headline.find('Congress') == -1) and (headline.find('World Muscle Society') == -1 and headline.find('Present') == -1 and headline.find('Publication') == -1 and headline.find('Publish') == -1): 
                    
                    ####TRIAL UPDATE
                    #if (headline.find('Update') != -1) and (headline.find('Financial Results') == -1 and headline.find('Trial') != -1):
                    
                    ####ENROLLMENT
                    #if (headline.find('Enrollment') != -1 and headline.find('Trial') != -1):
                    
                    ####INITIATION OF TRIAL
                    #if (headline.find('Initiation') != -1 and (headline.find('Study') != -1 or headline.find('Trial') != -1) and headline.find('Enrollment') == -1):
                    
                    ####DRUG PRESENTATION
                    #if (headline.find('Trial') != -1) and (headline.find('Data') != -1 or headline.find('Results') != -1)  and ((headline.find('Annual') != -1) or (headline.find('Conference') != -1) or (headline.find('Forum') != -1) or (headline.find('Symposium') != -1) or (headline.find('ESMO') != -1) or (headline.find('Congress') != -1) or (headline.find('World Muscle Society') != -1) or (headline.find('ASCO') != -1)): 

                    ####PRIMARY ENDPOINT
                    #if (headline.find('Primary') != -1 and headline.find('Endpoint') != -1): #and headline.find('Not') != -1):
                    
                    ####Negative trial results
                    #if(headline.find('Negative') != -1 and headline.find('Trial') != -1):

                    ####MISC
                    #if(headline.find('Trial') != -1 and headline.find('Type C') != -1 and headline.find('Meeting') == -1 and headline.find('FDA') == -1): # and headline.find('Study') != -1): # and headline.find('Data') != -1):
                    #if(headline.find('Supply Chain') != -1 and headline.find('Fair') != -1):

                    ####DEBT OFFERING
                    #if(headline.find('Offering') != -1 and headline.find('Debt') != -1 and headline.find('Initial') == -1 and headline.find('Acquisition') == -1 and headline.find('Rights') == -1 and headline.find('Prefer') == -1 and headline.find('Listing') == -1):
                    #if(headline.find('Repurchase') != -1 and headline.find('Dividend') == -1 and headline.find('Offering') == -1 and headline.find('Results') == -1 and headline.find('Split') == -1):
                    
                    ####EQUITY OFFERING
                    #if(headline.find('Clos') != -1 and headline.find('Offering') != -1 and headline.find('Note') == -1):
                    
                    ####STOCK SPLIT / REVERSE STOCK SPLIT
                    #if(headline.find('Stock Split') != -1 and headline.find('Reverse') != -1):

                    ####MERGER TERMINATION
                    #if(headline.find('Merger') != -1 and headline.find('Terminate') != -1):
                    #headline = companyName1 + " Announces Mutual Agreement to Terminate Proposed Merger with " + companyName2
                    #writer.writerow([headline])
                    
                    ####DELISTING
                    #if(headline.find('Delist') != -1 and (headline.find('NASDAQ') != -1 or headline.find('NYSE') != -1 or headline.find('New York Stock Exchange') != -1)):
                    
                    ####CLINICAL HOLD
                    #if(headline.find('Clinical Hold') != -1 and headline.find('Lift') == -1 and headline.find('Removes') == -1):
                    #headline = companyName1 + " Receives FDA Clinical Hold Letter"
                    
                    ####MERGER ANNOUNCEMENT
                    #if(headline.find('to Merge with') != -1):
                    
                    ####ANALYST INITIATION
                    #headline = companyName1 + " Initiated with " + randomRating + " Rating at " + randomBank
                    #headline = randomBank + " Initiates Coverage on " + companyName1 + " with " + randomRating + " Rating and Announces Price Target of $" + str(randomPrice)
                    #headline = randomBank + " Initiates " + randomRating + " Rating on " + companyName1
                    
                    ####ORPHAN DRUG DESIGNATION
                    #if(headline.find('Orphan Drug Designation') != -1 and (headline.find('European Union') != -1 or headline.find('EMA') != -1 or headline.find('European Medicines Agency') != -1 or headline.find('EU ') != -1)):

                    ####ANALYST DOWNGRADE
                    #headline = companyName1 + " Downgraded to a " + randomNegRating + " at " + randomBank
                    #headline = randomBank + " Downgrades " + companyName1 + " to a " + randomNegRating + " and Announces Price Target of $" + str(randomPrice)
                    #headline = randomBank + " Downgrades Rating on " + companyName1 + " to a " + randomNegRating

                    ####RMAT
                    #if(headline.find('Regenerative Medicine Advanced Therapy') != -1):
                    #headline = companyName1 + " Receives Regenerative Medicine Advanced Therapy (RMAT) Designation for " + drugName1 + " for the treatment of " + diseaseName
                    #headline = "FDA Designates " + companyName1 + "'s " + drugName1 + " as Regenerative Medicine Advanced Therapy"
                    #headline = companyName1 + " Announces Regenerative Medicine Advanced Therapy (RMAT) from FDA"
                    #headline = companyName1 + " Announces FDA Regenerative Medicine Advanced Therapy Designation Granted to " + drugName1
                    #headline = companyName1 + " Applies for Regenerative Medicine Advanced Therapy Designation from FDA for " + drugName1
                    #headline = companyName1 + " Submits FDA Regenerative Medicine Advanced Therapy Designation Request for " + drugName1
                    #headline = companyName1 + " Announces Response from FDA Regarding Regenerative Medicine Advanced Therapy Designation Request"
                    #headline = companyName1 + " Congratulates Clinical Partner " + companyName2 + " on Receiving FDA Regenerative Medicine Advanced Therapy Designation for " + drugName1
                    
                    ####ENDPOINTS
                    #if(headline.find('Endpoint') != -1 and headline.find('Fail') != -1):
                    #headline = companyName1 + " Announces " + drugName1 + " Did Not Meet Primary Endpoint in Phase " + str(numberRandom) + " Trial in Patients with " + diseaseName
                    #headline = companyName1 + " Announces That " + drugName1 + " Phase " + str(numberRandom) + " Trial in " + diseaseName + " Did Not Meet Endpoints"
                    #headline = companyName1 + " Announce Phase " + str(numberRandom) + " Study in " + diseaseName + " Did Not Meet Primary Efficacy Endpoints"
                    #headline = companyName1 + " Announces That Topeline Results of " + drugName1 + " Fail to Achieve Primary and Secondary Endpoints"
                    #headline = companyName1 + " Reports " + drugName1 + " Did Not Meet Endpoint of Overall Survival in " + diseaseName
                    #headline = companyName1 + " Announces " + drugName1 + " Phase " + str(numberRandom) + " Study Fails to Meet Primary Endpoint"
                    
                    ####DISCONTINUING TRIAL
                    #if(headline.find('Development') != -1 and headline.find('Pause') != -1):
                    #headline = companyName1 + " Discontinues Phase " + str(numberRandom) + " Trial of " + drugName1 + " for the Treatment of " + diseaseName + " Following Interim Analysis"
                    #headline = companyName1 + " to Discontinue Phase " + str(numberRandom) + " " + drugName1 + " Trial"
                    #headline = companyName1 + " Discontinues " + drugName1 + " Development Program"
                    #headline = companyName1 + " Discontinues Development of " + drugName1 + " for the Treatment of " + diseaseName
                    #headline = "Independent Data Monitoring Committee Recommends Discontinuation of the Phase " + str(numberRandom) + " Clinical Trial of " + drugName1 + " in " + diseaseName + " for Futility Following Its Planned Interim Data Review"
                    #headline = companyName1 + " Discontinues " + drugName1 + " Development Program"
                    #headline = companyName1 + " Announces Decision to Pause Clinical Development of " + drugName1

                    ####NEUTRAL TRIAL RESULTS
                    #if(headline.find('Trial') != -1) and (headline.find('Data') != -1 or headline.find('Results') != -1) and (headline.find('Positive') == -1 and headline.find('Promising') == -1 and headline.find('Encouraging') == -1 and headline.find('Effective') == -1 and headline.find('Benefi') == -1) and (headline.find('Annual') == -1) and (headline.find('Conference') == -1) and (headline.find('Forum') == -1) and (headline.find('Symposium') == -1) and (headline.find('ESMO') == -1) and (headline.find('Congress') == -1) and (headline.find('World Muscle Society') == -1 and headline.find('Present') == -1 and headline.find('Publication') == -1 and headline.find('Publish') == -1):
                    
                    ####TYPICAL POSITIVE RESULTS 
                    #if(headline.find(''))
                    
                    ####ASSET SALE // divestment // sells ... to 
                    #if(headline.find('Sale of') != -1 and headline.find('Complet') == -1):

                    ####CONTRACT/GENERAL DEAL OR AGREEMENT
                    #if(headline.find('Fast Track Designation') != -1):
                    #headline = companyName1 + " Requests for Fast Track Designation for " + drugName1 + " for the Treatment of " + diseaseName
                    #headline = companyName1 + " Congratulates " + companyName2 + " on Obtaining Fast Track Designation"
                    #headline = companyName1 + " Announces Fast Track Designation Application Denied by FDA"
                    
                    ####INSIDER BUYS NOT FILINGS
                    #if(headline.find('Open Market') != -1 and (headline.find('Purchas') != -1 or headline.find('Acquir') != -1)):
                    #if(headline.find('CEO') != -1 and headline.find('Purchas') != -1):
                    #headline = companyName1 + " Announces Purchase of Common Shares by " + randomPosition
                    #headline = companyName1 + " " + randomPosition + " Purchased a Total of " + str(randomPrice) + "000 Shares in the Open Market"
                    #headline = companyName1 + " " + randomPosition + " Acquires Shares of Common Stock on the Open Market"
                    
                    ####ACQUISITIONS
                    #if(headline.find('Acquisition') != -1 and headline.find('Complet') == -1 and headline.find('Close') == -1): 
                    #if(headline.find('To Be Acquired By') != -1 or headline.find('to be Acquired by') != -1):
                    #if(headline.find('Definitive Acquisition Agreement') != -1):
                    
                    ####LICENSING HEADLINES
                    #if((headline.find('Licensing') != -1 or headline.find('License') != -1) and (headline.find('Pharm') != -1 or headline.find('Bio') != -1 or headline.find('Therapeutics') != -1) and headline.find('Biologics License Application') == -1):

                    ####STRATEGIC ALTERNATIVES
                    #if(headline.find('Strategic Alternatives') != -1): 
                    
                    ####ANALYST UPGRADE
                    #headline = companyName1 + " Upgraded to a " + randomPosRating + " at " + randomBank
                    #headline = randomBank + " Upgrades " + companyName1 + " to a " + randomPosRating + " and Announces Price Target of $" + randomPrice
                    #headline = randomBank + " Upgrades Rating on " + companyName1 + " to a " + randomPosRating
                    #headline = randomBank + " Upgrades " + companyName1 + " to a " + randomPosRating + " from a " + randomNegRating + " with a Price Target of $" + randomPrice

                    ####GOOD EARNINGS HEADLINES
                    #if(headline.find('Record') != -1 and headline.find('Revenue') != -1 and headline.find('Increas') != -1):

                    ####EARNING REPOTS 
                    #if(headline.find('Quarter') != -1 and headline.find('Results') != -1): 
                    
                    ####EMERGENCY USE AUTHORIZATION
                    #if(headline.find('Emergency Use Authorization') != -1):
                    
                    ####FOREIGN COUNTRY DRUG APPROVAL
                    #if(headline.find('Regulatory Application') != -1):

                    ####CONTRACT TERMINATION
                    #if(headline.find('Contract') != -1 and headline.find('Terminat') != -1):
                    
                    ####COMPLETE ACQUISITION
                    #if(headline.find('Complet') != -1 and headline.find('Acquisition') != -1):
                    
                    ####PARTNERSHIP TERMINATION AND UPDATE
                    #if(headline.find('Partnership') != -1 and headline.find('Update') != -1):
                    
                    ####OUTSOURCE
                    #if(headline.find('Outsource') != -1):
                    
                    ####LICENSE NON-MEDICAL
                    #if(headline.find('License') != -1 and headline.find('Drug') == -1):

                    ####RESPONSE TO SHORT REPORT
                    #if(headline.find('Short Report') != -1): 
                    #headline = companyName1 + " Responds to Misleading Short Report"
                    #headline = companyName1 + " Refutes Short Report"
                    #headline = companyName1 + " Comments on Short Report"
                    #headline = companyName1 + " Provides Information Refuting Negative Claims in Recently Published Short Report"
                    #headline = companyName1 + " Adamantly Refutes Unfounded Claims By A Short Report"
                    #headline = companyName1 + " Reaffirms Strong Business Outlook and Responds to Short Report"

                    ####PRE-CLINICAL DATA
                    #if(headline.find('Preclinical') != -1 and headline.find('Present') == -1 and headline.find('Data') != -1 and headline.find('Publication') == -1):
                    
                    ####BREAKTHROUGH THERAPY DESIGNATION
                    #headline = "FDA Grants Breakthrough Device Designation to " + companyName1
                    #headline = companyName1 + " Receives Breakthrough Device Designation from FDA"
                    #writer.writerow([headline])
                    