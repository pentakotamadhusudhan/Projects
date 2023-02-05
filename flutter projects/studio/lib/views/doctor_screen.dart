import 'package:flutter/material.dart';
import 'package:studio/views/doctor_screen.dart';
import 'package:studio/views/screens/doctor_home_screeen.dart';

class typeofpartners extends StatelessWidget {
  const typeofpartners({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,

        
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                // padding: EdgeInsets.all(10),
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: TextButton(
                  child: Text('Certified Doctor',style: TextStyle(color: Colors.black87),),onPressed: (){
                    print('cerified doctor cilcked');
                    Navigator.push(context, MaterialPageRoute(builder: (doctor)=>doctor_home_screen()),
                  );
                  },

                ),

              ),
              Container(
                // padding: EdgeInsets.all(5),
                height: 150,
                width: 150,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    color: Colors.blue,
                  ),
                  child: TextButton(
                    child: Text('Pharmacy',style: TextStyle(color: Colors.black87),),onPressed: (){
                    print('cerified doctor cilcked');
                  },

                  )
              )
            ],
          ),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Diagnostics',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              ),
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Emergency',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              )
            ],
          ),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Clinic',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              ),
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Hospital',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              )
            ],
          ),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Home Care',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              ),
              Container(
                padding: EdgeInsets.only(top: 10),
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Delivery',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              )
            ],
          ),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Marketing',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              ),
              Container(
                height: 150,
                width: 150,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.blue,
                ),
                child: Center(child:Text(
                  'Blood Bank',
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.black87,
                  ),
                )
                ),
              )
            ],
          ),

        ],
      ),
    );
  }
}
