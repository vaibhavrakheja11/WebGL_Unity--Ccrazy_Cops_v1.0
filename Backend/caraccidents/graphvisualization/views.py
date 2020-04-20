# Django related dependencies
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from caraccidents import settings
# Django rest framework related dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from caraccidents.settings import original_data
#python dependencies
import pandas as pd
import json
import datetime

class AccidentDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            age_list=['Age (0-10) ','Age (10-20) ','Age (20-30) ','Age (30-40) ','Age (40-50) ','Age (50-60) ','Age (60-70) ','Age (70-80) ','Age (80-90) ','Age (90-100) ','Age (>100)']
            gender=request.GET.get('gender','M')
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            xx = data.groupby(['P_SEX','age_bracket']).size().to_frame().reset_index()
            xx=xx[xx['P_SEX']==gender]
            xx=xx.values.tolist()            
            result_list=[]
            for i in range(len(xx)):
                temp={}
                if(xx[i][1]>=0):
                    temp["name"]=age_list[xx[i][1]]
                else:
                    temp["name"]="Unknown"
                temp['value']=xx[i][2]
                result_list.append(temp)

            response['result']=result_list
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)





class FatalitiesDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            result_df_list=(data.groupby(['C_WDAY','C_SEV']).size().to_frame().reset_index()).values.tolist()
            response_result_temp=[]
            week_day=['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            fatility=['','Fatality','Non fatality']
            for i in range(len(result_df_list)):
                if len(response_result_temp)==0:
                    temp={}
                    try:                        
                        temp['week_day']=week_day[int(result_df_list[i][0])]                        
                    except:
                        temp['week_day']="Unknown"
                    try:
                        
                        temp[(fatility[int(result_df_list[i][1])])]=result_df_list[i][2]
                    except:
                        temp["Unknown"]=result_df_list[i][2]
                    response_result_temp.append(temp)
                else:
                    count=0
                    for j in range(len(response_result_temp)):     
                        try:                   
                            if(response_result_temp[j].get('week_day')==week_day[int(result_df_list[i][0])]):
                                try:
                                    if fatility[int(result_df_list[i][1])] in  response_result_temp[j]:
                                        response_result_temp[j][fatility[int(result_df_list[i][1])]]=response_result_temp[j].get(fatility[int(result_df_list[i][1])])+ result_df_list[i][2]
                                    else:
                                        response_result_temp[j][fatility[int(result_df_list[i][1])]]=result_df_list[i][2]
                                except Exception as e:
                                    if 'Unknown' in response_result_temp[j]:
                                        response_result_temp[j]['Unknown']=response_result_temp[j].get('Unknown')+ result_df_list[i][2]
                                    else:
                                        response_result_temp[j]['Unknown']=result_df_list[i][2]
                                count+=1
                        except Exception as e:
                            if(response_result_temp[j].get('week_day')=='Unknown'):
                                try:
                                    if fatility[int(result_df_list[i][1])] in  response_result_temp[j]:
                                        response_result_temp[j][fatility[int(result_df_list[i][1])]]=response_result_temp[j].get(fatility[int(result_df_list[i][1])])+ result_df_list[i][2]
                                    else:
                                        response_result_temp[j][fatility[int(result_df_list[i][1])]]=result_df_list[i][2]
                                except Exception as e:
                                    if 'Unknown' in response_result_temp[j]:
                                        response_result_temp[j]['Unknown']=response_result_temp[j].get('Unknown')+ result_df_list[i][2]
                                    else:
                                        response_result_temp[j]['Unknown']=result_df_list[i][2]
                                count+=1
                    if count==0:
                        temp={}
                        try:             
                            temp['week_day']=week_day[int(result_df_list[i][0])]                        
                        except:

                            temp['week_day']="Unknown"
                        try:                
                            temp[(fatility[int(result_df_list[i][1])])]=result_df_list[i][2]
                        except:
                            temp["Unknown"]=result_df_list[i][2]
                        response_result_temp.append(temp)
            print(response_result_temp)
            response['result']=response_result_temp
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)


class CollisionDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            xz=data.groupby(['C_HOUR']).size().to_frame().reset_index()
            max_value=xz.max()[0]
            min_value=xz.min()[0]
            print(max_value)
            print(min_value)
            middle_value1=int((max_value-min_value)/3)
            middle_value2=2*int((max_value-min_value)/3)
            result_list_temp=xz.values.tolist()
            result_list=[]
            data_green="data:image/png;base64,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"
            data_red="data:image/png;base64,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"
            data_yellow="data:image/png;base64,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"
            for i in range(len(result_list_temp)):
                temp={}
                temp["category"]= ""
                temp["start"]= "2019-01-10 "+result_list_temp[i][0]+":00"
                temp["end"]= "2019-01-10 "+result_list_temp[i][0]+":59"
                if(result_list_temp[i][1]<=middle_value1):
                    temp['icon']=data_green
                    temp["text"]= "Accidents are less than 30% of the maximum. Total number of accidents: "+ str(result_list_temp[i][1])
                elif(result_list_temp[i][1]<=middle_value2 and result_list_temp[i][1]>middle_value1):
                    temp['icon']=data_yellow
                    temp["text"]= "Accidents are less than 60% of the maximum. Total number of accidents: "+ str(result_list_temp[i][1])
                else:
                    temp['icon']=data_red
                    temp['text']="Too many accidents. Total number of accidents: "+ str(result_list_temp[i][1])
                result_list.append(temp)
            response['result']=result_list
            
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)


class VehicleController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            week_day=['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            pqr=data.groupby(['C_WDAY','vehicle_group']).size().to_frame().reset_index()
            pqr_list=pqr.values.tolist()
            temp_list=[]
            vehicle_list={-1:"Unknown",0:"0 vehicles",1:"1 vehicles",2:"2 vehicles",3:"3 vehicles",4:"4 vehicles",5:"5 vehicles",6: "6-10 vehicles",7:"11-15 vehicles",8:"16-20 vehicles",9:"21-25 vehicles",10:"26-30 vehicles",11:">30 vehicles" }
            for i in range(len(pqr_list)):
                temp={}
                count=0                
                for j in range(len(temp_list)):
                    try:
                        if int(pqr_list[i][1]) in temp_list[j]:
                            temp_list[j]['size']=temp_list[j].get('size')+int(pqr_list[i][2])
                            count+=1
                    except Exception as e:
                        print(e)
                        if 'Unknown' in temp_list[j]:
                            temp_list[j]['size']=temp_list[j].get('size')+int(pqr_list[i][2])
                            count+=1
                if(count==0):
                    try:
                        temp['sector']=int(pqr_list[i][1])
                    except Exception as e:
                        print(e)
                        temp['sector']='Unknown'
                    temp['size']=pqr_list[i][2]
                    temp_list.append(temp)
            rst=pqr.groupby(['C_WDAY']).size().to_frame().reset_index().values.tolist()
            final_dict={}
            counter=0
            for i in range(len(temp_list)):
                temp_list[i]['sector']=vehicle_list.get(int(temp_list[i].get("sector")))
            for i in range(len(rst)):
                try:
                    final_dict[week_day[int(rst[i][0])]]=temp_list[counter:counter+int(rst[i][1])]
                except Exception as e:
                    final_dict['Unknown']=temp_list[counter:counter+int(rst[i][1])]
                counter+=rst[i][1]
            response['result']=final_dict
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)

class SafetyDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            result_dict={}
            p_user_dict={"1":'Motor Vehicle Driver',"2":'Motor Vehicle Passenger',"3":'Pedestrian',"4":'Bicyclist',"5":'Motorcyclist'}
            p_safety_dict={"01":"No safety device used or No child restraint used","02":"Safety device used or child restraint used","09":"Helmet worn","10":"Reflective clothing worn","11":"Both helmet and reflective clothing used","12":"Other safety device used","13":"No safety device equipped","NN":"Unknown","QQ":"Unknown","UU":"Unknown","XX":"Unknown"}
            safety_device=data.groupby(['P_SAFE','P_USER']).size().to_frame().reset_index().values.tolist()
            for i in range(len(safety_device)):
                if p_safety_dict.get(safety_device[i][0]) in result_dict:
                    result_dict[p_safety_dict.get(safety_device[i][0])][p_user_dict.get(safety_device[i][1])]=safety_device[i][2]
                else:
                    result_dict[p_safety_dict.get(safety_device[i][0])]={}
                    result_dict[p_safety_dict.get(safety_device[i][0])][p_user_dict.get(safety_device[i][1])]=safety_device[i][2]
            response['result']=result_dict

            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)

class WeatherDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            weather_list={"1":"Clear/sunny","2":"Overcast, cloudy","3":"Raining","4":"Snowing excluding drifting snow","5":"Freezing rain, sleet, hail","6":"Visibility limitation","7":"Strong wind","Q":"Other","U":"Unknown","X":"Hidden Data"}
            road_list={"1":"Dry, normal","2":"Wet","3":"Snow ","4":"Slush ,wet snow","5":"Icy + packed snow","6":"Sand/gravel/dirt","7":"Muddy","8":"Oil ","9":"Flooded","Q":"Choice is other than the preceding values","U":"Unknown","X":"Jurisdiction does not provide data element"}
            sev={"1": "Collision producing at least one fatality","2": "Collision producing non-fatal injury","U": "Unknown","X": "Jurisdiction does not provide this data element"}
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            road_condition_sev=data.groupby(['C_WTHR','C_RSUR','C_SEV']).size().to_frame().reset_index()
            road_condition=road_condition_sev.groupby(['C_WTHR','C_RSUR']).size().to_frame().reset_index()
            weather_condition=road_condition.groupby(['C_WTHR']).size().to_frame().reset_index()
            lol = road_condition_sev.values.tolist()
            lol1=road_condition.values.tolist()
            lol2=weather_condition.values.tolist()
            result_age_list=[]
            for i in range(len(lol)):
                temp={}
                temp['name']=sev.get(str(lol[i][2]))+" : "+str(lol[i][3])
                temp['value']=lol[i][3]
                result_age_list.append(temp)
            result_sex_list=[]
            counter=0
            for i in range(len(lol1)):
                temp={}
                sum1=0
                for j in range(counter,counter+int(lol1[i][2])):
                    sum1+=result_age_list[j]['value']
                temp['name']=road_list.get(lol1[i][1])+" : "+str(sum1)
                temp['children']=result_age_list[counter:counter+int(lol1[i][2])]
                counter+=int(lol1[i][2])
                result_sex_list.append(temp)
            counter=0
            result_hour_list=[]
            for i in range(len(lol2)):
                temp={}
                sum1=0
                for j in range(counter,counter+int(lol2[i][1])):
                    sum1+=int(result_sex_list[j]['name'].split(":")[1])
                temp['name']=weather_list.get(lol2[i][0])+" : "+str(sum1)
                temp['children']=result_sex_list[counter:counter+int(lol2[i][1])]
                counter+=int(lol2[i][1])
                result_hour_list.append(temp)
            counter=0
            response['result'] =result_hour_list
            
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)
class RoadCollisionDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            print(start_date)
            print(end_date)
            
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            print(data)
            collision_config={"01": "Hit a moving object","02": "Hit a stationary object","03": "Ran off left shoulder ","04": "Ran off right shoulder","05": "Rollover on roadway","06": "Any other single vehicle collision configuration","21": "Rear-end collision","22": "Side swipe","23": "One vehicle passing to the left of the other, or left turn conflict","24": "One vehicle passing to the right of the other, or right turn conflict","25": "Any other two vehicle - same direction of travel configuration","31": "Head-on collision","32": "Approaching side-swipe","33": "Left turn across opposing traffic","34": "Right turn, including turning conflicts","35": "Right angle collision","36": "Any other two-vehicle - different direction of travel configuration","41": "Hit a parked motor vehicle","QQ": "Choice is other than the preceding values1","UU": "Unknown1","XX": "Jurisdiction does not provide this data element1"}
            road_config1={"01": "Non-intersection","02": "At an intersection of at least two public roadways","03": "Intersection with parking lot entrance/exit, private driveway or laneway","04": "Railroad level crossing","05": "Bridge, overpass, viaduct","06": "Tunnel or underpass","07": "Passing or climbing lane","08": "Ramp","09": "Traffic circle","10": "Express lane of a freeway system","11": "Collector lane of a freeway system","12": "Transfer lane of a freeway system","QQ": "Choice is other than the preceding values","UU": "Unknown","XX": "Jurisdiction does not provide this data element"}
            sev={"1": "Fatal","2": "Non-fatal injury","U": "Unknown","X": "Jurisdiction does not provide this data element"}
            fatalities=data.groupby(['C_CONF','C_RCFG','C_SEV']).size().to_frame().reset_index()
            road_config=fatalities.groupby(['C_CONF','C_RCFG']).size().to_frame().reset_index()
            lol=fatalities.values.tolist()
            lol1=road_config.values.tolist()
            result_list=[]

            for i in range(len(lol)):
                temp={}
                if road_config1.get(str(lol[i][1]))==sev.get(str(lol[i][2])): 
                    pass
                else:
                    temp['from']=road_config1.get(str(lol[i][1]))
                    temp['to']=sev.get(str(lol[i][2]))
                    temp['value']=lol[i][3]
                    result_list.append(temp)
            counter=0
            for i in range(len(lol1)):                
                if road_config1.get(str(lol1[i][1]))==collision_config.get(str(lol1[i][0])): 
                    pass
                else:
                    temp={}
                    temp['from']=collision_config.get(str(lol1[i][0]))
                    temp['to']=road_config1.get(str(lol1[i][1]))
                    sum1=0
                    for j in range(counter,counter+int(lol1[i][2])):    
                        sum1+=result_list[j].get('value')
                    temp['value']= int(sum1)
                    counter+=int(lol1[i][2])
                    result_list.append(temp)
            response['result']=result_list
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)

class WeekDetailsController(APIView):
    def get(self,request,format=None):
        try:
            data=settings.original_data
            response = {
                "status_code": 200,
                "message": "Result is achieved",
                "result":{}    
            }
            start_year=int(request.GET.get('startyear','2005'))
            start_month=int(request.GET.get('startmonth','01'))
            end_year=int(request.GET.get('endyear','2014'))
            end_month=int(request.GET.get('endmonth','12'))
            start_date = datetime.datetime(start_year,start_month,1).date()
            end_date = datetime.datetime(end_year,end_month,1).date()
            work_day={"1" :"Monday","2" :"Tuesday","3" :"Wednesday","4" :"Thursday","5" :"Friday","6" :"Saturday","7" :"Sunday","U" :"Unknown","X" :"Jurisdiction does not provide this data element"}
            data=data[(original_data['DATETIME']>=pd.to_datetime(start_date)) &( original_data['DATETIME']<=pd.to_datetime(end_date))]
            data['C_WDAY']=data['C_WDAY'].astype('str')
            week=data.groupby(['C_YEAR','C_WDAY']).size().to_frame().reset_index()
            year=week.groupby(['C_YEAR']).size().to_frame().reset_index()
            lol=week.values.tolist()
            lol1=year.values.tolist()
            result_list=[]
            result_dict={}
            for i in range(len(lol)):
                temp={}
                temp['network']=work_day.get(lol[i][1])
                temp['MAU']=lol[i][2]
                result_list.append(temp)
            counter=0
            for i in range(len(lol1)):
                result_dict[lol1[i][0]]=result_list[counter:counter+lol1[i][1]]
                counter+=lol1[i][1]
            response['result']=result_dict
            return Response(response,status=status.HTTP_200_OK,headers=None)
        except Exception as e:
            print(e)
            response['status_code']=400
            response['message']="Result can not be fetched at this moment"
            return Response(response,status=status.HTTP_200_OK,headers=None)

class Services:
    def age_replace(self, x):
        if x == 'NN':
            return -30
        elif x == 'UU':
            return -30
        elif x == 'XX':
            return -30
        else: 
            return x
    def month_replace(self, x):
        if x=='UU':
            return -30
        else:
            return x