import 'dart:convert';

import 'package:bot_project/models/Clinic_api_response_model.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

// var uri = "https://staging-api.vivifyhealthcare.com/HCP/HcpClinic/";
var uri = "https://staging-api.vivifyhealthcare.com/Offers/UserOfferPostAPI/";


var _headers = {
  "Content-Type": "application/json",
  'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0OTA2Mzg3LCJqdGkiOiI1ZmU3ODk2NjU1Nzc0NmVjODk4YzE3ZDM2ZDBlMzUyZCIsInVzZXJfaWQiOjV9.8cu2WKbPXdNKiiMgCIu_nK16GlplPXXAIgpk4thpBWw"};

// final data= jsonEncode({
//   "ClinicName": "MADHuu",
//   "Address": "string",
//   "FromDate": "2023-03-19",
//   "ToDate": "2023-03-19",
//   "FromTime": "10:00:00",
//   "ToTime": "13:00:00",
//   "Fee": 100,
//   "HcpId": 150
// });
final data = jsonEncode({
  "UserId": 145,
  "OfferId": 1,
  "CouponCode": "Madhu1"
});

class RemoteSevice{
  Future<ClinicApiResponseModel> clinicpostapi() async{
    var client = http.Client();
    var url = Uri.parse(uri);

    var response = await http.post(url,headers: _headers,body: data);
    print('object');
    print(response.statusCode);
    print(response.body);
    if  (response.statusCode  ==  200)  {
      //  If  the  server  did  return  a  201  CREATED  response,
      //  then  parse  the  JSON.
      return  ClinicApiResponseModel.fromJson(jsonDecode(response.body));
    }  else  {
      //  If  the  server  did  not  return  a  201  CREATED  response,
      //  then  throw  an  exception.
      throw  Exception('Failed  to  create  album.');
    } }

}



// Future<String>login_function() async{
//
//   print(uri);
//   var url = Uri.parse(uri);
//
//   final  data = jsonEncode({
//     "Username": "Rohitha",
//     "Password": "Test@1234",
//     "DeviceToken": "dioZHJ2yShWey-cYOYEnCa:APA91bE0KRtBrMnoBoAN0hs6iw_G0XJvR7uJHlyVAwXN04P6AN0oHVyIUoWE_Q9sBp4vb4t6KuVyUXUycaOEzM5WlZ69YxaCZrLcXXH2uJ020poXJuiLLndNjg-uatqv1Z6xk6xezYam"
//   });
//
//   var response = await http.post(url,headers: _header,body:data);
//   // print(data);
//   // print(response.statusCode);
//   var x = response.statusCode;
//   print(x);
//   // print(x.runtimeType);
//   return x.toString();
// }





