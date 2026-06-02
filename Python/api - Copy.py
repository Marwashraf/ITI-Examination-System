import json
from flask import Flask

from index import *
 
app = Flask(__name__)
@app.route('/CMEAnalyzes/<ALt_SGPT>/<AST_SGOT>')
def index(ALt_SGPT=0.0,AST_SGOT=0.0):
    result = CMEAnalyzes.LiverFunctionTest(float(ALt_SGPT),float(AST_SGOT))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes/<gender>/<Haemoglobin>/<Haematocrit_PCV>/<RBCs_Count>/<MCV>/<MCH>/<MCHC>/<RDW_CV>/<Platelet_Count_EDTA_Blood>/<Total_Leucocytic_Count_EDTA_Blood>/<Neutrophils>/<Staff>/<Segmented>/<Lymphocytes>/<Monocytes>/<Eosinophils>/<Basophils>')
def index1(gender='',Haemoglobin=0.0,Haematocrit_PCV=0.0,RBCs_Count=0.0,MCV=0.0,MCH=0.0,MCHC=0.0,RDW_CV=0.0,
            Platelet_Count_EDTA_Blood=0.0,Total_Leucocytic_Count_EDTA_Blood=0.0,Neutrophils=0.0,Staff=0.0,Segmented=0.0,
            Lymphocytes=0.0,Monocytes=0.0,Eosinophils=0.0,Basophils=0.0):
    result = CMEAnalyzes.CompleteBloodPicture(gender,float(Haemoglobin),float(Haematocrit_PCV),float(RBCs_Count),float(MCV),float(MCH),float(MCHC),float(RDW_CV),
            float(Platelet_Count_EDTA_Blood),float(Total_Leucocytic_Count_EDTA_Blood),float(Neutrophils),float(Staff),float(Segmented),
            float(Lymphocytes),float(Monocytes),float(Eosinophils),float(Basophils))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes1/<gender>/<Serum_Creatinine>/<Serum_Uric_Acid>')
def index2(gender='',Serum_Creatinine=0.0,Serum_Uric_Acid=0.0):
    result = CMEAnalyzes.KidneyFunctionTest(gender,float(Serum_Creatinine),float(Serum_Uric_Acid))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes/<FBS>')
def index3(FBS=0.0):
    result = CMEAnalyzes.FastingBloodSuger(float(FBS))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes2/<gender>/<First_Hours>/<Second_Hours>')
def index4(gender='',First_Hours=0.0,Second_Hours=0.0):
    result = CMEAnalyzes.ESR(gender,float(First_Hours),float(Second_Hours))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes3/<gender>/<UA>')
def index5(gender='',UA=0.0):
    result = CMEAnalyzes.UricAcidTest(gender,float(UA))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes/<Colour>/<Aspect>/<Nitrite>/<Albumin>/<Suger>/<Acetone>/<Bile_Salts>/<Bile_Pigments>/<Urobilinogen>/<Leukocyte_estrease>/<Epithelial_Cells>/<Casts>/<Mucus>/<Ova>/<Crystals>/<Yeast_Cells>/<Trichomonas_vaginalis>/<Volume>/<Reaction>/<Specific_Gravity_in_urine>/<RBCs>/<Pus_Cells>')
def index6(Colour='',Aspect='',Nitrite='',Albumin='',Suger='',Acetone='',Bile_Salts='',Bile_Pigments='',
             Urobilinogen='',Leukocyte_estrease='',Epithelial_Cells='', Casts='',Mucus='',Ova='',
                  Crystals='',Yeast_Cells='',Trichomonas_vaginalis='',Volume=0.0,Reaction=0.0,
                  Specific_Gravity_in_urine=0.0,RBCs=0.0,Pus_Cells=0.0):
    result = CMEAnalyzes.UrineTest(Colour,Aspect,Nitrite,Albumin,Suger,Acetone,Bile_Salts,Bile_Pigments,
             Urobilinogen,Leukocyte_estrease,Epithelial_Cells, Casts,Mucus,Ova,
                  Crystals,Yeast_Cells,Trichomonas_vaginalis,float(Volume),float(Reaction),
                  float(Specific_Gravity_in_urine),float(RBCs),float(Pus_Cells))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/CMEAnalyzes/<Cholesterol>/<Triglyceride>/<HDL_C>/<LDL_C>')
def index7(Cholesterol=0.0,Triglyceride=0.0,HDL_C=0.0,LDL_C=0.0):
    result = CMEAnalyzes.LipidProfile(float(Cholesterol),float(Triglyceride),float(HDL_C),float(LDL_C)) 
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/DiabetesAnalyzes/<FBS>')
def index8(FBS=0.0):
    result = DiabetesAnalyzes.FastingBloodSuger(float(FBS))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/DiabetesAnalyzes/<Fasting_Blood_Glucose>/<Glucose_After_2_Hours>/<Haemoglobin_A1C>')
def index9(Fasting_Blood_Glucose=0.0,Glucose_After_2_Hours=0.0,Haemoglobin_A1C=0.0):
    result = DiabetesAnalyzes.DiabeticProfile(float(Fasting_Blood_Glucose),float(Glucose_After_2_Hours),float(Haemoglobin_A1C))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/DiabetesAnalyzes/<state>/<Fasting_Blood_Glucose>/<Glucose_After_30_min>/<Glucose_After_1_Hour>/<Glucose_After_2_Hours>/<Glucose_After_3_Hours>')
def index10(state='',Fasting_Blood_Glucose=0.0,Glucose_After_30_min=0.0,Glucose_After_1_Hour=0.0,
             Glucose_After_2_Hours=0.0,Glucose_After_3_Hours=0.0):
    result = DiabetesAnalyzes.GlucoseCurve(state,float(Fasting_Blood_Glucose),float(Glucose_After_30_min),float(Glucose_After_1_Hour),
                     float(Glucose_After_2_Hours),float(Glucose_After_3_Hours))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/DiabetesAnalyzes/<gender>/<Normoalbuminuria>/<Microalbuminuria>/<Macroalbuminuria>')
def index11(gender='',Normoalbuminuria=0.0,Microalbuminuria=0.0,Macroalbuminuria=0.):
    result = DiabetesAnalyzes.Microalbuminuria(gender,float(Normoalbuminuria),float(Microalbuminuria),float(Macroalbuminuria))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/LiverFunctionTest/<ALt_SGPT>/<AST_SGOT>/<ALP>/<Albumin>/<Total_protein>/<Bilirubin>/<GGT>/<LD>/<PT>')
def index12(ALt_SGPT=0.0,AST_SGOT=0.0,ALP=0.0,Albumin=0.0,Total_protein=0.0,Bilirubin=0.0,GGT=0.0,LD=0.0,PT=0.0):
    result = LiverFunctionTest.LiverFunctionTest(float(ALt_SGPT),float(AST_SGOT),float(ALP),float(Albumin),float(Total_protein),float(Bilirubin),float(GGT),float(LD),float(PT))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/kidneyFuncyiontTest/<gender>/<Glucose>/<BUN>/<Creatinine>/<Calcium>/<GFR>/<Sodium>/<potassium>/<chloride>/<CO2>/<Anion_Gap>/<BUN_Creat_ratio>')
def index13(gender='',Glucose=0.0,BUN=0.0,Creatinine=0.0,Calcium=0.0,GFR=0.0,Sodium=0.0,potassium=0.0,chloride=0.0,
        CO2=0.0,Anion_Gap=0.0,BUN_Creat_ratio=0.0):
    result = kidneyFuncyiontTest.kidneyFuncyiontTest(gender,float(Glucose),float(BUN),float(Creatinine),float(Calcium),float(GFR),float(Sodium),
                        float(potassium),float(chloride),float(CO2),float(Anion_Gap),float(BUN_Creat_ratio))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ESRBlood/<Blood_Clotting_Time_CT>/<Bleeding_Time_BT>')
def index14(Blood_Clotting_Time_CT=0.0,Bleeding_Time_BT=0.0):
    result = ESRBlood.BleedandclottingTime(float(Blood_Clotting_Time_CT),float(Bleeding_Time_BT))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ESRBlood/<PT>/<APTT>/<Fibrinogen>/<AT_III>/<FDPs>')
def index15(PT=0.0,APTT=0.0,Fibrinogen=0.0,AT_III=0.0,FDPs=0.0):
    result = ESRBlood.ProthrombinTime(float(PT),float(APTT),float(Fibrinogen),float(AT_III),float(FDPs))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ESRBlood/<PC_Test>')
def index16(PC_Test=0.0):
    result = ESRBlood.PlateletCountTest(PC_Test)
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/BloodDiseases/<gender>/<Haemoglobin>/<Haematocrit_PCV>/<RBCs_Count>/<MCV>/<MCH>/<MCHC>/<RDW_CV>/<Platelet_Count_EDTA_Blood>/<Total_Leucocytic_Count_EDTA_Blood>/<Neutrophils>/<Staff>/<Segmented>/<Lymphocytes>/<Monocytes>/<Eosinophils>/<Basophils>')
def index17(gender='',Haemoglobin=0.0,Haematocrit_PCV=0.0,RBCs_Count=0.0,MCV=0.0,MCH=0.0,MCHC=0.0,RDW_CV=0.0,
            Platelet_Count_EDTA_Blood=0.0,Total_Leucocytic_Count_EDTA_Blood=0.0,Neutrophils=0.0,Staff=0.0,Segmented=0.0,
            Lymphocytes=0.0,Monocytes=0.0,Eosinophils=0.0,Basophils=0.0):
    result = BloodDiseases.CompleteBloodPicture(gender,float(Haemoglobin),float(Haematocrit_PCV),float(RBCs_Count),float(MCV),float(MCH),float(MCHC),float(RDW_CV),
            float(Platelet_Count_EDTA_Blood),float(Total_Leucocytic_Count_EDTA_Blood),float(Neutrophils),float(Staff),float(Segmented),
            float(Lymphocytes),float(Monocytes),float(Eosinophils),float(Basophils))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/BloodDiseases/<Hemoglobine_A>/<Hemoglobine_F>/<Hemoglobine_S>/<Hemoglobine_C>')
def index18(Hemoglobine_A=0.0,Hemoglobine_F=0.0,Hemoglobine_S=0.0,Hemoglobine_C=0.0):
    result = BloodDiseases.HbElectrophoresis(float(Hemoglobine_A),float(Hemoglobine_F),float(Hemoglobine_S),float(Hemoglobine_C))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/BloodDiseases/<DCT_User_Result>')
def index19(DCT_User_Result):
    if type(DCT_User_Result)==str:     
        result = BloodDiseases.DirectCoombsTest(DCT_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(DCT_User_Result)==float:
        result = BloodDiseases.DirectCoombsTest2(float(DCT_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح" 
    
@app.route('/BloodDiseases/,<IDCT_User_Result>')
def index20(IDCT_User_Result):
    if type(IDCT_User_Result)==str:     
        result = BloodDiseases.InDirectCoombsTest(IDCT_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(IDCT_User_Result)==float:
        result = BloodDiseases.InDirectCoombsTest2(float(/IDCT_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح" 
   
@app.route('/BloodDiseases/<BG>/<RH_Result>')
def index21(RH_Result,BG=''):
    if type(RH_Result)==str:     
        result = BloodDiseases.BloodGroupANDRh(RH_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(RH_Result)==float:
        result = BloodDiseases.BloodGroupANDRh2(float(RH_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح" 
   
@app.route('/BloodDiseases/<gender>/<G6P_User_Result>')
def index22(gender='',G6P_User_Result=0.0):
    result = BloodDiseases.Glucose6phosphate(gender,float(G6P_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/Hormones/<gender>/<age>/<Estrogen>/<Progesterone>/<FSH>/<LH>/<Prolactin>/<Testosteroe_Total>/<Testosteron_Free>')
def index23(gender='',age='',Estrogen=0.0 ,Progesterone=0.0,FSH=0.0,LH=0.0,Prolactin=0.0,Testosteroe_Total=0.0,Testosteron_Free=0.0):
    result = Hormones.InfertilityTestsF(gender,age,float(Estrogen),float(Progesterone),float(FSH),float(LH),float(Prolactin),float(Testosteroe_Total),float(Testosteron_Free))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<gender>/<Estrogen>/<FSH>/<LH>/<Prolactin>/<Testosteron_Total>/<Testosteron_Free>')
def index24(gender='',Estrogen=0.0,FSH=0.0,LH=0.0,Prolactin=0.0,Testosteron_Total=0.0,Testosteron_Free=0.0):
    result = Hormones.InfertilityTestsM(gender,float(Estrogen),float(FSH),float(LH),float(Prolactin),float(Testosteron_Total),float(Testosteron_Free))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<TSH>/<Total_T4>/<Free_T4>/<Free_T3>/<T3>')
def index25(TSH=0.0,Total_T4=0.0,Free_T4=0.0,Free_T3=0.0,T3=0.0):
    result = Hormones.TSHTest(float(TSH),float(Total_T4),float(Free_T4),float(Free_T3),float(T3))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/Cortisol_AM>/<Cortisol_PM>/<ACTH_AM>/<ACTH_PM><Adrenaline>/<Noradrenaline>/<Dopamine>/<Renin>')
def index26(Cortisol_AM=0.0, Cortisol_PM=0.0,ACTH_AM=0.0,ACTH_PM=0.0,Adrenaline=0.0,Noradrenaline=0.0,
            Dopamine=0.0 ,Renin=0.0):
    result = Hormones.AdrenalGland(float(Cortisol_AM),float(Cortisol_PM),float(ACTH_AM),float(ACTH_PM),float(Adrenaline),float(Noradrenaline),float(Dopamine),float(Renin))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<PH_User_Result>')
def index27(PH_User_Result=0.0):
    result = Hormones.ParathyroidHormoneTest(float(PH_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<gender>/<GH_User_Result>')
def index28(GH_User_Result=0.0,gender=''):
    result = Hormones.GrowthHormone(float(GH_User_Result),gender)
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<BHG_User_Result>/<status>')
def index29(BHG_User_Result=0.0,status=''):
    result = Hormones.B_HCGTest(float(BHG_User_Result),status)
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<DHEA_User_Result>/<status>')
def index30(DHEA_User_Result=0.0,status=''):
    result = Hormones.DHEA_STest(float(DHEA_User_Result),status)
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.route('/Hormones/<HYD_User_Result>/<status>)')
def index31(HYD_User_Result=0.0,status=''):
    result = Hormones.Hydroxyprogesterone(float(HYD_User_Result),status)
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/TORCHIGg_IGM/<Toxoplasma_IgM>/<Toxoplasma_IgG>/<Rubella_IgM>/<Rubella_IgG>/<CMV_IgM>/<CMV_IgG>/<HSV_IgM>/(HSV_IgG)')
def index32(Toxoplasma_IgM=0.0,Toxoplasma_IgG=0.0,Rubella_IgM=0.0,Rubella_IgG=0.0,
               CMV_IgM=0.0,CMV_IgG=0.0,HSV_IgM=0.0,HSV_IgG=0.0):
    result = TORCHIGg_IGM.TORCHIGgf(float(Toxoplasma_IgM),float(Toxoplasma_IgG),float(Rubella_IgM),float(Rubella_IgG),float(CMV_IgM),float(CMV_IgG),float(HSV_IgM),float(HSV_IgG))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/TherapeuticDrugs/<phenytoin_User_Result>')
def index33(phenytoin_User_Result=0.0):
    result = TherapeuticDrugs.phenytoin(float(phenytoin_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TherapeuticDrugs/<Carbamazepine_User_Result>')
def index34(Carbamazepine_User_Result=0.0):
    result = TherapeuticDrugs.Carbamazepine(float(Carbamazepine_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TherapeuticDrugs/<Digoxin_User_Result>')
def index35(Digoxin_User_Result=0.0):
    result = TherapeuticDrugs.Digoxin(float(Digoxin_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TherapeuticDrugs/<Lithium_User_Result>')
def index36(Lithium_User_Result=0.0):
    result = TherapeuticDrugs.Lithium(float(Lithium_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/GeneticsAnalyses/<Karyotyping_User_Result>')
def index37(Karyotyping_User_Result=0.0):
    result = GeneticsAnalyses.Karyotyping(float(Karyotyping_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/GeneticsAnalyses/<status>/<Alanine>/<Alpha_amino_N_butyric_acid>/<Arginine>/<Asparagine>/<Aspartic_acid>/<Beta_alanine>/<Citrulline>/<Cystine>/<Glutamic_acid>/<Glutamine>/<Glycine>/<Histidine>/<Isoleucine>/<Leucine>/<Lysine>/<Methionine>/<Ornithine>/<Phenylalanine>/<Proline>/<Serine>/<Taurine>/<Threonine>/<Tyrosine>/<Valine>/<Alpha_aminoadipic_acid>/<Beta_amino_isobutyric_acid>/<Carnosine>/<Hydroxyproline>/<i_methylhistidine>')
def index38(status='',Alanine=0.0,Alpha_amino_N_butyric_acid=0.0,Arginine=0.0,
            Asparagine=0.0,Aspartic_acid=0.0,Beta_alanine=0.0,Citrulline=0.0,
            Cystine=0.0,Glutamic_acid=0.0,Glutamine=0.0,Glycine=0.0,
            Histidine=0.0,Isoleucine=0.0,Leucine=0.0,Lysine=0.0,Methionine=0.0,
            Ornithine=0.0,Phenylalanine=0.0,Proline=0.0,Serine=0.0,Taurine=0.0,
            Threonine=0.0,Tyrosine=0.0,Valine=0.0,Alpha_aminoadipic_acid='',Beta_amino_isobutyric_acid='',
            Carnosine='',Hydroxyproline='',i_methylhistidine=''):
    result = GeneticsAnalyses.Aminograminplasma(status,float(Alanine),float(Alpha_amino_N_butyric_acid),float(Arginine),
                        float(Asparagine),float(Aspartic_acid),float(Beta_alanine),float(Citrulline),float(Cystine),float(Glutamic_acid),float(Glutamine),float(Glycine),
                        float(Histidine),float(Isoleucine),float(Leucine),float(Lysine),float(Methionine),float(Ornithine),float(Phenylalanine),float(Proline),float(Serine),float(Taurine),
                        float(Threonine),float(Tyrosine),float(Valine),float(Alpha_aminoadipic_acid),float(Beta_amino_isobutyric_acid),float(Carnosine),float(Hydroxyproline),float(i_methylhistidine))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/farmanalysis/<Colour>/<Aspect>/<Nitrite>/<Albumin>/<Suger>/<Acetone>/<Bile_Salts>/<Bile_Pigments>/<Urobilinogen>/<Leukocyte_estrease>/<Epithelial_Cells>/<Casts>/<Mucus>/<Ova>/<Crystals>/<Yeast_Cells>/<Trichomonas_vaginalis>/<Volume>/<Reaction>/<Specific_Gravity_in_urine>/<RBCs>/<Pus_Cells>')
def index39(Colour='',Aspect='',Nitrite='',Albumin='',Suger='',Acetone='',Bile_Salts='',Bile_Pigments='',
             Urobilinogen='',Leukocyte_estrease='',Epithelial_Cells='', Casts='',Mucus='',Ova='',
                  Crystals='',Yeast_Cells='',Trichomonas_vaginalis='',Volume=0.0,Reaction=0.0,
                  Specific_Gravity_in_urine=0.0,RBCs=0.0,Pus_Cells=0.0):
    result = farmanalysis.UrineTest(Colour,Aspect,Nitrite,Albumin,Suger,Acetone,Bile_Salts,Bile_Pigments,
             Urobilinogen,Leukocyte_estrease,Epithelial_Cells, Casts,Mucus,Ova,
                  Crystals,Yeast_Cells,Trichomonas_vaginalis,float(Volume),float(Reaction),
                  float(Specific_Gravity_in_urine),float(RBCs),float(Pus_Cells))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/farmanalysis/<Colour>/<Odure>,<Blood>/<Consistency>/<PH>/<Worms>/<Undigested_Food>/<Epithelial_Cells>/<Protozoa>/<Helminths>/<Yeast_Cells>/<RBCs>/<Pus_Cells>/<Vegetable_cells>/<Starch>/<Muscle_Fibers>/<Fat>')
def index40(Colour='',Odure='',Blood='',Consistency='',PH='',Worms='',Undigested_Food='',
         Epithelial_Cells='', Protozoa='',Helminths='',Yeast_Cells='',RBCs=0.0,Pus_Cells=0.0,Vegetable_cells='',
                      Starch='',Muscle_Fibers='',Fat=''):
    result = farmanalysis.StoolAnalysis(Colour,Odure,Blood,Consistency,PH,Worms,Undigested_Food,
         Epithelial_Cells, Protozoa,Helminths,Yeast_Cells,float(RBCs),float(Pus_Cells),float(Vegetable_cells),
                      float(Starch),float(Muscle_Fibers),float(Fat))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/farmanalysis/<RBCs>/<Pus_Cells>/<Bilharzial_Ova>/<Trichomonas_vaginalis>')
def index41(RBCs=0.0,Pus_Cells=0.0,Bilharzial_Ova='',Trichomonas_vaginalis=''):
    result = farmanalysis.Prostatic(float(RBCs),float(Pus_Cells),float(Bilharzial_Ova),float(Trichomonas_vaginalis))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/farmanalysis/<Vaginal_User_result>')
def index42(Vaginal_User_result):
    if type(Vaginal_User_result)==str:     
        result = farmanalysis.VaginalExam(Vaginal_User_result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(Vaginal_User_result)==float:
        result = farmanalysis.VaginalExam2(float(Vaginal_User_result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
@app.route('/farmanalysis/<Color>/<Method_of_production>/<Abstinence>/<Volume>/<Liquefaction_Time>/<PH>/<Sperm_Count>')
def index43(Color='',Method_of_production='',Abstinence=0.0,Volume=0.0,Liquefaction_Time=0.0,PH=0.0,Sperm_Count=0.0):
    result = farmanalysis.SemenExam(Color,Method_of_production,float(Abstinence),float(Volume),float(Liquefaction_Time),float(PH),float(Sperm_Count))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/farmanalysis/<Appearance>/<Gram_Stain>/<Pressure>/<Protein>/<Glucose>/<WCC>/<Glucose_serum_ratio>')
def index44(Appearance='',Gram_Stain='',Pressure=0.0,Protein=0.0,Glucose=0.0,WCC=0.0,Glucose_serum_ratio=0.0):
    result = farmanalysis.CSFExam(Appearance,Gram_Stain,float(Pressure),float(Protein),float(Glucose),float(WCC),float(Glucose_serum_ratio))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/AofSTdiseases/<RPR>/<VDRL>')
def index45(RPR,VDRL):
    SyphilisL=['RPR', 'VDRL']
    SyphilisL_User_Result={'RPR':RPR,'VDRL':VDRL}
    for i in range(0,len(SyphilisL_User_Result)) :
        if type(SyphilisL_User_Result.get(SyphilisL[i]))==str:     
            result = AofSTdiseases.SyphilisTests(RPR,VDRL)
            return json.dumps(result, ensure_ascii=False).encode('utf8')
        elif type(SyphilisL_User_Result.get(SyphilisL[i]))==float:
            result = AofSTdiseases.SyphilisTests2(float(RPR),float(VDRL))
            return json.dumps(result, ensure_ascii=False).encode('utf8')
        else:
            return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
        
@app.route('/AofSTdiseases/<HIV_AB_User_Result>')
def index46(HIV_AB_User_Result):
    if type(HIV_AB_User_Result)==str:     
        result = AofSTdiseases.AIDSTest(HIV_AB_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(HIV_AB_User_Result)==float:
        result = AofSTdiseases.AIDSTest2(float(HIV_AB_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
   
@app.route('/AofSTdiseases/<AbChlamydia_User_Result>')
def index47(AbChlamydia_User_Result):
    if type(AbChlamydia_User_Result)==str:     
        result = AofSTdiseases.ChlamydiaTest(AbChlamydia_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(AbChlamydia_User_Result)==float:
        result = AofSTdiseases.ChlamydiaTest2(float(AbChlamydia_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
   
@app.route('/AofSTdiseases/<HSV_User_Result>')
def index48(HSV_User_Result):
    if type(HSV_User_Result)==str:     
        result = AofSTdiseases.HerpesSimplexVirusTest(HSV_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(HSV_User_Result)==float:
        result = AofSTdiseases.HerpesSimplexVirusTest2(float(HSV_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
   
@app.route('/AofSTdiseases/<HBS_User_Result>')
def index49(HBS_User_Result):
    if type(HBS_User_Result)==str:     
        result = AofSTdiseases.HepatitisBBloodTests(HBS_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(HBS_User_Result)==float:
        result = AofSTdiseases.HepatitisBBloodTests2(float(HBS_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  



@app.route('/Tuberculosis/<TBS_User_Result>')
def index50(TBS_User_Result):
    if type(TBS_User_Result)==str:     
        result = Tuberculosis.TBTest(TBS_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(TBS_User_Result)==float:
        result = Tuberculosis.TBTest2(float(TBS_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  


@app.route('/ImmuneDiseases/<AN_User_Result>')
def index51(AN_User_Result):
    if type(AN_User_Result)==str:     
        result = ImmuneDiseases.AntinuclearAntibodyTest(AN_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(AN_User_Result)==float:
        result = ImmuneDiseases.AntinuclearAntibodyTest2(float(AN_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
   
@app.route('/ImmuneDiseases/<ASMA_User_Result>')
def index52(ASMA_User_Result):
    if type(ASMA_User_Result)==str:     
        result = ImmuneDiseases.AntiSmoothMuscleAntibodyTest(ASMA_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(ASMA_User_Result)==float:
        result = ImmuneDiseases.AntiSmoothMuscleAntibodyTest2(float(ASMA_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح" 
    
@app.route('/ImmuneDiseases/<AMA_User_Result>')
def index53(AMA_User_Result):
    if type(AMA_User_Result)==str:     
        result = ImmuneDiseases.AntiMitochondrialAntibodyTest(AMA_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(AMA_User_Result)==float:
        result = ImmuneDiseases.AntiMitochondrialAntibodyTest2(float(AMA_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
   
@app.route('/ImmuneDiseases/<ADNA_User_Result>')
def index54(ADNA_User_Result):
    if type(ADNA_User_Result)==str:     
        result = ImmuneDiseases.AntiDNATest(ADNA_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(ADNA_User_Result)==float:
        result = ImmuneDiseases.AntiDNATest2(float(ADNA_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
    
@app.route('/ImmuneDiseases/<ALKM_User_Result>')
def index55(ALKM_User_Result):
    if type(ALKM_User_Result)==str:     
        result = ImmuneDiseases.AntiliverkidneyMicrosomalTest(ALKM_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(ALKM_User_Result)==float:
        result = ImmuneDiseases.AntiliverkidneyMicrosomalTest2(float(ALKM_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
    
@app.route('/ImmuneDiseases/<ANCA_User_Result>')
def index56(ANCA_User_Result):
    if type(ANCA_User_Result)==str:     
        result = ImmuneDiseases.AntineutrophilCytoplasmicAntibodiesTest(ANCA_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(ANCA_User_Result)==float:
        result = ImmuneDiseases.AntineutrophilCytoplasmicAntibodiesTest2(float(ANCA_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
   
@app.route('/ImmuneDiseases/<AP_User_Result>')
def index57(AP_User_Result):
    if type(AP_User_Result)==str:     
        result = ImmuneDiseases.AntiPlateletABTest(AP_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(AP_User_Result)==float:
        result = ImmuneDiseases.AntiPlateletABTest2(float(AP_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
    
@app.route('/ImmuneDiseases/<AS_User_Result>')
def index58(AS_User_Result=0.0):
    result = ImmuneDiseases.AntiSpermABTest(float(AS_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ImmuneDiseases/<gender>/<C3>/<C4>')
def index59(gender='',C3=0.0,C4=0.0):
    result = ImmuneDiseases.ComplementSystemTest(gender,float(C3),float(C4))
    return json.dumps(result, ensure_ascii=False).encode('utf8')




@app.route('/SensitivityAnalyses/<food>/<IgE_Test>')
def index60(IgE_Test,food=''):
    if type(IgE_Test)==str:     
        result = SensitivityAnalyses.FoodpanelallergenspecificTest(food,IgE_Test)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(IgE_Test)==float:
        result = SensitivityAnalyses.FoodpanelallergenspecificTest2(food,float(IgE_Test))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
    



@app.route('/TumorsTest/<status>/<CEA_User_Result>')
def index61(status='',CEA_User_Result=0.0):
    result = TumorsTest.CEABreastTest(status,float(CEA_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<CEA_U_O_User_Result>')
def index62(CEA_U_O_User_Result=0.0):
    result = TumorsTest.CEAUterus_OvariesTest(float(CEA_U_O_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<TG_User_Result>')
def index63(TG_User_Result=0.0):
    result = TumorsTest.ThyroidGlandTest(float(TG_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<PG_User_Result>/<status>')
def index64(PG_User_Result=0.0,status=''):
    result = TumorsTest.PinealGlandTest(float(PG_User_Result),status)
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<AFP_User_Result>')
def index65(AFP_User_Result=0.0):
    result = TumorsTest.AlphaFetoproteinTest(float(AFP_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<Renin_User_Result>')
def index66(Renin_User_Result=0.0):
    result = TumorsTest.KidneyTest(float(Renin_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<Erythropoitein_User_Result>')
def index67(Erythropoitein_User_Result=0.0):
    result = TumorsTest.TestisTest(float(Erythropoitein_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<PSA_User_Result>')
def index68(PSA_User_Result=0.0):
    result = TumorsTest.ProstateTest(float(PSA_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<CA19_User_Result>')
def index69(CA19_User_Result=0.0):
    result = TumorsTest.DigestiveTest(float(CA19_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/TumorsTest/<LCT_User_Result>')
def index70(LCT_User_Result):
    if type(LCT_User_Result)==str:     
        result = TumorsTest.LungCancerTumorMarkersTest(LCT_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(LCT_User_Result)==float:
        result = TumorsTest.LungCancerTumorMarkersTest2(float(LCT_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"  
    
@app.route('/TumorsTest/<B_User_Result>')
def index71(B_User_Result):
    if type(B_User_Result)==str:     
        result = TumorsTest.BladderTest(B_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(B_User_Result)==float:
        result = TumorsTest.BladderTest2(float(B_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"



@app.route('/DawnTest/<DS_User_Result>')
def index72(DS_User_Result):
    if type(DS_User_Result)==str:     
        result = DawnTest.DawnSyndromeTest(DS_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(DS_User_Result)==float:
        result = DawnTest.DawnSyndromeTest2(float(DS_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"
   
@app.route('/DawnTest/<AF_User_Result>')
def index73(AF_User_Result=0.0):
    result = DawnTest.AlphaFetoproteinTest(float(AF_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/AIDSTest/<HIVAb_User_Result>')
def index74(HIVAb_User_Result):
    if type(HIVAb_User_Result)==str:     
        result = AIDSTest.HumanImmunodeficiencyVirusAntibodiesTest(HIVAb_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(HIVAb_User_Result)==float:
        result = AIDSTest.HumanImmunodeficiencyVirusAntibodiesTest2(float(HIVAb_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"

@app.route('/AIDSTest/<HIVPCR_User_Result>')        
def index75(HIVPCR_User_Result=0.0):
    result = AIDSTest.HIVbyPCRTest(float(HIVPCR_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/RiskEvaluationProfile/<Cholesterol>/<Triglyceride>/<HDL_C>/<LDL_C>')
def inde76(Cholesterol=0.0,Triglyceride=0.0,HDL_C=0.0,LDL_C=0.0):
    result = RiskEvaluationProfile.LipidProfile(float(Cholesterol),float(Triglyceride),float(HDL_C),float(LDL_C))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/RiskEvaluationProfile/<H_User_Result>')
def index77(H_User_Result=0.0):
    result = RiskEvaluationProfile.HomocysteineTest(float(H_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/RiskEvaluationProfile/<AF_User_Result>')
def index78(AF_User_Result=0.0):
    result = RiskEvaluationProfile.ActivatedfactorXIITest(float(AF_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/RiskEvaluationProfile/<SE_User_Result>')
def index79(SE_User_Result=0.0):
    result = RiskEvaluationProfile.SerumFibrinogenTest(float(SE_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/RiskEvaluationProfile/<HRCRP_User_Result>')
def index80(HRCRP_User_Result=0.0):
    result = RiskEvaluationProfile.HighSensitivityCReactiveProteinTest(float(HRCRP_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')



@app.route('/ThromboticRiskProfile/<PC_User_Result>')
def index81(PC_User_Result=0.0):
    result = ThromboticRiskProfile.PlateletCountTest(float(PC_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<PT_User_Result>')
def index82(PT_User_Result=0.0):
    result = ThromboticRiskProfile.ProthrombinTimeTest(float(PT_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<FV_User_Result>')
def index83(FV_User_Result=0.0):
    result = ThromboticRiskProfile.PCRFactorVbyPCRTest(float(FV_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<PTT_User_Result>')
def index84(PTT_User_Result=0.0):
    result = ThromboticRiskProfile.PartialThromboplastinTimeTest(float(PTT_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<TT_User_Result>')
def index85(TT_User_Result=0.0):
    result = ThromboticRiskProfile.ThrombinTimeTest(float(TT_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<AT_User_Result>')
def index86(AT_User_Result=0.0):
    result = ThromboticRiskProfile.AntiThrombinTest(float(AT_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<PC_User_Result>')
def index87(PC_User_Result=0.0):
    result = ThromboticRiskProfile.ProteinCTest(float(PC_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<PS_User_Result>')
def index88(PS_User_Result=0.0):
    result = ThromboticRiskProfile.ProteinSTest(float(PS_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<FDPs_User_Result>')
def index89(FDPs_User_Result=0.0):
    result = ThromboticRiskProfile.FibrinDegradationProductsTest(float(FDPs_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<SF_User_Result>')
def index90(SF_User_Result=0.0):
    result = ThromboticRiskProfile.SerumFibrinogenTest(float(SF_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

@app.route('/ThromboticRiskProfile/<LA_User_Result>')
def index91(LA_User_Result):
    if type(LA_User_Result)==str:     
        result = ThromboticRiskProfile.LupusAnticoagulantTest(LA_User_Result)
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    elif type(LA_User_Result)==float:
        result = ThromboticRiskProfile.LupusAnticoagulantTest2(float(LA_User_Result))
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "من فضلك تاكد من ادخال النتائج بشكل صحيح"
   
@app.route('/ThromboticRiskProfile/<ACAb_User_Result>')
def index92(ACAb_User_Result=0.0):
    result = ThromboticRiskProfile.AntiCardiolipinAbsTest(float(ACAb_User_Result))
    return json.dumps(result, ensure_ascii=False).encode('utf8')

app.run(port=7171)