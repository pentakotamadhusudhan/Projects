import 'package:flutter/material.dart';

import '../api/api_clinc.dart';
import '../models/Clinic_api_response_model.dart';



class ClinicScreen extends StatefulWidget {
  const ClinicScreen({Key? key}) : super(key: key);

  @override
  State<ClinicScreen> createState() => _ClinicScreenState();
}

class _ClinicScreenState extends State<ClinicScreen> {

  ClinicApiResponseModel? clinicApiResponseModel ;
  TextEditingController x = TextEditingController();
  @override
  void initState() {
    adookaname();

    // TODO: implement initState
    super.initState();


  }

  Future<void> adookaname()async {
    ClinicApiResponseModel? result = await RemoteSevice().clinicpostapi();
    if(result!=null){
      setState(() {
        clinicApiResponseModel = result;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(body:ListView.builder(
        itemCount: 1,
        itemBuilder: (context,index){
      return Container(
        child: Column(
          children: [
            ElevatedButton(onPressed: (){RemoteSevice().clinicpostapi();}, child: Text('button')),
           Text(clinicApiResponseModel!.result!.couponCode.toString()),
          ],
        ),
      );

    }));
  }
}
