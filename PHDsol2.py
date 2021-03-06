import pandas as pd                           #Importing Required Libraries
import numpy as np
import re      

col = 1
rej_count = 0
short_count = 0
non_count = 0


    
a = re.compile('computer' , re.I)                                              #Setting up various regex object to use for identification of key data
b = re.compile('cse' , re.I)
c = re.compile('information technology' , re.I)
d = re.compile('signal',re.I)
e = re.compile('cs',re.I)
f = re.compile('c.s.e',re.I)
g = re.compile('mathematics and computing',re.I)
q = re.compile('mathematics & computing',re.I)
h = re.compile('electronics',re.I)
j = re.compile('communication',re.I)
k = re.compile('digital',re.I)
l = re.compile('software' , re.I)
m = re.compile('IIT.*', re.I)
n  =re.compile('Indian Institute Of Technology.*',re.I)
o = re.compile('IISC' ,re.I)
p = re.compile('Indian Institute Of Science',re.I)
oo = re.compile('ISI',re.I)
pp = re.compile('Indian Statistical Institute',re.I)
mtech = re.compile('m.*tech',re.I|re.S)
mtech1 = re.compile('master.* of technology',re.I)
btech =  re.compile('b.*tech',re.I|re.S)
btech1 = re.compile('Bachelor Of Technology' ,re.I)
be = re.compile('b\.?e' ,re.I)
be1 = re.compile('bachelor of engineering',re.I)
me = re.compile('m.?e',re.I)
me1 = re.compile('master of engineering',re.I)
msc = re.compile('m.?sc',re.I|re.S)
msc1 = re.compile('master of science',re.I)
mca = re.compile('mca',re.I)
mca1 = re.compile('Master of Computer Application.?',re.I)
bca = re.compile('bca',re.I)
bca1 = re.compile('Bachelor of Computer Application.?',re.I)


#input_file = 'raw_info_from_form_input_file.csv'                             #Select which file to open
input_file = 'CSE_Phd_396.csv'                              
df_in = pd.read_csv(input_file,delimiter = ',')                               #Transferring data from csv file to pandas Datarame 
Invalid_degree = []
rejected_df = pd.DataFrame(columns = df_in.columns)
shortlisted_df = pd.DataFrame(columns = df_in.columns)
Non_shortlisted_df = pd.DataFrame(columns = df_in.columns)
shortlisted_df['Remarks']  = np.nan


for ind in df_in.index:
    check_flag = 0
    check_flag2 = 0
    check_flag3 = 0
    check_flag4 = 0
    Gate_exemp = 0                                                               
    age_exemp = 0
    ugcpi,ugper,qcpi,qper,hscpi,hsper,experience = [0]*7
    Candidate = df_in['159_e_full_name'][ind]
    qfd = df_in['101_e_qualification_degree'][ind]
    qdis = df_in['101_e_discipline'][ind]
    IIT_check = df_in['101_y_name_and_place_of_institution_or_university'][ind]

    if(df_in['101_e_overall_percentage_of_marks_or_final_grade_point_average'][ind]<=10):
        qcpi = df_in['101_e_overall_percentage_of_marks_or_final_grade_point_average'][ind]
    elif(df_in['101_e_overall_percentage_of_marks_or_final_grade_point_average'][ind]>10):
        qper = df_in['101_e_overall_percentage_of_marks_or_final_grade_point_average'][ind]
    if(df_in['104_e_percentage_of_marks_or_final_grade_point_average'][ind]<=10):
        ugcpi = df_in['104_e_percentage_of_marks_or_final_grade_point_average'][ind]
    elif(df_in['104_e_percentage_of_marks_or_final_grade_point_average'][ind]>10):
        ugper = df_in['104_e_percentage_of_marks_or_final_grade_point_average'][ind]     
    imper =  df_in['103_e_percentage_of_marks_or_final_grade_point_average'][ind] 
    if(df_in['102_e_percentage_of_marks_or_final_grade_point_average'][ind]<=10):
        hscpi = df_in['102_e_percentage_of_marks_or_final_grade_point_average'][ind]
    elif(df_in['102_e_percentage_of_marks_or_final_grade_point_average'][ind]>10):
        hsper = df_in['102_e_percentage_of_marks_or_final_grade_point_average'][ind]      
    gate = df_in['215_n_have_you_written_the_gate_examination'][ind] 
    category = df_in['159_y_category'][ind] 
    gender =   df_in['159_r_gender'][ind] 
    age =   2020 - int(df_in['159_h_date_of_birth'][ind].strip()[-4:])
    Phd_category = df_in['159_y_seeking_phd_admission_under_category'][ind]
    
    if(df_in['109_e_exam_name'][ind] == 'GATE'):                                        #Checking if the exam given in GATE or UGC-NET
        if(np.isnan(df_in['109_k_exam_rank'][ind]) == False and df_in['109_k_exam_rank'][ind]!='' and df_in['109_k_exam_rank'][ind] != '--'):
            gate_rank = df_in['109_k_exam_rank'][ind]
        else:
            gate_rank = 10000
    else:
        gate = 'No'
        
    pd = df_in['159_d_physically_handicapped'][ind]
    
    
    if(df_in['162_n_name_of_organization'][ind]!='' and type(df_in['162_n_name_of_organization'][ind]) is not float):                                                          #
                                                                                                                                                                               #                             
        if(df_in['162_k_end_date_of_work'][ind] == '' or type(df_in['162_k_end_date_of_work'][ind]) is float or df_in['162_k_end_date_of_work'][ind].strip()[-5] != '/'):      #
            experience =  2020 - int(df_in['162_k_start_date_of_work'][ind].strip()[-4:])                                                                         # 
        else:                                                                                                                                                                  #       
            experience =  int(df_in['162_k_end_date_of_work'][ind].strip()[-4:]) -  int(df_in['162_k_start_date_of_work'][ind].strip()[-4:])                                   # Calculating Experience from Start and End Date at current employer

    
    elif(df_in['161_n_name_of_organization'][ind]!='' and type(df_in['161_n_name_of_organization'][ind]) is not float):                                                        #
                                                                                                                                                                               #                             
        if(df_in['161_k_end_date_of_work'][ind] == '' or type(df_in['161_k_end_date_of_work'][ind]) is float or df_in['161_k_end_date_of_work'][ind].strip()[-5] != '/'):      #
            experience =  2020 - int(df_in['161_k_start_date_of_work'][ind].strip()[-4:])                                                                         # 
        else:                                                                                                                                                                  #       
            experience =  int(df_in['161_k_end_date_of_work'][ind].strip()[-4:]) -  int(df_in['161_k_start_date_of_work'][ind].strip()[-4:])                                   # 
                                                                                                                                                                               #          
                                                                                                                                                                               #              
    elif(df_in['106_n_name_of_organization'][ind]!='' and type(df_in['106_n_name_of_organization'][ind]) is not float):                                                        #          
                                                                                                                                                                               #           
        if(df_in['106_k_end_date_of_work'][ind] == '' or type(df_in['106_k_end_date_of_work'][ind]) is float or df_in['106_k_start_date_of_work'][ind].strip()[-5] != '/'):    #
            experience =  2020 - int(df_in['106_k_start_date_of_work'][ind].strip()[-4:])
        else:
            experience =  int(df_in['106_k_end_date_of_work'][ind].strip()[-4:]) -  int(df_in['106_k_start_date_of_work'][ind].strip()[-4:])
        

    
    
    if(a.search(qdis) == None and b.search(qdis) == None and c.search(qdis) == None and d.search(qdis) == None and e.match(qdis) == None and f.search(qdis) == None and g.search(qdis) == None and h.search(qdis) == None and j.search(qdis) == None and k.search(qdis) == None and l.search(qdis) == None and q.search(qdis) == None):
        disp_flag = 0          #Checking if correct discipline 
    else:
        disp_flag = 1
    
    
    if(m.match(IIT_check)!= None or n.search(IIT_check)!=None ):
       
        IIT_flag = 1          #Checking if IIT
    else:
        IIT_flag = 0
        
    if(o.match(IIT_check)!= None or p.search(IIT_check)!=None or oo.match(IIT_check)!=None or pp.match(IIT_check)!=None):
        IISC_flag = 1         #Checking if IISC or ISI
    else:
        IISC_flag = 0
        
    if(experience>=2 and Phd_category == 'Employed and Part Time'):       #Removing Age criteria if experience>=2years
        age_exemp = 1
    
    
    Mtech_check = bool(mtech.search(qfd))|bool(mtech1.search(qfd))            #Various checks for identifying degree
    MS_check    =(qfd.lower() == 'ms') or(qfd.lower() == 'm.s') or(qfd.lower() == 'm.s.') or (qfd.lower() == 'master of science')
    ME_check    = bool(me.search(qfd))|bool(me1.search(qfd))
    Btech_check = bool(btech.search(qfd))|bool(btech1.search(qfd))|bool(be.match(qfd))|bool(be1.search(qfd))
    MCA_check   = bool(mca.match(qfd))|bool(mca1.search(qfd))
    MSC_check   = bool(msc.search(qfd))|bool(msc1.search(qfd))
    
    if(Mtech_check == False and MS_check == False and ME_check==False and Btech_check == False and MCA_check == False and MSC_check == False):
        Invalid_degree.append([df_in['UserId'][ind],Candidate,qfd])
        rejected_df.loc[rej_count] = df_in.loc[ind]
        rej_count+=1
    
    if(Mtech_check or MS_check or ME_check):                                  #Relaxation Conditions as specified
        ugcpi_l,ugper_l,imper_l,hscpi_l,hsper_l = 6.5,60,60,6.5,60
        if(IIT_flag or IISC_flag or category == 'SC' or category == 'ST' or pd == 'Yes'):
            ugper_l = 55
            ugcpi_l = 6.0
        if(qcpi>=7.5 or qper>=70):                                            #If Cpi>7.5 or 70% allowing qualification of second class X and XII
            if(imper>=60):
                hscpi_l = 5.3
                hsper_l = 50
            elif(hscpi >= 6.5 or hsper >= 60):
                imper_l = 50
    
    
    
    if(Btech_check or MCA_check or MSC_check):
        ugcpi_l,ugper_l,imper_l,hscpi_l,hsper_l,gate_rank_l = 6.5,60,60,6.5,60,5000
        if(qcpi>=8.5 or qper>=80 or (Btech_check and IIT_flag and qcpi>=8.0)):   #If Cpi>8.5 or 80% allowing qualification of second class X and XII
            if(imper>=60):
                hscpi_l = 5.3
                hsper_l = 50
            elif(hscpi >= 6.5 or hsper >= 60):
                imper_l = 50
           
        if((Btech_check and IIT_flag and qcpi>=8.0) or (experience>=2 and Phd_category == 'Employed and Part Time')):           
            Gate_exemp = 1
        
        if(category == 'SC' or category == 'ST' or pd == 'Yes'):
            gate_rank_l = 6000
         
       
             
    
    
    if((Mtech_check or MS_check or ME_check)  and (qcpi>=6.5 or qper>=60) and (ugcpi>=ugcpi_l or ugper>=ugper_l) and (imper>=imper_l) and (hscpi>= hscpi_l or hsper>=hsper_l) and (gate == 'Yes')):
        check_flag3  = 1
        if((category=='General' and (age<=32 or age_exemp)) or ((category=='OBC Non Creamy Layer'  or category== 'EWS'  or gender == 'Female' or category == 'SC' or category == 'ST' or pd == 'Yes' ) and (age<=37 or age_exemp))):
            shortlisted_df.loc[short_count] = df_in.loc[ind]
            short_count+=1
            if(disp_flag == 0):
                shortlisted_df.loc[short_count-1,'Remarks'] = 'SHORTLISTED BUT PLEASE CHECK BRANCH ELIGIBILITY'
                
        else:
            Non_shortlisted_df.loc[non_count] = df_in.loc[ind]
            non_count+=1
            
                        
            
    elif((Btech_check or MCA_check or MSC_check)  and (qcpi>=8 or qper>=75)  and (ugcpi>=ugcpi_l or ugper>=ugper_l) and (imper>=imper_l) and (hscpi>= hscpi_l or hsper>=hsper_l) and (((gate=='Yes') and (gate_rank<=gate_rank_l)) or Gate_exemp)):
        check_flag2 = 1
        if((category=='General' and (age<=28 or age_exemp)) or ((category=='OBC Non Creamy Layer'  or category== 'EWS'  or gender == 'Female' or category == 'SC' or category == 'ST' or pd == 'Yes' ) and (age<=33 or age_exemp))):
            shortlisted_df.loc[short_count] = df_in.loc[ind]
            short_count+=1
            if(disp_flag == 0):
                shortlisted_df.loc[short_count-1,'Remarks'] = 'SHORTLISTED BUT PLEASE CHECK BRANCH ELIGIBILITY'
        else:
            check_flag = 1
            Non_shortlisted_df.loc[non_count] = df_in.loc[ind]
            non_count+=1
            
    
    
    if(check_flag3 == 0 and (check_flag2 == 0 or check_flag == 1) and Btech_check and (df_in['214_n_degree_or_examination'][ind] != '' and type(df_in['214_n_degree_or_examination'][ind]) is not float)):  # If qualification degree Btech , checking for Mtech passing criteria if possible
        check_flag4 = 1
        IIT_check = df_in['214_y_name_of_institution_or_university'][ind]
        
        if(df_in['214_e_percentage_of_marks_or_final_grade_point_average'][ind] != '' and np.isnan(df_in['214_e_percentage_of_marks_or_final_grade_point_average'][ind]) == False ):
            if(df_in['214_e_percentage_of_marks_or_final_grade_point_average'][ind]<=10):
                qcpi = df_in['214_e_percentage_of_marks_or_final_grade_point_average'][ind]
            elif(df_in['214_e_percentage_of_marks_or_final_grade_point_average'][ind]>10):
                qper = df_in['214_e_percentage_of_marks_or_final_grade_point_average'][ind]
        else:
            qcpi,qper = 0,0
        
        if(m.match(IIT_check)!= None or n.search(IIT_check)!=None ):
            IIT_flag = 1          
        else:
            IIT_flag = 0
        
        if(o.match(IIT_check)!= None or p.search(IIT_check)!=None or oo.match(IIT_check)!=None or pp.match(IIT_check)!=None):
            IISC_flag = 1         
        else:
            IISC_flag = 0
        
        
        if(IIT_flag or IISC_flag or category == 'SC' or category == 'ST' or pd == 'Yes'):                                                      
            ugper_l = 55
            ugcpi_l = 6.0
        if(qcpi>=7.5 or qper>=70):
            if(imper>=60):
                hscpi_l = 5.3
                hsper_l = 50
            elif(hscpi >= 6.5 or hsper >= 60):
                imper_l = 50
        if((qcpi>=6.5 or qper>=60) and (ugcpi>=ugcpi_l or ugper>=ugper_l) and (imper>=imper_l) and (hscpi>= hscpi_l or hsper>=hsper_l) and (gate == 'Yes')):
            if((category=='General' and (age<=32 or age_exemp)) or ((category=='OBC Non Creamy Layer'  or category== 'EWS'  or gender == 'Female' or category == 'SC' or category == 'ST' or pd == 'Yes' ) and (age<=37 or age_exemp))):
                shortlisted_df.loc[short_count] = df_in.loc[ind]
                short_count+=1
                if(check_flag == 1):
                    Non_shortlisted_df.drop(non_count-1,inplace = True)
                    non_count-=1

                #print(Candidate, 'New' ,df_in['UserId'][ind] )
                if(disp_flag == 0):
                    shortlisted_df.loc[short_count-1,'Remarks'] = 'SHORTLISTED BUT PLEASE CHECK BRANCH ELIGIBILITY'   
                    
            else:
                if(check_flag == 0):
                    Non_shortlisted_df.loc[non_count] = df_in.loc[ind]
                    non_count+=1
        else:
            if(check_flag == 0):
                Non_shortlisted_df.loc[non_count] = df_in.loc[ind]
                non_count+=1
            
                
    
    if(not(check_flag4) and not(check_flag3) and not(check_flag2)):
        Non_shortlisted_df.loc[non_count] = df_in.loc[ind]
        non_count+=1
        
 

o1 =  'CSE_Final_Format.xlsx'
o2 =  'CSE_Not_Shortlisted_Final_Format.xlsx'
#o1  =   'Final_Format.xlsx'
#o2  =   'Not_Shortlisted_Final_Format.xlsx'     
shortlisted_df.to_excel(o1,index = False)
Non_shortlisted_df.to_excel(o2,index=  False)     
rejected_df.to_excel('invalid_candidates.xlsx',index = False)      
print('Code Ran Sucessfully.Files has been generated for' , input_file , 'The generated files are' ,o1 ,'and', o2 )
for i in Invalid_degree:
    print('User ID',i[0],'Name',i[1],'No valid degree' , i[2])

        
        

        
        
        
    
    


      
    

   
    
    
    