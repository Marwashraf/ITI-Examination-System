import numpy as np

class CMEAnalyzes(): 
        def LiverFunctionTest(ALt_SGPT=0.0,AST_SGOT=0.0):
            LFT=['ALt_SGPT','AST_SGOT']
            LFT_User_Result={'ALt_SGPT':ALt_SGPT,'AST_SGOT':AST_SGOT}
            resultList=[]              
            liverFunctionTest ={'ALt_SGPT': np.around(np.arange(7,65.1,0.01),2) , 
                            'AST_SGOT': np.around(np.arange(5,40.1,0.01),2)}       
            liverFunctionTest_inarabic={'ALt_SGPT':' إنزيم ناقلة أمين الألانيإنزيم موجود في الكبد يساعد في تحويل البروتينات إلى طاقة لخلايا الكبد',
                                      'AST_SGOT':'إنزيم ناقلة أمين الأسبارتات هو إنزيم يساعد في استقلاب الأحماض الأمينية '}            
            for i in range(0,len(LFT)):
                if(LFT_User_Result[LFT[i]] in liverFunctionTest[LFT[i]]):
                    resultList.append((LFT[i],"نسبة التحليل طبيعية",liverFunctionTest_inarabic.get(LFT[i])))
                else:
                    resultList.append((LFT[i],"نسبة التحليل غير طبيعية",liverFunctionTest_inarabic.get(LFT[i])))
            return resultList
                                
        def CompleteBloodPicture(gender='',Haemoglobin=0.0,Haematocrit_PCV=0.0,RBCs_Count=0.0,MCV=0.0,MCH=0.0,MCHC=0.0,RDW_CV=0.0,
            Platelet_Count_EDTA_Blood=0.0,Total_Leucocytic_Count_EDTA_Blood=0.0,Neutrophils=0.0,Staff=0.0,Segmented=0.0,
            Lymphocytes=0.0,Monocytes=0.0,Eosinophils=0.0,Basophils=0.0):
            CBC=['Haemoglobin','Haematocrit_PCV','RBCs_Count','MCV','MCH','MCHC','RDW_CV',
                'Platelet_Count_EDTA_Blood','Total_Leucocytic_Count_EDTA_Blood','Neutrophils','Staff','Segmented',
                'Lymphocytes','Monocytes','Eosinophils','Basophils']
            CBC_User_Result ={'Haemoglobin':Haemoglobin,'Haematocrit_PCV':Haematocrit_PCV,'RBCs_Count':RBCs_Count,
                              'MCV':MCV,'MCH':MCH,'MCHC':MCHC,'RDW_CV':RDW_CV,'Platelet_Count_EDTA_Blood':Platelet_Count_EDTA_Blood,
                              'Total_Leucocytic_Count_EDTA_Blood':Total_Leucocytic_Count_EDTA_Blood,'Neutrophils':Neutrophils,'Staff':Staff,
                              'Segmented':Segmented,'Lymphocytes':Lymphocytes,'Monocytes':Monocytes,'Eosinophils':Eosinophils,'Basophils':Basophils}
            resultList=[]
            if gender=='f':
                HemoglobinN=np.round(np.arange(11.6,15.1,0.01),2)
                RBCsN=np.round(np.arange(3.92,5.14,0.001),3)
                HematocritN=np.round(np.arange(35.5,45,0.01),2)
                PlateletcountN=np.round(np.arange(157,371.1,0.01),2)
            elif gender=='m':
                HemoglobinN=np.round(np.arange(13.2 ,16.7,0.01),2)
                RBCsN=np.round(np.arange(4.35,5.57,0.01),2)
                HematocritN=np.round(np.arange(38.3,48.1,0.01),2)
                PlateletcountN=np.round(np.arange(135,371.1,0.01),2)
            else:
                resultList.append("من فضلك تاكد من ادخال البيانات بشكل صحيح")
            CBC_Test={'Haemoglobin':HemoglobinN,'Haematocrit_PCV':HematocritN,'RBCs_Count':RBCsN,'MCV':np.round(np.arange(80,100.1,0.01),2),
                          'MCH':np.round(np.arange(27,33.1,0.01),2),'MCHC':np.round(np.arange(31,37.1,0.01),2),
                      'RDW_CV':np.round(np.arange(11.5,15.1,0.01),2),'Platelet_Count_EDTA_Blood':PlateletcountN,
                      'Total_Leucocytic_Count_EDTA_Blood':np.round(np.arange(4,11.1,0.01),2),
                      'Neutrophils':np.round(np.arange(2,7.1,0.01),2),
                      'Staff':np.round(np.arange(0,CBC_User_Result[CBC[10]]+0.1,0.01),2),
                      'Segmented':np.round(np.arange(0,CBC_User_Result[CBC[11]]+0.1,0.01),2),'Lymphocytes':np.round(np.arange(1,4.1,0.01),2),
                      'Monocytes':np.round(np.arange(0.2,2,0.01),2),'Eosinophils':np.round(np.arange(0.1,0.46,0.01),2),'Basophils':np.round(np.arange(0,0.2,0.01),2)}

            CBC_Test_inarabic={'Haemoglobin':'الهيموغلوبين يقيس اختبار الهيموغلوبين نسبة الهيموغلوبين في الدم. الهيموغلوبين عبارة عن بروتين في خلايا الدم الحمراء التي تحمل الأكسجين إلى أعضاء الجسم',
                               'Haematocrit_PCV':'الهيماتوكريت للمساعدة في تشخيص اضطرابات الدم مثل كثرة الكريات الحمراء الحقيقية',
                               'RBCs_Count':'تعداد خلايا الدم الحمراء',
                               'MCV':'تحليل متوسط حجم كريات الدم',
                               'MCH': 'متوسط نسبة الهيموجلوبين هو تحليل للدم لمعرفة متوسط نسبة الهيموجلوبين فيه عن طريق حساب متوسط كتلة الهيموجلوبين في كرات الدم الحمراء كلاً على حده في عينة الدم. ويعد هذا التحليل مؤشراً هاماً على مستوى الحديد في الدم والذي يعطي كرات الدم الحمراء لونها المميز ',
                               'MCHC':' مقياس لتركيز الهيموغلوبين في حجم معين من خلايا الدم الحمراء',
                               'RDW_CV':' لقياس مدى تشتت أحجام كريات الدم الحمراء و توزيع كريات الدم الحمراء ',
                              'Platelet_Count_EDTA_Blood':'تعداد الصفيحات الدموية وهي أجزاء صغيرة من الخلايا، وتعد ضرورية لتخثر الدم الطبيعي',
                               'Total_Leucocytic_Count_EDTA_Blood':' تحليل عدد كريات الدم البيضاء وهي خلايا الدم التي تساعد الجسم على مكافحة العدوى والأمراض',
                               'Neutrophils':'خلايا العدلات يقوم بتحديد مستوى العدلات في الدم نسبة لإجمالي عدد كريات الدم البيضاء في الدم. إن العدلات هي أكثر أنواع خلايا الدم البيضاء المتواجدة في الدم، والتي يتم انتاجها في نخاع العظم ومن ثم تدخل إلى مجرى الدم من أجل القيام بوظيفتها',
                               'Staff':'يستخدم تحليل نسبة العدلات المجزأة من أجل الكشف عن الإصابة بمجموعة متنوعة من الاضطرابات، بما في ذلك العدوى، وفقر الدم، وأمراض الجهاز المناعي، وسرطانات الدم',
                               'Segmented':'إن العدلات هي نوع من خلايا الدم البيضاء والتي وظيفتها الأساسية هي حماية الجسم من العدوى',
                              'Lymphocytes':'الخلايا اللمفاوية هي إحدى أنواع خلايا الدم البيضاء المتواجدة في الدم، والتي تعد من الخلايا المناعية الرئيسية في الجسم، حيث أنها تعمل إلى جانب خلايا جهاز المناعة الأخرى من أجل حماية الجسم من مختلف أنواع الأمراض. يتم انتاج الخلايا الليمفاوية في نخاع العظم ومن ثم تدخل إلى مجرى الدم لتتواجد فيه وفي الأنسجة الليمفاوية',
                               'Monocytes':' خلايا الحيدات تقوم بتحديد نسبة الوحيدات في الدم، وهي احدى أنواع خلايا الدم البيضاء يتم انتاجها في نخاع العظم ومن ثم تدخل إلى مجرى الدم من أجل القيام بوظيفتها، ألا وهي محاربة بعض أنواع العدوى ومساعدة خلايا الدم البيضاء الأخرى على إزالة الخلايا الميتة أو التالفة ومحاربة الخلايا السرطانية',
                               'Eosinophils':'كثرة الحمضات هو الزيادة غير الطبيعية لمستوى الحمضات في الدم، وتعرف الحمضات بأنها نوع من خلايا الدم البيضاء التي تكافح المواد المسببة للأمراض في الجسم، مثل الطفيليات، ولها دور في تفاعلات الحساسية.',
                               'Basophils':' خلايا قاعدية يقوم بتحديد نسبة خلايا الدم البيضاء القاعدية في الدم، وهي احدى أنواع خلايا الدم البيضاء يتم انتاجها في نخاع العظم ومن ثم تدخل إلى مجرى الدم من أجل القيام بوظيفتها، ألا وهي الحفاظ على وظيفة جهاز المناعة'}
            for i in range(0,len(CBC)):
                if(CBC_User_Result[CBC[i]] in CBC_Test[CBC[i]]):
                    resultList.append((CBC[i],"نسبة التحليل طبيعية",CBC_Test_inarabic.get(CBC[i])))
                else:
                    resultList.append((CBC[i],"نسبة التحليل غير طبيعية",CBC_Test_inarabic.get(CBC[i])))
            return resultList

        def KidneyFunctionTest(gender='',Serum_Creatinine=0.0,Serum_Uric_Acid=0.0):
            KF=['Serum_Creatinine','Serum_Uric_Acid']
            KF_User_Result={'Serum_Creatinine':Serum_Creatinine,'Serum_Uric_Acid':Serum_Uric_Acid}
            resultList=[]
            if gender == 'f':
                SerumCreatinine=np.round(np.arange(0.59,1.05,0.01),2)
                SerumUricAcid=np.round(np.arange(2.7,7.4,0.01),2)
            elif gender =='m':
                Creatinine=np.round(np.arange(0.74 ,1.36,0.01),2)
                SerumUricAcid=np.round(np.arange(4.0,8.6,0.01),2)
            else:
                print("choose please between f and m ")
            KF_Test={'Serum_Creatinine':SerumCreatinine,'Serum_Uric_Acid':SerumUricAcid}
            KF_Test_inarabic={'Serum_Creatinine':' الكرياتينين في الدم  قياس لمدى كفاءة كليتيك في أداء وظيفتهما في ترشيح الفضلات من دمك',
                              'Serum_Uric_Acid':'مصل حمض اليوريك هو مادة كيميائية تنتج عندما يقوم الجسم بتكسير مواد تسمى البيورينات'}
            for i in range(0,len(KF)):
                if(KF_User_Result[KF[i]] in KF_Test[KF[i]]):
                    resultList.append((KF[i],"نسبة التحليل طبيعية",KF_Test_inarabic.get(KF[i])))
                else:
                    resultList.append((KF[i],"نسبة التحليل غير طبيعية",KF_Test_inarabic.get(KF[i])))
            return resultList

        def FastingBloodSuger(FBS=0.0):
            resultList=[]
            Diabetes=np.round(FBS,2)>7.0
            if Diabetes==True:
                Diabetes=True
            FBS_Tests={'FBS Normal':np.round(np.arange(3.9,5.6,0.01),2),
                       'FBS Prediabetes':np.around(np.arange(5.5,7.1,0.01),2),
                       'Diabetes':True}
            if FBS in FBS_Tests['FBS Normal']:
                     resultList.append(('نسبة السكر طبيعية','FBS Normal'))
            elif(FBS in FBS_Tests['FBS Prediabetes']):
                resultList.append(('نسبتك من المحتمل بنسبة كبيرة الاصابة بداء السكري بسبب ارتفاع في نسبة السكرعن المستوي الطبيعي','FBS Prediabetes'))
            elif Diabetes==True:
                resultList.append(('حسب نسبة تحليلك فالاحتمال الاكبر انك مصاب بداء السكري تواصل مع الطبيب لوضع خطة العلاج'))
            else:
                resultList.append(('هناك خطأ في النسبة المدخلة فليست من ضمن النسب الطبيعية للسكر والتي لا تقل عن 3.9 '))
            return resultList

        def ESR(gender='',First_Hours=0.0,Second_Hours=0.0):
            ESR=['First_Hours','Second_Hours']
            ESR_User_Result={'First_Hours':First_Hours,'Second_Hours':Second_Hours}
            resultList=[]
            if gender == 'f':
                ESRN=np.round(np.arange(0,29.1,0.01),2)
                FirstHoursN=np.round(np.arange(7,12.1,0.01),2)
                SecondHoursN=np.round(np.arange(12,17.1,0.01),2)
            elif gender=='m':
                ESR=np.round(np.arange(0,22.1,0.01),2)
                FirstHours=np.round(np.arange(3,7.1,0.01),2)
                SecondHours=np.round(np.arange(7,15.1,0.01),2) 
            else:
                resultList.append(("تاكد من اختيار النوع"))
            ESR_test={'First_Hours':FirstHoursN,'Second_Hours':SecondHoursN}
            ESR_test_inarabic={'First_Hours':' معدل الترسيب في الساعة الاولي  ','Second_Hours':' معدل الترسيب في الساعة الثانية'}
            for i in range(0,len(ESR)):
                if ESR_User_Result[ESR[i]] in ESR_test[ESR[i]]:
                    resultList.append((ESR[i],"نسبة معدل الترسيب أو سرعة تثفّل كرات الدم الحمراء طبيعية و هو أحد تحاليل الدم الذي يكشف عن وجود عدوى نشطة في الجسم",ESR_test_inarabic.get(ESR[i])))
                else:
                     resultList.append((ESR[i],"نسبة معدل الترسيب أو سرعة تثفّل كرات الدم الحمراء غير طبيعية و هو أحد تحاليل الدم الذي يكشف عن وجود عدوى نشطة في الجسم",ESR_test_inarabic.get(ESR[i])))
            return resultList

        def UricAcidTest(gender='',UA=0.0):
            resultList=[]
            if gender=='f':
                UricAcidN=np.round(np.arange(2.7,7.4,0.01),2)
                if UA in UricAcidN:
                    resultList.append(('نسبة املاح النقرص طبيعية إن تحليل حمض اليوريك في الدم هو تحليل يقيس كمية حمض اليوريك في الدم، أو حمض البوليك في الدم. ينتج حمض اليوريك عند تكسر البيورينات، والتي تنتج عندما تتقدم الخلايا في العمر وتموت، أو نتيجة تناول بعض أنواع الأطعمة مثل الفاصوليا والبازلاء، والكبد، وبعض أنواع المشروبات الكحولية'))
                else:
                    resultList.append(('نسبة املاح النقرص غير طبيعية إن تحليل حمض اليوريك في الدم هو تحليل يقيس كمية حمض اليوريك في الدم، أو حمض البوليك في الدم. ينتج حمض اليوريك عند تكسر البيورينات، والتي تنتج عندما تتقدم الخلايا في العمر وتموت، أو نتيجة تناول بعض أنواع الأطعمة مثل الفاصوليا والبازلاء، والكبد، وبعض أنواع المشروبات الكحولية'))
            elif gender=='m':
                UricAcidN=np.round(np.arange(4,8.6,0.01),2)
                if UA in UricAcidN:
                    resultList.append(('نسبة املاح النقرص طبيعية إن تحليل حمض اليوريك في الدم هو تحليل يقيس كمية حمض اليوريك في الدم، أو حمض البوليك في الدم. ينتج حمض اليوريك عند تكسر البيورينات، والتي تنتج عندما تتقدم الخلايا في العمر وتموت، أو نتيجة تناول بعض أنواع الأطعمة مثل الفاصوليا والبازلاء، والكبد، وبعض أنواع المشروبات الكحولية'))
                else:
                    resultList.append(('نسبة املاح النقرص غير طبيعية إن تحليل حمض اليوريك في الدم هو تحليل يقيس كمية حمض اليوريك في الدم، أو حمض البوليك في الدم. ينتج حمض اليوريك عند تكسر البيورينات، والتي تنتج عندما تتقدم الخلايا في العمر وتموت، أو نتيجة تناول بعض أنواع الأطعمة مثل الفاصوليا والبازلاء، والكبد، وبعض أنواع المشروبات الكحولية'))
            else:
                resultList.append(('تاكد من اختيار النوع'))
            return resultList 
        
        def UrineTest(Colour='',Aspect='',Nitrite='',Albumin='',Suger='',Acetone='',Bile_Salts='',Bile_Pigments='',
             Urobilinogen='',Leukocyte_estrease='',Epithelial_Cells='', Casts='',Mucus='',Ova='',
                  Crystals='',Yeast_Cells='',Trichomonas_vaginalis='',Volume=0.0,Reaction=0.0,
                  Specific_Gravity_in_urine=0.0,RBCs=0.0,Pus_Cells=0.0):
            UR1=['Colour','Aspect','Nitrite','Albumin','Suger','Acetone','Bile_Salts','Bile_Pigments',
                 'Urobilinogen','Leukocyte_estrease','Epithelial_Cells', 'Casts','Mucus','Ova','Crystals','Yeast_Cells','Trichomonas_vaginalis']                        
            UR2=['Volume','Reaction','Specific_Gravity_in_urine','RBCs','Pus_Cells']
            UR1_User_Result={'Colour':Colour,'Aspect':Aspect,'Nitrite':Nitrite,'Albumin':Albumin,'Suger':Suger,'Acetone':Acetone,
                             'Bile_Salts':Bile_Salts,'Bile_Pigments':Bile_Pigments,'Urobilinogen':Urobilinogen,
                             'Leukocyte_estrease':Leukocyte_estrease,'Epithelial_Cells':Epithelial_Cells,'Casts':Casts,
                             'Mucus':Mucus,'Ova':Ova,'Crystals':Crystals,'Yeast_Cells':Yeast_Cells,'Trichomonas_vaginalis':Trichomonas_vaginalis }
            UR2_User_Result={'Volume':Volume,'Reaction':Reaction,'Specific_Gravity_in_urine':Specific_Gravity_in_urine,'RBCs':RBCs,'Pus_Cells':Pus_Cells}
            resultList = []
            Urine_Test={'Colour':'yellow','Aspect':'clear','Volume':np.round(np.arange(0,1.6,0.01),2),
                'Reaction':np.round(np.arange(4,8.1,0.01),1),
                'Specific_Gravity_in_urine':np.round(np.arange(1.005,1.026,0.001),3),
               'Nitrite':'negative','Albumin':'negative','Suger':'negative','Acetone':'negative',
               'Bile_Salts':'negative','Bile_Pigments':'negative','Urobilinogen':'normal trace',
               'Leukocyte_estrease':'negative','RBCs':np.round(np.arange(0,1.1,0.01),2),
                'Pus_Cells':np.round(np.arange(0,1.1,0.01),2),'Epithelial_Cells':'nil',
                'Casts':'nil','Ova':'nil','Crystals':'nil','Mucus':'nil','Yeast_Cells':'nil','Trichomonas_vaginalis':'nil'}
            Urine_Test_inarabic={'Colour':'اللون','Aspect':'المظهر','Volume':'الحجم','Reaction':'درجة حموضة البول يشير قياس درجة الحموضة إلى كمية الحمض الموجودة في البول',
                                 'Specific_Gravity_in_urine':'الثقل النوعي','Nitrite':'النتريت',
                            'Albumin':'البيليروبين','Suger':'الجلوكوز','Acetone':'الكيتونات','Bile_Salts':'املاح',
                                 'Bile_Pigments':'الاصباغ','Urobilinogen':' البيليروبين ينتج عن  تكسر خلايا الدم الحمراء',
                            'Leukocyte_estrease':'دلائل العدوى','RBCs':'الدم','Pus_Cells':'خلايا صديد',
                                 'Epithelial_Cells':'الخلايا الطهارية خلايا مختلطة بالبول',
                            'Casts':'الأسطوانات وهي بروتينات التي تشبه الأنابيب','Ova':'بويضات','Crystals':'البلورات التي تتكوّن من المواد الكيميائية في البول',
                                 'Mucus':'مخاط','Yeast_Cells':'خلايا فطرية','Trichomonas_vaginalis':'المشعرات المهبلية'}
            for i in range(0,len(UR2)):
                if(UR2_User_Result[UR2[i]] in Urine_Test[UR2[i]]):
                    resultList.append((UR2[i],"نسبة التحليل طبيعية",Urine_Test_inarabic.get(UR2[i])))
                else:
                    resultList.append((UR2[i],"نسبة التحليل غير طبيعية",Urine_Test_inarabic.get(UR2[i])))

            for i in range(0,len(UR1)):
                if(UR1_User_Result[UR1[i]] == Urine_Test[UR1[i]]):
                    resultList.append((UR1[i],"نسبة التحليل طبيعية",Urine_Test_inarabic.get(UR1[i])))
                else:
                    resultList.append((UR1[i],"نسبة التحليل غير طبيعية",Urine_Test_inarabic.get(UR1[i])))
            return resultList

        def LipidProfile(Cholesterol=0.0,Triglyceride=0.0,HDL_C=0.0,LDL_C=0.0):
            LP=['Cholesterol','Triglyceride','HDL_C','LDL_C']
            LP_User_Result={'Cholesterol':Cholesterol,'Triglyceride':Triglyceride,'HDL_C':HDL_C,'LDL_C':LDL_C}
            resultList=[]
            LP_Test={'Cholesterol':np.round(np.arange(150,200.1,0.01),2),
                     'Triglyceride':np.round(np.arange(30,150.1,0.01),2),
                     'HDL_C':np.round(np.arange(40,60.1,0.01),2),
                     'LDL_C':np.round(np.arange(0,150.1,0.01),2)}
            LP_Test_inarabic={'Cholesterol':'الكوليسترول مادة ستيرويدية ضرورية لحياة الأفراد، وتدخل في تركيب أنسجة وأعضاء الجسم، والأحماض الصفراوية الضرورية لامتصاص المواد المغذية من الطعام ، كما تدخل في تركيب هرمونات الجسم الضرورية للنمو والتكاثر',
                              'Triglyceride':'الدهون الثلاثية وهي نوع من الدهون في الدم يستخدمه الجسم للحصول على الطاقة.',
                              'LDL_C':' كوليسترول البروتين الدهني منخفض الكثافة الكوليسترول (الخبيث)',
                              'HDL_C':'كوليسترول البروتين الدهني عالي الكثافة الكوليسترول (الحميد)'}
            for i in range(0,len(LP)):
                if(LP_User_Result[LP[i]] in LP_Test[LP[i]]):
                    resultList.append((LP[i],"نسبة التحليل طبيعية",LP_Test_inarabic.get(LP[i])))
                else:
                    resultList.append((LP[i],"نسبة التحليل غير طبيعية",LP_Test_inarabic.get(LP[i])))
            return resultList


class DiabetesAnalyzes:
    def FastingBloodSuger(FBS=0.0):
        resultList=[]
        Diabetes=np.round(FBS,2)>7.0
        if Diabetes==True:
            Diabetes=True
        FBS_Tests={'FBS Normal':np.round(np.arange(3.9,5.6,0.01),2),
                   'FBS Prediabetes':np.around(np.arange(5.5,7.1,0.01),2),
                   'Diabetes':True}
        if FBS in FBS_Tests['FBS Normal']:
                 resultList.append(('نسبة السكر طبيعية','FBS Normal'))
        elif(FBS in FBS_Tests['FBS Prediabetes']):
            resultList.append(('نسبتك من المحتمل بنسبة كبيرة الاصابة بداء السكري بسبب ارتفاع في نسبة السكرعن المستوي الطبيعي','FBS Prediabetes'))
        elif Diabetes==True:
            resultList.append(('حسب نسبة تحليلك فالاحتمال الاكبر انك مصاب بداء السكري تواصل مع الطبيب لوضع خطة العلاج'))
        else:
            resultList.append(('هناك خطأ في النسبة المدخلة فليست من ضمن النسب الطبيعية للسكر والتي لا تقل عن 3.9 '))
        return resultList
    
    def DiabeticProfile(Fasting_Blood_Glucose=0.0,Glucose_After_2_Hours=0.0,Haemoglobin_A1C=0.0):
        DP=['Fasting_Blood_Glucose','Glucose_After_2_Hours','Haemoglobin_A1C']
        DP_User_Result={'Fasting_Blood_Glucose':Fasting_Blood_Glucose,'Glucose_After_2_Hours':Glucose_After_2_Hours,
                        'Haemoglobin_A1C':Haemoglobin_A1C}
        resultList=[]
        DP_Tests={'Fasting Blood Glucose':np.round(np.arange(70,110.1,0.01),2),
                  'Glucose After 2 Hours Normal':np.round(np.arange(70,139.1,0.01),2),
              'Glucose After 2 Hours Prediabetes':np.round(np.arange(140,199.1,0.01),2),
                  'Glucose After 2 Hours Diabetes':DP_User_Result[DP[1]]>200,
             'Haemoglobin A1C Normal':DP_User_Result[DP[2]]<5.7,
                  'Haemoglobin A1C Prediabetes':np.round(np.arange(140,199.1,0.01),2),
              'Haemoglobin A1C Normal Diabetes':DP_User_Result[DP[2]]>200}
        for i in range(0,len(DP)):
            if DP[i]=='Fasting_Blood_Glucose':
                if DP_User_Result[DP[i]] in DP_Tests['Fasting Blood Glucose']:
                    resultList.append(('Fasting Blood Glucose',"نسبة الجلوكوز طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز"))
                else:
                    resultList.append(('Fasting Blood Glucose','نسبة الجلوكوز غير طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز'))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))

            if DP[i]=='Glucose_After_2_Hours':
                if DP_User_Result[DP[i]] in DP_Tests['Glucose After 2 Hours Normal']:
                    resultList.append(('Glucose After 2 Hours Normal',"نسبة الجلوكوز بعد ساعتان طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز"))
                elif(DP_User_Result[DP[i]] in DP_Tests['Glucose After 2 Hours Prediabetes']):
                    resultList.append(('Glucose After 2 Hours Prediabetes','من المحتمل بنسبة كبيرة الاصابة بمرض السكري بسبب ارتفاع في نسبة الجلوكوز بعد ساعتان عن المستوي الطبيعي '))
                elif DP_Tests['Glucose After 2 Hours Diabetes']==True:
                    resultList.append(('Glucose After 2 Hours Diabetes','حسب نسبة تحليلك فالاحتمال الاكبر انك مصاب بمرض السكري تواصل مع الطبيب لوضع خطة العلاج'))
                else:
                    resultList.append(('نسبة الجلوكوز غير طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز'))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))

            if DP[i] =='Haemoglobin_A1C':
                if DP_Tests['Haemoglobin A1C Normal']==True:
                    resultList.append(('Haemoglobin A1C Normal',"نسبة الهيموغلوبين المسكر طبيعية وهو اتحاد سكر الدم مع بروتين الهيموجلوبين المكون الأساسي لكريات الدم الحمراء"))
                elif(DP_User_Result[DP[i]] in DP_Tests['Haemoglobin A1C Prediabetes']):
                    resultList.append(('Haemoglobin A1C Prediabetes',' نسبتك من المحتمل بنسبة كبيرة الاصابة بداء السكري بسبب ارتفاع في نسبة الهيموغلوبين المسكرعن المستوي الطبيعي وهو اتحاد سكر الدم مع بروتين الهيموجلوبين المكون الأساسي لكريات الدم الحمراء'))
                else:
                    resultList.append(('Haemoglobin A1C Normal Diabetes',"حسب نسبة تحليلك فالاحتمال الاكبر انك مصاب بداء السكري تواصل مع الطبيب لوضع خطة العلاج "))
        else:
            resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))
        return resultList

    def GlucoseCurve(state='',Fasting_Blood_Glucose=0.0,Glucose_After_30_min=0.0,Glucose_After_1_Hour=0.0,
                     Glucose_After_2_Hours=0.0,Glucose_After_3_Hours=0.0):
        GC=['Fasting_Blood_Glucose','Glucose_After_30_min','Glucose_After_1_Hour','Glucose_After_2_Hours','Glucose_After_3_Hours']
        GC_User_Result={'Fasting_Blood_Glucose':Fasting_Blood_Glucose,'Glucose_After_30_min':Glucose_After_30_min,
                        'Glucose_After_1_Hour':Glucose_After_1_Hour,'Glucose_After_2_Hours':Glucose_After_2_Hours,
                        'Glucose_After_3_Hours':Glucose_After_3_Hours}
        resultList=[]
        GC_Tests={'Fasting Blood Glucose':np.round(np.arange(70,110.1,0.01),2),
          'Glucose After 30 min':np.round(np.arange(110,170.1,0.01),2),
          'Glucose After 1 Hour Male ':np.round(np.arange(120,170.1,0.01),2),
          'Glucose After 1 Hour Non pregnant':np.round(np.arange(120,170.1,0.01),2),
            'Glucose After 1 Hour pregnant':np.round(np.arange(120,190.1,0.01),2),
          'Glucose After 2 Hours Normal':np.round(np.arange(70,139.1,0.01),2),
          'Glucose After 2 Hours Prediabetes':np.round(np.arange(140,199.1,0.01),2),
            'Glucose After 2 Hours  Diabetes':GC_User_Result[GC[3]]>200,
          'Glucose After 3 Hours Normal':np.round(np.arange(70,139.1,0.01),2),
          'Glucose After 3 Hours Prediabetes':np.round(np.arange(140,199.1,0.01),2),
                 'Glucose After 3 Hours Diabetes':GC_User_Result[ GC[4]]>200}
        for i in range(0,len(GC)):
            if GC[i]=='Fasting_Blood_Glucose':
                if GC_User_Result[GC[i]] in GC_Tests['Fasting Blood Glucose']:
                    resultList.append(('Fasting Blood Glucose','نسبة الجلوكوز طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز'))
                else:
                    resultList.append(('Fasting Blood Glucose','نسبة الجلوكوز غير طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز'))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))
            if GC[i]=='Glucose_After_30_min' :
                if GC_User_Result[GC[i]] in GC_Tests['Glucose After 30 min']:
                        resultList.append(('Glucose After 30 min','نسبة الجلوكوز بعد ثلاثون دقيقة طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز'))
                else:
                    resultList.append(('Glucose After 30 min',"نسبة التحليل طبيعية",'نسبة الجلوكوز بعد ثلاثون دقيقة غير طبيعية وهو قدرة خلايا الجسم مثل العضلات والدهون على امتصاص السكر من الدم بعد تناول كمية معينة من السكر أو الجلوكوز'))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))

            if GC[i]=='Glucose_After_1_Hour':
                if state=='non pregnant' or state=='male':
                    if GC_User_Result[GC[i]] in GC_Tests['Glucose After 1 Hour Non pregnant']:
                        resultList.append(('Glucose After 1 Hours','نسبة الجلوكوزبعد ساعة طبيعية وهو نوع من أنواع السكريّات البسيطة'))
                    else:
                        resultList.append(('Glucose After 1 Hours','نسبة الجلوكوز بعد ساعة غير طبيعية وهو نوع من أنواع السكريّات البسيطة'))
                elif state=='pregnant' :
                    if GC_User_Result[GC[i]] in GC_Tests['Glucose After 1 Hour pregnant']:
                        resultList.append(('Glucose After 1 Hours','نسبة الجلوكوز بعد ساعة طبيعية وهو نوع من أنواع السكريّات البسيطة'))
                    else:
                        resultList.append(('Glucose After 1 Hours','نسبة الجلوكوز بعد ساعة غير طبيعية وهو نوع من أنواع السكريّات البسيطة'))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))
            if GC[i]=='Glucose_After_2_Hours':
                if GC_User_Result[GC[i]] in GC_Tests['Glucose After 2 Hours Normal']:
                    resultList.append(('Glucose After 2 Hours Normal','نسبة الجلوكوز بعد ساعتان طبيعية وهو نوع من أنواع السكريّات البسيطة'))
                elif GC_User_Result[GC[i]] in GC_Tests['Glucose After 2 Hours Prediabetes']:
                    resultList.append(('Glucose After 2 Hours Prediabetes','نسبتك من المحتمل بنسبة كبيرة الاصابة بمرض السكري بسبب ارتفاع في نسبة الجلوكوز المستوي الطبيعي بشكل كبير'))
                elif GC_Tests['Glucose After 2 Hours  Diabetes']==True:
                    resultList.append(('Glucose After 2 Hours  Diabetes',"نسبة التحليل طبيعية",'حسب نسبة تحليلك فالاحتمال الاكبر انك مصاب بمرض السكري تواصل مع الطبيب لوضع خطة العلاج'))
                else:
                    resultList.append(("نسبة الجلوكوز بعد ساعتان غير طبيعية"))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))
                    
            if GC[i]=='Glucose_After_3_Hours':
                if GC_User_Result[GC[i]] in GC_Tests['Glucose After 3 Hours Normal']:
                    resultList.append(('Glucose After 3 Hours Normal','نسبة الجلوكوزبعد ثلاث ساعات طبيعية'))
                elif GC_User_Result[GC[i]] in GC_Tests['Glucose After 3 Hours Prediabetes']:
                    resultList.append(('Glucose After 3 Hours Prediabetes','نسبتك من المحتمل بنسبة كبيرة الاصابة بمرض السكري بسبب ارتفاع في نسبة الجلوكوز المستوي الطبيعي بشكل كبير'))
                elif GC_Tests['Glucose After 3 Hours Diabetes']==True:
                    resultList.append(('Glucose After 3 Hours Diabetes','حسب نسبة تحليلك فالاحتمال الاكبر انك مصاب بمرض السكري تواصل مع الطبيب لوضع خطة العلاج'))
                else:
                    resultList.append(("نسبة الجلوكوز غير طبيعية "))
            else:
                resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))
        return resultList   

    def Microalbuminuria(gender='',Normoalbuminuria=0.0,Microalbuminuria=0.0,Macroalbuminuria=0.0):
        MIB=['Normoalbuminuria','Microalbuminuria','Macroalbuminuria']
        MIB_User_Result={'Normoalbuminuria':Normoalbuminuria,'Microalbuminuria':Microalbuminuria,'Macroalbuminuria':Macroalbuminuria}
        resultList=[]
        if gender=='f':
            NormoalbuminuriaNormal=np.round(np.arange(0,3.6,0.01),2)
            MicroalbuminuriaNormal=np.round(np.arange(3.5,36,0.01),2)
            MacroalbuminuriaNormal=MIB_User_Result[MIB[2]]>35
        elif gender=='m':
            NormoalbuminuriaNormal=np.round(np.arange(0,2.6,0.01),2)
            MicroalbuminuriaNormal=np.round(np.arange(2.5,25.1,0.01),2)
            MacroalbuminuriaNormal=MIB_User_Result[MIB[2]]>25
        else:
            print("please choose between f , m")
        MIB_test={'Normoalbuminuria':NormoalbuminuriaNormal,
                  'Microalbuminuria':MicroalbuminuriaNormal,'Macroalbuminuria':MacroalbuminuriaNormal}
        MIB_test_inarabic={'Normoalbuminuria':'الزلال الطبيعي','Microalbuminuria':'البيلة الألبومينية الزهيدة','Macroalbuminuria':'الزلال في البول'}
        for i in range(0,len(MIB)):
            if MIB[i]=='Normoalbuminuria':
                if MIB_User_Result[MIB[i]] in MIB_test[MIB[i]]:
                    resultList.append((MIB[i],"نسبة التحليل طبيعية",MIB_test_inarabic.get(MIB[i])))
                else:
                    resultList.append((MIB[i],"نسبة التحليل غير طبيعية",MIB_test_inarabic.get(MIB[i])))
            if MIB[i]=='Microalbuminuria':
                if MIB_User_Result[MIB[i]] in MIB_test[MIB[i]]:
                    resultList.append((MIB[i],"نسبة التحليل طبيعية",MIB_test_inarabic.get(MIB[i])))
                else:
                    resultList.append((MIB[i],"نسبة التحليل طبيعية",MIB_test_inarabic.get(MIB[i])))
            if MIB[i]=='Macroalbuminuria':
                if MIB_test[MIB[i]]==True:
                    resultList.append((MIB[i],"نسبة التحليل طبيعية",MIB_test_inarabic.get(MIB[i])))
                else:
                    resultList.append((MIB[i],"نسبة التحليل طبيعية",MIB_test_inarabic.get(MIB[i])))
        return resultList


class LiverFunctionTest:
    def LiverFunctionTest(ALt_SGPT=0.0,AST_SGOT=0.0,ALP=0.0,Albumin=0.0,Total_protein=0.0,Bilirubin=0.0,GGT=0.0,LD=0.0,PT=0.0):
        LFT=['ALt_SGPT','AST_SGOT','ALP','Albumin','Total_protein','Bilirubin','GGT','LD','PT']
        'ALt_SGPT','AST_SGOT','ALP','Albumin','Total_protein','Bilirubin','GGT','LD','PT'
        LFT_User_Result={'ALt_SGPT':ALt_SGPT,'AST_SGOT':AST_SGOT,'ALP':ALP,'Albumin':Albumin,'Total_protein':Total_protein,'Bilirubin':Bilirubin,
             'GGT':GGT,'LD':LD,'PT':PT}
        liverFunctionTest={'ALt_SGPT':np.round(np.arange(7,65.1,0.01),2),'AST_SGOT':np.round(np.arange(5,40.1,0.01),2),
                       'ALP':np.round(np.arange(40,129.1,0.01),2),'Albumin':np.round(np.arange(3.5,5.1,0.01),2),
                 'Total_protein':np.round(np.arange(6.3,8,0.01),2),'Bilirubin':np.round(np.arange(0.1,1.3,0.01),2),
                       'GGT':np.round(np.arange(8,61.1,0.01),2),'LD':np.round(np.arange(122,222.1,0.01),2),
                       'PT':np.round(np.arange(9.4,12.6,0.01),2)}
        liverFunctionTest_inarabic={'ALt_SGPT':' إنزيم ناقلة أمين الألانيإنزيم موجود في الكبد يساعد في تحويل البروتينات إلى طاقة لخلايا الكبد',
                                    'AST_SGOT':'إنزيم ناقلة أمين الأسبارتات هو إنزيم يساعد في استقلاب الأحماض الأمينية ',
                                    'ALP':'إنزيم الفوسفاتاز القلوي هو إنزيم موجود في الكبد والعظام وهو مُهم لتحلُّل البروتينات',
                              'Albumin':'الألبومين هو أحد البروتينات المُتعدِّدة التي تُنتج في الكبد',
                              'Total_protein':'البروتين الكلي','Bilirubin':'البيليروبين مادة تُنتج أثناء التكسر الطبيعي لخلايا الدم الحمراء',
                              'GGT':'انزيم ناقلة الببتيد غاما غلوتاميل هو إنزيم يُوجَد في الدم',
                              'LD':'إنزيم نازعة هيدروجين اللاكتات هو إنزيم موجود في الكبد',
                              'PT':'زمن البروثرومبين هو الوقت الذي يستغرقه دمك للتخثر'}
        resultList = []
        for i in range(0,len(LFT)):
            if LFT_User_Result[LFT[i]] in liverFunctionTest[LFT[i]]:
                resultList.append((LFT[i], "نسبته طبيعية وهو ", liverFunctionTest_inarabic.get(LFT[i])))    
            else:
                resultList.append((LFT[i], "نسبته غير طبيعية وهو ", liverFunctionTest_inarabic.get(LFT[i])))       
        return resultList
    
                    
class kidneyFuncyiontTest:
    def kidneyFuncyiontTest(gender='',Glucose=0.0,BUN=0.0,Creatinine=0.0,Calcium=0.0,GFR=0.0,Sodium=0.0,potassium=0.0,chloride=0.0,
                           CO2=0.0,Anion_Gap=0.0,BUN_Creat_ratio=0.0):
        KFT=['Glucose','BUN','Creatinine','Calcium','GFR','Sodium','potassium','chloride','CO2',
             'Anion_Gap','BUN_Creat_ratio']
        KFT_User_Result={'Glucose':Glucose,'BUN':BUN,'Creatinine':Creatinine,'Calcium':Calcium,
                         'GFR':GFR,'Sodium':Sodium,'potassium':potassium,'chloride':chloride,'CO2':CO2,
             'Anion_Gap':Anion_Gap,'BUN_Creat_ratio':BUN_Creat_ratio}
        KFT_Test_inarabic={'Glucose':'الجلوكوز','BUN':'نيتروجين اليوريا في الدم','Creatinine':' الكرياتين هو قياس لمدى كفاءة كليتيك في أداء وظيفتهما في ترشيح الفضلات من دمك والكرياتينين هو مركب كيميائي متبقٍ من عمليات إنتاج الطاقة في عضلاتك حيث ترشِّح الكلى السليمة الكرياتينين خارج الدم. ويخرج الكرياتينين من جسمك ضمن الفضلات الخارجة مع البول',
                         'Calcium':'الكالسيوم','GFR':'سرعة الترشيح الكبيبي وهي تستخدم لتقدير السرعة التي ترشح بها الدم ','Sodium':'الصوديوم',
                         'potassium':'البوتاسيوم','chloride':'كلوريد','CO2':'ثاني اكسيد الكربون',
                              'Anion_Gap':'تفاعلات الصوديوم والكالسيوم','BUN_Creat_ratio':'كمية الكرياتينين الموجودة'}
        if gender == 'f':
            Creatinine=np.round(np.arange(0.59,1.05,0.01),2)
        elif gender=='m':
            Creatinine=np.round(np.arange(0.74 ,1.35,0.01),2)
        else:
            print("من فضلك ادخل البيانات بشكل صحيح")
        if GFR>60:
            GFR=True
        else:
            GFR=False
        Creatinine_Test={'Glucose':np.round(np.arange(70,105,0.01),2),'BUN':np.round(np.arange(7,18.1,0.01),2),'Creatinine':Creatinine,
                         'Calcium':np.round(np.arange(8.4,10.6,0.01),2),'GFR':GFR,'Sodium':np.round(np.arange(133,134.1,0.01),2),
                         'potassium':np.round(np.arange(3.6,5.1,0.01),2),'chloride':np.round(np.arange(101,111.1,0.01),2),'CO2':np.round(np.arange(21,31.1,0.01),2),
                         'Anion_Gap':np.round(np.arange(4.0,26.1,0.01),2),'BUN_Creat_ratio':np.round(np.arange(7.3,21.8,0.01),2)}
        resultList = []
        for i in range(0,len(KFT)):
            if KFT[i]=='GFR':
                if KFT_User_Result[KFT[i]]==True:
                    resultList.append((KFT[i], "نسبته طبيعية وهو ", KFT_Test_inarabic.get(KFT[i])))
                else:
                    resultList.append((KFT[i], "نسبته غير طبيعية وهو ", KFT_Test_inarabic.get(KFT[i])))
            else:   
                if KFT_User_Result[KFT[i]] in Creatinine_Test[KFT[i]]:
                    resultList.append((KFT[i], "نسبته طبيعية وهو ", KFT_Test_inarabic.get(KFT[i])))
                else:
                    resultList.append((KFT[i], "نسبته غير طبيعية وهو ", KFT_Test_inarabic.get(KFT[i])))
        return resultList
    
                        
class ESRBlood:
    def BleedandclottingTime(Blood_Clotting_Time_CT=0.0,Bleeding_Time_BT=0.0):
        BCT=['Blood_Clotting_Time_CT','Bleeding_Time_BT']
        BCT_User_Result={'Blood_Clotting_Time_CT':Blood_Clotting_Time_CT,'Bleeding_Time_BT':Bleeding_Time_BT}
        resultList=[]
        BCT_Tests={'Blood_Clotting_Time_CT':np.round(np.arange(113,136.1,0.01),2),
                'Bleeding_Time_BT':np.round(np.arange(60,110.1,0.01),2)}
        BCT_Tests_inarabic={'Blood_Clotting_Time_CT':'سرعة التجلط','Bleeding_Time_BT':'سرعة النزف'}
        for i in range(0,len(BCT)):
            if BCT[i] == 'Blood_Clotting_Time_CT':
                if BCT_User_Result[BCT[i]] in BCT_Tests[BCT[i]]:
                    resultList.append(('Blood Clotting Time (CT)',"نسبة التحليل طبيعية",BCT_Tests_inarabic.get(BCT[i])))
                else:
                    resultList.append(('Blood Clotting Time (CT)',"نسبة التحليل طبيعية تشير ان الدم يتجلط في وقت غير طبيعي",BCT_Tests_inarabic.get(BCT[i])))
            elif BCT[i] == 'Bleeding_Time_BT':
                if BCT_User_Result[BCT[i]] in BCT_Tests[BCT[i]]:
                    resultList.append(('Bleeding Time (BT)',"نسبة التحليل طبيعية",BCT_Tests_inarabic.get(BCT[i])))
                else:
                    resultList.append(('Bleeding Time (BT)',"نسبة التحليل غير طبيعية تشير ان كمية النزيف غير طبيعية",BCT_Tests_inarabic.get(BCT[i])))
            else:
                print("من فضلك تاكد من ادخال البيانات بشكل صحيح")
        return resultList

   
    def ProthrombinTime(PT=0.0,APTT=0.0,Fibrinogen=0.0,AT_III=0.0,FDPs=0.0):  
        PTT=['PT','APTT','Fibrinogen','AT_III','FDPs']
        PTT_User_Result={'PT':PT,'APTT':APTT,'Fibrinogen':Fibrinogen,'AT_III':AT_III,'FDPs':FDPs}
        resultList=[]
        if PTT_User_Result[PTT[4]] <2.5:
            FDPs=True
        else:
             FDPs=False
        PTT_Test={'PT':np.round(np.arange(6.0,8.6,0.01),2),
            'APTT':np.round(np.arange(12.0,18.1,0.01),2),
             'Fibrinogen':np.round(np.arange(200,400.1,0.01),2),
            'AT_III':np.round(np.arange(85,150.1,0.01),2),
           'FDPs':FDPs}
        PTT_Tests_inarabic={'PT':'بروتين في بلازما الدم','APTT':'يخبرك الاختبار بعدد الثواني التي استغرقها دمك لتشكيل جلطة',
                            'Fibrinogen':'  الفبرينوجين أحد العوامل التي تساعد في تخثر الدم ',
                            'AT_III':'لا يعتمد على فيتامين K يمنع التخثر عن طريق تحييد النشاط الإنزيمي','FDPs':'يقيس منتجات تحلل الفبرين، وهي المواد التي تبقى في الدم عندما تذوب الجلطات في الدم'}
        for i in range(0,len(PTT)):
            if PTT[i]=='FDPs':
                if PTT_Test[PTT[i]]==True:
                    resultList.append((PTT[i],"نسبة التحليل طبيعية",PTT_Tests_inarabic.get(PTT[i])))
                else:
                    resultList.append((PTT[i],"نسبة التحليل طبيعية",PTT_Tests_inarabic.get(PTT[i])))
            else:
                if PTT_User_Result[PTT[i]] in PTT_Test[PTT[i]]:
                    resultList.append((PTT[i],"نسبة التحليل طبيعية",PTT_Tests_inarabic.get(PTT[i])))
                else:
                    resultList.append((PTT[i],"نسبة التحليل طبيعية",PTT_Tests_inarabic.get(PTT[i])))
        return resultList


    def PlateletCountTest(PC_Test=0.0):
        resultList=[]
        if PC_Test in np.round(np.arange(150,400.1,0.01),2):
            resultList.append(("عدد الصفائح الدموية الضرورية لتخنثر الدم طبيعي"))  
        else:
            resultList.append(("عدد الصفائح الدموية الضرورية لتخنثر الدم غير طبيعي")) 
        return resultList


class BloodDiseases:
    def CompleteBloodPicture(gender='',Haemoglobin=0.0,Haematocrit_PCV=0.0,RBCs_Count=0.0,MCV=0.0,MCH=0.0,MCHC=0.0,RDW_CV=0.0,
            Platelet_Count_EDTA_Blood=0.0,Total_Leucocytic_Count_EDTA_Blood=0.0,Neutrophils=0.0,Staff=0.0,Segmented=0.0,
            Lymphocytes=0.0,Monocytes=0.0,Eosinophils=0.0,Basophils=0.0):
        CBC=['Haemoglobin','Haematocrit_PCV','RBCs_Count','MCV','MCH','MCHC','RDW_CV',
            'Platelet_Count_EDTA_Blood','Total_Leucocytic_Count_EDTA_Blood','Neutrophils','Staff','Segmented',
            'Lymphocytes','Monocytes','Eosinophils','Basophils']
        CBC_User_Result ={'Haemoglobin':Haemoglobin,'Haematocrit_PCV':Haematocrit_PCV,'RBCs_Count':RBCs_Count,
                          'MCV':MCV,'MCH':MCH,'MCHC':MCHC,'RDW_CV':RDW_CV,'Platelet_Count_EDTA_Blood':Platelet_Count_EDTA_Blood,
                          'Total_Leucocytic_Count_EDTA_Blood':Total_Leucocytic_Count_EDTA_Blood,'Neutrophils':Neutrophils,'Staff':Staff,
                          'Segmented':Segmented,'Lymphocytes':Lymphocytes,'Monocytes':Monocytes,'Eosinophils':Eosinophils,'Basophils':Basophils}
        resultList=[]
        if gender=='f':
            HemoglobinN=np.round(np.arange(11.6,15.1,0.01),2)
            RBCsN=np.round(np.arange(3.92,5.14,0.001),3)
            HematocritN=np.round(np.arange(35.5,45,0.01),2)
            PlateletcountN=np.round(np.arange(157,371.1,0.01),2)
        elif gender=='m':
            HemoglobinN=np.round(np.arange(13.2 ,16.7,0.01),2)
            RBCsN=np.round(np.arange(4.35,5.57,0.01),2)
            HematocritN=np.round(np.arange(38.3,48.1,0.01),2)
            PlateletcountN=np.round(np.arange(135,371.1,0.01),2)
        else:
            resultList.append("من فضلك تاكد من ادخال البيانات بشكل صحيح")
        CBC_Test={'Haemoglobin':HemoglobinN,'Haematocrit_PCV':HematocritN,'RBCs_Count':RBCsN,'MCV':np.round(np.arange(80,100.1,0.01),2),
                      'MCH':np.round(np.arange(27,33.1,0.01),2),'MCHC':np.round(np.arange(31,37.1,0.01),2),
                  'RDW_CV':np.round(np.arange(11.5,15.1,0.01),2),'Platelet_Count_EDTA_Blood':PlateletcountN,
                  'Total_Leucocytic_Count_EDTA_Blood':np.round(np.arange(4,11.1,0.01),2),
                  'Neutrophils':np.round(np.arange(2,7.1,0.01),2),
                  'Staff':np.round(np.arange(0,CBC_User_Result[CBC[10]]+0.1,0.01),2),
                  'Segmented':np.round(np.arange(0,CBC_User_Result[CBC[11]]+0.1,0.01),2),'Lymphocytes':np.round(np.arange(1,4.1,0.01),2),
                  'Monocytes':np.round(np.arange(0.2,2,0.01),2),'Eosinophils':np.round(np.arange(0.1,0.46,0.01),2),'Basophils':np.round(np.arange(0,0.2,0.01),2)}

        CBC_Test_inarabic={'Haemoglobin':'الهيموغلوبين يقيس اختبار الهيموغلوبين نسبة الهيموغلوبين في الدم. الهيموغلوبين عبارة عن بروتين في خلايا الدم الحمراء التي تحمل الأكسجين إلى أعضاء الجسم',
                           'Haematocrit_PCV':'الهيماتوكريت للمساعدة في تشخيص اضطرابات الدم مثل كثرة الكريات الحمراء الحقيقية',
                           'RBCs_Count':'تعداد خلايا الدم الحمراء',
                           'MCV':'تحليل متوسط حجم كريات الدم',
                           'MCH': 'متوسط نسبة الهيموجلوبين هو تحليل للدم لمعرفة متوسط نسبة الهيموجلوبين فيه عن طريق حساب متوسط كتلة الهيموجلوبين في كرات الدم الحمراء كلاً على حده في عينة الدم. ويعد هذا التحليل مؤشراً هاماً على مستوى الحديد في الدم والذي يعطي كرات الدم الحمراء لونها المميز ',
                           'MCHC':' مقياس لتركيز الهيموغلوبين في حجم معين من خلايا الدم الحمراء',
                           'RDW_CV':' لقياس مدى تشتت أحجام كريات الدم الحمراء و توزيع كريات الدم الحمراء ',
                          'Platelet_Count_EDTA_Blood':'تعداد الصفيحات الدموية وهي أجزاء صغيرة من الخلايا، وتعد ضرورية لتخثر الدم الطبيعي',
                           'Total_Leucocytic_Count_EDTA_Blood':' تحليل عدد كريات الدم البيضاء وهي خلايا الدم التي تساعد الجسم على مكافحة العدوى والأمراض',
                           'Neutrophils':'خلايا العدلات يقوم بتحديد مستوى العدلات في الدم نسبة لإجمالي عدد كريات الدم البيضاء في الدم. إن العدلات هي أكثر أنواع خلايا الدم البيضاء المتواجدة في الدم، والتي يتم انتاجها في نخاع العظم ومن ثم تدخل إلى مجرى الدم من أجل القيام بوظيفتها',
                           'Staff':'يستخدم تحليل نسبة العدلات المجزأة من أجل الكشف عن الإصابة بمجموعة متنوعة من الاضطرابات، بما في ذلك العدوى، وفقر الدم، وأمراض الجهاز المناعي، وسرطانات الدم',
                           'Segmented':'إن العدلات هي نوع من خلايا الدم البيضاء والتي وظيفتها الأساسية هي حماية الجسم من العدوى',
                          'Lymphocytes':'الخلايا اللمفاوية هي إحدى أنواع خلايا الدم البيضاء المتواجدة في الدم، والتي تعد من الخلايا المناعية الرئيسية في الجسم، حيث أنها تعمل إلى جانب خلايا جهاز المناعة الأخرى من أجل حماية الجسم من مختلف أنواع الأمراض. يتم انتاج الخلايا الليمفاوية في نخاع العظم ومن ثم تدخل إلى مجرى الدم لتتواجد فيه وفي الأنسجة الليمفاوية',
                           'Monocytes':' خلايا الحيدات تقوم بتحديد نسبة الوحيدات في الدم، وهي احدى أنواع خلايا الدم البيضاء يتم انتاجها في نخاع العظم ومن ثم تدخل إلى مجرى الدم من أجل القيام بوظيفتها، ألا وهي محاربة بعض أنواع العدوى ومساعدة خلايا الدم البيضاء الأخرى على إزالة الخلايا الميتة أو التالفة ومحاربة الخلايا السرطانية',
                           'Eosinophils':'كثرة الحمضات هو الزيادة غير الطبيعية لمستوى الحمضات في الدم، وتعرف الحمضات بأنها نوع من خلايا الدم البيضاء التي تكافح المواد المسببة للأمراض في الجسم، مثل الطفيليات، ولها دور في تفاعلات الحساسية.',
                           'Basophils':' خلايا قاعدية يقوم بتحديد نسبة خلايا الدم البيضاء القاعدية في الدم، وهي احدى أنواع خلايا الدم البيضاء يتم انتاجها في نخاع العظم ومن ثم تدخل إلى مجرى الدم من أجل القيام بوظيفتها، ألا وهي الحفاظ على وظيفة جهاز المناعة'}
        for i in range(0,len(CBC)):
            if(CBC_User_Result[CBC[i]] in CBC_Test[CBC[i]]):
                resultList.append((CBC[i],"نسبة التحليل طبيعية",CBC_Test_inarabic.get(CBC[i])))
            else:
                resultList.append((CBC[i],"نسبة التحليل غير طبيعية",CBC_Test_inarabic.get(CBC[i])))
        return resultList
    
    def HbElectrophoresis(Hemoglobine_A=0.0,Hemoglobine_F=0.0,Hemoglobine_S=0.0,Hemoglobine_C=0.0):
        HbE=['Hemoglobine_A','Hemoglobine_F','Hemoglobine_S','Hemoglobine_C']
        HbE_User_Result={'Hemoglobine_A':Hemoglobine_A,'Hemoglobine_F':Hemoglobine_F,'Hemoglobine_S':Hemoglobine_S,'Hemoglobine_C':Hemoglobine_C}
        resultList=[]
        HbE_Test={'Hemoglobine_A':np.round(np.arange(95,98.1,0.01),2),
          'Hemoglobine_F':np.round(np.arange(1,2.1,0.01),2),
          'Hemoglobine_S':range(0),'Hemoglobine_C':range(0)}           
        HbE_Test_inarabic={'Hemoglobine_A':'هو النوع الاكثر تواجدا ','Hemoglobine_F':'يستبدل بهيموجلوبين A بعد فترة قصيرة من الولادة ',
                       'Hemoglobine_S':'هو النوع الموجود عند مرضى فقر الدم المنجلي','Hemoglobine_C':'ينقل هذا النوع من الهيموجلوبين الأكسجين بكفاءة'}
        for i in range(0,len(HbE)):
            if HbE_User_Result[HbE[i]] in HbE_Test[HbE[i]]:
                resultList.append((HbE[i],"نسبة التحليل طبيعية",HbE_Test_inarabic.get(HbE[i])))
            else:
                resultList.append((HbE[i],"نسبة التحليل غير طبيعية",HbE_Test_inarabic.get(HbE[i])))
        return resultList
         
    def DirectCoombsTest(DCT_User_Result=''):
        resultList=[]
        if DCT_User_Result=='negative':
            resultList.append((" لا يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        else:
            resultList.append((" يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        return resultList
    
    def DirectCoombsTest2(DCT_User_Result=0.0):
        resultList=[]
        if DCT_User_Result in np.round(np.arange(0,1.1,0.01),2) :
            resultList.append((" لا يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        else:
            resultList.append((" يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        return resultList


    def InDirectCoombsTest(IDCT_User_Result=''):
        resultList=[]
        if IDCT_User_Result=='negative' :
            resultList.append((" لا يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        else:
            resultList.append((" يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        return resultList
        
    def InDirectCoombsTest2(IDCT_User_Result=0.0):
        resultList=[]
        if IDCT_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لا يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        else:
            resultList.append((" يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        return resultList


    def  BloodGroupANDRh(BG='',RH_Result=''):
        resultList=[]
        resultList.append(("زمرت دمك",BG))
        if RH_Result=='negative':
            resultList.append((" لا يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        else:
            resultList.append((" يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        return resultList
            
    def  BloodGroupANDRh2(BG='',RH_Result=0.0):
        resultList=[]
        resultList.append(("زمرت دمك",BG))
        if RH_Result  in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لا يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        else:
            resultList.append((" يوجد اجسام مضادة تهاجم كريات الدم الحمراء"))
        return resultList

    def Glucose6phosphate(gender='',G6P_User_Result=0.0):
        resultList=[]
        G6P_inarabic={'G6P':' يساهم إنزيم نازعة هيدروجين الجلوكوز-6-فوسفات في الحفاظ على وظيفة خلايا الدم الحمراء، واستمرار عملها، إضافة لحمايتها من مكونات الدم الأخرى التي قد تلحق بها الضرر أو المواد الناتجة من العمليات الحيوية في الجسم'}
        if gender=='baby':
            Glucose6PhosphateDehydrogenaseTestB=np.round(np.arange(10.5,14.8,0.01),2)
            if G6P_User_Result in Glucose6PhosphateDehydrogenaseTestB:
                resultList.append(('Glucose6phosphate',"نسبة التحليل طبيعية",G6P_inarabic.get('G6P')))
            else:
                resultList.append(('Glucose6phosphate',"نسبة التحليل غير طبيعية",G6P_inarabic.get('G6P')))
        elif gender=='adult':
            Glucose6PhosphateDehydrogenaseTestA=np.round(np.linspace(5.5,20.1,0.01),2)
            if G6P_User_Result in Glucose6PhosphateDehydrogenaseTestA:
                resultList.append(('Glucose6phosphate',"نسبة التحليل طبيعية",G6P_inarabic.get('G6P')))
            else:
                resultList.append(('Glucose6phosphate',"نسبة التحليل غير طبيعية",G6P_inarabic.get('G6P')))
        else:
            resultList.append(("من فضلك ادخل البيانات بشكل صحيح"))
        return resultList


class Hormones:
    def InfertilityTestsF(gender='',age='',Estrogen=0.0 ,Progesterone=0.0,FSH=0.0,LH=0.0,Prolactin=0.0,Testosteroe_Total=0.0,Testosteron_Free=0.0):
        IT=['Estrogen' ,'Progesterone', 'FSH','LH','Prolactin','Testosteroe_Total','Testosteron Free']
        IT_User_Result={'Estrogen':Estrogen,'Progesterone':Progesterone,'FSH':FSH,'LH':LH,'Prolactin':Prolactin,
                        'Testosteroe_Total':Testosteroe_Total,'Testosteron_Free':Testosteron_Free}
        resultList = []
        Estrogen_Test={'Estrogen Follicular phase':np.round(np.arange(19,144.1,0.01),2),'Estrogen Mid-Cycle':np.round(np.arange(64,358.1,0.01),2) ,
                      'Estrogen Luteal phase':np.round(np.arange(56,214.1,0.01),2),'Estrogen post-Menopausal':np.round(np.arange(0,31.1,0.01),2),
                  'Estrogen child':np.round(np.arange(0,28.1,0.01),2)}
        Progesterone_Test={'Progesterone Follicular':np.round(np.arange(0.15,1.5,0.01),2), 'Progesterone Luteal':np.round(np.arange(3.34,25.57,0.01),2),
                           'Progesterone Mid-Cycle':np.round(np.arange(4.44,28.04,0.01),2),'Progesterone post-Menopausal':np.round(np.arange(0.1,0.74,0.01),2),
                         'Progesterone child':np.round(np.linspace(0,0.3,num=25,endpoint=True),2)}
        FSH_Test={'FSH Follicular': np.round(np.arange(2.5,10.3,0.01),2),'FSH Mid-Cycle Peak': np.round(np.arange(3.1,17.9,0.01),2),
                  'FSH Luteal phase': np.round(np.arange(1.5,9.3,0.01),2),'FSH post-Menopausal':np.round(np.arange(23.0,116.4,0.01),2),
                  'FSH Child':np.round(np.arange(0,4.1,0.01),2)}
        LH_Test={'LH Follicular phase':np.round(np.arange(1.9,12.7,0.01),2),'LH Mid-Cycle Peak':np.round(np.arange(8.7,76.5,0.01),2),
                  'LH Luteal phase':np.round(np.arange(0.5,17,0.01),2),'LH post-Menopausal ':np.round(np.arange(10.0,54.8,0.01),2),
                 'LH Child':np.round(np.arange(0.5,1.6,0.01),2)}   
        Prolactin_test={'Prolactin Non-pregnant':np.round(np.arange(3.0,30.1,0.01),2),'Prolactin pregnant' :np.round(np.arange(10.0,209.1,0.01),2), 
                        'Prolactin post-Menopausal':np.round(np.arange(2.0,20.1,0.01),2)}
        Testosteron_Total_Test=np.round(np.arange(15,70.1,0.01),2)

        Testosteron_Free_Test={'Testosteron free female (18-30)':np.round(np.arange(1,5.1,0.01),2),
                               'Testosteron free female (31-40)':np.round(np.arange(1,6.2,0.01),2),
                               'Testosteron free female (41-50)':np.round(np.arange(1,4.2,0.01),2),
                                'Testosteron free female less than 50':np.round(np.arange(0,3.1,0.01),2),
                               'Testosteron free Child':np.round(np.arange(30,3200.1,0.01),1)}
        IT_Test_inarabic={'Estrogen Follicular phase':'الاستروجين في مرحلة الخصوبة','Estrogen Mid-Cycle':'الاستروجين في دورة منتصف الدورة الشهرية' ,
                          'Estrogen Luteal phase':'الاستروجين المرحلة الأصفرية','Estrogen post-Menopausal':'الاستروجين بعد سن اليأس',
                          'Progesterone Follicular':'البروجيستيرون في مرحلة الخصوبة', 'Progesterone Luteal':'البروجيستيرون المرحلة الأصفرية',
                           'Progesterone Mid-Cycle':'البروجيستيرون في فترة منتصف الدورة الشهرية','Progesterone post-Menopausal':'البروجيستيرون بعد سن اليأس',
                          'FSH Follicular': ' الهرمون المنشط للحوصلة في مرحلة الخصوبة ','FSH Mid-Cycle Peak': 'الهرمون المنشط للحوصلة في فترة منتصف الدورة الشهرية',
                          'FSH Luteal phase': 'الهرمون المنشط للحوصلة في المرحلة الأصفرية','FSH post-Menopausal': 'الهرمون المنشط للحوصلة  بعد سن اليأس',
                          'LH Follicular phase':' الهرمون المنشط للجسم الاصفر في الدم في مرحلة الخصوبة','LH Mid-Cycle Peak':' الهرمون المنشط للجسم الاصفر في الدم في فترة منتصف الدورة الشهرية',
                          'LH Luteal phase':' الهرمون المنشط للجسم الاصفر في الدم في المرحلة الأصفرية ','LH post-Menopausal ':' الهرمون المنشط للجسم الاصفر في الدم عد سن اليأس ',
                          'Prolactin Non-pregnant' :'هرمون البرولاكتين في حالة عدم وجود حمل','Prolactin pregnant' :'هرمون البرولاكتين في حالة وجود حمل', 
                          'Prolactin post-Menopausal':'هرمون البرولاكتين بعد سن اليأس', 'Progesterone child':'البروجيستيرون للاطفال', 'Estrogen child':'الاستروجين للاطفال',
                        'Testosteron Total female':'التستستيرون الكلي للنساء','Testosteron free female (18-30)':'التستستيرون الحر للنساء التر تتراوح اعمارها بين 18 الي 30',
                            'Testosteron free female (31-40)': 'التستستيرون الحر للنساء التر تتراوح اعمارها بين 31 الي 40','Testosteron free female (41-50)':'التستستيرون الحر للنساء التر تتراوح اعمارها بين 41 الي 50',
                            'Testosteron free female less than 50':'التستستيرون الحر للنساء التي تزيد عن الخمسينا','FSH Child':'الهرمون المنشط للحوصلة' ,'LH Child':'الهرمون المنشط للجسم الاصفر في الدم',
                          'Testosteron free Child':'التستستيرون الحر للاطفال'}     
        if gender=='f':                   
            for i in range(0,len(IT)):
                if IT[i]=='Estrogen':
                    if IT_User_Result[IT[i]] in Estrogen_Test['Estrogen Follicular phase']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen Follicular phase')))
                    elif IT_User_Result[IT[i]] in Estrogen_Test['Estrogen Mid-Cycle']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen Mid-Cycle')))
                    elif IT_User_Result[IT[i]] in Estrogen_Test['Estrogen Luteal phase']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen Luteal phase')))
                    elif IT_User_Result[IT[i]] in Estrogen_Test['Estrogen post-Menopausal']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen post-Menopausal')))
                    else:
                        resultList.append(('نسبة الاستروجن غير طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ','Estrogen'))
                elif IT[i]=='Progesterone':
                    if IT_User_Result[IT[i]] in Progesterone_Test['Progesterone Follicular']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى، والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر",IT_Test_inarabic.get('Progesterone Follicular')))
                    elif IT_User_Result[IT[i]] in Progesterone_Test['Progesterone Luteal']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى، والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر",IT_Test_inarabic.get('Progesterone Luteal')))
                    elif IT_User_Result[IT[i]] in Progesterone_Test['Progesterone Mid-Cycle']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى،  والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر",IT_Test_inarabic.get('Progesterone Mid-Cycle')))
                    elif IT_User_Result[IT[i]] in Progesterone_Test['Progesterone post-Menopausal']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى،  والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر",IT_Test_inarabic.get('Progesterone post-Menopausal')))
                    else:
                        resultList.append(('نسبة البروجسترون غير طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى، والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر','Progesterone'))
                elif IT[i]=='FSH':
                    if IT_User_Result[IT[i]] in FSH_Test['FSH Follicular']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Follicular')))
                    elif IT_User_Result[IT[i]] in FSH_Test['FSH Mid-Cycle Peak']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Mid-Cycle Peak')))
                    elif IT_User_Result[IT[i]] in FSH_Test['FSH Luteal phase']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Luteal phase')))
                    elif IT_User_Result[IT[i]] in FSH_Test['FSH post-Menopausal']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH post-Menopausal')))
                    else:
                        resultList.append(('نسبة هرمون المنشط للحوصلة غير طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض','FSH'))
                elif IT[i]=='LH':
                    if IT_User_Result[IT[i]] in  LH_Test['LH Follicular phase']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH Follicular phase')))
                    elif IT_User_Result[IT[i]] in  LH_Test['LH Mid-Cycle Peak']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH Mid-Cycle Peak')))
                    elif IT_User_Result[IT[i]] in  LH_Test['LH Luteal phase']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH Luteal phase')))
                    elif IT_User_Result[IT[i]] in  LH_Test['LH post-Menopausal']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH post-Menopausal')))
                    else:
                        resultList.append(('نسبة هرمون المنشط للجسم الاصفر غير طبيعية وهو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية','LH'))
                elif IT[i]=='Prolactin':
                    if IT_User_Result[IT[i]] in Prolactin_test['Prolactin Non-pregnant']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو الهرمون الذي يحفز الرضاعة",IT_Test_inarabic.get('Prolactin Non-pregnant')))
                    elif IT_User_Result[IT[i]] in Prolactin_test['Prolactin pregnant']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو الهرمون الذي يحفز الرضاعة",IT_Test_inarabic.get('Prolactin pregnant')))
                    elif IT_User_Result[IT[i]] in Prolactin_test['Prolactin post-Menopausal']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو الهرمون الذي يحفز الرضاعة",IT_Test_inarabic.get('Prolactin post-Menopausal')))
                    else:
                         resultList.append(('نسبة هرمون البرولاكتين غير طبيعية وهو الهرمون الذي يحفز الرضاعة', 'Prolactin'))
                elif IT[i]=='Testosteroe_Total':
                    if IT_User_Result[IT[i]] in Testosteron_Total_Test:
                        resultList.append(('نسبة التستوستيرون الكلي طبيعية و يعد هرمون التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث' ,'Testosteroe Total'))
                    else:
                        resultList.append(('نسبة التستوستيرون الكلي غير طبيعية وهو نسب طبيعية و يعد التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteroe Total'))
                elif IT[i]=='Testosteron_Free':
                    if age=='A':
                        if IT_User_Result[IT[i]] in  Testosteron_Free_Test['Testosteron free female (18-30)']:
                             resultList.append(('Testosteroe Free',"نسبة التحليل طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female (18-30)')))
                        else:
                             resultList.append(('Testosteroe Free',"نسبة التحليل غير طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female (18-30)')))
                    elif age=='B':
                        if IT_User_Result[IT[i]] in  Testosteron_Free_Test['Testosteron free female (31-40)']:
                             resultList.append(('Testosteroe Free',"نسبة التحليل طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female (31-40)')))
                        else:
                             resultList.append(('Testosteroe Free',"نسبة التحليل غير طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female (31-40)')))
                    elif age=='C':
                        if IT_User_Result[IT[i]] in  Testosteron_Free_Test['Testosteron free female (41-50)']:
                            resultList.append(('Testosteroe Free',"نسبة التحليل طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female (41-50)')))
                        else: 
                            resultList.append(('Testosteroe Free',"نسبة التحليل غير طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female (41-50)')))
                    elif age=='D':
                        if IT_User_Result[IT[i]] in  Testosteron_Free_Test['Testosteron free female less than 50']:
                            resultList.append(('Testosteroe Free',"نسبة التحليل طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female less than 50')))
                        else:
                            resultList.append(('Testosteroe Free',"نسبة التحليل غير طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free female less than 50')))
                    else:
                        resultList.append(('نسبة هرمون التستيستيرون الحر غير طبيعية كما يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول ','Testosteron free'))
       
        elif gender=='child':
            for i in range(0,len(IT)):
                if IT[i]=='Estrogen':
                    if IT_User_Result[IT[i]] in Estrogen_Test['Estrogen child']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen child')))
                    else:
                        resultList.append(('نسبة الاستروجن غير طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ','Estrogen'))
                if IT[i]=='Progesterone': 
                    if IT_User_Result[IT[i]] in Progesterone_Test['Progesterone child']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى، خلال النصف الثاني من الدورة الشهرية، والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر",IT_Test_inarabic.get('Progesterone child')))
                    else:
                         resultList.append(('نسبة البروجسترون غير طبيعية وهو أحد الهرمونات الستيرويدية التي يفرزها الجهاز التناسلي عند الأنثى، خلال النصف الثاني من الدورة الشهرية، والذي يتم إفرازه بشكل أساسي عن طريق ما يعرف بالجسم الأصفر','Progesterone'))
                if IT[i]=='FSH':   
                    if IT_User_Result[IT[i]] in FSH_Test['FSH Child']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Child')))
                    else:
                        resultList.append(('نسبة هرمون المنشط للحوصلة غير طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض ','FSH'))
                if IT[i]=='LH':
                    if IT_User_Result[IT[i]] in  LH_Test['LH Child']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية و هو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH Child')))
                    else:
                        resultList.append(('نسبة هرمون المنشط للجسم الاصفر غير طبيعية و هو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية','LH'))
                if IT[i]=='Prolactin':
                    if IT_User_Result[IT[i]] in Prolactin_test['Prolactin Non-pregnant']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو الهرمون الذي يحفز الرضاعة",IT_Test_inarabic.get('Prolactin Non-pregnant')))
                    else:
                        resultList.append((IT[i],'نسبة هرمون البرولاكتين غير طبيعية وهو الهرمون الذي يحفز الرضاعة',IT_Test_inarabic.get('Prolactin Non-pregnant')))
                if IT[i]=='Testosteroe_Total':
                    if  IT_User_Result[IT[i]] in Testosteron_Total_Test:
                        resultList.append(('نسبة التستوستيرون الكلي طبيعية و يعد هرمون التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteron Total'))
                    else:
                        resultList.append(('نسبة التستوستيرون الكلي غير طبيعية وهو نسب طبيعية و يعد التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteron Total'))
                if IT[i]=='Testosteron_Free':
                        if  IT_User_Result[IT[i]] in  Testosteron_Free_Test['Testosteron free Child']:
                            resultList.append(('Testosteroe Free',"نسبة التحليل طبيعية يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free Child')))
                        else:
                            resultList.append(('Testosteroe Free',"نسبة التحليل غير طبيعية يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول",IT_Test_inarabic.get('Testosteron free Child')))
        else:
            resultList.append(('من فضلك ادخل البيانات بشكل صحيح')) 
        return resultList

    def InfertilityTestsM(gender='',Estrogen=0.0,FSH=0.0,LH=0.0,Prolactin=0.0,Testosteron_Total=0.0,Testosteron_Free=0.0):
        IT=['Estrogen','LH', 'FSH','Prolactin' , 'Testosteron_Total','Testosteron_Free']
        IT_User_Result={'Estrogen':Estrogen,'FSH':FSH,'LH':LH,'Prolactin':Prolactin,'Testosteron_Total':Testosteron_Total,'Testosteron_Free':Testosteron_Free}
        resultList = []
        Estrogen_Test={'Estrogen male':np.round(np.arange(0,39.9,0.01),2),
                       'Estrogen child':np.round(np.arange(0,28.1,0.01),2)}
        FSH_Test={ 'FSH Male':np.round(np.arange(2,12.1,0.01),2),
              'FSH Child':np.round(np.arange(0,5.1,0.01),2)}
        LH_Test={'LH male':np.round(np.arange(1.42,15.5,0.01),2),
             'LH Child':np.round(np.arange(0.5,1.6,0.01),2)}
        Prolactin_test={'Prolactin male':np.round(np.arange(0,15.1,0.01),2)} 
        Testosteron_Total_Test={'Testosteron Total':np.round(np.arange(1.64,7.54,0.01),2)}         
        Testosteron_Free_Test={'Testosteron Free male':np.round(np.arange(1.0,28.4,0.01),2),
                           'Testosteron free Child':np.round(np.arange(30,3200.1,0.01),2)}
        IT_Test_inarabic={'Estrogen child':'الاستروجين للاطفال','FSH Child':'الهرمون المنشط للحوصلة' ,'LH male':'الهرمون المنشط للجسم الاصفر في الدم',
                      'Testosteron free Child':'التستستيرون الحر للاطفال','Estrogen male':'الاستروجين للرجال','FSH Male':'الهرمون المنشط للحوصلة',
                       'Testosteron Total':'التستستيرون الكلي ','Testosteron free male':'التستستيرون الحر للرجال' }
        if gender=='male':    
                for i in range(0,len(IT)):
                    if IT[i]=='Estrogen':
                        if IT_User_Result[IT[i]] in Estrogen_Test['Estrogen male']:
                             resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen male')))
                        else:
                            resultList.append((IT[i],"نسبة التحليل غر طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen male')))
                    elif IT[i]=='FSH':
                        if IT_User_Result[IT[i]] in FSH_Test['FSH Male']:
                            resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Male')))
                        else:
                            resultList.append((IT[i],"نسبة التحليل غير طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Male')))
                    elif IT[i]=='LH':
                        if IT_User_Result[IT[i]] in  LH_Test['LH male']:
                            resultList.append((IT[i],"نسبة التحليل طبيعية و هو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH male')))
                        else:
                            resultList.append((IT[i],"نسبة التحليل غير طبيعية و هو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH male')))
                    elif IT[i]=='Prolactin':
                        if IT_User_Result[IT[i]] in Prolactin_test['Prolactin male']:
                             resultList.append((IT[i],"نسبة التحليل طبيعية وهو الهرمون الذي يحفز الرضاعة"))
                        else:
                            resultList.append((IT[i],"نسبة التحليل غير طبيعية وهو الهرمون الذي يحفز الرضاعة"))
                    elif IT[i]=='Testosteron_Total':
                        if IT_User_Result[IT[i]] in Testosteron_Total_Test['Testosteron Total']:
                            resultList.append(('نسبة التستوستيرون الكلي طبيعية و يعد هرمون التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteron Total'))
                        else:
                            resultList.append(('نسبة التستوستيرون الكلي غير طبيعية و يعد هرمون التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteron Total'))
                    elif IT[i]=='Testosteron_Free':
                        if IT_User_Result[IT[i]] in Testosteron_Free_Test['Testosteron Free male']:
                            resultList.append(('Testosteron Free','نسبة هرمون التستيستيرون الحر طبيعية وهو يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول '))
                        else:
                            resultList.append(('Testosteron Free','نسبة هرمون التستيستيرون الحر غير طبيعية وهو يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول '))
        elif gender=='child':
            for i in range(0,len(IT)):
                if IT[i]=='Estrogen':
                    if IT_User_Result[IT[i]] in Estrogen_Test['Estrogen child']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen child')))
                    else:
                        resultList.append((IT[i],"نسبة التحليل غير طبيعية وهو هرمون التحكم فى الجهاز التناسلي ,يلعب دور فى بلوغ البنت , الطمث , و الحمل و يؤثر أيضا على بقية أجزاء الجسم مثل العظام , الأوعية الدموية , القلب , و المخ",IT_Test_inarabic.get('Estrogen child')))
                elif IT[i]=='FSH':   
                    if IT_User_Result[IT[i]] in FSH_Test['FSH Child']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Child')))
                    else:
                        resultList.append((IT[i],"نسبة التحليل غير طبيعية وهو أحد الهرمونات المحفز لنمو البويضات في المبايض",IT_Test_inarabic.get('FSH Child')))
                elif IT[i]=='LH':
                    if IT_User_Result[IT[i]] in  LH_Test['LH Child']:
                        resultList.append((IT[i],"نسبة التحليل طبيعية و هو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH Child')))
                    else:
                        resultList.append((IT[i],"نسبة التحليل غير طبيعية و هو هرمون يُفرز من الفص الأمامي من الغدة النخامية في الدماغ مع هرمونات مثل الهرمون المنشط للحوصلة والهرمون المنشط للدرقية والبرولاكتين ويلعب دوراً في الوظائف الإنجابية",IT_Test_inarabic.get('LH Child')))
                elif IT[i]=='Prolactin':
                    if IT_User_Result[IT[i]] in Prolactin_test['Prolactin male']:
                         resultList.append((IT[i],"نسبة التحليل طبيعية وهو الهرمون الذي يحفز الرضاعة"))
                    else:
                        resultList.append((IT[i],"نسبة التحليل غير طبيعية وهو الهرمون الذي يحفز الرضاعة"))
                elif IT[i]=='Testosteron_Total':
                    if IT_User_Result[IT[i]] in Testosteron_Total_Test['Testosteron Total']:
                         resultList.append(('نسبة التستوستيرون الكلي طبيعية و يعد هرمون التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteron Total'))
                    else:
                         resultList.append(('نسبة التستوستيرون الكلي غير طبيعية و يعد هرمون التستوستيرون أو هرمون الذكورة أو الأندروجين هو الهرمون المسؤول عن تطوير الصفات الذكورية ويتم إنتاجه في الخصيتين عند الرجال، أو المبيضين عند النساء والغدد الكظرية، إذا يساعد التستوستيرون في التغيرات التي تحدث عند الأولاد في مرحلة البلوغمثل العضلات ونمو الشعر، أو تضخم القضيب، أو تعميق الصوت، ويوجد عند الذكور بعد البلوغ بكميات كبيرة للحفاظ على كتلة العضلات وتنظيم الدافع الجنسي يتم تحويل التستوستيرون عند النساء إلى هرمون الاستراديول وهو الهرمون الجنسي الرئيسي عند الإناث','Testosteron Total'))
                elif IT[i]=='Testosteron_Free':
                        if IT_User_Result[IT[i]] in Testosteron_Free_Test['Testosteron free Child']:
                            resultList.append(('Testosteron Free','نسبة هرمون التستيستيرون الحر طبيعية وهو يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول '))
                        else:
                            resultList.append(('Testosteron Free','نسبة هرمون التستيستيرون الحر غير طبيعية وهو يحفز التستوستيرون تطور الخصائص الجنسية الثانوية مثل نمو العضلات، أو نمو شعر الجسم، أما عند النساء فإنه يتم تحويل هرمون التستوستيرون إلى هرمون الاستراديول '))
        else:
            resultList.append(("من فضلك ادخل البيانات بشكل صحيح "))
        return resultList


    def TSHTest(TSH=0.0,Total_T4=0.0,Free_T4=0.0,Free_T3=0.0,T3=0.0):
        TSH=['TSH','Total_T4','Free_T4','Free_T3','T3']
        TSH_User_Result={'TSH':TSH,'Total_T4':Total_T4,'Free_T4':Free_T4,'Free_T3':Free_T3,'T3':T3}
        resultList=[]
        TSH_Test={'TSH':np.round(np.arange(0.27,4.3,0.01),2),
                  'Total_T4':np.round(np.arange(4.7,13.6,0.01),2),
                   'Free_T4':np.round(np.arange(0.9,2,0.01),2),
                  'Free_T3':np.round(np.arange(1.68,3.55,0.01),2),
                   'T3':np.round(np.arange(0.8,2.1,0.01),2)}
        TSH_Test_inarabic={'TSH':'الهرمون المنبه للدرقية','Total_T4':'نوع من انواع هرمون المنبه للغدة الدرقية',
                           'Free_T4':'هو الشكل النشط لهرمون هرمون الغدة الدرقية الذي يدخل الأنسجة عند الحاجة',
                            'Free_T3':'شكل من اشكال هرمون الغدة الدرقية النشط','T3':'نوع من انواع هرمون المنبه للغدة الدرقية'}
        for i in range(0,len(TSH)):
            if TSH_User_Result[TSH[i]] in TSH_Test[TSH[i]]:
                resultList.append((TSH[i],"نسبة التحليل طبيعية",TSH_Test_inarabic.get(TSH[i])))
            else:
                resultList.append((TSH[i],"نسبة التحليل غير طبيعية",TSH_Test_inarabic.get(TSH[i])))
        return resultList


    def AdrenalGland(Cortisol_AM=0.0, Cortisol_PM=0.0,ACTH_AM=0.0,ACTH_PM=0.0,Adrenaline=0.0,Noradrenaline=0.0,
                     Dopamine=0.0 ,Renin=0.0):
        AG=['Cortisol_AM', 'Cortisol_PM','ACTH_AM', 'ACTH_PM','Adrenaline', 'Noradrenaline' , 'Dopamine' ,'Renin']
        AG_User_Result={'Cortisol_AM':Cortisol_AM, 'Cortisol_PM':Cortisol_PM,'ACTH_AM':ACTH_AM,'ACTH_PM':ACTH_PM,
                        'Adrenaline':Adrenaline,'Noradrenaline':Noradrenaline , 'Dopamine':Dopamine ,'Renin':Renin}
        resultList=[]
        AG_Test={'Cortisol_AM':np.round(np.arange(6.2,19.5,0.01),2),
                 'Cortisol_PM':np.round(np.arange(2.3,19.5,0.01),2),
                 'ACTH_AM':np.round(np.arange(9,52.1,0.01),2),
                 'ACTH_PM':np.round(np.arange(0,10.1,0.01),2),
                 'Adrenaline' :np.round(np.arange(0,140.1,0.01),2),
                 'Noradrenaline' :np.round(np.arange(100,450.1,0.01),2), 
                 'Dopamine':np.round(np.arange(0,30.1,0.01),2) ,
                 'Renin':np.round(np.arange(1.9,3.8,0.01),2)}
        AG_Test_inarabic={'Cortisol_AM':'الكورتيزول الصباحي', 'Cortisol_PM':'الكورتيزول المسائي',
                 'ACTH_AM':'هرمون يفرز من الغدة النخامية في الدماغ', 'ACTH_PM':'هرمون يفرز من الغدة النخامية في الدماغ',
                 'Adrenaline' :'هرمون تقوم الغدة الكظرية بافرازه','Noradrenaline' :' يستخدم النوربينفرين لزيادة ضغط الدم والحفاظ عليه في حالات صحية خطيرة محدودة وقصيرة المدى',
                 'Dopamine':'هرمون يعزز من الشعور بالسعاد' ,'Renin':'إنزيم تقوم الكلى'}
        for i in range(0,len(AG)):
            if AG_User_Result[AG[i]] in AG_Test[AG[i]]:
                resultList.append((AG[i],"نسبة التحليل طبيعية",AG_Test_inarabic.get(AG[i])))
            else:
                resultList.append((AG[i],"نسبة التحليل غير طبيعية",AG_Test_inarabic.get(AG[i])))
        return resultList

    
    def ParathyroidHormoneTest(PH_User_Result=0.0):
        resultList=[]
        PH_Test={'Parathyroid Hormone Test':np.round(np.arange(10,55.1,0.01),2)}
        PH_Test_inarabic={'Parathyroid Hormone Test':'هرمون الغدة الجار درقية يساعد في الحفاظ على التوازن السليم للكالسيوم في مجرى الدم والأنسجة التي تعتمد على الكالسيوم من أجل أداء وظائفها بطريقة سليمة وهذا مهم خاصة لوظائف الأعصاب والعضلات، فضلاً عن صحة العظام'}
        if PH_User_Result in PH_Test['Parathyroid Hormone Test']:
            resultList.append(('Parathyroid Hormone Test',"نسبة التحليل طبيعية",PH_Test_inarabic.get('Parathyroid Hormone Test')))
        else:
            resultList.append(('Parathyroid Hormone Test',"نسبة التحليل غير طبيعية",PH_Test_inarabic.get('Parathyroid Hormone Test')))
        return resultList

                 
    def GrowthHormone(GH_User_Result=0.0,gender=''):
        resultList=[]
        if gender=='f':
            if GH_User_Result in np.round(np.arange(1,14.1,0.01),2):
                 resultList.append(("هرمون النمو لديك ذو نسبة طبيعية"))
            else:
                resultList.append(("هرمون النمو لديك ذو نسبة غير طبيعية"))
        elif gender=='m':
            if GH_User_Result in np.round(np.arange(0.4,110.1,0.01),2):
                 resultList.append(("هرمون النمو لديك ذو نسبة طبيعية"))
            else:
                resultList.append(("هرمون النمو لديك ذو نسبة غير طبيعية"))
        elif gender=='child':
            if GH_User_Result in np.round(np.arange(10,50.1,0.01),2):
                resultList.append(("هرمون النمو لديك ذو نسبة طبيعية"))
            else:
                resultList.append(("هرمون النمو لديك ذو نسبة غير طبيعية"))
        else:
            resultList.append(("من فضلك تاكد من ادخال البيانات بشكل صحيح"))
        return resultList
            

    def B_HCGTest(BHG_User_Result=0.0,status=''):    
        resultList=[]
        if status=='non':
            BHGN=np.round(np.arange(0,5.1,0.01),2)
        elif status=='m' :
            BHGN=np.round(np.arange(0,2.1,0.01),2)
        else:
            print("please choose the status")
        BHG_Test={'B-HCG Test':BHGN}
        BHG_Test_inarabic={'B-HCG Test':'فحص الهرمون الموجه للغدد التناسلية المشيمائية البشرية مثل معرفة اذا كانت المراة حامل ام لا '}
        if  BHG_User_Result in BHG_Test['B-HCG Test']:
            resultList.append(('B-HCG',"نسبة التحليل طبيعية",BHG_Test_inarabic.get('B-HCG Test')))
        elif BHG_User_Result in np.round(np.arange(5,72.1,0.01),2):
            resultList.append(('B-HCG',"نسبة التحليل تتجه الي انك حامل في الاسبوع الثالث",BHG_Test_inarabic.get('B-HCG Test')))
        elif BHG_User_Result in np.round(np.arange(10,708.1,0.01),2):
            resultList.append(('B-HCG',"نسبة التحليل تتجه الي انك حامل في الاسبوع الرابع",BHG_Test_inarabic.get('B-HCG Test')))
        else:
            resultList.append(('B-HCG',"نسبة التحليل غير طبيعية",BHG_Test_inarabic.get('B-HCG Test')))
        return resultList


    def DHEA_STest(DHEA_User_Result=0.0,status=''):
        resultList=[]
        DHEA_Test_inarabic={'DHEA-S Test':'أحد الهرمونات الذكرية الذي يتم إنتاجه في الغدة الكظرية'}
        if status=='f':
            DHEAN=np.round(np.arange(40,410.1,0.01),2)
            if DHEA_User_Result in DHEAN:
                resultList.append(('DHEA-S',"نسبة التحليل طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
            else:
                resultList.append(('DHEA-S',"نسبة التحليل غير طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
        elif status=='f-menopause':
            DHEAN=np.round(np.arange(0,100.1,0.01),2)
            if DHEA_User_Result in DHEAN:
                resultList.append(('DHEA-S',"نسبة التحليل طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
            else:
                resultList.append(('DHEA-S',"نسبة التحليل غير طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
        elif status=='m':
            DHEAN=np.round(np.arange(143,486.1,0.01),2)
            if DHEA_User_Result in DHEAN:
                resultList.append(('DHEA-S',"نسبة التحليل طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
            else:
                resultList.append(('DHEA-S',"نسبة التحليل غير طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
        elif status=='child':
            DHEAN=np.round(np.arange(0.3,3.9,0.01),2)
            if DHEA_User_Result in DHEAN:
                resultList.append(('DHEA-S',"نسبة التحليل طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
            else:
                resultList.append(('DHEA-S',"نسبة التحليل غير طبيعية",DHEA_Test_inarabic.get('DHEA-S Test')))
        else:
             resultList.append(("تاكد من ادخال البيانات بشكل صحيح"))
        return resultList



    def Hydroxyprogesterone(HYD_User_Result=0.0,status=''):
        resultList=[]
        HYD_F_Test={'first part of the menstrual cycle':np.round(np.arange(4.6,8.1,0.01),2),
                    'The second half of the menstrual cycle':np.round(np.arange(8,80.1,0.01),2),
                    'The last months of pregnancy':np.round(np.arange(234,1166.1,0.01),2)}
        HYD_F_Test_inarabic={'first part of the menstrual cycle':'خلال الجزء الأول من الدورة الشهرية',
                    'The second half of the menstrual cycle':'خلال النصف الثاني من الدورة الشهرية',
                    'The last months of pregnancy':'أثناء الأشهر الأخيرة للحمل'}
        if status=='f':
            if HYD_User_Result in HYD_F_Test['first part of the menstrual cycle']:
                resultList.append(('Hydroxyprogesterone',"نسبة التحليل طبيعية كما يعرف البروجسترون بأنه هرمون ستيرويدي ينتجه المبيض في جسم المرأة، ويلعب هرمون البروجسترون دوراً مهماً في الحمل، إذ يساعد في جعل الرحم جاهزاً لغرس البويضة المخصبة، ويكون مستوى البروجسترون أثناء الحمل أعلى بحوالي عشر مرات من مستواه عند المرأة غير الحامل",HYD_F_Test_inarabic.get('first part of the menstrual cycle')))
            elif HYD_User_Result in HYD_F_Test['The second half of the menstrual cycle']:
                resultList.append(('Hydroxyprogesterone',"نسبة التحليل طبيعية كما يعرف البروجسترون بأنه هرمون ستيرويدي ينتجه المبيض في جسم المرأة، ويلعب هرمون البروجسترون دوراً مهماً في الحمل، إذ يساعد في جعل الرحم جاهزاً لغرس البويضة المخصبة، ويكون مستوى البروجسترون أثناء الحمل أعلى بحوالي عشر مرات من مستواه عند المرأة غير الحامل",HYD_F_Test_inarabic.get('The second half of the menstrual cycle')))
            elif HYD_User_Result in HYD_F_Test['The last months of pregnancy']:
                resultList.append(('Hydroxyprogesterone',"نسبة التحليل طبيعية كما يعرف البروجسترون بأنه هرمون ستيرويدي ينتجه المبيض في جسم المرأة، ويلعب هرمون البروجسترون دوراً مهماً في الحمل، إذ يساعد في جعل الرحم جاهزاً لغرس البويضة المخصبة، ويكون مستوى البروجسترون أثناء الحمل أعلى بحوالي عشر مرات من مستواه عند المرأة غير الحامل",HYD_F_Test_inarabic.get('The last months of pregnancy')))
            else:
                resultList.append(('Hydroxyprogesterone',"نسبة التحليل غير طبيعية كما يعرف البروجسترون بأنه هرمون ستيرويدي ينتجه المبيض في جسم المرأة، ويلعب هرمون البروجسترون دوراً مهماً في الحمل، إذ يساعد في جعل الرحم جاهزاً لغرس البويضة المخصبة، ويكون مستوى البروجسترون أثناء الحمل أعلى بحوالي عشر مرات من مستواه عند المرأة غير الحامل"))
        elif status=='child' :
            if HYD_User_Result in np.round(np.arange(2.1,95.1,0.01),2):
                resultList.append(('Hydroxyprogesterone',"نسبة التحليل طبيعية هرمون البروجسترون عبارة عن هرمون يتم إنتاجه من خلال الغدد الكظرية" ))
            else:
                resultList.append(('Hydroxyprogesterone',"نسبة التحليل غير طبيعية هرمون البروجسترون عبارة عن هرمون يتم إنتاجه من خلال الغدد الكظرية" ))
        elif status=='m':
            if HYD_User_Result in np.round(np.arange(3,18.1,0.01),2):
                 resultList.append(('Hydroxyprogesterone',"نسبة التحليل طبيعية هرمون البروجسترون عبارة عن هرمون يتم إنتاجه من خلال الغدد الكظرية" ))
            else :
                 resultList.append(('Hydroxyprogesterone',"نسبة التحليل غير طبيعية هرمون البروجسترون عبارة عن هرمون يتم إنتاجه من خلال الغدد الكظرية" ))
        else:
            resultList.append(("من فضلك تاكد من ادخال البيانات بشكل صحيح"))
        return resultList
            
            
class TORCHIGg_IGM:
    def TORCHIGgf(Toxoplasma_IgM=0.0,Toxoplasma_IgG=0.0,Rubella_IgM=0.0,Rubella_IgG=0.0,
               CMV_IgM=0.0,CMV_IgG=0.0,HSV_IgM=0.0,HSV_IgG=0.0):
        TORCHL=['Toxoplasma_IgM','Toxoplasma_IgG','Rubella_IgM','Rubella_IgG',
               'CMV_IgM','CMV_IgG','HSV_IgM','HSV_IgG']
        TORCHL_User_Result={'Toxoplasma_IgM':Toxoplasma_IgM,'Toxoplasma_IgG':Toxoplasma_IgG,'Rubella_IgM':Rubella_IgM,
                            'Rubella_IgG':Rubella_IgG,'CMV_IgM':CMV_IgM,'CMV_IgG':CMV_IgG,'HSV_IgM':HSV_IgM,'HSV_IgG':HSV_IgG}
        resultList = []
        TORCHL_Test={'Toxoplasma_IgM':np.round(np.arange(0.178,24,0.001),3),
                     'Toxoplasma_IgG':np.round(np.arange(0.156,1.02,0.001),3),
                     'Rubella_IgM':np.round(np.arange(0.019,51.7,0.001),3),
                     'Rubella_IgG':np.arange(0.314,31.9,0.001),
                      'CMV_IgM':np.round(np.arange(0.314,31.9,0.001),3),
                     'CMV_IgG':np.round(np.arange(0.012,8.23,0.001),3),
                       'HSV_IgM':np.round(np.arange(0.081,2.75,0.001),3),
                     'HSV_IgG':np.round(np.arange(0.016,1.27,0.001),3)}
        TORCHL_Test_inarabic={'Toxoplasma_IgM':'داء المقوسات الطفيلي يمكن أن يسبب تشوهات خطيرة في الجنين مع وجود اجسام مضادة من نوع G','Toxoplasma_IgG':'داء المقوسات الطفيلي يمكن أن يسبب تشوهات خطيرة في الجنين مع وجود اجسام مضادة من نوع M',
                              'Rubella_IgM':'فيروس الحصبة الألمانية مع وجود اجسام مضادة من نوع G','Rubella_IgG':'فيروس الحصبة الألمانية مع وجود اجسام مضادة من M',
                              'CMV_IgM':'الفيروس المضخم للخلايا مع وجود اجسام مضادة من نوع G','CMV_IgG':'الفيروس المضخم للخلايا مع وجود اجسام مضادة من نوع M',
                              'HSV_IgM':'فيروس الهربس مع وجود اجسام مضادة من نوع G','HSV_IgG':'فيروس الهربس مع وجود اجسام مضادة من نوع M'}
        for i in range(0,len(TORCHL)):
            if TORCHL_User_Result[TORCHL[i]] in TORCHL_Test[TORCHL[i]]:
                resultList.append((TORCHL[i],"نسبة التحليل طبيعية",TORCHL_Test_inarabic.get(TORCHL[i])))
            else:
                resultList.append((TORCHL[i],"نسبة التحليل غير طبيعية",TORCHL_Test_inarabic.get(TORCHL[i])))
        return resultList
                
                
class TherapeuticDrugs:
    def phenytoin(phenytoin_User_Result=0.0):
        resultList = []
        if phenytoin_User_Result in np.round(np.arange(10,20,0.01),2):
             resultList.append(("نسبة دواء الفنيتوين لعلاج نوبات الصرع ضمن النسبة الطبيعية"))
        else:
             resultList.append(("نسبة دواء الفنيتوين لعلاج نوبات الصرع ليست ضمن النسبة الطبيعية"))
        return resultList
            
    def Carbamazepine(Carbamazepine_User_Result=0.0):
        resultList = []
        if Carbamazepine_User_Result in np.round(np.arange(4,12.1,0.01),2):
             resultList.append(("نسبة دواء الكاربامازيبين لعلاج اضطرابات الصرع، وألم الأعصاب ضمن النسبة الطبيعية"))
        else:
             resultList.append(("نسبة دواء الكاربامازيبين  لعلاج اضطرابات الصرع، وألم الأعصاب ليست ضمن النسبة الطبيعية"))
        return resultList

    def Digoxin(Digoxin_User_Result=0.0):
        resultList = []
        if Digoxin_User_Result in np.round(np.arange(2,8.1,0.01),2):
             resultList.append(("نسبة دواء الديجوكسين لعلاج قصور القلب ضمن النسبة الطبيعية"))
        else:
             resultList.append(("نسبة دواء الديجوكسين لعلاج قصور القلب  ليست ضمن النسبة الطبيعية"))
        return resultList

    def Lithium(Lithium_User_Result=0.0):
        resultList = []
        if Lithium_User_Result in np.round(np.arange(2,8.1,0.01),2):
             resultList.append(("نسبة دواء الليثيوم للمساعدة على منع عودة أعراض اضطراب الحالة المزاجیة ثنائي القطب مثل الاكتئاب أو الهوس ضمن النسبة الطبيعية"))
        else:
             resultList.append(("نسبة دواء الليثيوم  للمساعدة على منع عودة أعراض اضطراب الحالة المزاجیة ثنائي القطب مثل الاكتئاب أو الهوس ليست ضمن النسبة الطبيعية"))
        return resultList


class GeneticsAnalyses:
    def Karyotyping(Karyotyping_User_Result=0.0):
        resultList = []
        if Karyotyping_User_Result ==46:
            resultList.append(("عدد كروموزومات الانسجة ضمن النسبة الطبيعية"))
        else:
            resultList.append(("عدد كروموزومات الانسجة ليست ضمن النسبة الطبيعية"))
        return resultList

    def Aminograminplasma(status='',Alanine=0.0,Alpha_amino_N_butyric_acid=0.0,Arginine=0.0,
                          Asparagine=0.0,Aspartic_acid=0.0,Beta_alanine=0.0,Citrulline=0.0,
                          Cystine=0.0,Glutamic_acid=0.0,Glutamine=0.0,Glycine=0.0,
                          Histidine=0.0,Isoleucine=0.0,Leucine=0.0,Lysine=0.0,Methionine=0.0,
                          Ornithine=0.0,Phenylalanine=0.0,Proline=0.0,Serine=0.0,Taurine=0.0,
                        Threonine=0.0,Tyrosine=0.0,Valine=0.0,Alpha_aminoadipic_acid='',Beta_amino_isobutyric_acid='',
                          Carnosine='',Hydroxyproline='',i_methylhistidine=''):
        Aminogram=['Alanine','Alpha_amino_N_butyric_acid',
                  'Arginine','Asparagine','Aspartic_acid','Beta_alanine',
                  'Citrulline','Cystine','Glutamic_acid','Glutamine','Glycine',
                  'Histidine','Isoleucine','Leucine','Lysine','Methionine',
                  'Ornithine','Phenylalanine','Proline','Serine','Taurine',
                   'Threonine','Tyrosine','Valine']
        Aminogram2=['Alpha_aminoadipic_acid','Beta_amino_isobutyric_acid','Carnosine','Hydroxyproline',
                   '1_methylhistidine']
        Aminogram_User_Result={'Alanine':Alanine,'Alpha_amino_N_butyric_acid':Alpha_amino_N_butyric_acid,'Arginine':Arginine,
                               'Asparagine':Asparagine,'Aspartic_acid':Aspartic_acid,'Beta_alanine':Beta_alanine,
                                'Citrulline':Citrulline,'Cystine':Cystine,'Glutamic_acid':Glutamic_acid,'Glutamine':Glutamine,
                               'Glycine':Glycine,'Histidine':Histidine,'Isoleucine':Isoleucine,'Leucine':Leucine,'Lysine':Lysine,
                               'Methionine':Methionine,'Ornithine':Ornithine,'Phenylalanine':Phenylalanine,
                               'Proline':Proline,'Serine':Serine,'Taurine':Taurine,'Threonine':Threonine,'Tyrosine':Tyrosine,'Valine':Valine}
        Aminogram_User_Result2={'Alpha_aminoadipic_acid':Alpha_aminoadipic_acid,'Beta_amino_isobutyric_acid':Beta_amino_isobutyric_acid,
                                'Carnosine':Carnosine,'Hydroxyproline':Hydroxyproline,'1_methylhistidine':i_methylhistidine}
        resultList = []
        Aminogram_Test_A={'Alanine':np.round(np.arange(230,510.1,0.01),2),'Alpha_aminoadipic_acid':'not detected',
                  'Alpha_amino_N_butyric_acid':np.round(np.arange(15,41.1,0.01),2),'Arginine':np.round(np.arange(13,64.1,0.01),2),
                  'Asparagine':np.round(np.arange(45,130.1,0.01),2),'Aspartic_acid':np.round(np.arange(0,6.1,0.01),2),
                  'Beta_alanine':np.round(np.arange(0,29.1,0.01),2),'Beta_amino_isobutyric_acid':'not detected',
                  'Carnosine':'not detected','Citrulline':np.round(np.arange(16,55.1,0.01),2),'Cystine':np.round(np.arange(30,65.1,0.01),2),
                  'Glutamic_acid':np.round(np.arange(18,98.1,0.01),2),'Glutamine':np.round(np.arange(390,650.1,0.01),2),'Glycine':np.round(np.arange(170,330.1,0.01),2),
                  'Histidine':np.round(np.arange(26,120.1,0.01),2),'Hydroxyproline':'not detected','Isoleucine':np.round(np.arange(42,100.1,0.01),2),
                  'Leucine':np.round(np.arange(66,170.1,0.01),2),'Lysine':np.round(np.arange(150,220.1,0.01),2),'Methionine':np.round(np.arange(16,30.1,0.01),2),
                  '_methylhistidine':'not detected','3-methylhistidine':np.arange(0,64.1,0.001),'Ornithine':np.arange(27,80.1,0.001),
                  'Phenylalanine':np.round(np.arange(41,68.1,0.01),2),'Phosphoserine':np.round(np.arange(0,12,0.01),2),'Phosphoethanolamine':np.round(np.arange(0,55.1,0.01),2),
                  'Proline':np.round(np.arange(110,360.1,0.01),2),'Serine':np.round(np.arange(56,140.1,0.01),2),'Taurine': np.round(np.arange(45,130.1,0.01),2),
                'Threonine':np.round(np.arange(92,240.1,0.01),2), 'Tyrosine':np.round(np.arange(45,74.1,0.01),2),'Valine':np.round(np.arange(150,310.1,0.01),2)}

        Aminogram_Test_Ch={'Alanine':np.round(np.arange(200,450.1,0.01),2),'Alpha_aminoadipic_acid':'not detected',
              'Alpha_amino_N_butyric_acid':np.round(np.arange(8,37.1,0.01),2),'Arginine':np.round(np.arange(44,120.1,0.01),2),
              'Asparagine':np.round(np.arange(15,40.1,0.01),2),'Aspartic_acid':np.round(np.arange(0,26.1,0.01),2),
              'Beta_alanine':np.round(np.arange(0,49.1,0.01),2),'Beta_amino_isobutyric_acid':'not detected',
              'Carnosine':'not detected','Citrulline':np.arange(16,32.1,0.001),'Cystine':np.round(np.arange(19,47.1,0.01),2),
              'Glutamic_acid':np.round(np.arange(32,140.1,0.01),2),'Glutamine':np.round(np.arange(420,730.1,0.01),2),'Glycine':np.round(np.arange(110,240.1,0.01),2),
              'Histidine':np.round(np.arange(68,120.1,0.01),2),'Hydroxyproline':np.round(np.arange(0,5.1,0.01),2),'Isoleucine':np.round(np.arange(37,140.1,0.01),2),
              'Leucine':np.round(np.arange(70,170.1,0.01),2),'Lysine':np.round(np.arange(120,290.1,0.01),2),'Methionine':np.round(np.arange(13,30.1,0.01),2),
              '1_methylhistidine':'not detected','3-methylhistidine':np.round(np.arange(0,52.1,0.01),2),'Ornithine':np.round(np.arange(44,90.1,0.01),2),
              'Phenylalanine':np.round(np.arange(26,86.1,0.01),2),'Phosphoserine':np.round(np.arange(0,12,0.01),2),'Phosphoethanolamine':np.round(np.arange(0,12.1,0.01),2),
              'Proline':np.round(np.arange(130,290.1,0.01),2),'Serine':np.round(np.arange(93,150.1,0.01),2),'Taurine':np.round(np.arange(11,120.1,0.01),2),
                   'Threonine':np.round(np.arange(67,150.1,0.01),2),'Tyrosine':np.round(np.arange(26,110.1,0.01),2),'Valine':np.round(np.arange(160,350.1,0.01),2)}

        Aminogram_inarabic={'Alanine':'يعتبر الألانين  من أنواع الأحماض الأمينية  الأكثر استخداماً لبناء البروتين  مصدراً مهماً للطاقة اللازمة في بناء العضلات ،  تقوية جهاز المناعة، ويساعد أيضاً في عملية أيض السكريات والأحماض العضوية',
                 'Alpha_aminoadipic_acid':' حمض اميني الفا هو مقوم كيميائي من مقومات البروتين  ',
                 'Alpha_amino_N_butyric_acid':' حمض اميني الفا هو مقوم كيميائي من مقومات البروتين  ',
                 'Arginine':'يساهم الأرجينين  في عدد من الوظائف المختلفة في الجسم، كالتئام الجروح، ومساعدة الكلى على التخلص من فضلات الجسم، والحفاظ على وظيفة الهرمونات، كما ويعمل الأرجينين أيضاً على توسعة الشرايين',
                 'Asparagine':'هو حمض اميني بلوري موجود في البروتينات',
                 'Aspartic_acid':'يساعد حمض الأسبارتيك  في إنتاج الهرمونات وإفرازها لمختلف أنحاء الجسم،يحافظ على وظائف الجهاز العصبي ',
                 'Beta_alanine':'بيتا-ألانين هو حمض أميني له دور في تكوين البروتين وبالتالي في الأنشطة الحيوية بشكل غير مباشر',
                 'Citrulline':'سيترولين هو حمض أميني موجود في البطيخ، كما أنه يصنع في الجسم',
                 'Cystine':'يعتبر السيستين  من الأحماض الأمينية التي تعمل على إزالة السموم من الجسم، كما له دوراً هاماً في تصنيع العديد من البروتينات',
                 'Glutamic acid':'حمض الغلوتاميك حمض أميني، مركب عام للبروتين',
                 'Glutamine':'عزز الجلوتامين  وظائف الدماغ، كما ويعتبر ضرورياً لتكوين جزيئات الحمض النووي الريبوزييمكن',
                 'Glycine':'يعتبر الجلايسين  من مكونات الجلد الأساسية ويساعد في التئام الجروح، كما ويعمل كناقل عصبي، كما أن وجود الجلايسين بكميات كبيرة في الجسم قد يسبب الإعياء',
              'Histidine':'يعتبر الهيستيدين  من الأحماض الأمينية التي تعمل على: تكوين خلايا الدم, إصلاح الأنسجة, تنمية الذاكرة والوظيفة الإدراكية, تحسين عملية الهضم، وذلك من خلال تحفيز المعدة على إنتاج العصارة الهضمية، تحسين فعالية الأدوية المستخدمة في علاج السرطان',
              'Isoleucine':'يساهم الحمض الأميني الإيزولوسين  في العديد من الوظائف في الجسم، ومنها المساعدة على التئام الجروح. تنظيم نسبة السكر في الدم, تنظيم إنتاج الهرمونات',
                 'Leucine':'يساعد اللوسين في تنظيم مستويات السكر في الدم, نمو وإصلاح العضلات والعظام , التئام الجروح, إنتاج هرمون النمو',
                'Lysine':'ساعد اللوسين تنظيم مستويات السكر في الدم نمو وإصلاح العضلات والعظام , التئام الجروح , إنتاج هرمون النمو و نقص اللوسين قد يؤدي إلى الإصابة بطفح جلدي، وتساقط في الشعر، والإحساس بالتعب ',
                'Methionine':'يلعب الميثيونين دوراً أساسياً في صحة ومرونة الجلد والشعر، كما ويساعد في الحفاظ على قوة الأظافر،  يساعد على امتصاص السيلينيوم والزنك المهمان لصحة الجسم',
                 'Ornithine':'الأورنيثين هو من الأحماض الأمينية التي تلعب دورا في دورة اليوريا',
                 'Phenylalanine':'يساعد فينيل ألانين استخدام الأحماض الأمينية الأخرى، والبروتينات، والإنزيمات, تصنيع المشروبات الغازية الخاصة بالحمية الغذائية، حيث غالباً ما يوجد فينيل ألانين في المحلي الصناعي الأسبارتام',
                  'Proline':'يعتبر البرولين  من الأحماض الأمينية المهمة في نقل الإشارات العصبية داخل الخلايا، ويعتبر الحليب واللحوم من أفضل المصادر الغذائية للبرولين',
                 'Serine':'يعتبر السيرين  أحد البروتينات المكونة للدماغ، كما ويساعد في تكوين البروتينات اللازمة لعمل الجهاز المناعي، بالإضافة إلى أنه مفيد لنمو عضلات الجسم',
                 'Taurine':'يعتبر التورين  من الأحماض الأمينية غير الأساسية الضرورية لوظائف الدماغ، وتصنيع الأحماض الأمينية الأخرى، كما ويعتبر مهماً في امتصاص العناصر الغذائية، مثل المغنيسيوم، والكالسيوم، والبوتاسيوم',
                 'Threonine':'يعتبر الثريونين  من الأحماض الأمينية الضرورية للحفاظ على صحة الأسنان، الحفاظ على صحة الجلد، والأنسجة الضامة',
                 'Tyrosine':'يعتبر الحمض الأميني التربتوفان مهدئاً للأعصاب، ولهذا يساعد في تحسين التركيز وتقليل التوتر ,يمكن أن يتسب النقص بالإصابة بحالة تسمى البلاجرا ، والتي يمكن أن تؤدي إلى الخرف، والطفح الجلدي، ومشاكل في الجهاز الهضمي',
                'Valine':'الفالين  من الأحماض الأمينية التي تعمل على تحسين القدرة على التركيز والمحافظة على النشاط الذهني، كما ويعمل على تجديد أنسجة الجسم، ويجدر الذكر أنه قد يؤدي نقص الفالين إلى الإصابة بالأرق وانخفاض الوظيفة العقلية',
                   'Beta_amino_isobutyric_acid':'يمنع حمض الپروپيونيك نمو العفن وبعض أنواع الجراثيم','Carnosine':'هي مادة ينتجها الجسم بشكل طبيعي. يصنف على أنه ثنائي الببتيد، وهو مركب يتكون من اثنين من الأحماض الأمينية المرتبطة (الألانين و الهيستيدين)',
                    'Hydroxyproline':'هو عبارة عن حمض أميني مشهور بخواصه المفيدة للجلد والمضادة للأكسدة، يدخل في تركيب الكولاجين والإيلاستين (البروتينات التي تتحكم في مرونة الأنسجة الضامة)، وبالتالي يحمي الخلايا والأنسجة التالفة من فقدان مرونتها وقوامها، يدخل في تركيب الكثير من مستحضرات التجميل مثل كريمات العيون وكريمات الشد للنساء في فترة الحمل والمتقدمات بالعمر',
           '1_methylhistidine':'هو احادي ببتيد يحتوي على البيتا-ألانين والهستيدين، ويمكن أن يوجد في العضلات الهيكلية والدماغ عند الثدييات والطيور'}
        if status=='adult':
            for i in range(0,len(Aminogram)):
                if Aminogram_User_Result[Aminogram[i]] in Aminogram_Test_A[Aminogram[i]]:
                    resultList.append((Aminogram[i],"نسبة التحليل طبيعية",Aminogram_inarabic.get(Aminogram[i])))
                else:
                    resultList.append((Aminogram[i],"نسبة التحليل غير طبيعية",Aminogram_inarabic.get(Aminogram[i])))
            for i in range(0,len(Aminogram2)):
                if Aminogram_User_Result2[Aminogram2[i]] =='not detected':
                    resultList.append((Aminogram2[i],"نسبة التحليل طبيعية",Aminogram_inarabic.get(Aminogram2[i])))
                else:
                    resultList.append((Aminogram2[i],"نسبة التحليل غير طبيعية",Aminogram_inarabic.get(Aminogram2[i])))
        elif status=='child':
            for i in range(0,len(Aminogram)):
                if Aminogram_User_Result[Aminogram[i]] in Aminogram_Test_Ch[Aminogram[i]]:
                    resultList.append((Aminogram[i],"نسبة التحليل طبيعية",Aminogram_inarabic.get(Aminogram[i])))
                else:
                    resultList.append((Aminogram[i],"نسبة التحليل غير طبيعية",Aminogram_inarabic.get(Aminogram[i])))
            for i in range(0,len(Aminogram2)):
                if Aminogram_User_Result2[Aminogram2[i]] =='not detected':
                    resultList.append((Aminogram2[i],"نسبة التحليل طبيعية",Aminogram_inarabic.get(Aminogram2[i])))
                else:
                    resultList.append((Aminogram2[i],"نسبة التحليل غير طبيعية",Aminogram_inarabic.get(Aminogram2[i])))
        else:
            resultList.append(("من فضلك ادخل البيانات الصحيحة "))
        return resultList


class farmanalysis:
    def UrineTest(Colour='',Aspect='',Nitrite='',Albumin='',Suger='',Acetone='',Bile_Salts='',Bile_Pigments='',
             Urobilinogen='',Leukocyte_estrease='',Epithelial_Cells='', Casts='',Mucus='',Ova='',
                  Crystals='',Yeast_Cells='',Trichomonas_vaginalis='',Volume=0.0,Reaction=0.0,
                  Specific_Gravity_in_urine=0.0,RBCs=0.0,Pus_Cells=0.0):
        UR1=['Colour','Aspect','Nitrite','Albumin','Suger','Acetone','Bile_Salts','Bile_Pigments',
             'Urobilinogen','Leukocyte_estrease','Epithelial_Cells', 'Casts','Mucus','Ova','Crystals','Yeast_Cells','Trichomonas_vaginalis']                        
        UR2=['Volume','Reaction','Specific_Gravity_in_urine','RBCs','Pus_Cells']
        UR1_User_Result={'Colour':Colour,'Aspect':Aspect,'Nitrite':Nitrite,'Albumin':Albumin,'Suger':Suger,'Acetone':Acetone,
                         'Bile_Salts':Bile_Salts,'Bile_Pigments':Bile_Pigments,'Urobilinogen':Urobilinogen,
                         'Leukocyte_estrease':Leukocyte_estrease,'Epithelial_Cells':Epithelial_Cells,'Casts':Casts,
                         'Mucus':Mucus,'Ova':Ova,'Crystals':Crystals,'Yeast_Cells':Yeast_Cells,'Trichomonas_vaginalis':Trichomonas_vaginalis }
        UR2_User_Result={'Volume':Volume,'Reaction':Reaction,'Specific_Gravity_in_urine':Specific_Gravity_in_urine,'RBCs':RBCs,'Pus_Cells':Pus_Cells}
        resultList = []
        Urine_Test={'Colour':'yellow','Aspect':'clear','Volume':np.round(np.arange(0,1.6,0.01),2),
            'Reaction':np.round(np.arange(4,8.1,0.01),1),
            'Specific_Gravity_in_urine':np.round(np.arange(1.005,1.026,0.001),3),
           'Nitrite':'negative','Albumin':'negative','Suger':'negative','Acetone':'negative',
           'Bile_Salts':'negative','Bile_Pigments':'negative','Urobilinogen':'normal trace',
           'Leukocyte_estrease':'negative','RBCs':np.round(np.arange(0,1.1,0.01),2),
            'Pus_Cells':np.round(np.arange(0,1.1,0.01),2),'Epithelial_Cells':'nil',
            'Casts':'nil','Ova':'nil','Crystals':'nil','Mucus':'nil','Yeast_Cells':'nil','Trichomonas_vaginalis':'nil'}
        Urine_Test_inarabic={'Colour':'اللون','Aspect':'المظهر','Volume':'الحجم','Reaction':'درجة حموضة البول يشير قياس درجة الحموضة إلى كمية الحمض الموجودة في البول',
                             'Specific_Gravity_in_urine':'الثقل النوعي','Nitrite':'النتريت',
                        'Albumin':'البيليروبين','Suger':'الجلوكوز','Acetone':'الكيتونات','Bile_Salts':'املاح',
                             'Bile_Pigments':'الاصباغ','Urobilinogen':' البيليروبين ينتج عن  تكسر خلايا الدم الحمراء',
                        'Leukocyte_estrease':'دلائل العدوى','RBCs':'الدم','Pus_Cells':'خلايا صديد',
                             'Epithelial_Cells':'الخلايا الطهارية خلايا مختلطة بالبول',
                        'Casts':'الأسطوانات وهي بروتينات التي تشبه الأنابيب','Ova':'بويضات','Crystals':'البلورات التي تتكوّن من المواد الكيميائية في البول',
                             'Mucus':'مخاط','Yeast_Cells':'خلايا فطرية','Trichomonas_vaginalis':'المشعرات المهبلية'}
        for i in range(0,len(UR2)):
            if(UR2_User_Result[UR2[i]] in Urine_Test[UR2[i]]):
                resultList.append((UR2[i],"نسبة التحليل طبيعية",Urine_Test_inarabic.get(UR2[i])))
            else:
                resultList.append((UR2[i],"نسبة التحليل غير طبيعية",Urine_Test_inarabic.get(UR2[i])))

        for i in range(0,len(UR1)):
            if(UR1_User_Result[UR1[i]] == Urine_Test[UR1[i]]):
                resultList.append((UR1[i],"نسبة التحليل طبيعية",Urine_Test_inarabic.get(UR1[i])))
            else:
                resultList.append((UR1[i],"نسبة التحليل غير طبيعية",Urine_Test_inarabic.get(UR1[i])))
        return resultList

    def StoolAnalysis(Colour='',Odure='',Blood='',Consistency='',PH='',Worms='',Undigested_Food='',
         Epithelial_Cells='', Protozoa='',Helminths='',Yeast_Cells='',RBCs=0.0,Pus_Cells=0.0,Vegetable_cells='',
                      Starch='',Muscle_Fibers='',Fat=''):
        ST1=['Colour','Odure','Blood','Consistency','PH','Worms','Undigested_Food',
         'Epithelial_Cells', 'Protozoa','Helminths','Yeast_Cells']
        ST2=['RBCs','Pus_Cells']
        ST3=['Vegetable_cells','Starch','Muscle_Fibers','Fat']
        ST1_User_Result={'Colour':Colour,'Odure':Odure,'Blood':Blood,'Consistency':Consistency,'PH':PH,
                         'Worms':Worms,'Undigested_Food':Undigested_Food,'Epithelial_Cells':Epithelial_Cells,
                         'Protozoa':Protozoa,'Helminths':Helminths,'Yeast_Cells':Yeast_Cells}
        ST2_User_Result={'RBCs':RBCs,'Pus_Cells':Pus_Cells}
        ST3_User_Result={'Vegetable_cells':Vegetable_cells,'Starch':Starch,'Muscle_Fibers':Muscle_Fibers,'Fat':Fat}
        resultList = []
        Stool_Test={'Colour':'brown','Odure':'faecal','Consistency':'semi_formed','Blood':'nil','PH':'alkaline',
             'Worms':'nil','Undigested_Food':'nil',
            'Protozoa':'nil','Helminths':'nil','RBCs':np.round(np.arange(0,1.1,0.01),3),
            'Pus_Cells':np.round(np.arange(0,1.1,0.01),3),'Epithelial_Cells':'nil',
            'Mucus':'nil','Yeast_Cells':'nil'}
        Stool_Test2={'Vegetable cells':'few' or 'nil','Starch':'few' or 'nil','Muscle_Fibers':'few' or 'nil','Fat':'few' or 'nil'}
        Stoole_Test_inarabic={'Colour':'اللون','Odure':'الرائحة','Consistency':'الكثافة','PH':'درجة حموضة البول يشير قياس درجة الحموضة إلى كمية الحمض الموجودة في البراز',
                        'Blood':'الدم','Worms':'جهازيته للعمل عليه','Undigested_Food':'الطعام الغير مهضوم','Starch':'نشي',
                        'Muscle_Fibers':'الالياف العضلية','Fat':'الدهون','Protozoa':'الكائنات الاوليه',
                       'Helminths':'الديدان الطفيلية','RBCs':' خلايا الدم','Pus_Cells':'خلايا صديد','Epithelial_Cells':'الخلايا الطهارية خلايا مختلطة بالبول',
                       'Mucus':'مخاط','Yeast_Cells':'خلايا فطرية','Vegetable_cells':'خلايا نباتية'}
        s_matching={'state 1':'few','state 2':'nil'}
        for i in range(0,len(ST1)):
            if ST1_User_Result[ST1[i]] in Stool_Test[ST1[i]] :
                resultList.append((ST1[i],"نسبة التحليل طبيعية",Stoole_Test_inarabic.get(ST1[i])))
            else:
                resultList.append((ST1[i],"نسبة التحليل غير طبيعية",Stoole_Test_inarabic.get(ST1[i])))

        for i in range(0,len(ST2)):
            if ST2_User_Result[ST2[i]] in Stool_Test[ST2[i]]:
                 resultList.append((ST2[i],"نسبة التحليل طبيعية",Stoole_Test_inarabic.get(ST2[i])))
            else:
                resultList.append((ST2[i],"نسبة التحليل غير طبيعية",Stoole_Test_inarabic.get(ST2[i])))
        for i in range(0,len(ST3)):
            if ST3_User_Result[ST3[i]] in  s_matching['state 1'] or ST3_User_Result[ST3[i]] in s_matching['state 2'] :
                resultList.append((ST3[i],"نسبة التحليل طبيعية",Stoole_Test_inarabic.get(ST3[i])))
            else:
                resultList.append((ST3[i],"نسبة التحليل غير طبيعية",Stoole_Test_inarabic.get(ST3[i])))
            return resultList

    def Prostatic(RBCs=0.0,Pus_Cells=0.0,Bilharzial_Ova='',Trichomonas_vaginalis=''):
        P1=['RBCs','Pus_Cells']
        P2=['Bilharzial_Ova','Trichomonas_vaginalis']
        P1_User_Result={'RBCs':RBCs,'Pus_Cells':Pus_Cells}
        P2_User_Result={'Bilharzial_Ova':Bilharzial_Ova,'Trichomonas_vaginalis':Trichomonas_vaginalis}
        resultList = []
        P_Test={'RBCs':np.round(np.arange(0,1.1,0.01),3),'Pus_Cells':np.round(np.arange(0,1.1,0.01),3),
                     'Bilharzial_Ova':'absent'or 'nil','Trichomonas_vaginalis':'absent'or 'nil'}
        P_Test_inarabic={'RBCs':'خلايا الدم الحمراء','Pus Cells':'خلايا صديد',
                             'Bilharzial_Ova':'بلهاريسيا','Trichomonas_vaginalis':'المشعرات المهبلية'}
        s_matching={'state 1':'absent','state 2':'nil'}

        for i in range(0,len(P1)):
            if P1_User_Result[P1[i]] in P_Test[P1[i]]:
                resultList.append((P1[i],"نسبة التحليل طبيعية",P_Test_inarabic.get(P1[i])))
            else:
                resultList.append((P1[i],"نسبة التحليل غير طبيعية",P_Test_inarabic.get(P1[i])))
        for i in range(0,len(P2)):
            if P2_User_Result[P2[i]] in s_matching['state 1'] or P2_User_Result[P2[i]] in s_matching['state 2'] :
                resultList.append((P2[i],"نسبة التحليل طبيعية",P_Test_inarabic.get(P2[i])))
            else:
                resultList.append((P2[i],"نسبة التحليل غير طبيعية",P_Test_inarabic.get(P2[i])))
            return resultList

    def VaginalExam(Vaginal_User_result=''):
        resultList = []
        if Vaginal_User_result=='negative':
            resultList.append(('نتجية الفحص المهبلي طبيعية '))
        else:
            resultList.append(('نتيجة الفحص المهبلي غير طبيعية '))
        return resultList
            
    def VaginalExam2(Vaginal_User_result=0.0):
        resultList = []
        if  Vaginal_User_result in np.round(np.arange(0,1.1,0.01),2) :
            resultList.append(('نتجية الفحص المهبلي طبيعية '))
        else:
            resultList.append(('نتيجة الفحص المهبلي غير طبيعية '))
        return resultList


    def SemenExam(Color='',Method_of_production='',Abstinence=0.0,Volume=0.0,Liquefaction_Time=0.0,PH=0.0,Sperm_Count=0.0):
        Semenl1=['Color','Method_of_production']
        Semenl2=['Abstinence','Volume','Liquefaction_Time','PH','Sperm_Count']
        Semenl1_User_result={'Color':Color,'Method_of_production':Method_of_production}
        Semenl2_User_result={'Abstinence':Abstinence,'Volume':Volume,'Liquefaction_Time':Liquefaction_Time,'PH':PH,'Sperm_Count':Sperm_Count}
        resultList = []
        semen_test={'Color':'Gray'or 'White','Method_of_production':'masterbuation',
                    'Abstinence':np.round(np.arange(3,5.1,0.01),3),'Volume':np.round(np.arange(1,5.1,0.01),2),
                    'Liquefaction_Time':np.round(np.arange(0,30.1,0.01),2),'PH':np.round(np.arange(7.2,8.1,0.01),2),
            'Sperm_Count':np.round(np.arange(0,20.1,0.01),2)}
        s_match={'Color 1':'gray','Color 2':'white'}
        semen_test_inarabic={'Color':'اللون','Method_of_production':'Masterbuation',
                           'Abstinence':'التقشف','Volume':'الحجم','Liquefaction_Time':'وقت التسييل',
                    'PH':'درجة الحموضة','Sperm_Count':'عدد الحيوانات المنوية'}          
        for i in range(0,len(Semenl1)):
            if Semenl1[i]=='Color':
                if Semenl1_User_result[Semenl1[i]] in s_match['Color 1'] or Semenl1_User_result[Semenl1[i]] in s_match['Color 2']:
                    resultList.append(("اللون طبيعي",Semenl1[i]))
                else:
                    resultList.append(("اللون غير طبيعي",Semenl1[i]))
                    
            elif Semenl1[i]=='Method of production':
                if Semenl1_User_result[Semenl1[i]] in semen_test[Semenl1[i]]:
                    resultList.append((Semenl1[i],"نسبة التحليل طبيعية",semen_test_inarabic.get(Semenl1[i])))
                else:
                    resultList.append((Semenl1[i],"نسبة التحليل غير طبيعية",semen_test_inarabic.get(Semenl1[i])))

        for i in range(0,len(Semenl2)):
            if Semenl2_User_result[Semenl2[i]] in semen_test[Semenl2[i]]:
                resultList.append((Semenl2[i],"نسبة التحليل طبيعية",semen_test_inarabic.get(Semenl2[i])))
            else:
                resultList.append((Semenl2[i],"نسبة التحليل غير طبيعية",semen_test_inarabic.get(Semenl2[i])))
        return resultList

    def CSFExam(Appearance='',Gram_Stain='',Pressure=0.0,Protein=0.0,Glucose=0.0,WCC=0.0,Glucose_serum_ratio=0.0):
        CSFl1=['Appearance','Gram_Stain']
        CSFl2=['Pressure','Protein','Glucose','WCC','Glucose_serum_ratio']
        CSFl1_User_result={'Appearance':Appearance,'Gram_Stain':Gram_Stain}
        CSFl2_User_result={'Pressure':Pressure,'Protein':Protein,'Glucose':Glucose,'WCC':WCC,'Glucose_serum_ratio':Glucose_serum_ratio}
        resultList = []
        CSF_test={'Pressure':np.arange(7,18.1,0.001),'Appearance':'Clear'or 'Colorless',
                            'Protein':np.arange(23,38.1,0.001),'Glucose':np.arange(2.5,3.5,0.001),
                    'Gram_Stain':'negative','Glucose_serum_ratio':range(0),'WCC':np.arange(0,5.1,0.001)}
        s_match={'Appearance 1':'clear','Appearance 2':'colorless'}
        CSF_test_inarabic={'Pressure':'الضغط','Appearance':'المظهر',
                            'Protein':'البرروتين','Glucose':'الجلوكوز',
                            'Gram_Stain':'الميكروبات','Glucose_serum_ratio':'نسبة مصل الجلوكوز','WCC':'عدد كريات الدم البيضاء'} 
        for i in range(0,len(CSFl1)):
            if CSFl1[i]=='Appearance':
                if CSFl1_User_result[CSFl1[i]] in s_match['Appearance 1'] or CSFl1_User_result[CSFl1[i]] in s_match['Appearance 2']:
                    resultList.append((CSFl1[i],"نسبة التحليل طبيعية",CSF_test_inarabic.get(CSFl1[i])))
                else:
                    resultList.append((CSFl1[i],"نسبة التحليل غير طبيعية",CSF_test_inarabic.get(CSFl1[i])))
            elif CSFl1[i]=='Gram Stain':    
                if CSFl1_User_result[CSFl1[i]] in CSF_test[CSFl1[i]]:
                    resultList.append((CSFl1[i],"نسبة التحليل طبيعية",CSF_test_inarabic.get(CSFl1[i])))
                else:
                    resultList.append((CSFl1[i],"نسبة التحليل غير طبيعية",CSF_test_inarabic.get(CSFl1[i])))
            else:
                resultList.append(("تاكد من ادخال البيانات بشكل صحيح "))

        for i in range(0,len(CSFl2)):
            if CSFl2_User_result[CSFl2[i]] in CSF_test[CSFl2[i]]:
                resultList.append((CSFl2[i],"نسبة التحليل طبيعية",CSF_test_inarabic.get(CSFl2[i])))
            else:
                resultList.append((CSFl2[i],"نسبة التحليل غير طبيعية",CSF_test_inarabic.get(CSFl2[i])))
        return resultList
                

class AofSTdiseases:
    def SyphilisTests(RPR='',VDRL=''):
        SyphilisL=['RPR', 'VDRL']
        SyphilisL_User_Result={'RPR':RPR, 'VDRL':VDRL}
        resultList = []
        Syphilis_Test_inarabic={'RPR':'كشف الأجسام المضادة التي ينتجها الجسم ضد الزهري يصاب الفرد بعدوى بكتيرية تسمى اللولبية الشاحبة',
                                'VDRL':'للكشف عن الأجسام المضادة'}
        for i in range(0,len(SyphilisL)):
            if  SyphilisL_User_Result[SyphilisL[i]] =='negative':
                resultList.append((SyphilisL[i],"نسبة التحليل طبيعية",Syphilis_Test_inarabic.get(SyphilisL[i])))
            else:
                resultList.append((SyphilisL[i],"نسبة التحليل غير طبيعية",Syphilis_Test_inarabic.get(SyphilisL[i])))
        return resultList
                
    def SyphilisTests2(RPR=0.0,VDRL=0.0):
        SyphilisL=['RPR', 'VDRL']
        SyphilisL_User_Result={'RPR':RPR, 'VDRL':VDRL}
        resultList = []
        Syphilis_Test_inarabic={'RPR':'كشف الأجسام المضادة التي ينتجها الجسم ضد الزهري يصاب الفرد بعدوى بكتيرية تسمى اللولبية الشاحبة',
                                'VDRL':'للكشف عن الأجسام المضادة'}
        for i in range(0,len(SyphilisL)):
            if SyphilisL_User_Result[SyphilisL[i]] in np.round(np.arange(0,1.1,0.01),2):
                resultList.append((SyphilisL[i],"نسبة التحليل طبيعية",Syphilis_Test_inarabic.get(SyphilisL[i])))
            else:
                resultList.append((SyphilisL[i],"نسبة التحليل غير طبيعية",Syphilis_Test_inarabic.get(SyphilisL[i])))
        return resultList

    def AIDSTest(HIV_AB_User_Result=''):
        resultList = []
        if HIV_AB_User_Result=='negative':
            resultList.append(("لم يظهر لديك فيروس نقص المناعة البشرية"))
        else:
            resultList.append(("تظهرنتيجة التحليل بان لديك فيروس نقص المناعة البشرية"))
        return resultList
    
    def AIDSTest2(HIV_AB_User_Result=0.0):
        resultList = []
        if  HIV_AB_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append(("لم يظهر لديك فيروس نقص المناعة البشرية"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك فيروس نقص المناعة البشرية"))
        return resultList

                
    def ChlamydiaTest(AbChlamydia_User_Result=''):
        resultList = []
        if AbChlamydia_User_Result=='negative':
            resultList.append(("لم تظهر لديك عدوي بكتيرية"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك عدوي بكتيرية"))
        return resultList
            
    def ChlamydiaTest2(AbChlamydia_User_Result=0.0):
        resultList = []
        if  AbChlamydia_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append(("لم تظهر لديك عدوي بكتيرية"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك عدوي بكتيرية")) 
        return resultList
       
    def HerpesSimplexVirusTest(HSV_User_Result=''):
        resultList = []
        if HSV_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي اصابة بفيروس الهربيس البسيط وهو فيروس مناعي"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك اصابة بفيروس الهربيس البسيط وهو فيروس مناعي "))
        return resultList
            
    def HerpesSimplexVirusTest2(HSV_User_Result=0.0):
        resultList = []
        if  HSV_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append(("لم يظهر لديك اي اصابة بفيروس الهربيس البسيط وهو فيروس مناعي"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك اصابة بفيروس الهربيس البسيط وهو فيروس مناعي ")) 
        return resultList

    def HepatitisBBloodTests(HBS_User_Result=''):
        resultList = []
        if HBS_User_Result=='negative':
            resultList.append((" لم يظهر لديك التهاب الكبد الفيروسي ب"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك اصابة بالالتهاب الكبد الفيروسي ب"))
        return resultList
            
    def HepatitisBBloodTests2(HBS_User_Result=0.0):
        resultList = []
        if  HBS_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append(("لم يظهر لديك التهاب الكبد الفيروسي ب"))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك اصابة بالالتهاب الكبد الفيروسي ب"))
        return resultList
            

class Tuberculosis:
    def TBTest(TBS_User_Result=''):
        resultList = []
        if TBS_User_Result=='negative':
            resultList.append((" لم يظهر في نتيجة التحليل بانك مصاب بمرض السل"))
        else:
            resultList.append(("تظهر نتيجة التحليل بانه من المحتمل الاصابة بمرض السل"))
        return resultList
            
    def TBTest2(TBS_User_Result=0.0):
        resultList = []
        if  TBS_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر في نتيجة التحليل بانك مصاب بمرض السل"))
        else:
            resultList.append(("تظهر نتيجة التحليل بانه من المحتمل الاصابة بمرض السل"))
        return resultList
    

class ImmuneDiseases:
    def AntinuclearAntibodyTest(AN_User_Result=''):
        resultList = []
        if AN_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي اضطرابات في المناعة الذاتية "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك اضطرابات في المناعة الذاتية"))
        return resultList

    def AntinuclearAntibodyTest2(AN_User_Result=0.0):
        resultList = []
        if  AN_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر لديك اي اضطرابات في المناعة الذاتية "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك اضطرابات في المناعة الذاتية "))
        return resultList

    def AntiSmoothMuscleAntibodyTest(ASMA_User_Result=''):
        resultList = []
        if ASMA_User_Result=='negative':
             resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة ضد العضلات الملساء في الدم "))
        else:
             resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة ضد العضلات الملساء في الدم"))
        return resultList
    
    def AntiSmoothMuscleAntibodyTest2(ASMA_User_Result=0.0):
        resultList = []
        if  ASMA_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة ضد العضلات الملساء في الدم "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة ضد العضلات الملساء في الدم"))
        return resultList

    def AntiMitochondrialAntibodyTest(AMA_User_Result=''):
        resultList = []
        if AMA_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للميتوكوندريا وهي مثال علي الاستجابة المناعية الذاتية التي تحدث عندما ينقلب الجسم ضد الاوعية الدموية "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة للميتوكوندريا وهي مثال علي الاستجابة المناعية الذاتية التي تحدث عندما ينقلب الجسم ضد الاوعية الدموية"))
        return resultList

    def AntiMitochondrialAntibodyTest2(AMA_User_Result=0.0):
        resultList = []
        if  AMA_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للميتوكوندريا وهي مثال علي الاستجابة المناعية الذاتية التي تحدث عندما ينقلب الجسم ضد الاوعية الدموية "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة للميتوكوندريا وهي مثال علي الاستجابة المناعية الذاتية التي تحدث عندما ينقلب الجسم ضد الاوعية الدموية"))
        return resultList

            
    def AntiDNATest(ADNA_User_Result=''):
        resultList = []
        if ADNA_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للحمض النووي المضاعف "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة ضد الحمض النووي المضاعف"))
        return resultList
            
    def AntiDNATest2(ADNA_User_Result=0.0):
        resultList = []
        if  ADNA_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للحمض النووي المضاعف "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة ضد الحمض النووي المضاعف"))  
        return resultList

    def AntiliverkidneyMicrosomalTest(ALKM_User_Result=''):
        resultList = []
        if ALKM_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للالتهاب الكبدي "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة للالتهاب الكبدي"))
        return resultList
    
    def AntiliverkidneyMicrosomalTest2(ALKM_User_Result=0.0):
        resultList = []
        if  ALKM_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للالتهاب الكبدي "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة للالتهاب الكبدي")) 
        return resultList

    def AntineutrophilCytoplasmicAntibodiesTest(ANCA_User_Result=''):
        resultList = []
        if ANCA_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للسيتوبلازم "))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك أجسام مضادة للسيتوبلازم"))
        return resultList
            
    def AntineutrophilCytoplasmicAntibodiesTest2(ANCA_User_Result=0.0):
        resultList = []
        if  ANCA_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append(("لم يظهر لديك اي وجود لأجسام مضادة للسيتوبلازم"))
        else:
            resultList.append(("تُظهر نتيجة التحليل بان لديك أجسام مضادة للسيتوبلازم " )) 
        return resultList

    def AntiPlateletABTest(AP_User_Result=''):
        resultList = []
        if AP_User_Result=='negative':
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للصفائح الدموية "))
        else:
            resultList.append(("تُظهر نتيجة التحليل بان لديك أجسام مضادة للصفائح الدموية"))
        return resultList
    
    def AntiPlateletABTest2(AP_User_Result=0.0):
        resultList = []
        if  AP_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للصفائح الدموية "))
        else:
            resultList.append(("تُظهر نتيجة التحليل بان لديك أجسام مضادة للصفائح الدموية")) 
        return resultList


    def AntiSpermABTest(AS_User_Result=0.0):
        resultList = []
        if AS_User_Result in np.round(np.arange(0,60.1,0.01),2):
            resultList.append((" لم يظهر لديك اي وجود لأجسام مضادة للحيوانات المنوية "))
        else:
            resultList.append(("تُظهر نتيجة التحليل بان لديك أجسام مضادة للحيوانات المنوية "))
        return resultList

    def ComplementSystemTest(gender='',C3=0.0,C4=0.0):
        CSL=['C3','C4']
        CSL_User_Result={'C3':C3,'C4':C4}
        resultList = []
        CS_Test_inarabic={'C3':'بروتين سي 3','C4':'بروتين سي 4'}
        if gender=='f':
            for i in range(0,len(CSL)):
                C3N=np.round(np.arange(88,206.1,0.01),2)
                C4N=np.round(np.arange(16,48.1,0.01),2)
                CS_Test={'C3':C3N,'C4':C4N}
                if CSL_User_Result[CSL[i]] in CS_Test[CSL[i]]:
                    resultList.append((CSL[i],"نسبة التحليل طبيعية",CS_Test_inarabic.get(CSL[i])))
                else:
                    resultList.append((CSL[i],"نسبة التحليل غير طبيعية",CS_Test_inarabic.get(CSL[i])))
        elif gender=='ch' :
            for i in range(0,len(CSL)):
                C3N=np.round(np.arange(88,201.1,0.01),2)
                C4N=np.round(np.arange(15,45.1,0.01),2)
                CS_Test={'C3':C3N,'C4':C4N}
                if CSL_User_Result[CSL[i]] in CS_Test[CSL[i]]:
                    resultList.append((CSL[i],"نسبة التحليل طبيعية",CS_Test_inarabic.get(CSL[i])))
                else:
                   resultList.append((CSL[i],"نسبة التحليل غير طبيعية",CS_Test_inarabic.get(CSL[i])))
        elif gender=='m':
            for i in range(0,len(CSL)):
                C3N=np.round(np.arange(88,252.1,0.01),2)
                C4N=np.round(np.arange(16,48.1,0.01),2)
                CS_Test={'C3':C3N,'C4':C4N}
                if CSL_User_Result[CSL[i]] in CS_Test[CSL[i]]:
                    resultList.append((CSL[i],"نسبة التحليل طبيعية",CS_Test_inarabic.get(CSL[i])))
                else:
                    resultList.append((CSL[i],"نسبة التحليل غير طبيعية",CS_Test_inarabic.get(CSL[i])))
        else:
            print("من فضلك تاكد من ادخال النتائج بشكل صحيح")
        return resultList

                      
class SensitivityAnalyses:
     def FoodpanelallergenspecificTest(food='',IgE_Test=''):
        resultList = []
        if IgE_Test =='negative':
            resultList.append((" لم يظهر لديك اي حساسية  ",food))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك حساسية  ",food))
        return resultList
 
     def FoodpanelallergenspecificTest2(food='',IgE_Test=0.0):
        resultList = []
        if IgE_Test in np.round(np.arange(0,60.1,0.01),2):
            resultList.append((" لم يظهر لديك اي حساسية  ",food))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك حساسية  ",food))
        return resultList       
            

class TumorsTest:
    def CEABreastTest(status='',CEA_User_Result=0.0):
        resultList = []
        if status=='no':
            if CEA_User_Result in np.round(np.arange(0,2.6,0.01),2):
                resultList.append(("  نسبتك طبيعية و هو عبارة عن بروتين ينتج من خلايا الثدي بشكل طبيعي، لكن يزداد إفرازه في حالات الإصابة بسرطان الثدي",'CA15.3' ))
            else:
                resultList.append(("تظهر نتيجة التحليل بان نسبتك غير طبيعية  و هو عبارة عن بروتين ينتج من خلايا الثدي بشكل طبيعي، لكن يزداد إفرازه في حالات الإصابة بسرطان الثدي",'CA15.3'))
        elif status=='yes':
            if CEA_User_Result in np.round(np.arange(0,5.1,0.01),2):
                resultList.append(("  نسبتك طبيعية و هو عبارة عن بروتين ينتج من خلايا الثدي بشكل طبيعي، لكن يزداد إفرازه في حالات الإصابة بسرطان الثدي",'CA15.3'))
            else:
                resultList.append(("تظهر نتيجة التحليل بان نسبتك غير طبيعية و هو عبارة عن بروتين ينتج من خلايا الثدي بشكل طبيعي، لكن يزداد إفرازه في حالات الإصابة بسرطان الثدي",'CA15.3'))
        else:
            print("من فضلك تاكد من ادخال النتائج بشكل صحيح")
        return resultList

    def CEAUterus_OvariesTest(CEA_U_O_User_Result=0.0):
        resultList = []
        if CEA_U_O_User_Result in np.round(np.arange(0,35.1,0.01),2):
            resultList.append(("نسبة تحليلك طبيعية و هو عبارة عن بروتين يزداد إفرازه في حالات الإصابة بسرطان المبيض",'CA125'))
        else:
            resultList.append(("تظهر نتيجة التحليل بان لديك نسبة غير طبيعية و هو عبارة عن بروتين يزداد إفرازه في حالات الإصابة بسرطان المبيض",'CA125'))
        return resultList
      
    def ThyroidGlandTest(TG_User_Result=0.0):
        resultList = []
        if TG_User_Result in np.round(np.arange(1.1,2.2,0.01),2):
            resultList.append((" لم يظهر لديك نسب غير طبيعية كما يجرى تحليل الغلوبيولين المرتبط بالثيروكسين هذا التحليل لتقييم وظائف الغدة الدرقية وتشخيص أي اضطرابات قد تصيبها كما يستخدم أيضاً لتشخيص أي اضطرابات أخرى في الجسم قد تؤثر على مستويات ووظائف هرمونات الغدة الدرقية في الجسم",'TBG'))
        else:
            resultList.append((" تظهر نتيجة التحليل بان لديك نسبة غير طبيعية كما يجرى تحليل الغلوبيولين المرتبط بالثيروكسين هذا التحليل لتقييم وظائف الغدة الدرقية وتشخيص أي اضطرابات قد تصيبها كما يستخدم أيضاً لتشخيص أي اضطرابات أخرى في الجسم قد تؤثر على مستويات ووظائف هرمونات الغدة الدرقية في الجسم",'TBG'))
        return resultList

    def PinealGlandTest(PG_User_Result=0.0,status=''):
        resultList = []
        if status=='f':
            if PG_User_Result in np.round(np.arange(2,29.1,0.01),2):
                resultList.append(("نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود ورم سرطاني ام لا "))
            else:
                 resultList.append((" نسبتك غير طبيعية يحدد هذا وجود ورم سرطاني ام لا"))
        elif status=='f-pregnant' :
            if PG_User_Result in np.round(np.arange(10,209.1,0.01),2):
                resultList.append(("نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود ورم سرطاني ام لا "))
            else:
                 resultList.append((" نسبتك غير طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود ورم سرطاني ام لا"))
        elif status=='m':
            if PG_User_Result in np.round(np.arange(2,18.1,0.01),2):
                resultList.append(("نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود ورم سرطاني ام لا "))
            else:
                 resultList.append((" نسبتك غير طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود ورم سرطاني ام لا"))
        else:
            resultList.append(("من فضلك تاكد من ادخال النتائج بشكل صحيح"))
        return resultList

            
    def AlphaFetoproteinTest(AFP_User_Result=0.0):
        resultList = []
        if AFP_User_Result in np.round(np.arange(10,20.1,0.01),2):
            resultList.append((" نسبتك طبيعية يقيس هذا التحليل كمية بروتين الفا فيتو عند الأفراد البالغين تعرف مؤشرات الورم بأنها مواد تصنعها الخلايا الطبيعية استجابة للسرطان، أو الخلايا السرطانية، إذ يتم إفرازها بمستويات أعلى من المستويات الطبيعية عند وجود أورام، كما أن معظمها عبارة عن بروتينات",'Alpha Fetoprotein'))
        else:
            resultList.append(("نسبتك غير طبيعية يقيس هذا التحليل كمية بروتين الفا فيتو عند الأفراد البالغين تعرف مؤشرات الورم بأنها مواد تصنعها الخلايا الطبيعية استجابة للسرطان، أو الخلايا السرطانية، إذ يتم إفرازها بمستويات أعلى من المستويات الطبيعية عند وجود أورام، كما أن معظمها عبارة عن بروتينات ",'Alpha Fetoprotein')) 
        return resultList

    
    def KidneyTest(Renin_User_Result=0.0):
        resultList = []
        if Renin_User_Result in np.round(np.arange(1.9,3.8,0.01),2):
            resultList.append((" نسبتك طبيعية , الرنين هو إنزيم تقوم الكلى بإفرازه، ويقوم هو بتفعيل منظومة الرينين أنجيوتنسين ، هذه المنظومة هي المسؤولة بالأساس عن إفراز الغدة الكظرية للألدوستيرون للتحكم بمستويات ضغط الدم، كما أنها المسؤولة عن انقباض الأوعية الدموية"))
        else:
            resultList.append((" نسبتك غير طبيعية , الرنين هو إنزيم تقوم الكلى بإفرازه، ويقوم هو بتفعيل منظومة الرينين أنجيوتنسين ، هذه المنظومة هي المسؤولة بالأساس عن إفراز الغدة الكظرية للألدوستيرون للتحكم بمستويات ضغط الدم، كما أنها المسؤولة عن انقباض الأوعية الدموية"))
        return resultList

    
    def TestisTest(Erythropoitein_User_Result=0.0):
        resultList = []
        if Erythropoitein_User_Result in np.round(np.arange(2.6,18.6,0.01),2):
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل لاكتشاف وجود سرطان ام لا ",'Erythropoitein'))
        else:
            resultList.append(("نسبتك غير طبيعية من المحتمل وجود ورم سرطاني يحدد هذا التحليل لاكتشاف وجود سرطان ام لا",'Erythropoitein') ) 
        return resultList

    def ProstateTest(PSA_User_Result=0.0):
        resultList = []
        if PSA_User_Result in np.round(np.arange(0,4.6,0.01),2):
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل لاكتشاف وجود سرطان ام لا "))
        elif PSA_User_Result in np.round(np.arange(4,10.1,0.01),2):
            resultList.append((" نسبة التحليل تثير الشكوك تجاه سرطان البروستاتا "))  
        else:
            resultList.append(("نسبة التحليل تتجه تجاه سرطان البروستاتا ")) 
        return resultList

                 
    def DigestiveTest(CA19_User_Result=0.0):
        resultList = []
        if CA19_User_Result in np.round(np.arange(0,37.1,0.01),2):
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل لاكتشاف سرطان في الجهاز الهضمي ام لا "))   
        else:
            resultList.append(("نسبة التحليل يحدد غير طبيعية تتجه تجاه وجود سرطان في الجهاز الهضمي ")) 
        return resultList


    def LungCancerTumorMarkersTest(LCT_User_Result=''):
        resultList = []
        if LCT_User_Result =='negative':
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود سرطان في الرئة ام لا ",'CA 19.9'))   
        else:
            resultList.append(("نسبتك غير طبيعية تتجه تجاه السرطان يحدد هذا التحليل وجود سرطان في الرئة  ام لا " ,'CA 19.9')) 
        return resultList
        
    def LungCancerTumorMarkersTest2(LCT_User_Result=0.0):
        resultList = []
        if LCT_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود سرطان في الرئة ام لا ",'CA 19.9'))   
        else:
            resultList.append(("نسبتك غير طبيعية تتجه تجاه السرطان يحدد هذا التحليل وجود سرطان في الرئة  ام لا " ,'CA 19.9'))
        return resultList

    def BladderTest(B_User_Result=''):
        resultList = []
        if B_User_Result =='negative':
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود سرطان في المثانة ام لا",'CA50'))   
        else:
            resultList.append(("نسبتك غير طبيعية تتجه ناحية السرطان يحدد هذا التحليل وجود سرطان في المثانة ام لا",'CA50')) 
        return resultList
    
    def BladderTest2(B_User_Result=0.0):
        resultList = []
        if B_User_Result in np.round(np.arange(350,450.1,0.01),2):
            resultList.append((" نسبتك طبيعية لا يوجد اي ورم سرطاني يحدد هذا التحليل وجود سرطان في المثانة ام لا",'CA50'))   
        else:
            resultList.append(("نسبتك غير طبيعية تتجه ناحية السرطان يحدد هذا التحليل وجود سرطان في المثانة ام لا",'CA50')) 
        return resultList
    
    
class DawnTest:
    def DawnSyndromeTest(DS_User_Result=''):
        resultList = []
        if DS_User_Result =='negative':
             resultList.append(("الطفل طبيعي "))  
        else:
             resultList.append(("من المرجح ان الطفل مصاب بملازمة داون ")) 
        return resultList
        
    def DawnSyndromeTest2(DS_User_Result=0.0):
        resultList = []
        if DS_User_Result in np.round(np.arange(0,1.1,0.01),2):
             resultList.append(("الطفل طبيعي "))   
        else:
             resultList.append(("من المرجح ان الطفل مصاب بملازمة داون"))
        return resultList

    def AlphaFetoproteinTest(AF_User_Result=0.0):
        resultList = []
        if AF_User_Result in  np.round(np.arange(10,150.1,0.01),2):
            resultList.append((" نسبتك طبيعية {} يقيس وجود عيوب في الجنين ام لا ",'Alpha Fetoprotein') )  
        else:
            resultList.append(("نسبتك غير طبيعية تتجه ناحية ان الجنبن مصاب بعيوب "))
        return resultList
    
    
class AIDSTest:
    def HumanImmunodeficiencyVirusAntibodiesTest(HIVAb_User_Result=''):
        resultList = []
        if HIVAb_User_Result =='negative':
            resultList.append(("نتيجتك طبيعية هذا التحليل يقيس وجود اجسام مضادة لمرض الايدز ",'HIV Ab'))   
        else:
            resultList.append(("من المرجح الاصابة بفيروس الايدز ")) 
        return resultList
    def HumanImmunodeficiencyVirusAntibodiesTest2(HIVAb_User_Result2=0.0):
        resultList = []
        if HIVAb_User_Result2 in np.round(np.arange(10,150.1,0.01),2):
            resultList.append(("نتيجتك طبيعية هذا التحليل يقيس وجود اجسام مضادة لمرض الايدز ",'HIV Ab'))   
        else:
             resultList.append(("من المرجح الاصابة بفيروس الايدز ")) 
        return resultList
         
    def HIVbyPCRTest(HIVPCR_User_Result=0.0):
        resultList = []
        if HIVPCR_User_Result in np.round(np.arange(10,150.1,0.01),2):
            resultList.append(("نتيجتك طبيعية هذا التحليل يقيس وجود اجسام مضادة لمرض الايدز ",'HIV Ab'))    
        else:
            resultList.append(("من المرجح الاصابة بفيروس الايدز")) 
        return resultList
    
    
class RiskEvaluationProfile:
    
    def LipidProfile(Cholesterol=0.0,Triglyceride=0.0,HDL_C=0.0,LDL_C=0.0):
        LP=['Cholesterol','Triglyceride','HDL_C','LDL_C']
        LP_User_Result={'Cholesterol':Cholesterol,'Triglyceride':Triglyceride,'HDL_C':HDL_C,'LDL_C':LDL_C}
        LP_Test={'Cholesterol':np.round(np.arange(150,200.1,0.01),2),'Triglyceride':np.round(np.arange(30,150.1,0.01),2),
                 'HDL_C':np.round(np.arange(40,60.1,0.01),2),'LDL_C':np.round(np.arange(0,150.1,0.01),2)}
        LP_Test_inarabic={'Cholesterol':' نسبة الكوليسترول.','Triglyceride':'الدهون الثلاثية','LDL_C':' كوليسترول البروتين الدهني منخفض الكثافة الكوليسترول (الخبيث)',
                          'HDL_C':'كوليسترول البروتين الدهني عالي الكثافة الكوليسترول (الحميد)'}
        resultList = []
        for i in range(0,len(LP)):
            if(LP_User_Result[LP[i]] in LP_Test[LP[i]]):
                resultList.append((LP[i], "نسبته طبيعية  ", LP_Test_inarabic.get(LP[i])))
            else:
                resultList.append((LP[i], "نسبته غير طبيعية", LP_Test_inarabic.get(LP[i])))
        return resultList        

    def HomocysteineTest(H_User_Result=0.0):
        resultList = []
        if H_User_Result in np.round(np.arange(0,15.1,0.01),2):
            resultList.append((" نتيجتك طبيعية هذا التحليل مسؤل عن اكتشاف احد امراض القلب",'Homocystiene'))   
        else:
            resultList.append(("من المرجح الاصابة باحد امراض القلب فان وظيفة هذا التحليل اكتشاف وجود احد امراض القلب ام لا "))
        return resultList

    
    def ActivatedfactorXIITest(AF_User_Result=0.0):
        resultList = []
        if AF_User_Result==100:
            resultList.append((" نتيجتك طبيعية هذا التحليل يقيس وجود خلل في عوامل تخنثر الدم ام لا",'Activated factor XII')  ) 
        else:
            resultList.append(("من المرجح وجود خلل في عوامل التخنثر فان هذا التحليل يقيس وجود خلل في عوامل التخنثر ام لا ")) 
        return resultList

    def SerumFibrinogenTest(SE_User_Result=0.0):
        resultList = []
        if SE_User_Result in np.round(np.arange(200,400.1,0.01),2):
            resultList.append((" نتيجتك طبيعية يقيس مستوي الفيبرينوجين وجود خلل في احد عوامل التخنثر ام لا ", 'Fibrinogen level'))   
        else:
            resultList.append(("من المرجح بوجود خلل في احد عوامل التخنثر فن تحليل مستوي الفيبرينوجين يقيس وجود خلل في احد عوامل التخنثر ام لا ",'Fibrinogen level'))
        return resultList

            
    def HighSensitivityCReactiveProteinTest(HRCRP_User_Result=0.0):
        resultList = []
        if HRCRP_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append((" نتيجتك طبيعية بروتين سي يقيس مستوي الحساسية"))   
        else:
            resultList.append(("نسبة بروتين سي غير طبيعية فهو يقيس مقدار الحساسيىة"))
        return resultList
             
             
class ThromboticRiskProfile:
    def PlateletCountTest(PC_User_Result=0.0):
        resultList = []
        if PC_User_Result in np.round(np.arange(150,400.1,0.01),2): 
            resultList.append(("عدد الصفائح الدموية الضرورية لتخنثر الدم طبيعي"))
        else:  
            resultList.append(("عدد الصفائح الدموية الضرورية لتخنثر الدم غير طبيعي"))
        return resultList

            
    def ProthrombinTimeTest(PT_User_Result=0.0):
        resultList = []
        if PT_User_Result in np.round(np.arange(11,13.6,0.01),2):  
            resultList.append(("الوقت الذي ياخذه الدم لكي يتخنثر طبيعي"))
        else:  
            resultList.append(("لوقت الذي ياخذه الدم لكي يتخنثر غير طبيعي"))
        return resultList

    def  PCRFactorVbyPCRTest(FV_User_Result=0.0):
        resultList = []
        if FV_User_Result in np.round(np.arange(50,150.1,0.01),2):
            resultList.append(("نسبة عامل التجلط {} طبيعي",'PCR Factor V'))
        else:
            resultList.append(("نسبة عامل التجلط {} غير طبيعي",'PCR Factor V'))
        return resultList

    def PartialThromboplastinTimeTest(PTT_User_Result=0.0):
        resultList = []
        if PTT_User_Result in np.round(np.arange(60,70.1,0.01),2):
            resultList.append(("نتيجة الوقت الذي ياخذه الدم لكي يتخنثر طبيعي "))
        else:
            resultList.append(("نتيجة الوقت الذي ياخذه الدم لكي يتخنثر غير طبيعي "))
        return resultList

    def ThrombinTimeTest(TT_User_Result=0.0):
        resultList = []
        if TT_User_Result in np.round(np.arange(4,11.1,0.01),2):
            resultList.append(("نتيجة الوقت الذي ياخذه الدم لكي يتخنثر طبيعي"))
        else:
            resultList.append(("نتيجة الوقت الذي ياخذه الدم لكي يتخنثر غير طبيعي"))
        return resultList

    def AntiThrombinTest(AT_User_Result=0.0):
        resultList = []
        if AT_User_Result in np.round(np.arange(80,120.1,0.01),2):
            resultList.append(("نتيجة الوقت الذي ياخذه الدم لكي يتخنثر طبيعي يقيس كمية بروتين مضاد الثرومبين الموجود في الجسم، ويؤدي نقص بروتين مضاد الثرومبين إلى تجلط الدم بسهولة ",'Anti Thrombin'))
        else:
            resultList.append(("نتيجة الوقت الذي ياخذه الدم لكي يتخنثر غير طبيعي يقيس كمية بروتين مضاد الثرومبين الموجود في الجسم، ويؤدي نقص بروتين مضاد الثرومبين إلى تجلط الدم بسهولة",'Anti Thrombin'))
        return resultList

    def ProteinCTest(PC_User_Result=0.0):
        resultList = []
        if PC_User_Result in np.round(np.arange(60,150.1,0.01),2):
            resultList.append(("نسبة بروتين سي طبيعية وهو أحد البروتينات التي ينتجها الكبد ويرتفع مستوى البروتين المتفاعل C عند وجود التهاب في الجسم"))   
        else:
            resultList.append(("نسبة بروتين سي غير طبيعية وهو أحد البروتينات التي ينتجها الكبد ويرتفع مستوى البروتين المتفاعل")) 
        return resultList

    def ProteinSTest(PS_User_Result=0.0):
        resultList = []
        if PS_User_Result in np.round(np.arange(60,150.1,0.01),2):
            resultList.append((" نسبة بروتين {} غير طبيعية كما يساعد في تشخيص إصابة الفرد باضطرابات التخثر",'Protein S'))  
        else:
            resultList.append(("نسبة بروتين {} غير طبيعية كما يساعد في تشخيص إصابة الفرد باضطرابات التخثر",'Protein S'))  
        return resultList
            
    def FibrinDegradationProductsTest(FDPs_User_Result=0.0):
        resultList = []
        if FDPs_User_Result in np.round(np.arange(0,10.1,0.01),2):
            resultList.append((" نسبتك طبيعية وهو تحليل يقيس منتجات تحلل الفبرين، وهي المواد التي تبقى في الدم عندما تذوب الجلطات في الدم، ويساعد في معرفة إصابة الفرد باضطراب في التخثر ",'FDPs'))  
        else:
            resultList.append((" نسبتك غير طبيعية وهو تحليل يقيس منتجات تحلل الفبرين، وهي المواد التي تبقى في الدم عندما تذوب الجلطات في الدم، ويساعد في معرفة إصابة الفرد باضطراب في التخثر ",'FDPs'))  
        return resultList

    def SerumFibrinogenTest(SF_User_Result=0.0):
        resultList = []
        if SF_User_Result in np.round(np.arange(200,400.1,0.01),2):
            resultList.append((" نتيجتك طبيعية وهو تحليل يقيس مستوى الفيبرينوجين في البلازما كما يعد أحد العوامل التي تساعد في تخثر الدم بشكل طبيعي، والتي يصل عددها إلى ثلاثة عشر عامل، وهو بروتين بلازما الدم ويصنع في الكبد، وعندما يحدث نزيف لدى الفرد فإن الجسم يستجيب لذلك من خلال تكوين جلطة أو خثرة بمساعدة عوامل التخثر بمساعدة عوامل التخثر، وعند وجود مشكلة في الفيبرينوجين فإنه قد يسبب نزيفاً مفرطاً "))   
        else:
            resultList.append(("نسبتك غير طبيعية وهو تحليل يقيس مستوى الفيبرينوجين في البلازما كما يعد أحد العوامل التي تساعد في تخثر الدم بشكل طبيعي، والتي يصل عددها إلى ثلاثة عشر عامل، وهو بروتين بلازما الدم ويصنع في الكبد، وعندما يحدث نزيف لدى الفرد فإن الجسم يستجيب لذلك من خلال تكوين جلطة أو خثرة بمساعدة عوامل التخثر بمساعدة عوامل التخثر، وعند وجود مشكلة في الفيبرينوجين فإنه قد يسبب نزيفاً مفرطاً ")) 
        return resultList

    def LupusAnticoagulantTest(LA_User_Result=''):
        resultList = []
        if LA_User_Result =='negative':
            resultList.append(("نتيجتك طبيعية يستخدم لتشخيص الإصابة بمتلازمة أضداد الشحوم الفسفورية، أو لاكتشاف سبب تكون خثرات في الدم، وتقييم زمن الثرومبوبلاستين الجزئي، فضلاً عن استخدامه في تحديد سبب الاجهاضات المتكررة، ولا يستخدم تحليل مانع التخثر الذئبي في تشخيص الإصابة بمرض الذئبة",'Lupus Anticoagulant'))
        else:
            resultList.append(("من المرجح وجود اجسام مضادة ذاتية يستخدم لتشخيص الإصابة بمتلازمة أضداد الشحوم الفسفورية، أو لاكتشاف سبب تكون خثرات في الدم، وتقييم زمن الثرومبوبلاستين الجزئي، فضلاً عن استخدامه في تحديد سبب الاجهاضات المتكررة، ولا يستخدم تحليل مانع التخثر الذئبي في تشخيص الإصابة بمرض الذئبة",'Lupus Anticoagulant')) 
        return resultList
        
    def LupusAnticoagulantTest2(LA_User_Result=0.0):
        resultList = []
        if LA_User_Result in np.round(np.arange(0,1.1,0.01),2):
            resultList.append(("نتيجتك طبيعية يستخدم لتشخيص الإصابة بمتلازمة أضداد الشحوم الفسفورية، أو لاكتشاف سبب تكون خثرات في الدم، وتقييم زمن الثرومبوبلاستين الجزئي، فضلاً عن استخدامه في تحديد سبب الاجهاضات المتكررة، ولا يستخدم تحليل مانع التخثر الذئبي في تشخيص الإصابة بمرض الذئبة",'Lupus Anticoagulant'))  
        else:
            resultList.append(("من المرجح وجود اجسام مضادة ذاتية يستخدم لتشخيص الإصابة بمتلازمة أضداد الشحوم الفسفورية، أو لاكتشاف سبب تكون خثرات في الدم، وتقييم زمن الثرومبوبلاستين الجزئي، فضلاً عن استخدامه في تحديد سبب الاجهاضات المتكررة، ولا يستخدم تحليل مانع التخثر الذئبي في تشخيص الإصابة بمرض الذئبة","Lupus Anticoagulant")) 
        return resultList


    def AntiCardiolipinAbsTest(ACAb_User_Result=0.0):
        resultList = []
        if ACAb_User_Result in np.round(np.arange(0,40.1,0.01),2):
            resultList.append(("نتيجتك طبيعية وهو تحليل لاكتشاف الأجسام مُضادة ذاتيّة يُنتجها الجهاز المناعيّ بالخطأ إذ يُهاجم الكارديوليبين الموجود في الجسم، ممّا يؤدي لحدوث مشاكل في التخثر وحدوث ما يُسمى بمتلازمة مُضادات الفوسفوليبيد","Anti Cardiolipin Abs"))   
        else:
            resultList.append(("من المرجح وجود اجسام مضادة ذاتية وهو تحليل الأجسام مُضادة ذاتيّة يُنتجها الجهاز المناعيّ بالخطأ إذ يُهاجم الكارديوليبين الموجود في الجسم، ممّا يؤدي لحدوث مشاكل في التخثر وحدوث ما يُسمى بمتلازمة مُضادات الفوسفوليبيد","Anti Cardiolipin Abs"))
        return resultList    

            
    
if __name__ == "__main__":
    print(LiverFunctionTest.LiverFunctionTest(10,20,10,10,10,10,10,10,10))

